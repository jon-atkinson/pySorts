from typing import List

import numpy as np
import scipy.stats as stats


def test_array_shape_normal(array: List[int], generator_name: str) -> None:
    skewness = stats.skew(array)
    assert (
        abs(skewness) < 0.1
    ), f"{generator_name} array generator produced an array that was not symmetric."
    _, p_val = stats.normaltest(array)
    assert (
        p_val > 0.01
    ), f"{generator_name} array generator produced an array that did not fit the normal distribution."


def test_array_shape_uniform(array: List[int], generator_name: str) -> None:
    _, p_val = stats.kstest(
        array, "uniform", args=(np.min(array), np.max(array) - np.min(array))
    )
    assert (
        p_val > 0.05
    ), f"{generator_name} array generator produced an array that did not fit the uniform distribution."


def test_array_shape_positive_skew(array: List[int], generator_name: str) -> None:
    skewness = stats.skew(array)
    assert (
        skewness > 0.5
    ), f"{generator_name} array generator produced an array with incorrect skewness. Expected={'> 0.5'}. Got={skewness}"


def test_array_shape_negative_skew(array: List[int], generator_name: str) -> None:
    skewness = stats.skew(array)
    assert (
        skewness < -0.5
    ), f"{generator_name} array generator produced an array with incorrect skewness. Expected={'< -0.5'}. Got={skewness}"


def test_array_sorted(array: List[int], generator_name: str) -> None:
    assert all(
        array[i] <= array[i + 1] for i in range(len(array) - 1)
    ), f"{generator_name} array generator produced an array that was not sorted. Got={str(array)}. Expected={str(np.sorted(array))}."


def test_array_reverse_sorted(array: List[int], generator_name: str) -> None:
    assert all(
        array[i] >= array[i + 1] for i in range(len(array) - 1)
    ), f"{generator_name} array generator produced an array that was not reverse sorted. Got={str(array)}. Expected={str(np.sorted(array))}."


def test_array_length(
    array: List[int], expected_length: int, generator_name: str
) -> None:
    assert (
        len(array) == expected_length
    ), f"{generator_name} array generator produced array of incorrect length. Got={len(array)}. Expected={expected_length}."
