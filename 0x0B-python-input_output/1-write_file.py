#!/usr/bin/python3
""" write file """


def write_file(filename='', text=''):
    """ write text in file """
    count = 0
    with open(filename, 'w', encoding='UTF-8') as f:
        count = f.write(text)
    f.closed
    return count
