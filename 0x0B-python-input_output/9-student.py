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

    def to_json(self):
        """This is the to_json funtion
        Is to return a dict with the data of the student
        Returns:
          A dict width data
        """
        return {'first_name': self.first_name, 'last_name': self.last_name,
                'age': self.age}
