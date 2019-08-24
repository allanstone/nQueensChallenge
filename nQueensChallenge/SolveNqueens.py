#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""
.. module:: Solvers
.. module author:: agarrido
:synopsis: Core module for solving the 8 queens puzzle problem
"""

from .BackTrackAlgo import BackTrack
from .db import DatabaseSession
from .models import Results
from .utils import timing

class Solver(object):
    '''
        Solver class for resolve the n Queens puzzle
        This is the main class for the whole project
    '''
    def __init__(self, algorithm, boardSize):
        self.__algorithm = algorithm
        self.__boardSize = boardSize

    def set_boardSize(self, boardSize):
        self.__boardSize = boardSize

    def call_solver(self, solver):
        print('Resolving {0}x{0} queens board with: {1}'.format(
            self.__boardSize, self.__algorithm))
        results = solver.solve()
        return results

class BackTrackSolver(Solver):
    '''
        BackTrackSolver class for resolve the n Queens puzzle
        implementing BackTrack algorithm and save in the db
    '''
    def __init__(self, boardSize=0):
        self.__dbs = DatabaseSession()
        self.__algorithm = 'Backtracking'
        super().__init__(self.__algorithm, boardSize)

    def __repr__(self):
        return self.__algorithm

    def save_to_db(self, boardSize, solutions, boards):
        '''Save result of execution to db'''
        result_model = Results(
            boardSize = boardSize,
            solutions = solutions,
            boards = boards)
        self.__dbs.save(result_model)

    def solve(self, size):
        '''Solve the puzzel for n queens'''
        return super(BackTrackSolver, self).call_solver(BackTrack(size))

    def solve_to_n(self, n):
        '''Solve the puzzel for n queens'''
        for size in range(1, n+1):
            self.set_boardSize(size)
            solutions, boards = self.solve(size)
            self.save_to_db(size, solutions, boards)

if __name__ == "__main__":
    from db import recreate_database, Base
    recreate_database()
    bs = BackTrackSolver()
    bs.solve_to_n(4)

