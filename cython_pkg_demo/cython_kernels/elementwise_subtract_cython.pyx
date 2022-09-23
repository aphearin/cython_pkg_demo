# cython: language_level=2
"""Cython module implementing the elementwise_subtract_cython_kernel function"""

import numpy as np

cimport cython
# import cython


__all__ = ("elementwise_subtract_cython_kernel",)


@cython.boundscheck(False)
@cython.nonecheck(False)
@cython.wraparound(False)
def elementwise_subtract_cython_kernel(double[:] x, double[:] y, int n):

    cdef double[:] result = np.zeros(n, dtype='f8')
    cdef int i

    for i in range(n):
        result[i] = x[i] - y[i]

    return result
