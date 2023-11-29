#!/usr/bin/python3
def uppercase(str):
    for letters in str:
        if 'a' <= letters <= 'z':
            print("{}"
                    .format(chr(ord(letters) - ord('a') + ord('A')), end=""))
        else:
            print("{}".format(letters), end="")
