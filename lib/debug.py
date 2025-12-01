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

print("\n FREEBIE -> DEV/COMPANY")

freebie = session.query(Freebie).first()

print("Freebie:", freebie)
print("Developer:", freebie.dev)
print("Company:", freebie.company)
print("print_details():", freebie.print_details())

# company.devs + companies.freebies
print("\n COMPANY -> DEVS/FREEBIES")

company = session.query(Company).first()

print("Company:", company)
print("Developers:", company.devs)
print("Freebies:", company.freebies)


# oldest company
print("\n OLDEST COMPANY")
oldest = Company.oldest_company()
print("Oldest Company:", oldest)

# def.give_away(freebie, other_dev)
print("\n GIVE AWAY FREEBIE")

giver = session.query(Dev).filter_by(name='Azdak').first()
receiver = session.query(Dev).filter_by(name='Vashnadze').first()

freebie = session.query(Freebie).filter_by(item_name='MacBook Pro').first()

print("Before giving:")
print("giver.freebies:", giver.freebies)
print("receiver.freebies:", receiver.freebies)

giver.give_away(freebie, receiver)

print("\nAfter giving:")
print("giver.freebies:", giver.freebies)
print("receiver.freebies:", receiver.freebies)



  
# import ipdb; ipdb.set_trace()
  
