#!/usr/bin/python3

"""Define a class called rectangle"""


class Rectangle:
    """The rectangle class"""
    pass

def __init__(self, width=0, height=0):
    """initializing width and height"""
    self.__width = width
    self.__width = height

    @property
    def width(self):
    """getting the width of the rectangle"""
        return int(self.__width)

    @width.setter
    def width(self, value):
    """setting the width of the triangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
    """getting the height of the rectangle"""
        return int(self.__length)

    @height.setter
    def height(self, value):
    """Setting the height of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
