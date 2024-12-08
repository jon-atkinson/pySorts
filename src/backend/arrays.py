import ctypes
import numpy as np

language_converters = {
    "python": lambda array : array,
    "c": lambda array : (ctypes.c_int * len(array))(*array),
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

def generate_random_array(n: int):
    return np.random.randint(0, n, n)

def generate_normal_array(n: int):
    return np.random.normal(loc=n / 2, scale=1, size=n).astype(int)

def generate_sorted_array(n: int):
    return np.arange(0, n)

def generate_reverse_sorted_array(n: int):
    return np.arange(0, n, -1)

def generate_positive_skew_array(n: int):
    return (np.random.exponential(scale=n / 10, size=n)).astype(int)

def generate_negative_skew_array(n: int):
    return (n - 1 - np.random.exponential(scale=n / 10, size=n)).astype(int)

def generate_many_repeats_array(n: int):
    num_uniques = max(1, n // 10)
    uniques = np.random.randint(0, num_uniques, num_uniques)
    values = np.repeat(uniques, 10)
    np.random.shuffle(values)
    if len(values) < n:
        additional_values = np.random.choice(uniques, n - len(values), replace=True)
        values = np.concatenate([values, additional_values])
    np.random.shuffle(values)
    return values
