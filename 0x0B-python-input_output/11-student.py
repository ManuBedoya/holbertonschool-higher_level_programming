#!/usr/bin/python3
"""Module to create a Student Class
"""


class Student:
    def __init__(self, first_name, last_name, age):
        """This is the __init__ method
        Is to initianilize all variables
        Args:
           first_name (str): First name
           last_name (str): Last name
           age (str): Age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """This is the to_json funtion
        Is to return a dict with the data of the student
        Returns:
          A dict width data
        """
        if attrs is None:
            return {'first_name': self.first_name, 'last_name': self.last_name,
                    'age': self.age}

        dict_student = {}
        for item in attrs:
            if hasattr(self, item):
                dict_student[item] = getattr(self, item)
        return dict_student

    def reload_from_json(self, json):
        """This is the reload_from_json method
        Is to replace all variables of a student
        Args:
          json (dict) : New values
        """
        if 'first_name' in json.keys():
            self.first_name = json['first_name']
        if 'last_name' in json.keys():
            self.last_name = json['last_name']
        if 'age' in json.keys():
            self.age = json['age']
