#!/usr/bin/python3
def class_to_json(obj):
    attrs = [attr for attr in dir(obj) if not callable(getattr(obj, attr)) and
             not attr.startswith("__")]
    dict_obj = {}
    for item in attrs:
        dict_obj[item] = getattr(obj, item)
    return dict_obj
