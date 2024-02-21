#!/usr/bin/python3
"""Start link class to table in database
List all objects from database
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]),pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    results = session.query(State.name).order_by(asc(State.id)).all()
    i = 1
    for result in results:
        print("{}: {}".format(i, result[0]))
        i += 1
    session.close()
