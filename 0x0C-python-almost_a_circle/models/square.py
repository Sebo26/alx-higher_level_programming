#!/usr/bin/python3
"""Makes class Square that inherits from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Create class Square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Create attributes of the square"""
        super().__init__(id, x, y, size, size)

    @property
    def width(self):
        """Return getter and sets properties for width"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Return getter and sets properties for height"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    def __str__(self):
        """Return a string stating values of square"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)
