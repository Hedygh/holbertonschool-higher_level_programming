#!/usr/bin/python3
"""This module provides a function that adds two integers."""


def add_integer(a, b=98):
    """Return the addition of a and b as integers.

    a and b must be integers or floats. Floats are cast to integers before
    performing the addition.
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
