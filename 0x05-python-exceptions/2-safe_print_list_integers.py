#!/usr/bin/python3
count = 0
def safe_print_list_integers(my_list=[], x=0):
    for i in range(x):
        try:
            value = my_list[i]
            if isinstance(value, int):
                print("{:d}".format(value), end=" ")
                count += 1
        except IndexError:
        pass
    print()
    return count
                
