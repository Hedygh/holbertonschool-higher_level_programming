#!/usr/bin/python3
""" Class Mylist """


class MyList(list):
    """ class mylist inherite from list """

    def print_sorted(self):
        """ print sorted list """
        print(sorted(self))
