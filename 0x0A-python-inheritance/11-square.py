#!/usr/bin/python3
"""Module to create a BaseGeometry class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class
    """
    def __init__(self, size):
        super().__init__(size, size)
        self.__size = size

    def area(self):
        return self.__size ** 2

    def __str__(self):
        return '[Square] {:d}/{:d}'.format(str(self.__size), str(self.__size))
