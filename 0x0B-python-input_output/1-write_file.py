#!/usr/bin/python3
"""Function writes a string to a text file and return No of chr"""


def write_file(filename="", text=""):
    """Writes string and return number of characters"""
    with open(filename, mode="w", encoding="utf-8") as myFile:
        return (myFile.write(text))
