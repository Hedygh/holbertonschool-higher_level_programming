#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "":
        s = (len(sentence), None)
    else:
        s = (len(sentence), sentence[0])
    return s
