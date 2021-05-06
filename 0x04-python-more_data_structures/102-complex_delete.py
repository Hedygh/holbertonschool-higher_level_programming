#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    tmp = []
    for k, v in a_dictionary.items():
        if v == value:
            tmp.append(k)
    for k in tmp:
        del(a_dictionary[k])
    print(tmp)
    return a_dictionary
