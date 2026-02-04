#!/usr/bin/python3
""" Class Rectangle inherite from BaseGeometry """


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """ Class Rectangle inherite BaseGeometry """
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)

    def area(self):
        return (self.__width * self.__height)

    def __str__(self):
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
