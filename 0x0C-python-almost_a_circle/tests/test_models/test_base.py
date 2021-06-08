#!/usr/bin/python3
""" In this module, testing related to Base class will be done. """
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """ Test the base class """

    def test_without_arguments(self):
        """ Test cases of normal initialization """
        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base()
        self.assertEqual(b2.id, 2)

        b3 = Base()
        self.assertEqual(b3.id, 3)

        b4 = Base()
        self.assertEqual(b4.id, 4)

        b4 = Base()
        self.assertEqual(b4.id, 5)

    def test_with_arguments(self):
        """ Test cases of normal initialization """
        b1 = Base(8)
        self.assertEqual(b1.id, 8)

        b2 = Base(4)
        self.assertEqual(b2.id, 4)

        b3 = Base(1)
        self.assertEqual(b3.id, 1)

        b4 = Base(25)
        self.assertEqual(b4.id, 25)

        b4 = Base(123)
        self.assertEqual(b4.id, 123)
