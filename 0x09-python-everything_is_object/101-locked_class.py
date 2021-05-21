#!/usr/bin/python3
"""Module to create a class
"""


class LockedClass:
    """This is a lockedClass
    """
    __isfrozen = False

    def __init__(self):
        self.first_name = ""
        self._freeze()

    def __setattr__(self, key, value):
        if self.__isfrozen and not hasattr(self, key):
            raise AttributeError("'{}' object has no attribute '{}'".format
                                 (LockedClass.__name__, key))
        else:
            object.__setattr__(self, key, value)

    def _freeze(self):
        self.__isfrozen = True
