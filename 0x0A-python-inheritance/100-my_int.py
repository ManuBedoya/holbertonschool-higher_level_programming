#!/usr/bin/python3
"""Module to create MyInt class
"""


class MyInt(int):
    """MyInt class
    """
    def __eq__(self, other):
        return False

    def __ne__(self, other):
        return True
