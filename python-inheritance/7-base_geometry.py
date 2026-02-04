#!/usr/bin/python3
""" BaseGeometry Class """


class BaseGeometry:
    """ BaseGeometry Class """
    def area(self):
        """ area method """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ integer validator method """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
