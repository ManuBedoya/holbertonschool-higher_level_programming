#!/usr/bin/python3
for letter in reversed(range(97, 123)):
    if (letter % 2 == 0):
        print("{:c}".format(letter), end='')
    else:
        print("{:c}".format(letter - 32), end='')
