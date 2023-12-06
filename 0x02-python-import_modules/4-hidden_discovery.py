#!/usr/bin/python3
if __name == "__main__":
    import hidden_4
    for n in sorted(dir(hidden_4)):
        if n[:2] != '__':
            print("{}".format(n))
