#!/usr/bin/python3
def uppercase(str):
    for letters in str:
        if 'a' <= letter <= 'z':
            print("{}"
                    .format(chr(ord(letters) - ord('a') + ord('A')), end="")
        else:
            print("{}".format(letter), end="")
