#!/usr/bin/python3
""" class Square that defines a square """


class Square:
    """ square class """

    def __init__(self, size=0):
        """ initialise size of square """
        self.size = size

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

    def area(self):
        """ Return current square area """
        return (self.__size * self.__size)

    def my_print(self):
        """ print square """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
