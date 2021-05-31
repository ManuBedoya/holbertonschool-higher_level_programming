#!/usr/bin/python3
import json


def save_to_json_file(my_obj, filename):
    with open(filename, 'w+') as json_file:
        json.dump(my_obj, json_file)
    json_file.close()
