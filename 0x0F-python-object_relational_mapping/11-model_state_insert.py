#!/usr/bin/python3
""" Write a script that adds the State object “Louisiana” to the
database hbtn_0e_6_usa

Your script should take 3 arguments: mysql username, mysql password and
database name
You must use the module SQLAlchemy
You must import State and Base from model_state - from model_state
import Base, State
Your script should connect to a MySQL server running on localhost at port 3306
Print the new states.id after creation
Your code should not be executed when imported """

import sys
from model_state import Base, State
import sqlalchemy
from sqlalchemy import (create_engine)
from sqlalchemy.orm import session, sessionmaker


if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1], sys.argv[2],
                                  sys.argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    newState = State(name='Louisiana')
    session.add(newState)
    getState = (session.query(State).filter_by(name='Louisiana').first()).id
    print("{}".format(str(getState)))
    session.commit()
    session.close()
