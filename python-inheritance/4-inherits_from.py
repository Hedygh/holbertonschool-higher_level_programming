#!/usr/bin/python3
""" inheritance class """


def inherits_from(obj, a_class):
    """ Inheritance from a_class """
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    else:
        return False
