#!/usr/bin/python3
"""
Print state id of state passed as argument
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
    results = session.query(State.id).filter(State.name == sys.argv[4]).first()
    if results == None:
        print("Not found")
    else:
        print(results[0])
    session.close()
