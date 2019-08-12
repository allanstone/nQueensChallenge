#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""
.. module:: test_8queens
.. moduleauthor:: agarrido
:synopsis: Module for testing 8Solve8queens module.
"""

from .solutions import results
from .code.Solve8queens import Solver

class TestSolver():
    """
        Test class for 8queen solver algorithm
    """

    def setup_class(self):
        """
        Setup for test Solver
        """
        self.solv = Solver()

    def test_instance(self):
        assert isinstance(self.solv, Solver)
