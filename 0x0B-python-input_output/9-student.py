#!/usr/bin/python3
"""Class student that defines students"""


class Students:
    """This class represents a students"""

    def __init__(self, first_name, last_name, age):
        """Sudents are define by names and age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves a dictionary representation of a Student"""
        return self.__dict__
