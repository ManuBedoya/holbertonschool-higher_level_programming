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
