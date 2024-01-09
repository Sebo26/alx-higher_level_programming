#!/usr/bin/python3
"""Function reads file and prints it in the stdout"""


def read_file(filename=""):
    """Definition for file to be read"""
    with open(filename, encoding="utf-8") as myFile:
        print(myFile.read(), end="")
