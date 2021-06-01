#!/usr/bin/python3
""" Function inherits from. """


def inherits_from(obj, a_class):
    """ check if obj inherit from a class """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False
