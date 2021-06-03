#!/usr/bin/python3
""" append write """


def append_write(filename='', text=''):
    """ append string to end of file """
    count = 0
    with open(filename, 'a', encoding='UTF-8') as f:
        count = f.write(text)
    f.closed
    return count
