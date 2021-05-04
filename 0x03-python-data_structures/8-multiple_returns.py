#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) > 0:
        c = sentence[0]
    else:
        c = None
    return (len(sentence), c)
