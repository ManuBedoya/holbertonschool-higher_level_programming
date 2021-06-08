#!/usr/bin/python3
""" In this module, testing related to Base class will be done. """
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """ Test the base class """

    def test_init(self):
        """ Test cases of normal initialization """
        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base()
        self.assertEqual(b2.id, 2)

        b3 = Base()
        self.assertEqual(b3.id, 3)

        b4 = Base(12)
        self.assertEqual(b4.id, 12)

        b4 = Base()
        self.assertEqual(b4.id, 4)
