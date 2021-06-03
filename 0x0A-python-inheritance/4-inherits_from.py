#!/usr/bin/python3
"""Module have a function verify inherit classes"""


def inherits_from(obj, a_class):
    """determinates is obj is inherits of class
    Args:
      obj (object): object
      a_class (object): object
    Returns:
       True : yes
       False : No
    """
    return isinstance(obj.__class__, a_class)
