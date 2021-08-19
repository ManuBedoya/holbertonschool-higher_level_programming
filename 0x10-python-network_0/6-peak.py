#!/usr/bin/python3
"""Fin the pick
"""

def find_peak(list_of_integers):
    """Method to find the pick
    """
    if len(list_of_integers) == 0:
        return (None)
    else:
        list_of_integers.sort()
        return (list_of_integers[-1])
