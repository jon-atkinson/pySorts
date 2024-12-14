from typing import List

import numpy as np
import scipy.stats as stats

import src.backend_config as config

first_language = list(config.algorithms.keys())[0]
first_algorithm = list(config.algorithms[first_language])[0]
first_array_type = list(config.arrays.keys())[0]


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
        p_val > 0.01
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


def test_comparison_results_shape(response_data: dict) -> None:
    assert len(response_data["data_series"]) == 1 and all(
        "data" in single_series
        and isinstance(single_series["data"], list)
        and all(
            len(point) == 2
            and isinstance(point[0], int)
            and isinstance(point[1], float)
            for point in single_series["data"]
        )
        for single_series in response_data["data_series"]
    )


def test_get_all_comparisons_shape(response_data: dict) -> None:
    assert "comparisons" in response_data
    assert len(response_data["comparisons"]) == 1
    assert all(
        key in list(response_data["comparisons"][0].keys())
        for key in ["id", "type", "algorithms"]
    )
    assert len(response_data["comparisons"][0]["algorithms"]) == 1
    assert len(response_data["comparisons"][0]["algorithms"][0]) == 3
    assert all(
        key in list(response_data["comparisons"][0]["algorithms"][0][2].keys())
        for key in ["type", "length", "repeats", "step", "start", "stop"]
    )
