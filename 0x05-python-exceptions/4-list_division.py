def list_division(my_list_1, my_list_2, list_length):
    my_list_3 = []
    value = 0
    for i in range(list_length):
        try:
            value = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
            value = 0
        except TypeError:
            print("wrong type")
            value = 0
        except IndexError:
            print("out of range")
            value = 0
        finally:
            my_list_3.append(value)
    return my_list_3
