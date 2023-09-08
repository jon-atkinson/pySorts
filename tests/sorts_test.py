import unittest
from src.python.sorts import is_sorted
from src.python.gen_data_sets import *
from src.python.sorts import *


class TestBucketSortPy(unittest.TestCase):
    n = 10000

    def test_zero_input(self):
        arr = [0]
        self.assertTrue(is_sorted(bucket_sort(arr, 1)))

    def test_single_input(self):
        arr = [1]
        self.assertTrue(is_sorted(bucket_sort(arr, 1)))

    def test_num_bck_greater_than_num_inputs(self):
        arr = [1, 0]
        self.assertTrue(is_sorted(bucket_sort(arr, 2)))

    def test_rand_input(self):
        arr = gen_rand_arr(self.n, "python")
        self.assertTrue(is_sorted(bucket_sort(arr, self.n)))
       
    def test_sorted_input(self):
        arr = gen_pre_sorted_arr(self.n, "python")
        self.assertTrue(is_sorted(bucket_sort(arr, self.n)))

    def test_reversed_input(self):
        arr = gen_rev_sorted_arr(self.n, "python")
        self.assertTrue(is_sorted(bucket_sort(arr, self.n)))

    def test_many_rep_input(self):
        arr = gen_many_rep_arr(self.n, "python")
        self.assertTrue(is_sorted(bucket_sort(arr, self.n)))


class TestBubbleSortPy(unittest.TestCase):
    n = 10000
    
    def test_zero_input(self):
        arr = [0]
        self.assertTrue(is_sorted(bubble_sort(arr, 1)))

    def test_single_input(self):
        arr = [7]
        self.assertTrue(is_sorted(bubble_sort(arr, 1)))

    def test_rand_input(self):
        arr = gen_rand_arr(self.n, "python")
        self.assertTrue(is_sorted(bubble_sort(arr, self.n)))
       
    def test_sorted_input(self):
        arr = gen_pre_sorted_arr(self.n, "python")
        self.assertTrue(is_sorted(bubble_sort(arr, self.n)))

    def test_reversed_input(self):
        arr = gen_rev_sorted_arr(self.n, "python")
        self.assertTrue(is_sorted(bubble_sort(arr, self.n)))

    def test_many_rep_input(self):
        arr = gen_many_rep_arr(self.n, "python")
        self.assertTrue(is_sorted(bubble_sort(arr, self.n)))


class TestCountSortPy(unittest.TestCase):
    n = 10000

    def test_rand_input(self):
        arr = gen_rand_arr(self.n, "python")
        self.assertTrue(is_sorted(count_sort(arr, self.n)))
       
    def test_sorted_input(self):
        arr = gen_pre_sorted_arr(self.n, "python")
        self.assertTrue(is_sorted(count_sort(arr, self.n)))

    def test_reversed_input(self):
        arr = gen_rev_sorted_arr(self.n, "python")
        self.assertTrue(is_sorted(count_sort(arr, self.n)))

    def test_many_rep_input(self):
        arr = gen_many_rep_arr(self.n, "python")
        self.assertTrue(is_sorted(count_sort(arr, self.n)))


class TestHeapSortPy(unittest.TestCase):
    n = 10000

    def test_rand_input(self):
        arr = gen_rand_arr(self.n, "python")
        self.assertTrue(is_sorted(heap_sort(arr, self.n)))
       
    def test_sorted_input(self):
        arr = gen_pre_sorted_arr(self.n, "python")
        self.assertTrue(is_sorted(heap_sort(arr, self.n)))

    def test_reversed_input(self):
        arr = gen_rev_sorted_arr(self.n, "python")
        self.assertTrue(is_sorted(heap_sort(arr, self.n)))

    def test_many_rep_input(self):
        arr = gen_many_rep_arr(self.n, "python")
        self.assertTrue(is_sorted(heap_sort(arr, self.n)))


class TestInsertionSortPy(unittest.TestCase):
    n = 10000

    def test_rand_input(self):
        arr = gen_rand_arr(self.n, "python")
        self.assertTrue(is_sorted(insertion_sort(arr, self.n)))
       
    def test_sorted_input(self):
        arr = gen_pre_sorted_arr(self.n, "python")
        self.assertTrue(is_sorted(insertion_sort(arr, self.n)))

    def test_reversed_input(self):
        arr = gen_rev_sorted_arr(self.n, "python")
        self.assertTrue(is_sorted(insertion_sort(arr, self.n)))

    def test_many_rep_input(self):
        arr = gen_many_rep_arr(self.n, "python")
        self.assertTrue(is_sorted(insertion_sort(arr, self.n)))


class TestMergeSortPy(unittest.TestCase):
    n = 10000

    def test_rand_input(self):
        arr = gen_rand_arr(self.n, "python")
        self.assertTrue(is_sorted(merge_sort(arr, self.n)))
       
    def test_sorted_input(self):
        arr = gen_pre_sorted_arr(self.n, "python")
        self.assertTrue(is_sorted(merge_sort(arr, self.n)))

    def test_reversed_input(self):
        arr = gen_rev_sorted_arr(self.n, "python")
        self.assertTrue(is_sorted(merge_sort(arr, self.n)))

    def test_many_rep_input(self):
        arr = gen_many_rep_arr(self.n, "python")
        self.assertTrue(is_sorted(merge_sort(arr, self.n)))


class TestQuickSortPy(unittest.TestCase):
    # n = 10000 exceeds python max recursion depth for this algorithm
    n = 1000

    def test_rand_input(self):
        arr = gen_rand_arr(self.n, "python")
        self.assertTrue(is_sorted(quick_sort(arr, self.n)))
       
    def test_sorted_input(self):
        arr = gen_pre_sorted_arr(self.n, "python")
        self.assertTrue(is_sorted(quick_sort(arr, self.n)))

    def test_reversed_input(self):
        arr = gen_rev_sorted_arr(self.n, "python")
        self.assertTrue(is_sorted(quick_sort(arr, self.n)))

    def test_many_rep_input(self):
        arr = gen_many_rep_arr(self.n, "python")
        self.assertTrue(is_sorted(quick_sort(arr, self.n)))


class TestRadixSortPy(unittest.TestCase):
    n = 10000

    def test_rand_input(self):
        arr = gen_rand_arr(self.n, "python")
        self.assertTrue(is_sorted(radix_sort(arr, self.n)))
       
    def test_sorted_input(self):
        arr = gen_pre_sorted_arr(self.n, "python")
        self.assertTrue(is_sorted(radix_sort(arr, self.n)))

    def test_reversed_input(self):
        arr = gen_rev_sorted_arr(self.n, "python")
        self.assertTrue(is_sorted(radix_sort(arr, self.n)))

    def test_many_rep_input(self):
        arr = gen_many_rep_arr(self.n, "python")
        self.assertTrue(is_sorted(radix_sort(arr, self.n)))


class TestSelectionSortPy(unittest.TestCase):
    n = 10000

    def test_rand_input(self):
        arr = gen_rand_arr(self.n, "python")
        self.assertTrue(is_sorted(selection_sort(arr, self.n)))
       
    def test_sorted_input(self):
        arr = gen_pre_sorted_arr(self.n, "python")
        self.assertTrue(is_sorted(selection_sort(arr, self.n)))

    def test_reversed_input(self):
        arr = gen_rev_sorted_arr(self.n, "python")
        self.assertTrue(is_sorted(selection_sort(arr, self.n)))

    def test_many_rep_input(self):
        arr = gen_many_rep_arr(self.n, "python")
        self.assertTrue(is_sorted(selection_sort(arr, self.n)))


class TestShellSortPy(unittest.TestCase):
    n = 10000

    def test_rand_input(self):
        arr = gen_rand_arr(self.n, "python")
        self.assertTrue(is_sorted(shell_sort(arr, self.n)))
       
    def test_sorted_input(self):
        arr = gen_pre_sorted_arr(self.n, "python")
        self.assertTrue(is_sorted(shell_sort(arr, self.n)))

    def test_reversed_input(self):
        arr = gen_rev_sorted_arr(self.n, "python")
        self.assertTrue(is_sorted(shell_sort(arr, self.n)))

    def test_many_rep_input(self):
        arr = gen_many_rep_arr(self.n, "python")
        self.assertTrue(is_sorted(shell_sort(arr, self.n)))


class TestTimSortPy(unittest.TestCase):
    n = 10000

    def test_rand_input(self):
        arr = gen_rand_arr(self.n, "python")
        self.assertTrue(is_sorted(tim_sort(arr, self.n)))
       
    def test_sorted_input(self):
        arr = gen_pre_sorted_arr(self.n, "python")
        self.assertTrue(is_sorted(tim_sort(arr, self.n)))

    def test_reversed_input(self):
        arr = gen_rev_sorted_arr(self.n, "python")
        self.assertTrue(is_sorted(tim_sort(arr, self.n)))

    def test_many_rep_input(self):
        arr = gen_many_rep_arr(self.n, "python")
        self.assertTrue(is_sorted(tim_sort(arr, self.n)))


class TestTreeSortPy(unittest.TestCase):
    n = 10000

    def test_rand_input(self):
        arr = gen_rand_arr(self.n, "python")
        self.assertTrue(is_sorted(tree_sort(arr, self.n)))
       
    def test_sorted_input(self):
        arr = gen_pre_sorted_arr(self.n, "python")
        self.assertTrue(is_sorted(tree_sort(arr, self.n)))

    def test_reversed_input(self):
        arr = gen_rev_sorted_arr(self.n, "python")
        self.assertTrue(is_sorted(tree_sort(arr, self.n)))

    def test_many_rep_input(self):
        arr = gen_many_rep_arr(self.n, "python")
        self.assertTrue(is_sorted(tree_sort(arr, self.n)))


if __name__ == '__main__':
    unittest.main()