from typing import List

import numpy as np
import pytest

import backend.backend_config as config
import backend.sorter as sorter

TEST_ARRAY_LEN = 10


class TestSorts:
    @pytest.mark.parametrize(
        "language, algorithm, array",
        [
            (language, algorithm, config.arrays["sorted"](TEST_ARRAY_LEN))
            for language in config.algorithms
            for algorithm in config.algorithms[language]
        ],
    )
    def test_sorted_input(self, language: str, algorithm: str, array: List[int]):
        output_array, _ = sorter.call(algorithm, language, array)
        assert all(
            output_array[i] <= output_array[i + 1] for i in range(TEST_ARRAY_LEN - 1)
        ), f"{algorithm} in {language} had incorrect output for sorted input. Expected={np.sort(array)}. Got={output_array}."

    @pytest.mark.parametrize(
        "language, algorithm, array",
        [
            (language, algorithm, config.arrays["reverse sorted"](TEST_ARRAY_LEN))
            for language in config.algorithms
            for algorithm in config.algorithms[language]
        ],
    )
    def test_reverse_sorted_input(
        self, language: str, algorithm: str, array: List[int]
    ):
        output_array, _ = sorter.call(algorithm, language, array)
        assert all(
            output_array[i] <= output_array[i + 1] for i in range(TEST_ARRAY_LEN - 1)
        ), f"{algorithm} in {language} had incorrect output for reverse sorted input. Expected={np.sort(array)}. Got={output_array}"
