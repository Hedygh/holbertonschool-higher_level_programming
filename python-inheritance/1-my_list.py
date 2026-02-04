#!/usr/bin/python3
""" class Mylist """


class MyList(list):
    """ class mylist inherite from list """
    def print_sorted(self):
        print(sorted(self))
