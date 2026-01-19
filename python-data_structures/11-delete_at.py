#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0 or idx > len(my_list) - 1:
        return my_list
    i = 0
    while i < idx:
        i += 1
    del my_list[i]
    return my_list
