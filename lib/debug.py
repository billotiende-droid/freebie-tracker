#!/usr/bin/env python3

from sqlalchemy import create_engine
from models import Company, Dev, Freebie
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine('sqlite:///freebies.db')

    #Create a session to query database

    Session = sessionmaker(bind=engine)
    session = Session()
print(session.query(Company).all())
print(session.query(Dev).all())
print(session.query(Freebie).all())
  
import ipdb; ipdb.set_trace()
  
