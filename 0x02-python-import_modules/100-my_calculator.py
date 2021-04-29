#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div
if __name__ != "__main__":
    exit()
if (len(sys.argv)) != 4:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    exit(1)
if sys.argv[2] != "+" and "-" and "*" and "/":
    print("Unknown operator. Available operators: +, -, * and /")
    exit(1)
a = int(sys.argv[1])
b = int(sys.argv[3])
print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
