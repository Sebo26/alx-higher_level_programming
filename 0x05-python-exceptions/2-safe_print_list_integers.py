#!/usr/bin/python3
class NotDigit(Exception):
    pass

def safe_print_list_integers(my_list=[], x=0):
    try:
        for i in range(x):
            if not my_list[i].isnumeric():
                raise NotDigit
            print("{:d}".format(int(my_list[i])), end=" ")
    except (ValueError, NotDigit):
            print("Not an integer", end=" ")
    print()
                
