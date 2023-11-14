#!/usr/bin/python3

"""
Unit tests for the Base class.

These tests cover various scenarios for initializing instances of
the Base class with different types of 'id' parameters.

Tested scenarios include:
- Initializing with an integer 'id'.
- Initializing with a float 'id'.
- Initializing with a string 'id'.
- Initializing with a list 'id'.
- Initializing with a tuple 'id'.
- Initializing with a dictionary 'id'.
- Initializing with a boolean 'id'.
- Initializing multiple instances to ensure unique 'id' values.
- Checking the value of the class variable __nb_objects
after multiple instances are created.

"""

import unittest
from models.base import Base

class TestBaseClass(unittest.TestCase):

    def test_init_with_int_id(self):
        """Test initializing with an integer 'id'."""
        obj = Base(id=42)
        self.assertEqual(obj.id, 42)

    def test_init_with_float_id(self):
        """Test initializing with a float 'id'."""
        obj = Base(id=3.14)
        self.assertEqual(obj.id, 3.14)

    def test_init_with_string_id(self):
        """Test initializing with a string 'id'."""
        obj = Base(id="abc")
        self.assertEqual(obj.id, "abc")

    def test_init_with_list_id(self):
        """Test initializing with a list 'id'."""
        custom_list = [1, 2, 3]
        obj = Base(id=custom_list)
        self.assertEqual(obj.id, custom_list)

    def test_init_with_tuple_id(self):
        """Test initializing with a tuple 'id'."""
        custom_tuple = (4, 5, 6)
        obj = Base(id=custom_tuple)
        self.assertEqual(obj.id, custom_tuple)

    def test_init_with_dict_id(self):
        """Test initializing with a dictionary 'id'."""
        custom_dict = {"key": "value"}
        obj = Base(id=custom_dict)
        self.assertEqual(obj.id, custom_dict)

    def test_init_with_bool_id(self):
        """Test initializing with a boolean 'id'."""
        obj_true = Base(id=True)
        obj_false = Base(id=False)
        self.assertEqual(obj_true.id, True)
        self.assertEqual(obj_false.id, False)

    def test_init_with_multiple_instances(self):
        """Test initializing multiple instances to ensure unique 'id' values."""
        obj1 = Base()
        obj2 = Base()
        self.assertNotEqual(obj1.id, obj2.id)

    def test_base_to_json_string_none(self):
        """Test to json string"""
        self.assertEqual(Base.to_json_string(None), [])

    def test_base_to_json_string_empty_list(self):
        self.assertEqual(Base.to_json_string([]), [])
if __name__ == '__main__':
    unittest.main()
