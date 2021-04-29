#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div
if __name__ != "__main__":
    exit()
if (len(sys.argv)) != 4:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    exit(1)
a = int(sys.argv[1])
b = int(sys.argv[3])
operators = ["+", "-", "*", "/"]
functions = [add, sub, mul, div]
if sys.argv[2] not in operators:
    print("Unknown operator. Available operators: +, -, * and /")
    exit(1)
i = 0
while i < 4:
    if sys.argv[2] == operators[i]:
        print("{:d} {:s} {:d} = {:d}".format
              (a, operators[i], b, functions[i](a, b)))
        break
    i = i + 1
