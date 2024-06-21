#!/usr/bin/python3
"""Write a script that prints the State object\
    with the name passed as argument from the database hbtn_0e_6_usa"""

import sys
from sqlalchemy import create_engine, exc
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    if len(sys.argv) == 4:
        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]

        engine = create_engine(
            f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}',
            pool_pre_ping=True
            )
        Session = sessionmaker(bind=engine)
        session = Session()

        new_state = State(name="Louisiana")
        session.add(new_state)
        session.commit()

        print(new_state.id)
        session.close()
    else:
        print("Usage: <username> <password> <database_name>")
