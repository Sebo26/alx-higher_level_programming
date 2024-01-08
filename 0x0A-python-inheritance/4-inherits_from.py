#!/usr/bin/python3
"""Checks if function is an instance of an inheritance"""


def inherits_from(obj, a_class):
    if issubclass(obj, a_class):
        return True
    else:
        return False
