#!/usr/bin/env python3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import  Company, Dev, Freebie

engine = create_engine('sqlite:///freebies.db')
Session = sessionmaker(bind=engine)
session = Session()

# Clear existing data
session.query(Freebie).delete()
session.query(Dev).delete()
session.query(Company).delete()
session.commit()

# Create companies
apple = Company(name='Apple', founding_year=1976)
google = Company(name='Google', founding_year=1998)
microsoft = Company(name='Microsoft', founding_year=1975)
session.add_all([apple, google, microsoft])
session.commit()  # IDs assigned

# Create devs
azdak = Dev(name='Azdak')
vashnadze = Dev(name='Vashnadze')
grusha = Dev(name='Grusha')
session.add_all([azdak, vashnadze, grusha])
session.commit()  # IDs assigned

# Create freebies using objects directly
apple_freebie = Freebie(item_name='MacBook Pro', value=1500, dev=azdak, company=apple)
google_freebie = Freebie(item_name='Pixel 6', value=800, dev=vashnadze, company=google)
microsoft_freebie = Freebie(item_name='Surface Pro', value=1200, dev=grusha, company=microsoft)

session.add_all([apple_freebie, google_freebie, microsoft_freebie])
session.commit()

print("Companies:",session.query(Company).all())
print("Developers:",session.query(Dev).all())
print("Freebies:",session.query(Freebie).all())

session.close()
