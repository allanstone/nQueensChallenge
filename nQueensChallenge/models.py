#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""
.. module:: models
.. module author:: agarrido
:synopsis: Data model definitions for nqueens problem
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects import postgresql
from sqlalchemy import Column, Integer

from sqlalchemy import create_engine

Base = declarative_base()

class Results(Base):
    '''
        Model for storing results from algorithm runs
        testdb=# select * from results;
         id | boardSize | solutions |        boards
        ----+-----------+-----------+-----------------------
          1 |         1 |         1 | {{0}}
          2 |         4 |         2 | {{1,3,0,2},{2,0,3,1}}
    '''
    __tablename__ = 'results'
    id = Column(Integer, primary_key=True)
    boardSize = Column(Integer)
    solutions =  Column(Integer)
    boards =  Column(postgresql.ARRAY(Integer))

    def __repr__(self):
        return "<Result(boardSize='{0}x{0}', solutions='{1}', boars={2})>"\
                .format(self.boardSize, self.solutions, self.boards)
