#!/usr/bin/python3
def write_file(filename='', text=''):
    with open(filename, 'w+') as file:
        number_chars = file.write(text)
    file.close()
    return number_chars
