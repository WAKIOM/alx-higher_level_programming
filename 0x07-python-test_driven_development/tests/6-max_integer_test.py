#!/usr/bin/python3
"""
This script defines unit tests for the max_integer function.
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    This class contains unit tests for the max_integer function.
    """

    def test_integer(self):
        """
        Test for the max_integer function with a list of integers.
        It asserts that the function correctly returns the maximum integer.
        """
        self.assertEqual(max_integer([4, 7, 3, 5]), 7)
        self.assertEqual(max_integer([-8, -16, -12]), -8)

    def test_values(self):
        """
        Test for the max_integer function with non-list input.
        It asserts that the function raises a TypeError for non-list inputs.
        """
        self.assertRaises(TypeError, max_integer, 8)
