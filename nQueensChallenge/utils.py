#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""
.. module:: utils
.. module author:: agarrido
:synopsis: Common utilities for the project
"""

from functools import wraps
from time import time,sleep

#Constants

SOLUTIONS = { #Dictionary for having the number of solutions
 1  :  1,     #given a size board (e.g. 4x4 has only 2 solutions)
 2  :  0,
 3  :  0,
 4  :  2,
 5  :  10,
 6  :  4,
 7  :  40,
 8  :  92,
 9  :  352,
 10 :  724,
 11 :  2680,
 12 :  14200,
 13 :  73712,
 14 :  365596,
 15 :  2279184
}



def timing(f):
    '''
        Decorator for measuring execution time for functions
    '''
    @wraps(f)
    def wrap(*args, **kw):
        ts = time()
        result = f(*args, **kw)
        te = time()
        print('func:%r args:[%r, %r] took: %2.4f sec' % \
          (f.__name__, args, kw, te-ts))
        return result
    return wrap

