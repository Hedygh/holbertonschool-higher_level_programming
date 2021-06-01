#!/usr/bin/python3
""" Define class MyList that inherit from list """


class MyList(list):
    """ Method sorted print """
    def print_sorted(self):
        """ sorted print """
        print(sorted(self))
