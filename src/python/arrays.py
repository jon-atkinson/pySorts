import ctypes
import numpy as np
from typing import List
from copy import deepcopy

language_converters = {
    "python": lambda array : array,
    "c": lambda array : (ctypes.c_int * len(array))(*array),
}

generators = {
    "random": lambda n : np.random.randint(0, n, n),
    "normal": lambda n : np.random.normal(loc=n / 2, scale=1, size=n).astype(int),
    "sorted" : lambda n : np.arange(0, n),
    "reverse sorted" : lambda n : np.arange(0, n, -1),
    "positive skew" : lambda n: (np.random.exponential(scale=n / 10, size=n)).astype(int),
    "negative skew" : lambda n: (n - 1 - np.random.exponential(scale=n / 10, size=n)).astype(int),
    "many repeats" : lambda n : np.random.randint(n // 10, size=n),
}

def deep_copy(array: np.ndarray) -> np.ndarray:
    """
    Creates a deep copy of an array.

    Args:
        array (np.ndarray): The array to be copied.

    Returns:
        np.ndarray: A deep copy of the input array.
    """
    return np.copy(array)