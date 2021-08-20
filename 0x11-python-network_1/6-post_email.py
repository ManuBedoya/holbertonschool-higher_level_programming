#!/usr/bin/python3
"""Module to do a POST
"""
import requests
import sys


if __name__ == '__main__':
    values = {'email': sys.argv[2]}
    req = requests.post(sys.argv[1], data = values)
    print(req.text)
