#!/usr/bin/python3
class NotDigit(Exception):
    pass

def safe_print_list_integers(my_list=[], x=0):
    for i in range(x):
        try:
            if not my_list[i].isnumeric():
                raise NotDigit
            print("{:d}".format(int(my_list[i])), end=" ")
        except (ValueError, NotDigit):
            print("Not an integer", end=" ")
    print()
                
