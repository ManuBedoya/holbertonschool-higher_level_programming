#!/usr/bin/python3
def append_write(filename='', text=''):
    with open(filename, 'a+') as file:
        number_chars = file.write(text)
    file.close()
    return number_chars
