#!/usr/bin/python3
"""Module to Code Errors
"""
import requests
import sys

if __name__ == '__main__':
    try:
        print(requests.get(sys.argv[1]).content.decode("utf8"))
    except HTTPError as err:
        print("Error code: {}".format(err))
