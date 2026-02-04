#!/usr/bin/python3
""" class Square inherite from Rectangle"""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """ Class Square inherite Rectangle """
    def __init__(self, size):
        self.__size = size
        self.integer_validator("size", self.__size)
        super().__init__(size, size)

    def area(self):
        return (self.__size * self.__size)
