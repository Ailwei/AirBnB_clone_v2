#!/usr/bin/python3
"""IT is  City Module for the HBNB project """
import os
from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.orm import relationship

from models.base_model import BaseModel, Base


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'city'
    id = Column(String(60), primary_key=True)
    state_id = Column(
           String(60), ForeignKey('state.id'), nullable=False)
    name = Column(
        String(128), nullable=False
    ) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else ''
    state_id = Column(
        Integer, ForeignKey('state.id'), nullable=False
    ) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else ''
    places = relationship(
        'Place',
        cascade='all, delete, delete-orphan',
        backref='city'
    ) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else None
