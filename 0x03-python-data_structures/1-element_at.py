#!/usr/bin/python3
def element_at(my_list, idx):
    length = len(my_list)
    if idx < 0 or idx >= length:
        return "None"
    else:
        print("Element at index {} is {}".format(idx, my_list[i]))