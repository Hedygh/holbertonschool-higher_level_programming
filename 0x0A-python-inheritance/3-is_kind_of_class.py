#!/usr/bin/python3
""" Defines is kind of class function. """


def is_kind_of_class(obj, a_class):
    """ is_kind_of_class function
        see if obj is an instance of class
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
