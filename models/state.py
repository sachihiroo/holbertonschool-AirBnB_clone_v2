#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
import os


class State(BaseModel, Base):
    """State class"""

    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    cities = relationship("City", backref="state", cascade="delete")
    if os.getenv("HBNB_TYPE_STORAGE") != "db":

    
        @property
        def cities(self):
            from models import storage
            """getter attribute cities that returns the list of
            City instances with state_id equals to the current State.id"""
            cities = storage.all(City)
            citieslist = {}
            for city in cities:
                if city.state_id == State.id:
                    citieslist.append(city)
            return citieslist
