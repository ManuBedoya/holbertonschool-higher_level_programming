#!/usr/bin/python3
"""This module is to create a rectangle
"""
import sys
from .base import Base


class Rectangle(Base):
    """Rectangle class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """this is the init method
        Args:
           width (int): size_width
           height (int): size_height
           x (int): position_x
           y (int): position_y
           id (int): id
        """

        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """method width
        Returns:
           The width
        """

        return self.__width

    @width.setter
    def width(self, value):
        """method width
           Set the width
        """

        if type(value) != int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        """method heigth
        Returns:
           The height
        """

        return self.__height

    @height.setter
    def height(self, value):
        """method width
        Returns:
           The width
        """
        if type(value) != int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        """method width
        Returns:
           The width
        """

        return self.__x

    @x.setter
    def x(self, value):
        """method width
        Returns:
           The width
        """

        if type(value) != int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        """method width
        Returns:
           The width
        """

        return self.__y

    @y.setter
    def y(self, value):
        """method width
        Returns:
           The width
        """

        if type(value) != int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """method width
        Returns:
           The width
        """

        return self.__width * self.__height

    def display(self):
        """method width
        Returns:
           The width
        """

        for i in range(self.__y):
            print()
        for i in range(self.__height):
            print(' ' * self.__x, end='')
            print('#' * self.__width, file=sys.stdout)

    def update(self, *args, **kwargs):
        """method width
        Returns:
           The width
        """

        if args is None or len(args) == 0:
            for item in kwargs:
                if hasattr(self, item):
                    if item == 'id':
                        self.id = kwargs[item]
                    if item == 'width':
                        self.width = kwargs[item]
                    if item == 'height':
                        self.height = kwargs[item]
                    if item == 'x':
                        self.x = kwargs[item]
                    if item == 'y':
                        self.y = kwargs[item]
        else:
            len_args = len(args)

            if (len_args > 0):
                self.id = args[0]

            if (len_args > 1):
                self.width = args[1]

            if (len_args > 2):
                self.height = args[2]

            if (len_args > 3):
                self.x = args[3]

            if (len_args > 4):
                self.y = args[4]

    def to_dictionary(self):
        """method width
        Returns:
           The width
        """

        return {'id': self.id, 'width': self.__width, 'height': self.__height,
                'x': self.__x, 'y': self.__y}

    def __str__(self):
        """method width
        Returns:
           The width
        """

        return '[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}'.format(self.id,
                                                                 self.__x,
                                                                 self.__y,
                                                                 self.__width,
                                                                 self.__height)
