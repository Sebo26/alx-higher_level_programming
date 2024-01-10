#!/usr/bin/python3
"""The function prints text with 2 line after special characters"""


def text_indentation(text):
    """prints two lines after '.', '?', ':'"""
    if text in ['.', '?', ':']:
        print('\n')
        print('\n')
    elif not isinstance(text, str):
        raise TypeError("text must be a string")
