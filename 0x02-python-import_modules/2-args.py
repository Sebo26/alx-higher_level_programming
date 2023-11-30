#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg = sys.argv
    length = len(arg) - 1

    if length == 0:
        print("{} arguments.".format(length))
    elif length > 1:
        print("{} arguments:".format(length))
        for n in range(1, length + 1):
            print("{}: {}".format(n, arg[n]))
    else:
        print("{} argument:".format(length))
        print("{}: {}".format(length, arg[1]))
