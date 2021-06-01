#!/usr/bin/python3
""" Define class MyList that inherit from list. """


class MyList(list):
    """ Method sorted print inside Mylist class. """

    def print_sorted(self):
        """ Method sorted print to display sorted list. """
        print(sorted(self))
