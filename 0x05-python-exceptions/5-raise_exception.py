#!/usr/bin/python3
def raise_exception():
    try:
        raise TypeError("Type error")
    except TypeError as e:
        print(f"Exception raised: {e}")
