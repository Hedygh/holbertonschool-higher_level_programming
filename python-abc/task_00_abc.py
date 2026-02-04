#!/usr/bin/python3
""" Abstract class Animal """


from abc import ABC, abstractmethod


class Animal(ABC):
    """ Abstract class Animal """
    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    """ Sub class Dog """
    def sound(self):
        return ("Bark")


class Cat(Animal):
    """ Sub class Cat"""
    def sound(self):
        return ("Meow")
