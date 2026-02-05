#!/usr/bin/python3
""" Duck typing """


from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    """ Abstract class Shape """
    @abstractmethod
    def area(self):
        """ area method """
        pass

    @abstractmethod
    def perimeter(self):
        """ perimeter method """
        pass


class Circle(Shape):
    """ sub class Circle """
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """ area method """
        return pi * self.radius ** 2

    def perimeter(self):
        """ perimeter method """
        res = 2 * pi * self.radius
        if res < 0:
            res = -res
        return res


class Rectangle(Shape):
    """ sub class Rectangle"""
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        """ area method """
        return self.width * self.height

    def perimeter(self):
        """ perimeter method """
        res = 2 * (self.width + self.height)
        if res < 0:
            res = -res
        return res


def shape_info(shape):
    """ duck typing function """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
