#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for numbers in range(x):
            print("{}".format(my_list[numbers], end=" ")
            count = count + 1
    except IndexError:
        print("Index doesn't exist")
        pass
        print("\n")
        return count
