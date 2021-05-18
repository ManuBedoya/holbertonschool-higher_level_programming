#!/usr/bin/python3
class Square:

    def __init__(self, size=0):
     self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
         if (type(value) != int):
             raise TypeError("size must be an integer")
         elif (value < 0):
             raise ValueError("size must be >= 0")
         else:
             self.__size = int(value)

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if (self.__size == 0):
            print()
        for row in range(self.__size):
            for col in range(self.__size):
                print("#", end='')
            print()