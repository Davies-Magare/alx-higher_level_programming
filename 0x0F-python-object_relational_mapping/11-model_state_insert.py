#!/usr/bin/python3

"""
This module inserts the state of Louisiana into the
State table
"""

import sys
from model_state import State, Base
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sqlalchemy import insert

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                           sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    ins = insert(State).values(name='Louisiana')
    with engine.connect() as conn:
        result = conn.execute(ins)
        conn.commit()
    state_id = session.query(State.id).filter(State.name ==
                                              'Louisiana').first()
    print(state_id[0])
