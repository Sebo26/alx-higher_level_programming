#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_set = set(my_list)
    print(list(map((lambda a, b: a + b), unique_set)))
