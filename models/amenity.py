#!/usr/bin/python3
""" Amenity Module for HBNB project """
import os
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
#from models import storage
from models.base_model import BaseModel, Base


class Amenity(BaseModel, Base):
    """Represent an amenity data set."""
    __tablename__ = 'amenity'
    name = Column(
        String(128), nullable=False
    ) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else ''
