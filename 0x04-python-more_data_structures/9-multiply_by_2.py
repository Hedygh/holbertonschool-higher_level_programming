#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    a_dic = {}
    for k, v in a_dictionary.items():
        a_dic[k] = v * 2
    return a_dic
