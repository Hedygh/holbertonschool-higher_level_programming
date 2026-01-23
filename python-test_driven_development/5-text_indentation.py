#!/usr/bin/python3
"""This module provides a function that prints text with indentation rules."""


def text_indentation(text):
    """Print text with 2 new lines after '.', '?' and ':'."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    new_line = True  # True = we are at the start of a line
    for ch in text:
        if ch == " " and new_line:
            continue
        print(ch, end="")
        new_line = False
        if ch in ".?:":
            print("\n")
            new_line = True
