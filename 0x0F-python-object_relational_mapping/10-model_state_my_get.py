#!/usr/bin/python3

"""
This module lists the state objects ids from the database hbtn_0e_6_usa
whose name match the argument
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
    state_id = session.query(State.id).filter(State.name ==
                                              sys.argv[4]).first()
    if state_id is None:
        print('Not found')
    else:
        print(state_id[0])
