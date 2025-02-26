#!/usr/bin/python3
""" Place Module for HBNB project """
import os
from sqlalchemy import Column, Float, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship

from models.base_model import BaseModel, Base
from models.review import Review
from models.amenity import Amenity


PlaceAmenity = Table(
    'PlaceAmenity',
    Base.metadata,
    Column(
        'place_id',
        String(60),
        ForeignKey('Place.id'),
        nullable=False,
        primary_key=True
    ),
    Column(
        'amenity_id',
        String(60),
        ForeignKey('Amenity.id'),
        nullable=False,
        primary_key=True
    )
)
"""This Represent the many to many relationships of the  table
between Place and Amenity records.
"""


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'Place'
    id = Column(String(60), primary_key=True)
    city_id = Column(String(60), ForeignKey('City.id'), nullable=False
    ) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else ''
    user_id = Column(
        String(60), ForeignKey('User.id'), nullable=False
    ) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else ''
    name = Column(
        String(128), nullable=False
    ) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else ''
    description = Column(
        String(1024), nullable=True
    ) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else ''
    number_rooms = Column(
        Integer, nullable=False, default=0
    ) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else 0
    number_bathrooms = Column(
        Integer, nullable=False, default=0
    ) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else 0
    max_guest = Column(
        Integer, nullable=False, default=0
    ) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else 0
    price_by_night = Column(
        Integer, nullable=False, default=0
    ) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else 0
    latitude = Column(
        Float, nullable=True
    ) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else 0.0
    longitude = Column(
        Float, nullable=True
    ) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else 0.0
    amenity_ids = []
    reviews = relationship(
        'Review',
        cascade="all, delete, delete-orphan",
        backref='Place'
    ) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else None
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        amenity = relationship(
            'Amenity',
            secondary=PlaceAmenity,
            viewonly=False,
            backref='PlaceAmenity'
        )
    else:
        @property
        def amenities(self):
            """Returns the amenities of the Place"""
            from models import storage
            amenities_of_place = []
            for value in storage.all(Amenity).values():
                if value.id in self.amenity_ids:
                    amenities_of_place.append(value)
            return amenities_of_place

        @amenities.setter
        def amenities(self, value):
            """Adds an amenity to the Place class"""
            if type(value) is Amenity:
                if value.id not in self.amenity_ids:
                    self.amenity_ids.append(value.id)

        @property
        def reviews(self):
            """Returning the reviews of this Place"""
            from models import storage
            reviews_of_place = []
            for value in storage.all(Review).values():
                if value.place_id == self.id:
                    reviews_of_place.append(value)
            return reviews_of_place
