#!/usr/bin/python3
"""The function prints the first and last name inside a string"""


def say_my_name(first_name, last_name=""):
    """Prints first name and last name inside a string"""
    if not isinstance(first_name, str) or not isinstance(last_name, str):
        raise TypeError("first_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
