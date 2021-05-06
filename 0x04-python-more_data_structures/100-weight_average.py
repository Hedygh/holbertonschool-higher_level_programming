#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    sum1 = 0
    for i, j in my_list:
        sum1 += i * j
    sum2 = 0
    for i, j in my_list:
        sum2 += j
    return sum1 / sum2
