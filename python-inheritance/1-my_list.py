#!/usr/bin/python3
""" Class MyList """


class MyList(list):
    """ class MyList inherite from list """

    def print_sorted(self):
        """ print sorted list """
        print(sorted(self))
