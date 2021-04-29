#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, mul, div
if __name__ != "__main__":
    exit()
if (len(argv)) != 4:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    exit(1)
a = int(argv[1])
b = int(argv[3])
operators = ["+", "-", "*", "/"]
functions = [add, sub, mul, div]
if argv[2] not in operators:
    print("Unknown operator. Available operators: +, -, * and /")
    exit(1)
i = 0
while i < 4:
        print("{:d} {:s} {:d} = {:d}".format
              (a, operators[i], b, functions[i](a, b)))
        break
        i = i + 1
