#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    length = len(my_list)
    if idx < 0 or idx > length - 1:
        return my_list
    else:
        number = my_list[i]
        my_list.remove(number)