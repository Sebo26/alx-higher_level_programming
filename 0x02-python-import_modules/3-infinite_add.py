#!/usr/bin/python3
def add_arg(argv):
    length = len(arg) - 1
    if length == 0:
        print("{}".format(length))
        return
    else:
        i = 1
        add = 0
        while i <= length:
            add = add + int(argv[i])
            i = i + 1
        print("{}".format(add))

if __name__ == "__main__":
    import sys
    add_arg(sys.argv)
