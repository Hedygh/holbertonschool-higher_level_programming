#!/usr/bin/python3
""" Defines class BaseGeometry """


class BaseGeometry():
    """ Class basegeometry """
    def area(self):
        """ Raise exception """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ method integer validator """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
