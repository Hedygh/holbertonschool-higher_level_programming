#!/usr/bin/python3
""" Locked Class """


class LockedClass:
    """ prevent user from creating new instance """
    __slots__ = ["first_name"]
