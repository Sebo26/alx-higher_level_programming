#!/usr/bin/python3
"""The function prints a square made of #"""


def print_square(size):
    """Prints the square made of #"""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for m in range(size):
            print('#')
    print()
