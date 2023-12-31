#!/usr/bin/python3
"""Rectangle that inherits from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class rectengle inheriting BaseGeometry"""

    def __init__(self, width, height):
        """Define the dimensions of Rectangle"""
        super().integer_validator("width", width)
        width = self.__width
        super().integer_validator("height", height)
        height = self.__height
