#!/usr/bin/python3
"""The function writes an Object to a text file, using a JSON"""


import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, using a JSON representation"""
    with open(filename, mode="w") as myFile:
        json.dump(my_obj, myFile)
