#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""
.. module:: Solvers
.. module author:: agarrido
:synopsis: Core module for solving the 8 queens puzzle problem
"""

from BackTrackAlgo import BackTrack
from utils import timing

class Solver(object):
    '''
        Solver class for resolve the n Queens puzzle
    '''
    def __init__(self, algorithm, boardSize):
        '''
           General Solver constructor
        '''
        self.__algorithm = algorithm
        self.__boardSize = boardSize

    @timing
    def call_solver(self, solver):
        print('Resolving {0}x{0} queens board with: {1}'.format(
            self.__boardSize, self.__algorithm))
        results = solver.solve()
        return results

class BackTrackSolver(Solver):
    '''
        BackTrackSolver class for resolve the n Queens puzzle
        implementing BackTrack algorithm
    '''
    def __init__(self, boardSize):
        '''
           General Solver class
        '''
        super(BackTrackSolver, self).__init__('Backtracking', boardSize)
        self.__solver = BackTrack(boardSize)

    def solve(self):
        return super(BackTrackSolver, self).call_solver(self.__solver)

if __name__ == "__main__":
    bs = BackTrackSolver(4)
    r = bs.solve()
    print(r)

