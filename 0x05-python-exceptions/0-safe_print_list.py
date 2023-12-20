#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for numbers in range(x):
            print("{}".format(my_list[numbers], end=" "))
            count = count + 1
    except IndexError:
        if x < 0 or x > count:
            print("Index doesn't exist")
    print("\n")
    return count
