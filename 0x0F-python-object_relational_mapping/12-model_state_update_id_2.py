#!/usr/bin/python3

"""
This module updates the states table to 'New Mexico'
where the id = 2
"""

import sys
from model_state import State, Base
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sqlalchemy import insert
from sqlalchemy import update

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                           sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    updt = (
            update(State).where(State.id == 2).
            values(name='New Mexico')
    )
    with engine.connect() as conn:
        result = conn.execute(updt)
        conn.commit()
