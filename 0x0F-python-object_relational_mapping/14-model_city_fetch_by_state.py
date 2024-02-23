#!/usr/bin/python3
"""Start link class to table in database
List all city objects from database
"""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for city, state in session.query(City, State)
    .filter(City.state_id == State.id).all():
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.close()
