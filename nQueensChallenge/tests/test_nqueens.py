#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""
.. module:: test_nqueens
.. moduleauthor:: agarrido
:synopsis: Testing module for testing SolveNqueens module.
"""

from ..SolveNqueens import Solver
from ..utils import SOLUTIONS
from ..BackTrackAlgo import BackTrack


class TestSolver():
    """
        Test class for SolveNqueens algorithm
    """

    def setup_class(self):
        """
        Setup for test Solver
        """
        self.solv = Solver()
        self.lower_bounds = range(1,9)

    def test_instance(self):
        assert isinstance(self.solv, Solver)

#    def test_results(self, boardSize):
#        assert self.solver(boardSize)[0] == SOLUTIONS[boardSize]


    def test_lower_bounds()
