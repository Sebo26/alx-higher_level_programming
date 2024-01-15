#!/usr/bin/python3
"""Define Rectangle which inherits from Base"""
from models.base import Base


class Rectangle(Base):
    """Create class Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Create the private instance attributes and getters/setters"""
        super().__init__(id)
        self.__width = __width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """Return getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets properties for value of width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value = 0 or value < 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Return getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets properties for the value of height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value = 0 or value < 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """Return getter for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Sets properties for the value of x"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """Return getter for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Sets properties for the value of y"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value
