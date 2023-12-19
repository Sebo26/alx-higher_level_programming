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

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

    def my_print(self):
        if self.__size == 0:
            print("\n")
        else:
            for m in range(self.__size):
                for n in range(self.__size):
                    print("#", end="")
                print()
