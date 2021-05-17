#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        res = fct(*args)
    except Exception as e:
        print("Exceptions: {}".format(e), file=sys.stderr)
        return None
    return res
