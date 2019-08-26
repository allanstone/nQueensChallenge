#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""
.. module:: test_nqueens
.. moduleauthor:: agarrido
:synopsis: Testing module for testing SolveNqueens module.
"""
# Syspath hack to use db class with pytest to avoid ModuleNotFoundError
import sys, os
curPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, curPath + '/../')

from ..SolveNqueens import Solver, BackTrackSolver
from ..utils import SOLUTIONS

import pytest

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

    def test_mocked_solve(self, mocker):
        '''Mocking result when do not have an algorithm'''
        mock_solver = mocker.patch.object(Solver, 'call_solver')
        mock_solver.return_value = True
        assert self.solver.call_solver()

# Create a subset with dictionary comprehension
subdict = {k: SOLUTIONS[k] for k in range(1,9)}
lower_bounds = [(k, v) for k, v in subdict.items()]

class TestBackTrackSolver():

    def setup_class(self):
        self.bs = BackTrackSolver()

    @pytest.mark.parametrize("boardSize,results", lower_bounds)
    def test_lower_bounds(self, boardSize, results):
        solutions, _ = self.bs.solve(boardSize)
        assert solutions == results




