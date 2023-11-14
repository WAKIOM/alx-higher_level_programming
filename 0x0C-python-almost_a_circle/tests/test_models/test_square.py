#!/usr/bin/python3
"""unittests for models/square.py"""
import unittest
from models.base import Base
from models.square import Square


class TestSquare_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Square class."""

    def test_is_base(self):
        self.assertIsInstance(Square(10), Base)

    def test_is_rectangle(self):
        self.assertIsInstance(Square(10), Square)

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Square()
    def test_string_rep_w(self):
        s = Square(3)
        self.assertEqual(str(s), "[Square] (16) 0/0 - 3")
