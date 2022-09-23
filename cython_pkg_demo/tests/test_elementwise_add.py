"""
"""
import numpy as np
from ..elementwise_add import elementwise_add_numpy, elementwise_add_cython_wrapper


def test_elementwise_addition():
    x = np.arange(10).astype("f8")
    y = np.arange(10).astype("f8")

    result1 = elementwise_add_numpy(x, y)
    result2 = elementwise_add_cython_wrapper(x, y)
    assert np.allclose(result1, result2)
