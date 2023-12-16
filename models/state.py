#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy.orm import relationship
import models
from models.city import City
from os import getenv
from sqlalchemy import Column, Integer, String, ForeignKey


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        @property
        def cities(self):
            """Getter for cities related to the current state
            """
            from models import storage
            all_cities = storage.all(City)
            return [city for city in all_cities.values()
                    if getattr(city, 'state_id', None) == self.id]

    #    @property
    #    def cities(self):
    #        """Getter"""
    #        city_lst = []
    #        all_cities = models.storage.all(City)
    #        for city in all_cities.values():
    #            if city.state_id == self.id:
    #                city_lst.append(city)
    #        return city_lst
