#!/usr/bin/python3
"""This is the State Module for HBNB clone project """
import os
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

from models.base_model import BaseModel, Base
from models.city import City


class State(BaseModel, Base):
    """This is the  State class """
    __tablename__ = 'State'
    id = Column(String(60), primary_key=True)
    name = Column(
        String(128), nullable=False
    ) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else ''
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        city = relationship(
            'City',
            cascade='all, delete, delete-orphan',
            backref='State'
        )
    else:
        @property
        def cities(self):
            """Return the cities in this State"""
            from models import storage
            city_in_state = []
            for value in storage.all(City).values():
                if value.state_id == self.id:
                    city_in_state.append(value)
            return city_in_state
