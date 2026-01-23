#!/usr/bin/python3
"""This module provides a function that prints text with indentation rules."""


def text_indentation(text):
    """Print text with 2 new lines after '.', '?' and ':'.

    No spaces are printed at the beginning or at the end of each line.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    i = 0
    while i < len(text):
        ch = text[i]
        if ch in ".?:":
            print(ch, end="")
            print("\n")
            i += 1
            while i < len(text) and text[i] == " ":
                i += 1
            continue
        if ch != " ":
            print(ch, end="")
        else:
            # print spaces only if not at line start (handled by skipping after punctuation)
            print(ch, end="")
        i += 1
