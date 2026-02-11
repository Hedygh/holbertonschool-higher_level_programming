#!/usr/bin/python3
"""Append a string to a text file (UTF-8)."""


def append_write(filename="", text=""):
    """Append text to a file and return number of characters added."""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
