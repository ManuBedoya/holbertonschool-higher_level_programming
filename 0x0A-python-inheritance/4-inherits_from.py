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
    if type(obj) != a_class:
        if isinstance(obj, a_class):
            return True
        else:
            return False
    return False
