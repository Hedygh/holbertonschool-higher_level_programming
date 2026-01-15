#!/usr/bin/python3
for i in range(122, 97, -1):
    if i % 2 != 0:
        i -= 32
    print("{:c}".format(i), end='')
