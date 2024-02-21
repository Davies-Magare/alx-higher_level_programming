#!/usr/bin/python3
"""
print first state object from hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]),pool_pre_ping=True)
    Base.metadata.create_all(engine)
    lous = State(name='Louisiana')
    Session = sessionmaker(bind=engine)
    session = Session()
    session.add(lous)
    session.commit()
    results = session.query(State.id).filter(State.name == "Louisiana").first()
    if results == None:
        print("Nothing")
    else:
        print(results[0])
    session.close()
