#!/usr/bin/env python3

from sqlalchemy import create_engine
from models import Company, Dev, Freebie
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine('sqlite:///freebies.db')

    #Create a session to query database

    Session = sessionmaker(bind=engine)
    session = Session()


print("\n===ALL DATA FROM DATABASE===")   
 
print(session.query(Company).all())
print(session.query(Dev).all())
print(session.query(Freebie).all())

print("n\=== TESTING RELATIONSHIPS & METHODS ===")

# freebie.dev + freebie.company

freebie = session.query(Freebie).first()

print("Freebie:", freebie)
print("Developer:", freebie.dev)
print("Company:", freebie.company)
print("print_details():", freebie.print_details())

# company.devs + companies.freebies
print("\n COMPANY -> DEVS/FEEBIES")

company = session.query(Company).first()

print("Company:", company)
print("Developers:", company.devs)
print("Freebies:", company.freebies)


  
# import ipdb; ipdb.set_trace()
  
