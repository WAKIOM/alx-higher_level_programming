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
        self.assertEqual(str(s), "[Square] (23) 0/0 - 3")

    def test_string_rep_w_x(self):
        s1 = Square(1, 2)
        self.assertEqual(str(s1), "[Square] (24) 2/0 - 1")

    def test_string_rep_w_x_y(self):
        s2 = Square(1, 2, 3)
        self.assertEqual(str(s2), "[Square] (25) 2/3 - 1")

    def test_strinf_rep_w_x_y_id(self):
        s3 = Square(1,2,3,4)
        self.assertEqual(str(s3), "[Square] (4) 2/3 - 1")

    def test_init_width_string(self):
        with self.assertRaises(TypeError):
            Square("1")

    def test_init_x_string(self):
        with self.assertRaises(TypeError):
            Square(1, "2")

    def test_init_y_string(self):
        with self.assertRaises(TypeError):
            Square(1, 2, "3")

    def test_init_negative_width(self):
        with self.assertRaises(ValueError):
            Square(-1)
    def test_init_negative_x(self):
        with self.assertRaises(ValueError):
            Square(1, -2)

    def test_init_negative_y(self):
        with self.assertRaises(ValueError):
            Square(1, 2, -3)

    def test_init_zero_width(self):
        with self.assertRaises(ValueError):
            Square(0)

    def test_to_dictionary(self):
        s4 = Square(1, 2, 3, 4)
        self.assertEqual(s4.to_dictionary(), {'id': 4, 'x': 2, 'size': 1, 'y': 3})
    def test_update(self):
        s3 = Square(1,2,3,4)
        s3.update(89)
        s3.update(89, 1)
        s3.update(89, 1, 2)
        s3.update(89, 1, 2, 3)
        self.assertEqual(s3.id, 89)
        self.assertEqual(s3.size, 1)
        self.assertEqual(s3.x, 2)
        self.assertEqual(s3.y, 3)

