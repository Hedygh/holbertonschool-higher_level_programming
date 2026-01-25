#!/usr/bin/python3
"""Unittests for max_integer function."""

import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Tests for max_integer."""

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_one_element(self):
        self.assertEqual(max_integer([7]), 7)

    def test_max_at_end(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_at_beginning(self):
        self.assertEqual(max_integer([9, 2, 3, 4]), 9)

    def test_max_in_middle(self):
        self.assertEqual(max_integer([1, 8, 3, 4]), 8)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-10, -3, -50, -4]), -3)

    def test_mixed_numbers(self):
        self.assertEqual(max_integer([-10, 0, 5, 3]), 5)

    def test_duplicates(self):
        self.assertEqual(max_integer([2, 2, 2]), 2)

    def test_unsorted_list(self):
        self.assertEqual(max_integer([3, 1, 4, 2]), 4)


if __name__ == "__main__":
    unittest.main()
