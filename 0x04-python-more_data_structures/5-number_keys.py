#!/usr/bin/python3
def number_keys(a_dictionary):
    summation = 0
    for value in a_dictionary.values():
        summation += value
    return (summation)
