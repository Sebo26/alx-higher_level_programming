#!/usr/bin/python3

"""Define class named Square"""


class Square:
    """The square class"""
    pass
    def __init__(self, size=0):
        """initializing new square with attribute size"""
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
    
    def area(self):
        return int(self.__size) * int(self.__size)
