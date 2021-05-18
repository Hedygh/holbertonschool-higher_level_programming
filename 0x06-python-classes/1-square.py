#!/usr/bin/python3
""" Define size private instance attribute for Square class. """


class Square:
    """Square Class."""
    def __init__(self, size):
        """ Initialize the Square.


        Attributes:
            size (int): Size of the square.
        """
        self.__size = size
