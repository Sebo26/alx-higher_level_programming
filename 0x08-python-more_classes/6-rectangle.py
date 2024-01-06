#!/usr/bin/python3

"""Define a class called rectangle"""


class Rectangle:
    """The rectangle class"""
    pass

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initializing width and height"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (2 * self.__width) + (2 * self.__height)

    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ""
        else:
            return '#' * self.__width + '\n'

    def __repr__(self):
        width_rect = str(self.__width)
        height_rect = str(self.__height)
        return "Rectangle(" + width_rect + ", " + height_rect + ")"

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
