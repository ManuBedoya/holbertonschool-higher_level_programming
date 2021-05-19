#!/usr/bin/python3
"""Module to create a class
"""


class Square:
    """This is the Square class
    """
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def position(self):
        """this is a position method
        Is to get the position
        Returns:
           The position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """This is a position method
        Is to set the value of the position
        Args:
            value (tuple): position
        """
        if isinstance(value, tuple) and len(value) == 2 \
           and isinstance(value[0], int)\
           and isinstance(value[1], int) \
           and value[0] >= 0 and value[1] >= 0:
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    @property
    def size(self):
        """This is a size method
        Is to get the size of the square
        Returns:
            The square's size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """This is a size method
        Is to set the square's size
        Args:
           value (int): new size of the square
        """
        if (type(value) != int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = int(value)

    def area(self):
        """This is the area method
        Is to calculate the area of the square
        Returns:
           The area of the square
        """
        return self.__size ** 2

    def my_print(self):
        """This is the my_print method
        Is to print the square with #
        """
        if (self.__size == 0):
            print()

        for row in range(self.__size):
            for i in range(self.__position[0]):
                print(" ", end="")
            for col in range(self.__size):
                print("#", end="")
            print()
