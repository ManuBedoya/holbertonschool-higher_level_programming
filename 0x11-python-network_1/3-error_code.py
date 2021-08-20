#!/usr/bin/python3
"""Module to Code Errors
"""
import urllib.error
import urllib.request
import sys

if __name__ == '__main__':
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            print(response.read().decode('utf8'))
    except urllib.error.HTTPError as err:
        print("Error code: {}".format(err.getcode()))
