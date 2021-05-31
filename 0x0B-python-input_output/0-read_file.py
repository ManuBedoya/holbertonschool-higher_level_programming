#!/usr/bin/python3
def read_file(filename=""):
    with open(filename, 'r') as file:
        read_data = file.read()
    file.close()
    print(read_data)
