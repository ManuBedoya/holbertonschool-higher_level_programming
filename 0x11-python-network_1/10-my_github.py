#!/usr/bin/python3
"""Module to take id of github
"""
import sys
import requests


if __name__ == '__main__':
    r = requests.get('https://api.github.com/user', auth=(sys.argv[1],
                                                          sys.argv[2]))
    msg = '{"message":"Requires authentication","documentation_url":"https:'
    msg += '//docs.github.com/rest/reference/'
    msg += 'users#get-the-authenticated-user"}'
    if r.text == msg:
        print(None)
    else:
        catch_var = r.text.split(":")[2]
        print(catch_var.split(",")[0])
