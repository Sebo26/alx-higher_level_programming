#!/usr/bin/python3
"""Function appends string at end of file"""


def append_write(filename="", text=""):
    """Appends string to file and return number of characters"""
    with open(filename, mode="a", encoding="utf-8") as myFile:
        return (myFile.write(text))
