#!/usr/bin/python3
"""Module to have a function verify instances"""


def is_kind_of_class(obj, a_class):
    if isinstance(obj.__class__, a_class) or\
       issubclass(obj.__class__, a_class):
        return True
    return False
