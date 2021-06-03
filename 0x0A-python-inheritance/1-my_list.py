#!/usr/bin/python3
"""Module to create a class inherit"""


class MyList(list):
    """This is the MyList class"""

    def print_sorted(self):
        """print the list in sort
        """
        new_list = self[:]
        new_list.sort()
        print(new_list)
