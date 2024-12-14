import numpy as np
import scipy.stats as stats

import src.backend_config as config
import tests.helpers as helpers

TEST_ARRAY_LEN = 100000


class TestArrays:
    def test_generating_sorted_arrays(self):
        array = config.arrays["sorted"](TEST_ARRAY_LEN)

        helpers.test_array_length(array, TEST_ARRAY_LEN, "sorted")
        helpers.test_array_sorted(array, "sorted")

    def test_generating_reverse_sorted_arrays(self):
        array = config.arrays["reverse sorted"](TEST_ARRAY_LEN)

        helpers.test_array_length(array, TEST_ARRAY_LEN, "reverse sorted")
        helpers.test_array_reverse_sorted(array, "reverse sorted")

    def test_generating_random_arrays(self):
        array = config.arrays["random"](TEST_ARRAY_LEN)

        helpers.test_array_length(array, TEST_ARRAY_LEN, "random")
        helpers.test_array_shape_uniform(array, "random")

    def test_generating_normal_arrays(self):
        array = config.arrays["normal"](TEST_ARRAY_LEN)

        helpers.test_array_length(array, TEST_ARRAY_LEN, "normal")
        helpers.test_array_shape_normal(array, "normal")

    def test_generating_positive_skew_arrays(self):
        array = config.arrays["positive skew"](TEST_ARRAY_LEN)

        helpers.test_array_length(array, TEST_ARRAY_LEN, "positive skew")
        helpers.test_array_shape_positive_skew(array, "positive skew")

    def test_generating_negative_skew_arrays(self):
        array = config.arrays["negative skew"](TEST_ARRAY_LEN)

        helpers.test_array_length(array, TEST_ARRAY_LEN, "negative skew")
        helpers.test_array_shape_negative_skew(array, "negative skew")
