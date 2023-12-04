#!/usr/bin/python3
def max_integer(my_list=[]):
    length = len(my_list)
    if length == 0:
        return None
    else:
        my_list.sort()
        max_num = my_list[-1]
        return max_num
