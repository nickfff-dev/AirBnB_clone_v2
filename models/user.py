#!/usr/bin/python3
"""This module defines a class User"""
from sqlalchemy import Column, String
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from os import getenv


class User(BaseModel, Base):
    """The User class."""
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'users'
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        places = relationship('Place', backref='user',
                              cascade="delete, delete-orphan")
        reviews = relationship('Review', backref='user',
                               cascade='delete, delete-orphan')
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""
