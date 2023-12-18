#!/usr/bin/python3
def safe_print_division(a, b):
    quotient = None
    try:
        quotient = int(a) / int(b)
    except ZeroDivisionError:
        print("You cannot divide by 0")
    finally:
        print("Inside result: {}".format(quotient))
