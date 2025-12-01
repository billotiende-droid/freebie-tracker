from sqlalchemy import ForeignKey, Column, Integer, String, MetaData
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

# Naming convention for constraints (useful for Alembic migrations)
convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}

# Apply naming convention to metadata
metadata = MetaData(naming_convention=convention)

# Create Base class with metadata attached
Base = declarative_base(metadata=metadata) 

class Company(Base):
    __tablename__ = 'companies'

    # Primary key
    id = Column(Integer(), primary_key=True)

    # Basic attributes
    name = Column(String())
    founding_year = Column(Integer())

    # One-to-many relationship: a company has many freebies
    # backref="company" allows freebie.company to reference the parent
    # cascade ensures deletion of freebies when company is deleted
    freebies = relationship('Freebie', backref='company', cascade='all, delete-orphan')
    @property
    def devs(self):
        return list({freebie.dev for freebie in self.freebies})
    
    # create instances
    def give_freebies(self, dev, item_name, value):
        new_freebie = Freebie(
        item_name=item_name, 
        value=value, 
        dev=dev, 
        company=self)

        session.add(new_freebie)
        session.commit()    

        return new_freebie
    @classmethod
    def oldest_company(cls, session):
        return session.query(cls).order_by(cls.founding_year).first()

    # String representation of the Company object
    def __repsr__(self):
        return f'<Company {self.name}>'

class Dev(Base):
    __tablename__ = 'devs'

    # Primary key
    id = Column(Integer(), primary_key=True)
    name = Column(String())

    # One-to-many relationship: a dev has many freebies
    # backref="dev" allows freebie.dev to access the related dev
    freebies = relationship('Freebie', backref='dev', cascade='all, delete-orphan')
    

    def __repr__(self):
        return f'<Dev {self.name}>'
    # 
    def received_one(self, item_name):
        return any(f.item_name == item_name for f in self.freebies)
    
    def give_away(self, other_dev, freebie):
       # Check if the freebie belongs to this dev
        if freebie in self.freebies:
            freebie.dev = other_dev
            return True
        return False


    
class Freebie(Base):
    __tablename__ = 'freebies'

    # Primary key
    id = Column(Integer(), primary_key=True)

    # Basic attributes
    item_name = Column(String(), nullable=False)
    value = Column(Integer(), nullable=False)

    # Foreign keys linking each freebie to one dev and one company
    dev_id = Column(Integer(), ForeignKey('devs.id'), nullable=False)
    company_id = Column(Integer(), ForeignKey('companies.id'), nullable=False)

    def __repr__(self):
        # Note: Freebie does not have attribute "name" — you may want item_name instead
        return f'<Freebie {self.name}>'
