#!/usr/bin/python3
"""Module to task of interview (List all commits of rails rails)
"""
import sys
import requests


if __name__ == '__main__':
    url = "https://api.github.com/repos/{}/{}/commits"
    r = requests.get(url.format(sys.argv[1], sys.argv[2]))

    for commit in r.json()[:10]:
        print(commit['sha'], end=': ')
        print(commit['commit']['author']['name'])
