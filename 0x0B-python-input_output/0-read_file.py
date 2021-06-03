#!/usr/bin/python3
""" Read file module """


def read_file(filename=""):
    with open(filename, encoding="UTF-8") as f:
        read_file = f.read()
        print(read_file, end='')
    f.closed
