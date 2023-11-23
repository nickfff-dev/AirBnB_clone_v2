#!/usr/bin/python3
""" State Module for HBNB project """

from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.city import City
from models import storage


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state',
                          cascade="all, delete, delete-orphan")

    @property
    def cities(self):
        """Returns the list of City instances with state_id
        equals to the current State.id"""
        city_list = []
        all_cities = storage.all(City)
        for key, city in all_cities.items():
            if city.state_id == self.id:
                city_list.append(city)
        return city_list
