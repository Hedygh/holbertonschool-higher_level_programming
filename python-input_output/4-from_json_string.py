#!/usr/bin/python3
"""Convert a JSON string to a Python object."""

import json


def from_json_string(my_str):
    """Return a Python object from a JSON string."""
    return json.loads(my_str)
