import unittest
from src.python.sorts import is_sorted
from src.python.gen_data_sets import *


class TestArrayGen(unittest.TestCase):
    n = 10000
    
    def test_gen_rand_sorted_arr(self):
        arr = gen_rand_arr(self.n, "python")
        self.assertFalse(is_sorted(arr))
        self.assertFalse(arr[0] == arr[1] == arr[self.n // 2] == arr[self.n - 2] == arr[self.n - 1])

    def test_gen_pre_sorted_arr(self):
        arr = gen_pre_sorted_arr(self.n, "python")
        self.assertTrue(is_sorted(arr))
        self.assertTrue(arr[0] < arr[self.n // 2] < arr[self.n - 1])

    def test_gen_rev_sorted_arr(self):
        arr = gen_rev_sorted_arr(self.n, "python")
        self.assertFalse(is_sorted(arr))
        self.assertTrue(arr[0] > arr[self.n // 2] > arr[self.n - 1])
        arr.reverse()
        self.assertTrue(is_sorted(arr))
        

if __name__ == '__main__':
    unittest.main()
    