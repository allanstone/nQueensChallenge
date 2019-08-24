#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""
.. module:: test_nqueens
.. moduleauthor:: agarrido
:synopsis: Testing module for testing SolveNqueens module.
"""
import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

from ..SolveNqueens import Solver, BackTrackSolver
from ..utils import SOLUTIONS
from ..db import Base

class TestSolver():
    """
        Test class for SolveNqueens algorithm
    """

    def setup_class(self):
        """
        Setup for test Solver
        """
        self.boardSize = 0
        self.algorithm = None
        self.solver = Solver(self.boardSize, self.algorithm)

    def test_instance(self):
        assert isinstance(self.solver, Solver)

    def test_solve(self, boardSize):
        assert self.solver.call_solver()
#
#class TestBackTrackSolver():
#
#    def setup_class(self):
#        self.bkts = 0
#        self.lower_bounds = range(1,9)
#
#    def test_lower_bounds():
#        assert True == True
