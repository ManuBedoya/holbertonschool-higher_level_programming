#!/usr/bin/python3
""" In this module, testing related to Base class will be done. """
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):
    """ Test the base class """

    def test_without_arguments(self):
        """ Test cases witout ids """
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

    def test_errors(self):
        b4 = Base('2')
        self.assertRaises(TypeError)
        b4 = Base(-1)
        self.assertRaises(ValueError)

    def test_to_json_string(self):
        json_string = Base.to_json_string(None)
        self.assertEqual(json_string, '[]')

    def test_from_json_string(self):
        json_string = Base.from_json_string(None)
        self.assertEqual(json_string, [])
