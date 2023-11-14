import unittest
import sys
import io
from models.rectangle import Rectangle
""" test cases for rectangle class """


class TestRectangle(unittest.TestCase):

    def test_init_with_valid_arguments(self):
        """Test initializing Rectangle with valid arguments."""
        rect = Rectangle(width=10, height=20, x=5, y=7, id=1)
        self.assertEqual(rect.width, 10)
        self.assertEqual(rect.height, 20)
        self.assertEqual(rect.x, 5)
        self.assertEqual(rect.y, 7)
        self.assertEqual(rect.id, 1)

    def test_init_with_invalid_width(self):
        """Test initializing Rectangle with invalid width."""
        with self.assertRaises(TypeError):
            Rectangle(width="invalid", height=20, x=5, y=7, id=1)

    def test_init_with_invalid_height(self):
        """Test initializing Rectangle with invalid height."""
        with self.assertRaises(TypeError):
            Rectangle(width=10, height="invalid", x=5, y=7, id=1)

    def test_init_with_negative_width(self):
        """Test initializing Rectangle with negative width."""
        with self.assertRaises(ValueError):
            Rectangle(width=-10, height=20, x=5, y=7, id=1)

    def test_init_with_negative_height(self):
        """Test initializing Rectangle with negative height."""
        with self.assertRaises(ValueError):
            Rectangle(width=10, height=-20, x=5, y=7, id=1)

    def test_init_with_invalid_x(self):
        """Test initializing Rectangle with invalid x."""
        with self.assertRaises(TypeError):
            Rectangle(width=10, height=20, x="invalid", y=7, id=1)

    def test_init_with_negative_x(self):
        """Test initializing Rectangle with negative x."""
        with self.assertRaises(ValueError):
            Rectangle(width=10, height=20, x=-5, y=7, id=1)

    def test_init_with_invalid_y(self):
        """Test initializing Rectangle with invalid y."""
        with self.assertRaises(TypeError):
            Rectangle(width=10, height=20, x=5, y="invalid", id=1)

    def test_init_with_negative_y(self):
        """Test initializing Rectangle with negative y."""
        with self.assertRaises(ValueError):
            Rectangle(width=10, height=20, x=5, y=-7, id=1)

    def test_str_representation(self):
        """Test the __str__ representation of Rectangle."""
        rect = Rectangle(width=10, height=20, x=5, y=7, id=1)
        self.assertEqual(str(rect), "[Rectangle] (1) 5/7 - 10/20")

    def test_str_representation_w_h(self):
        rect = Rectangle(1, 2)
        self.assertEqual(str(rect), "[Rectangle] (3) 0/0 - 1/2")

    def test_str_representation_w_h_x(self):
        rect = Rectangle(1, 2, 3)
        self.assertEqual(str(rect), "[Rectangle] (4) 3/0 - 1/2")

    def test_str_representation_whxy(self):
        rect = Rectangle(1,2,3,4)
        self.assertEqual(str(rect), "[Rectangle] (5) 3/4 - 1/2")

    def test_area_calculation(self):
        """Test calculating the area of Rectangle."""
        rect = Rectangle(width=10, height=20, x=5, y=7, id=1)
        self.assertEqual(rect.area(), 200)

    def test_display_method(self):
        """Test the display method of Rectangle."""
        rect = Rectangle(width=3, height=2, x=1, y=1, id=1)
        expected_output = "\n ###\n ###\n"
        captured_output = io.StringIO()
        sys.stdout = captured_output
        rect.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_update_method_with_args(self):
        """Test the update method of Rectangle with arguments."""
        rect = Rectangle(width=10, height=20, x=5, y=7, id=1)
        rect.update(2, 15, 25, 8, 10)
        self.assertEqual(rect.id, 2)
        self.assertEqual(rect.width, 15)
        self.assertEqual(rect.height, 25)
        self.assertEqual(rect.x, 8)
        self.assertEqual(rect.y, 10)

    def test_update_method_with_kwargs(self):
        """Test the update method of Rectangle with keyword arguments."""
        rect = Rectangle(width=10, height=20, x=5, y=7, id=1)
        rect.update(id=2, width=15, height=25, x=8, y=10)
        self.assertEqual(rect.id, 2)
        self.assertEqual(rect.width, 15)
        self.assertEqual(rect.height, 25)
        self.assertEqual(rect.x, 8)
        self.assertEqual(rect.y, 10)


if __name__ == '__main__':
    unittest.main()
