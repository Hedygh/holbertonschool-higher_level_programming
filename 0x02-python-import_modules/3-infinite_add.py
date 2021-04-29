#!/usr/bin/python3
import sys
if __name__ == "__main__":
    i = 1
    res = 0
    while i < len(sys.argv):
        res += (int(sys.argv[i]))
        i = i + 1
print(res)
