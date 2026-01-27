#!/usr/bin/python3
""" class Square that defines a square """


class Square:
    """ square class """

    def __init__(self, size=0, position=(0, 0)):
        """ initialise size of square """
        self.size = size
        self.position = position

    @property
    def size(self):  # getter permet de lire une valeur privée
        """ get current size """
        return self.__size

    @size.setter
    def size(self, value):
        """ Set the size """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if isinstance(value, int) and value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """ get current position """
        return self.__position

    @position.setter
    def position(self, value):
        """ set the position """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not isinstance(value[0], int)
                or not isinstance(value[1], int) or
                value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """ Return current square area """
        return (self.__size * self.__size)

    def my_print(self):
        """ print square """
        if self.__size == 0:
            print()
            return
        for _ in range(self.__position[1]):
            print()
        for i in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
