#!/usr/bin/python3

"""This module lists the first state objects from the database hbtn_0e_6_usa"""

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
    first_state = session.query(State.name).first()
    if first_state is None:
        print(Nothing)
    else:
        print("{}: {}".format(1, first_state[0]))
