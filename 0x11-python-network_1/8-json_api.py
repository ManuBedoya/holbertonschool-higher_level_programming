#!/usr/bin/python3
"""Module to take id  and name with letter
"""
import requests
import sys


if __name__ == '__main__':
    if bool(sys.argv[1]):
        values = {"q": sys.argv[1]}
    else:
        values = {"q": ""}

    r = requests.post('http://0.0.0.0:5000/search_user', data=values)
    try:
        if bool(r.json()):
            print("[{}] {}".format(r.json()["id"], r.json()["name"]))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
