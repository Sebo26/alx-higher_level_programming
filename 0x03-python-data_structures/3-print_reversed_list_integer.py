#!/usr/bin/python3
def print_list_integer(my_list=[]):
    length = len(my_list)
    new_list = my_list.copy()
    new_list.reverse()
    for i in range(length):
        print("{:d}".format(new_list[i]))
