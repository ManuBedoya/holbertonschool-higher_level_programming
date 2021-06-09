#!/usr/bin/python3
"""Test of rectangle
"""
import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):
    """Class of tests
    """
    def test_init(self):
        """Init a rectangle normally
        """
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.width, 10)

        r2 = Rectangle(10, 2, 0, 0, 23)
        self.assertEqual(r2.height, 2)

    def test_error_types(self):
        """Test of errors
        """
        try:
            r1 = Rectangle(1, '2')
        except Exception as err:
            pass
        self.assertRaises(TypeError)

        try:
            r2 = Rectangle('1', 2)
        except Exception as err:
            pass
        self.assertRaises(TypeError)

    def test_error_values(self):
        """Test with arguments negatives
        """
        try:
            r1 = Rectangle(-10, 6)
        except Exception as err:
            pass
        self.assertRaises(ValueError)

        try:
            r1 = Rectangle(8, -6)
        except Exception as err:
            pass
        self.assertRaises(ValueError)


        try:
            r1 = Rectangle(0, 6)
        except Exception as err:
            pass
        self.assertRaises(ValueError)

        try:
            r1 = Rectangle(8, 0)
        except Exception as err:
            pass
        self.assertRaises(ValueError)
