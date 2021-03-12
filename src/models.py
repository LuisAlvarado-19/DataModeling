import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    userid = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    password = Column(String(50), nullable=False)
     
    
    
class Planets(Base):
    __tablename__ = 'planets'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    plaid = Column(Integer, primary_key=True)
    full_name = Column(String(50), nullable=False)
    description = Column(String(250))
    diameter = Column(String(100))
    rotation_period = Column(String(100))
    orbital_period = Column(String(100))
    gravity = Column(String(100))
    population = Column(String(100))
    Climate = Column(String(100))
    terrain = Column(String(100))
    surface_water = Column(String(100))
    
class Character(Base):
    __tablename__ = 'character'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    chaid = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    description = Column(String(250))
    height = Column(String(100))
    mass = Column(String(100))
    hair_color = Column(String(100))
    eye_color = Column(String(100))
    skin_color = Column(String(100))
    birth_year = Column(String(100))
    gender = Column(String(100))
    
class Favorites(Base):
    __tablename__ = 'favorites'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    favid = Column(Integer, primary_key=True)
    user_userid = Column(Integer, ForeignKey('user.userid'))
    user = relationship(User)
    planets_plaid = Column(Integer, ForeignKey('planets.plaid'))
    planets = relationship(Planets)
    character_chaid = Column(Integer, ForeignKey('character.chaid'))
    character = relationship(Character)
    
    

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')