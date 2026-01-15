#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:
    n = number % 10
else:
    n = number % -10
if n > 5:
    print("The last digit of", number, "is", n, "and is greater than 5")
elif n == 0:
    print("The last digit of", number, "is", n, "and is 0")
else:
    print("The last digit of", number, "is", n, "and is less than 6 and not 0")
