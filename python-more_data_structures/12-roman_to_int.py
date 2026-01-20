#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) is not str:
        return 0
    values = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    total = 0
    n = len(roman_string)
    for i in range(n):
        current = values.get(roman_string[i])
        if current is None:
            return 0
        if i + 1 < n:
            next_val = values.get(roman_string[i + 1])
            if next_val is None:
                return 0

            if current < next_val:
                total -= current
            else:
                total += current
        else:
            total += current
    return total
