#!/usr/bin/python3
def print_last_digit(number):
    lDigit = 0
    if (number < 0):
        lDigit = ((number * -1) % 10)
    else:
        lDigit = number % 10
    print("{:d}".format(lDigit), end='')
    return (lDigit)
