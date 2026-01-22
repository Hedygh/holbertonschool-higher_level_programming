#!/usr/bin/python3
"""Function that add two integers.



"""


def add_integer(a, b=98):
    """
    :param a: int to add :param b: int to add
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
