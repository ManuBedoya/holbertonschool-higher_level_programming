#!/usr/bin/python3
"""Module to create a class
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


Base = declarative_base()
class State(Base):
    """Class state
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False, unique=True)
    name = Column(String(128), nullable=False)
    def __str__(self):
        return "{:d}: {}".format(self.id, self.name)
