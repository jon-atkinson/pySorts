import unittest
from src.python.sorts import is_sorted

class TestArrayValidationMethods(unittest.TestCase):
    
    def test_array_sorted(self):
        self.assertFalse(is_sorted([9, 8, 7, 6, 5]))
        self.assertFalse(is_sorted([1, 0, 1, 2, 3]))
        self.assertFalse(is_sorted([4, 2645, 133, 1867]))

        self.assertTrue(is_sorted([0, 0, 0, 0, 0]))
        self.assertTrue(is_sorted([1, 1, 1, 1, 1]))
        self.assertTrue(is_sorted([0, 0, 1, 2, 3]))
        self.assertTrue(is_sorted([2, 4, 6, 45, 3263456]))
       

if __name__ == '__main__':
    unittest.main()