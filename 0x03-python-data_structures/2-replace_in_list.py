#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    length = len(my_list)
    if idx >= 0 or idx < length:
        my_list[idx] = element
        print(my_list)
    else:
        print(my_list)
