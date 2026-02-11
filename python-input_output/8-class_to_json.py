#!/usr/bin/python3
"""Return a dictionary description for JSON serialization."""


def class_to_json(obj):
    """Return the dictionary description of obj for JSON serialization."""
    return obj.__dict__
