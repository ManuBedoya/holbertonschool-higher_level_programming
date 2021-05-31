#!/usr/bin/python3
"""Read a file
"""


def read_file(filename=""):
    """This is the read_file method
    Is to read a file
    Args:
       filename (str): Name of the file
    """
    with open(filename, enconding='utf-8') as file:
        read_data = file.read()
    print(read_data)
