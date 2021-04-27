#!/usr/bin/python3
def uppercase(str):
    for letter in str:
        if (ord(letter) <= 122 and ord(letter) >= 97):
            letter = chr(ord(letter) - 32)
        print("{}".format(letter), end='')
    print(end='\n')
