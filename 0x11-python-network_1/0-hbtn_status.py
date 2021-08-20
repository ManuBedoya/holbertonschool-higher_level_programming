#!/usr/bin/python3
"""Module to fetches
"""
import urllib.request


if __name__ == '__main__':
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        res = response.read()

        print("Body response:\n\t- type: {}\n\t- content: {}\n\
        - utf8 content: {}".format(type(res), res, res.decode("utf8")))
