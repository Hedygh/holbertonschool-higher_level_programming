#!/usr/bin/python3
for a in range(97, 123):
    if a not in (ord('q'), ord('e')):
        print("{:c}".format(a), end='')
