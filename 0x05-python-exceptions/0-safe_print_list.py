#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    for numbers in range(x):
        try:
            print("{}".format(my_list[numbers], end=" "))
            count = count + 1
    except IndexError:
        pass 
    print(" ")
    return count
