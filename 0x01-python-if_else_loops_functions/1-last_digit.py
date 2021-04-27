#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 0:
    a = number % 10
else:
    a = number % -10
if a > 5:
    print("Last digit of", number, "is", a, "and is greater than 5")
elif a == 0:
    print("Last digit of", number, "is", a, "and is 0")
else:
    print("Last digit of", number, "is", a, "and is less than 6 and not 0")
