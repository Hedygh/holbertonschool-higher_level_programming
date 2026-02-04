#!/usr/bin/python3
""" class Square inherite from Rectangle"""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """ Class square inherite Rectangle """
    def __init__(self, size):
        self.__size = size
        self.integer_validator("size", self.__size)
        super().__init__(size, size)

    def area(self):
        return (self.__size * self.__size)

    def __str__(self):
        return ("[Square] {}/{}".format(self.__size, self.__size))
