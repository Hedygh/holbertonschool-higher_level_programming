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
op = ["+", "-", "*", "/"]
f = [add, sub, mul, div]
if argv[2] not in op:
    print("Unknown operator. Available operators: +, -, * and /")
    exit(1)
for i in range(len(op)):
    if argv[2] == op[i]:
        print("{:d} {:s} {:d} = {:d}".format(a, op[i], b, f[i](a, b)))
        break
