#!/usr/bin/python3
"""Checks if function is an instance of an inheritance"""


def inherits_from(obj, a_class):
    """Checks instance of a class that inherited from"""
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False
