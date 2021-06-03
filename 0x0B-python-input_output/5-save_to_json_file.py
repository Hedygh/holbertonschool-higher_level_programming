#!/usr/bin/python3
""" save to json file """


import json


def save_to_json(my_obj, filename):
    """ save to json module """
    with open(filename, 'w') as f:
        json.dump(my_obj, filename)
    f.closed
