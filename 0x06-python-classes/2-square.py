#!/usr/bin/python3
""" Defines class Square with size attribute.
    Raise error for type and value."""


class Square:
    """ Define Square class."""
    def __init__(self, size=0):
        """ Initialize the Square.


        Attributes:
            size (int): Size of the Square.
        """
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
