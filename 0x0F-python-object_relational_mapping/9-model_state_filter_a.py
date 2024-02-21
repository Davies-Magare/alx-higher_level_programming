#!/usr/bin/python3
"""
Print state objects with 'a' in name from hbtn_0e_6_usa
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
    results = session.query(State.name).filter(State.name.like('%a%')).order_by(asc(State.id)).all()
    if results == None:
        print("Nothing")
    else:
        i = 1
        for result in results:
            print("{}: {}".format(i, result[0]))
            i += 1
    session.close()
