#!/usr/bin/python3
"""This module defines a class User"""
import models
from sqlalchemy import Column, String
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """The User class."""
    if models.what_storage == 'db':
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

    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)
