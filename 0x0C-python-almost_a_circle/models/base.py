#!/usr/bin/python3
"""This file stores the class Base"""


class Base:
    """Class wil be the Base of other classes"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Manages id to avoid duplications"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
