#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""
.. module:: db
.. module author:: agarrido
:synopsis: Provide basic/core API for db functionality
"""

from sqlalchemy_utils import database_exists
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from .config import DATABASE_URI
from .models import Base, Results

from functools import wraps

# Creating a thread safe session factory
engine = create_engine(DATABASE_URI)
session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)

# Functions to manage the database

def create_database():
    ''' Creates the database from scratch'''
    Base.metadata.create_all(engine)

def drop_database():
    ''' Drops all database contents'''
    Base.metadata.drop_all(engine)

def create_database_if_not_exists():
    ''' Creates the database if not already exists'''
    if not database_exists(engine.url):
        create_database(engine.url)

def recreate_database():
    ''' drops database and creates it from scratch '''
    drop_database()
    create_database()


def dbconnect(func):
    '''
    Session helper, provide a transactional scope around a series of operations
    '''
    @wraps(func)
    def inner(*args, **kwargs):
        session = Session()  # with all the requirements
        try:
            func(*args, session=session, **kwargs)
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()
    return inner

class DatabaseSession(object):

    @dbconnect
    def save(self, model,session):
        session.add(model)

    @dbconnect
    def query(self,model,session):
        for row in session.query(model).all():
            print(row)

    @dbconnect
    def destroy(self,model,session):
        session.delete(model)


if __name__ == '__main__':
    recreate_database()
    result = Results(
        boardSize = 1,
        solutions = 1,
        boards = [[1]]
    )
    dbs = DatabaseSession()
    dbs.save(result)
    dbs.query(Results)
    dbs.destroy(result)
