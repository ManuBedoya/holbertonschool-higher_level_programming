#!/usr/bin/python3
"""Module to display value
"""
import requests
import sys


if __name__ == '__main__':
    r = requests.get(sys.argv[1])
    print(dict(r.headers)["X-Request-Id"])
