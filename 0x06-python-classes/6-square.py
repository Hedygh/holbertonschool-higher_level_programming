#!/usr/bin/python3
""" Defines class Square with size attribute.
    Raise error for type and value.
    Calculate and return the square area"""


class Square:
    """ Define Square class."""

    def __init__(self, size=0, position=(0, 0)):
        """ Initialize the square.


        Args:
            size (int): Size of the square.
            position (tuple): Position of the square.
        """
        self.size = size
        self.position = position

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
        self.__size = value

    @property
    def position(self):
        """ Return position of the square. """
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                value[0] < 0 or value[1] < 0 or
                len(value) != 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """ Calculate area of the square.


        Returns:
            Area value.
        """
        return (self.__value * self.__value)

    def my_print(self):
        """ Print the current square fill with '#'
        """
        if self.__size == 0:
            print()
            return
        for i in range(self.__position[1]):
            print()
        for i in range(self.__size):
            for n in range(self.__position[0]):
                print(" ", end='')
            for j in range(self.__size):
                print("#", end='')
            print()
