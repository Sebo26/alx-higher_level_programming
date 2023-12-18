#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for numbers in range(x):
            print("{}".format(my_list[i], end="")
    except IndexError:
        print("Index doesn't exist")
