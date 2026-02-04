#!/usr/bin/python3
""" test of ihneritance """


def is_kind_of_class(obj, a_class):
    """ check for obj of a_class """
    if isinstance(obj, a_class):
        return True
    else:
        return False
