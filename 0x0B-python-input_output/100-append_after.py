#!/usr/bin/python3
"""Module to manage files"""


def append_after(filename="", search_string="", new_string=""):
    """Insert new_string the search_string"""
    with open(filename, 'r+') as file:
        lines = file.readlines()
        for i, line in enumerate(lines):
            if line.startswith(search_string):
                lines[i] = lines[i].strip() + new_string
        file.seek(0)
        for line in lines:
            file.write(line)
