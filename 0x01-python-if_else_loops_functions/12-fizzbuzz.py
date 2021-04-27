#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        text = i
        if (i % 3 == 0 and i % 5 == 0):
            text = "FizzBuzz"
        elif (i % 3 == 0):
            text = "Fizz"
        elif (i % 5 == 0):
            text = "Buzz"
        print("{}".format(text), end=' ')
