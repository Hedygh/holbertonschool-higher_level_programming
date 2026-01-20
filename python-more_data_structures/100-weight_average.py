#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    res1 = 0
    for i, j in my_list:
        res1 += i * j
    res2 = 0
    for i, j in my_list:
        res2 += j
    return res1 / res2
