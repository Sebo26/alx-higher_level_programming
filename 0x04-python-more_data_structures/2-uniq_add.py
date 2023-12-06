#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_set = set(my_list)
    def summation(a, b):
        return a + b
    print(list(map(summation, unique_set)))
