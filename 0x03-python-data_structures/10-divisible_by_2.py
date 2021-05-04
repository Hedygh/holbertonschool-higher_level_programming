#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    _list = []
    if my_list:
        for i in my_list:
            if my_list[i] % 2 == 0:
                _list.append(True)
            else:
                _list.append(False)
    return _list
