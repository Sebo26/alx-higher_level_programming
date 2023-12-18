#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    try:
        for num1 in my_list_1:
        for num2 in my_list_2:
            product = num1 / num2
            return product
    except ZeroDivisionError:
        print(division by 0)

