#!/usr/bin/python3
def uniq_add(my_list=[]):
    _list = set(my_list)
    result = 0
    for i in _list:
        result += i
    return result
