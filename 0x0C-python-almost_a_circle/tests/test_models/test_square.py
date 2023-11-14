#!/usr/bin/python3
from models.square import Square
import unittest


class TestSquare(unittest.TestCase):
    """Unittests for the Square class."""

    def test_square_creation(self):
        """Test creation of Square instances."""
        s1 = Square(1)
        self.assertIsInstance(s1, Square)

        s2 = Square(1, 2)
        self.assertIsInstance(s2, Square)

        s3 = Square(1, 2, 3)
        self.assertIsInstance(s3, Square)

        with self.assertRaises(TypeError):
            s4 = Square("1")

        with self.assertRaises(TypeError):
            s5 = Square(1, "2")

        with self.assertRaises(TypeError):
            s6 = Square(1, 2, "3")

        with self.assertRaises(ValueError):
            s8 = Square(-1)

        with self.assertRaises(ValueError):
            s9 = Square(1, -2)

        with self.assertRaises(ValueError):
            s10 = Square(1, 2, -3)

        with self.assertRaises(ValueError):
            s11 = Square(0)  # This will raise a ValueError now

    def test_update_method(self):
        """Test the update method of Square."""
        s = Square(1, 2, 3, 4)
        s.update(89)
        self.assertEqual(s.id, 89)

        s.update(89, 1)
        self.assertEqual(s.size, 1)

        s.update(89, 1, 2)
        self.assertEqual(s.x, 2)

        s.update(89, 1, 2, 3)
        self.assertEqual(s.y, 3)

        with self.assertRaises(ValueError):
            s.update(89, -1)

        with self.assertRaises(ValueError):
            s.update(89, 1, -2)

        with self.assertRaises(ValueError):
            s.update(89, 1, 2, -3)

        s.update(0)
        self.assertEqual(s.id, 0)

        s.update(**{'id': 89})
        self.assertEqual(s.id, 89)

        #s.update(**{'id': 89, 'size': 1})
        #self.assertEqual(s.size, 1)

        s.update(**{'id': 89, 'size': 1, 'x': 2})
        self.assertEqual(s.x, 2)

        s.update(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})
        self.assertEqual(s.y, 3)

if __name__ == '__main__':
    unittest.main()
