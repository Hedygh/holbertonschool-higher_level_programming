#!/usr/bin/python3
""" Addition of integer """


def add_integer(a, b=98):
    """ Add two integer a and b

    Arguments are checked for error type and casted into int
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
