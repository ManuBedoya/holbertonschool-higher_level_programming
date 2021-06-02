#!/usr/bin/python3
"""Module to have a function that adds new attributes
"""


def add_attribute(a_class, name, value):
    types = ['str', [], {}, (1, 1), 1.1, 1, None]
    for item in types:
        if type(a_class) == type(item):
            raise TypeError("can't add new attribute")
    a_class.name = value
