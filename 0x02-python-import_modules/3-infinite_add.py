#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg = sys.argv
    length = len(arg) - 1
    add = 0
    if length == 0:
        print("{}".format(length))
    else:
        i = 1
        while i <= length:
            add = add + int(argv[i])
            i = i + 1
        print("{}".format(add))
