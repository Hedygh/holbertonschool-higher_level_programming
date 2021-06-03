#!/usr/bin/python3
""" objet to json string """


import json


def from_json_string(my_str):
    """ json string module """
    new_str = json.dumps(my_str)
    return new_str
