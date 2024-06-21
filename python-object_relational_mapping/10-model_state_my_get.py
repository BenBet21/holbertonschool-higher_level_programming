#!/usr/bin/python3
"""Write a script that prints the State object\
    with the name passed as argument from the database hbtn_0e_6_usa"""

import sys
from sqlalchemy import create_engine, exc
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    if len(sys.argv) == 5:
        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]
        state_name = sys.argv[4]

        engine = create_engine(
            f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}',
            pool_pre_ping=True
            )
        Session = sessionmaker(bind=engine)
        session = Session()

        try:
            state = session.query(State).filter(State.name == state_name).one()
            print(state.id)
        except exc.NoResultFound:
            print("Not found")
        finally:
            session.close()
    else:
        print("Usage: <username> <password> <database_name> <state_name>")
