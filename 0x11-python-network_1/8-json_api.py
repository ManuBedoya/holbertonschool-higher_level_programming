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

    try:
        r = requests.post('http://0.0.0.0:5000/search_user', data=values)
        if r.text == "{}\n":
            print("No result")
        else:
            catch_var = r.text.split(":")
            print("[{}] {}".format(catch_var[1].split(",")[0],
                                   catch_var[2][1:-3]))
    except ValueError:
        print("Not a valid JSON")
