#!/usr/bin/python3
""" Duck typing """


from abc import ABC, abstractmethod

PI = 3.141592653589793


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
        return PI * self.radius ** 2

    def perimeter(self):
        """ perimeter method """
        return 2 * PI * self.radius


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
        return 2 * (self.width + self.height)


def shape_info(shape):
    """ duck typing function """
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())
