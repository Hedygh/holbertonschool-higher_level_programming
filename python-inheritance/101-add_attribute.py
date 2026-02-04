#!/usr/bin/python3
""" add attribute to an object """


def add_attribute(obj, name, value):
    """ add attribute method """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
