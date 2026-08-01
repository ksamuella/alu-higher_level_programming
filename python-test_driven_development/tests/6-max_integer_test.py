#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Unit tests for the max_integer function."""

    def test_ordered_list(self):
        """Test with an ordered list."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test with an unordered list."""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_start(self):
        """Test with the max value at the start."""
        self.assertEqual(max_integer([9, 1, 2, 3]), 9)

    def test_max_at_end(self):
        """Test with the max value at the end."""
        self.assertEqual(max_integer([1, 2, 3, 9]), 9)

    def test_single_element(self):
        """Test with a single-element list."""
        self.assertEqual(max_integer([5]), 5)

    def test_empty_list(self):
        """Test with an empty list."""
        self.assertIsNone(max_integer([]))

    def test_default_argument(self):
        """Test with no argument (uses default empty list)."""
        self.assertIsNone(max_integer())

    def test_negative_numbers(self):
        """Test with negative numbers."""
        self.assertEqual(max_integer([-1, -2, -3]), -1)

    def test_mixed_sign_numbers(self):
        """Test with mixed positive and negative numbers."""
        self.assertEqual(max_integer([-5, 3, -2, 8, 0]), 8)

    def test_duplicate_max(self):
        """Test with duplicate max values."""
        self.assertEqual(max_integer([4, 4, 4]), 4)


if __name__ == "__main__":
    unittest.main()
