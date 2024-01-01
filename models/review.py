#!/usr/bin/python3
""" Review module for the HBNB project """
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from os import getenv


class Review(BaseModel, Base):
    """ Review class to store review information """
    if models.what_storage == 'db':
        __tablename__ = "reviews"
        text = Column(String(1024), nullable=False)
        place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    else:
        text = ""
        user_id = ""
        place_id = ""

    def __init__(self, *args, **kwargs):
        """initializes review"""
        super().__init__(*args, **kwargs)
