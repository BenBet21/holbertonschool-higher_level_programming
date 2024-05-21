import unittest

class TestMaxInteger(unittest.TestCase):
    """Define unit tests for the max_integer function"""

    def test_max_at_end(self):
        """Test list with max value at the end"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_in_middle(self):
        """Test list with max value in the middle"""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_single_element(self):
        """Test list with a single element"""
        self.assertEqual(max_integer([7]), 7)

    def test_empty_list(self):
        """Test an empty list"""
        self.assertIsNone(max_integer([]))

    def test_negative_numbers(self):
        """Test list with all negative numbers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_numbers(self):
        """Test list with mixed positive and negative numbers"""
        self.assertEqual(max_integer([-1, 2, 3, -4]), 3)


if __name__ == '__main__':
    unittest.main()
