#!/usr/bin/python3

"""
This module deletes names from the states table
where each name has an 'a'
"""

import sys
from model_state import State, Base
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sqlalchemy import delete

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                           sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    dlt = delete(State).where(State.name.like('%a%'))
    with engine.connect() as conn:
        result = conn.execute(dlt)
        conn.commit()
