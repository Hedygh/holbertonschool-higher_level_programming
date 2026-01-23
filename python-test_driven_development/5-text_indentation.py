#!/usr/bin/python3
"""This module provides a function that prints text with indentation rules."""


def text_indentation(text):
    """Print text with 2 new lines after '.', '?' and ':'."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    buf = ""
    just_split = False

    for ch in text:
        if ch == "\n":
            if just_split:
                just_split = False
                continue

            # flush current line (trim end) then print exactly one newline
            if buf != "":
                print(buf.rstrip(), end="")
                buf = ""
            print("", end="\n")  # exactly one newline
            continue

        if ch == " " and buf == "":
            continue

        if ch in ".?:":
            print(buf.rstrip() + ch, end="\n\n")
            buf = ""
            just_split = True
            continue

        buf += ch
        just_split = False

    # final flush: print WITHOUT adding newline
    if buf != "":
        print(buf.rstrip(), end="")
