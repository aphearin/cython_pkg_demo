"""
"""
import numpy as np
from .cython_kernels import elementwise_subtract_cython_kernel


def elementwise_subtract_numpy(x, y):
    return np.array(x) - np.array(y)


def elementwise_add_cython_wrapper(x, y):
    x = np.atleast_1d(x)
    y = np.atleast_1d(y)
    n = x.size
    result = elementwise_subtract_cython_kernel(x, y, n)
    return np.array(result)
