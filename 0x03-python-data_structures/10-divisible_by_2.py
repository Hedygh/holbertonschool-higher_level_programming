#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list:
        _list = list(my_list)
        for i in my_list:
            if my_list[i] % 2 == 0:
                _list[i] = True
            else:
                _list[i] = False
        return _list
    return my_list
