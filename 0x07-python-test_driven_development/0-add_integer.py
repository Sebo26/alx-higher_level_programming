def add_integer(a, b=98):
    if type(a) and type(b) not in [int, float]:
        raise TypeError("a must be an integer")
    if a or b is float:
        a = int(a)
        b = int(b)
    return a + b
