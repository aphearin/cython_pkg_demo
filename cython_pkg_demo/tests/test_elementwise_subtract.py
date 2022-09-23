"""
"""
import numpy as np
from ..elementwise_subtract import elementwise_subtract_numpy
from ..elementwise_subtract import elementwise_subtract_cython_wrapper


def test_elementwise_subtraction():
    x = np.arange(10).astype("f8")
    y = np.arange(10).astype("f8")

    result1 = elementwise_subtract_numpy(x, y)
    result2 = elementwise_subtract_cython_wrapper(x, y)
    assert np.allclose(result1, result2)
