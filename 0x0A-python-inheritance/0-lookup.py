#!/usr/bin/python3
"""The function looksup attributes and methods in object"""


def lookup(obj):
    """Return the list of attributes in object"""
    items = dir(obj)
    return items
