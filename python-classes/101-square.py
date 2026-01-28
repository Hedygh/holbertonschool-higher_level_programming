#!/usr/bin/python3
""" Defines class Square with size attribute.
    Raise error for type and value.
    Calculate and return the square area"""


class Square:
    """ Define Square class."""

    def __init__(self, size=0, position=(0, 0)):
        """ Initialize Square.

        Args:
            size (int): Size of square
            position (int, int): position of square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(n, int) for n in value) or
                not all(n >= 0 for n in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        return (self.__size * self.__size)

    def my_print(self):
        if self.__size <= 0:
            print()
            return

        for i in range(0, self.__position[1]):
            print()
        for i in range(0, self.__size):
            for n in range(0, self.__position[0]):
                print(" ", end='')
            for j in range(0, self.__size):
                print("#", end='')
            print()

    def __str__(self):
        if self.__size <= 0:
            return ('')
        for i in range(self.__position[1]):
            print()
        for i in range(self.__size):
            for j in range(self.__position[0]):
                print(" ", end='')
            for n in range(self.__size):
                print("#", end='')
            if i != self.__size - 1:
                print()
        return ('')
