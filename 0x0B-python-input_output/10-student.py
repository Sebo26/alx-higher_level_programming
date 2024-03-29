#!/usr/bin/python3
"""Class student that defines students"""


class Student:
    """This class represents a student"""

    def __init__(self, first_name, last_name, age):
        """Sudents are define by names and age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student"""
        if attrs and isinstance(attrs, list) and all(isinstance(item, str) for item in attrs):
            return {attr: getattr(self, attr) for attr in attrs}
        return self.__dict__
