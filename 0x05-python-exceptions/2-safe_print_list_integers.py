#!/usr/bin/python3
count = 0
def safe_print_list_integers(my_list=[], x=0):
    global count
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError):
            pass
    print("")
    return count
                
