#!/usr/bin/python3
"""Module to create a base
"""
import json


class Base:
    """Base class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """This method is to initialize variables
        Args:
          id (integer): id
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Falta
        de
        documentacion
        """

        if list_dictionaries is None:
            return '[]'
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Falta
        de
        documentacion
        """

        temp_dicts = []
        if list_objs:
            for obj in list_objs:
                insert_dict = obj.to_dictionary()
                temp_dicts.append(insert_dict)
        with open(cls.__name__ + '.json', 'w', encoding='utf-8') as json_file:
            json_file.write(cls.to_json_string(temp_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Falta
        de
        documentacion
        """

        if json_string is None or json_string == '':
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Falta
        de
        documentacion
        """

        if cls.__name__ == 'Rectangle':
            obj = cls(1, 1)
        else:
            obj = cls(1)

        obj.update(**dictionary)
        return obj

    @classmethod
    def load_from_file(cls):
        """Falta
        de
        documentacion
        """

        list_instances = []
        try:
            with open(cls.__name__ + '.json', 'r', encoding='utf-8') as file:
                str_json_file = cls.from_json_string(file.read())
                for item in str_json_file:
                    list_instances.append(cls.create(**item))
            return list_instances
        except Exception as error:
            return []
