#!/usr/bin/python3
"""Module to create a class
"""
from model_state import State, Base
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """Class state
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False, unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

    def __str__(self):
        return "{:d}: {}".format(self.id, self.name)
