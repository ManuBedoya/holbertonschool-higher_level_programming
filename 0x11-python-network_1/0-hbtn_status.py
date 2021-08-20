#!/usr/bin/python3
"""Module to fetches
"""
import urllib.request


if __name__ == '__main__':
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        is_utf8 = ""
        verify = response.headers["Content-Type"].split("; ")
        if verify[1] == "charset=utf-8":
            is_utf8 = "OK"
        res = response.read()
        print("Body response:\n\t- type: {}\n\t- content: {}\n\
        - utf8 content: {}".format(type(res), res, is_utf8))
