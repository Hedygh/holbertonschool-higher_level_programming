#!/usr/bin/python3
""" Defines class Rectangle that inherits from BaseGeometry """


class Rectangle(BaseGeometry):
    """ Rectangle class """
    def __init__(self, width, height):
        self.intself.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
