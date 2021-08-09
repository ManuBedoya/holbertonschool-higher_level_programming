#!/usr/bin/python3
"""Module to create a class
"""
from model_state import State, Base
from model_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import sqlalchemy
import sys

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(engine)
    session = Session()

    data = session.query(State, City).join(City).filter(State.id == City.state_id)
    for item in data:
        print("{}: ({:d}) {}".format(item[0].name, item[1].id, item[1].name))
