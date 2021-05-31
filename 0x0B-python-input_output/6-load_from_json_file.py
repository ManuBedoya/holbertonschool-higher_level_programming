#!/usr/bin/python3
import json


def load_from_json_file(filename):
    with open(filename, 'r') as json_file:
        data = json_file.read()
    json_file.close()
    return json.loads(data)
