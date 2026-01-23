#!/usr/bin/python3
"""This module provides a function that prints text with indentation rules."""


def text_indentation(text):
    """Print text with 2 new lines after '.', '?' and ':'."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    buf = ""  # current line buffer (without final trimming yet)
    for ch in text:
        if ch == "\n":
            if buf:
                print(buf.rstrip(), end="")
                buf = ""
            print("\n", end="")
            continue

        if ch == " " and buf == "":
            continue
        if ch in ".?:":
            print(buf.rstrip() + ch, end="")
            print("\n")
            buf = ""
            continue
        buf += ch
    if buf:
        print(buf.rstrip(), end="")
