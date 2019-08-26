#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""
.. module:: conftest
.. module author:: agarrido
:synopsis: Fixture definitions accessible across multiple test files
:note: Based on https://github.com/toirl/pytest-sqlalchemy
"""

import pytest
import sqlalchemy_utils.functions
from sqlalchemy.engine import create_engine


@pytest.fixture(scope="session")
def engine(request, sqlalchemy_connect_url, config_file):
    """Engine configuration.
    :sqlalchemy_connect_url: Connection url directly passed as a parameter
    :config_file: Using config.py file to import the url string
    :returns: Engine instance
    """
    if config_file:
        engine = create_engine(config_file)
    elif sqlalchemy_connect_url:
        engine = create_engine(sqlalchemy_connect_url)
    else:
        raise RuntimeError("Can not establish a connection to the database")

    def finalize():
        print ("Disposing engine")
        engine.dispose()

    request.addfinalizer(finalize)
    return engine


@pytest.fixture(scope="session")
def db_schema(request, engine, sqlalchemy_manage_db, sqlalchemy_keep_db):
    if not sqlalchemy_manage_db:
        return

    db_exists = sqlalchemy_utils.functions.database_exists(engine.url)
    if db_exists and not sqlalchemy_keep_db:
        raise RuntimeError("DB exists, remove it before proceeding")

    if not db_exists:
        sqlalchemy_utils.functions.create_database(engine.url)

    if not sqlalchemy_keep_db:
        def finalize():
            print ("Tearing down DB")
            sqlalchemy_utils.functions.drop_database(engine.url)

        request.addfinalizer(finalize)


@pytest.fixture(scope="module")
def connection(request, engine, db_schema):
    connection = engine.connect()

    def finalize():
        print ("Closing connection")
        connection.close()

    request.addfinalizer(finalize)
    return connection


@pytest.fixture()
def transaction(request, connection):
    """Will start a transaction on the connection. The connection will
    be rolled back after it leaves its scope."""
    transaction = connection.begin() # begin a non-ORM transaction

    def finalize():
        print ("Rollback")
        transaction.rollback()

    request.addfinalizer(finalize)
    return connection

@pytest.yield_fixture(scope='module')
def dbsession(request, connection):
    """ Creates a session within a transaction used scoped_session()
        for thread safety.
    """
    from sqlalchemy.orm import scoped_session
    from sqlalchemy.orm import sessionmaker
    session_factory = sessionmaker(bind=connection)
    session = scoped_session(session_factory)
    #yield session

    def finalize():
        print ("Session close")
        session.remove()

    request.addfinalizer(finalize)
    return session

@pytest.fixture()
def truncate_db(connection,engine):
    # delete all table data (but keep tables)
    # we do cleanup before test 'cause if previous test errored,
    # DB can contain dust
    from sqlalchemy import MetaData
    metadata = MetaData()
    metadata.reflect(bind=engine)
    transaction = connection.begin()
    print ("Truncating all tables")
    for table in metadata.sorted_tables:
        connection.execute(table.delete())
    transaction.commit()

# Config options
@pytest.fixture(scope="session")
def sqlalchemy_connect_url(request):
    return request.config.getoption("--sqlalchemy-connect-url")


@pytest.fixture(scope="session")
def connect_uri(request, sqlalchemy_connect_url):
    return sqlalchemy_connect_url


@pytest.fixture(scope="session")
def sqlalchemy_manage_db(request):
    return request.config.getoption("--sqlalchemy-manage-db")


@pytest.fixture(scope="session")
def sqlalchemy_keep_db(request):
    return request.config.getoption("--sqlalchemy-keep-db")


@pytest.fixture(scope="session")
def config_file(request):
    """Import the engine url from config file"""
    try:
        from ..config import DATABASE_URI as url
        return url
    except ImportError:
        raise ImportError('Can not import url string, check config file')
    return None


def pytest_addoption(parser):
    parser.addoption("--sqlalchemy-connect-url", action="store",
                     default=None,
                     help="Name of the database to connect to")

    parser.addoption("--sqlalchemy-config-file", action="store_true",
                     default=None,
                     help="Use ../config.py file to import the engine "
                     "url string.")

    parser.addoption("--sqlalchemy-manage-db", action="store_true",
                     default=None,
                     help="Automatically creates and drops database")

    parser.addoption("--sqlalchemy-keep-db", action="store_true",
                     default=None,
                     help="Do not delete database after test suite, "
                     "allowing for its reuse.")
