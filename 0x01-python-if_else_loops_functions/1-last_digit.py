#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if (number < 0):
    lDigit = (number * -1) % 10
    lDigit *= -1
else:
    lDigit = number % 10
if (lDigit > 5):
    print("Last digit of {:d} is {:d} and is greater than 5".format(number,
                                                                    lDigit))
elif (lDigit == 0):
    print("Last digit of {:d} is {:d} and is 0".format(number, lDigit))
else:
    print("Last digit of {:d} is {:d} and is less than 6 and not 0".format
          (number, lDigit))
