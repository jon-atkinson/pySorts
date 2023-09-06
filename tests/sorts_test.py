import unittest
from src.python.sorts import is_sorted
from src.python.sorts import *

class TestBubbleSortPy(unittest.TestCase):
    n = 10000
    rand_in = gen_data_sets.gen_rand_arr(n, "python")
    sorted_in = gen_data_sets.gen_pre_sorted_arr(n, "python")
    reversed_in = gen_data_sets.gen_rev_sorted_arr(n, "python")
    
    def test_rand_input(self):
        self.assertTrue(is_sorted(bubble_sort(self.rand_in, self.n)))
       
    def test_sorted_input(self):
        self.assertTrue(is_sorted(bubble_sort(self.sorted_in, self.n)))

    def test_reversed_input(self):
        self.assertTrue(is_sorted(bubble_sort(self.reversed_in, self.n)))


if __name__ == '__main__':
    unittest.main()