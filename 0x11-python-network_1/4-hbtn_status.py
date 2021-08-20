#!/usr/bin/python3
"""Module to Status
"""
import requests


if __name__ == '__main__':
    r = requests.get('https://intranet.hbtn.io/status')
    print("Body response:\n\ttype: {}\n\
    \tcontent: {}".format(type(str(r)), r.content.decode("utf8")))
