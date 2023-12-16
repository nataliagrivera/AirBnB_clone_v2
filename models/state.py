from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy.orm import relationship
from os import getenv
from sqlalchemy import Column, Integer, String, ForeignKey
from models.city import City

class State(BaseModel, Base):
    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship("City", backref="state", cascade="all, delete")

    else:
        @property
        def cities(self):
            """Getter for cities related to the current state"""
            from models import storage
            all_cities = storage.all(City)
            return [city for city in all_cities.values() if getattr(city, 'state_id', None) == self.id]
