#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""
.. module:: test_utils
.. moduleauthor:: agarrido
:synopsis: Module for testing utils module.
"""

from  ..utils import timing
import time, sys, io

class TestUtils():
    """
        Test class for utils
    """

    def setup_class(self):
        """
        Setup for test Solver
        """
        pass

    def test_time_deco(self):
        # redirect sys.stdout to a buffer
        stdout = sys.stdout
        sys.stdout = io.StringIO()
        @timing
        def _f(t):
            time.sleep(t)
        _f(1)
        # get output and restore sys.stdout
        time_out = sys.stdout.getvalue()
        sys.stdout = stdout
        test_time = "func:'_f' args:[(1,), {}] took: 1.0011 sec\n"
        assert time_out == test_time


