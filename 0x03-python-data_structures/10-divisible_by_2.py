#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    for i in my_list:
        modulos = my_list[i] % 2
        if modulos == 0:
            print(i)
            return True
        else:
            return False
