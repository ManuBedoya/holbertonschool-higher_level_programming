#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    aux = []
    for item in a_dictionary:
        if a_dictionary.get(item) == value:
            aux.append(item)
    for item in aux:
        del a_dictionary[item]
    return a_dictionary
