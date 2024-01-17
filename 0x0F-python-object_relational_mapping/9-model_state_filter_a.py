#!/usr/bin/python3

"""
This module lists the state objects from the database hbtn_0e_6_usa
with letter 'a'
"""

import sys
from model_state import State, Base
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                           sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    all_states = session.query(State.name).filter(State.name.like('%a%')).all()
    i = 1
    for state in all_states:
        print("{}: {}".format(i, state[0]))
        i += 1
