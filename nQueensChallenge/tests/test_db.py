import pytest
from ..models import Base, Results

def test_connection(connection):
    # Do fancy stuff with the connection.
    # Note you will not need to close the connection. This is done
    # automatically when the scope (module) of the fixtures ends.
    assert connection

def test_truncate(truncate_db,dbsession):
    assert dbsession.query(Results).count() == 0


def test_create_result(dbsession):
    result = Results(
        boardSize = 1,
        solutions = 1,
        boards = [[1]]
    )
    dbsession.add(result)
    dbsession.commit()
    assert dbsession.query(Results).count() == 1

def test_read_result(dbsession):
    for result in dbsession.query(Results).all():
        print(type(result))
    assert dbsession.query(Results).filter(Results.boards==[[1]]).one()

def test_update_result(dbsession):
    result = Results(
        boardSize = 4,
        solutions = 9,
        boards = [[1]]
    )
    dbsession.add(result)
    result.solutions = 2
    dbsession.commit()
    assert dbsession.query(Results).count() == 2
    assert dbsession.query(Results).filter(Results.solutions==2).one()

def test_delete_result(dbsession):
    dbsession.query(Results).filter(
        Results.boardSize == 4).delete(synchronize_session=False)
    dbsession.commit()
    assert dbsession.query(Results).count() == 1
    assert not dbsession.query(Results).filter(Results.boardSize==4).all()
