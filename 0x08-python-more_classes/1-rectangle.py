#!/usr/bin/python3

"""Define a class called rectangle"""


class Rectangle:
    """The rectangle class"""
    pass
    def __init__(self, width)
    """initializing rectangle with width"""
    self.__width = width

    @property
    def width(self):
        return int(self.__width)

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")

    def __init__(self, height)
    """initializing rectangle with width"""
    self.__width = height

    @property
    def height(self):
        return int(self.__length)

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
    def __init__(self, width=0, height=0):
