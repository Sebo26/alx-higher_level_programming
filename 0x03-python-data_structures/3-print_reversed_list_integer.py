#!/usr/bin/python3
def print_list_integer(my_list=[]):
    length = len(my_list)
    for i in range(length):
        my_list.reverse()
        print("{:d}".format(my_list[i]))
