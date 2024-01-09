#!/usr/bin/python3
"""The function creates an Object from a “JSON file”"""


import json


def load_from_json_file(filename):
    """creates an Object from a “JSON file”"""
    with open(filename, mode="r") as myFile:
        return json.load(myFile)
