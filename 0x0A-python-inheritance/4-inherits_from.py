#!/usr/bin/python3
"""Module have a function verify inherit classes"""


def inherits_from(obj, a_class):
    return isinstance(obj.__class__, a_class)
