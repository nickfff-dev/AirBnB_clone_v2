#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from models.review import Review
from models import storage
from sqlalchemy import Table
from models.amenity import Amenity
from os import getenv

place_amenity = Table(
    'place_amenity',
    Base.metadata,
    Column('place_id', String(60), ForeignKey('places.id'),
           primary_key=True, nullable=False),
    Column('amenity_id', String(60), ForeignKey('amenities.id'),
           primary_key=True, nullable=False)
)


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []
    reviews = relationship('Review', backref='place',
                           cascade="delete, delete-orphan")
    amenities = relationship('Amenity', secondary='place_amenity',
                             backref='place_amenities', viewonly=False)

    @property
    def reviews(self):
        """Returns the list of Review instances with place_id
        equals to the current place.id"""
        review_list = []
        all_reviews = storage.all(Review)
        for key, review in all_reviews.items():
            if review.place_id == self.id:
                review_list.append(review)
        return review_list

    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def amenities(self):
            """getter for amenities"""
            return self.amenity_ids

        @amenities.setter
        def amenities(self, obj):
            """Setter for amenities"""
            if isinstance(obj, Amenity):
                self.amenity_ids.append(obj.id)
