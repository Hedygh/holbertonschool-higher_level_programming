#!/usr/bin/python3
""" Defines class Square with size attribute.
    Raise error for type and value.
    Calculate and return the square area"""


class Square:
    """ Define Square class."""

    def __init__(self, size=0):
        """ Initialize the square.


        Args:
            size (int): Size of the square.
        """
        self.size = size

    @property
    def size(self):
        return self.__value

    @size.setter
    def size(self, value):
        self.__value = value
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """ Calculate area of the square.


        Returns:
            Area value.
        """
        return (self.__value * self.__value)
