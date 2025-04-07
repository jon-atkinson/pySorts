import numpy as np
import scipy.stats as stats

import src.backend_config as config
import tests.helpers as helpers
from src.arrays import deep_copy

TEST_ARRAY_LEN = 100000


class TestArrays:
    def test_generating_sorted_arrays(self):
        array = config.arrays["sorted"](TEST_ARRAY_LEN)

        helpers.test_array_length(array, TEST_ARRAY_LEN)
        helpers.test_array_sorted(array)

    def test_generating_reverse_sorted_arrays(self):
        array = config.arrays["reverse sorted"](TEST_ARRAY_LEN)

        helpers.test_array_length(array, TEST_ARRAY_LEN)
        helpers.test_array_reverse_sorted(array)

    def test_generating_random_arrays(self):
        array = config.arrays["random"](TEST_ARRAY_LEN)

        helpers.test_array_length(array, TEST_ARRAY_LEN)
        helpers.test_array_shape_uniform(array)

    def test_generating_normal_arrays(self):
        array = config.arrays["normal"](TEST_ARRAY_LEN)

        helpers.test_array_length(array, TEST_ARRAY_LEN)
        helpers.test_array_shape_normal(array)

    def test_generating_positive_skew_arrays(self):
        array = config.arrays["positive skew"](TEST_ARRAY_LEN)

        helpers.test_array_length(array, TEST_ARRAY_LEN)
        helpers.test_array_shape_positive_skew(array)

    def test_generating_negative_skew_arrays(self):
        array = config.arrays["negative skew"](TEST_ARRAY_LEN)

        helpers.test_array_length(array, TEST_ARRAY_LEN)
        helpers.test_array_shape_negative_skew(array)

    def test_deep_copy_new_memory(self):
        array = config.arrays["reverse sorted"](TEST_ARRAY_LEN)
        helpers.test_array_reverse_sorted(array)

        copy_array = deep_copy(array)
        array.sort()

        helpers.test_array_sorted(array)
        helpers.test_array_reverse_sorted(copy_array)
