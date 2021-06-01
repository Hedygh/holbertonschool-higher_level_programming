#!/usr/bin/python3
""" Defines class Rectangle that inherits from BaseGeometry """
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle class """
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        """ return area of rectangle """
        return (self.__height * self.__width)

    def __str__(self):
        """ return string representation of rectangle """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
