#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        return fct(*args)
    except:
        e = sys.exc_info()[1]
        print("Exception: {}".format(e.args[0]), file=sys.stderr)
        return None
