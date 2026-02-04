#!/usr/bin/python3
""" Class with inverted comparison """


class MyInt(int):
    """ Class MyInt """
    def __eq__(self, other):
        return int.__ne__(self, other)

    def __ne__(self, other):
        return int.__eq__(self, other)
