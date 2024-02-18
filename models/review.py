#!/usr/bin/python3
""" Reviews module for the HBNB project """
import os
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship

from models.base_model import BaseModel, Base


class Review(BaseModel, Base):
    """ Review class to save the review information """
    __tablename__ = 'review'
    place_id = Column(
        String(60), ForeignKey('Place.id'), nullable=False
    ) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else ''
    user_id = Column(
        String(60), ForeignKey('User.id'), nullable=False
    ) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else ''
    text = Column(
        String(1024), nullable=False
    ) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else ''
