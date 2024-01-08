#!/usr/bin/python3
"""The function checks if two classes are the same"""


def is_same_class(obj, a_class):
    """Checks if a class is an instance of another"""
    if type(obj) == a_class:
        return True
    else:
        return False
