#!/usr/bin/python3
"""This module provides a function that adds two integers."""


def add_integer(a, b=98):
    """Return the addition of a and b as integers.

    a and b must be integers or floats. Floats are cast to integers before
    performing the addition.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if isinstance(a, bool) or not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if isinstance(b, bool) or not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
