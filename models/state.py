#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from models.city import City
import os

Base = declarative_base()


class State(BaseModel, Base):
    """ State class """

    __tablename = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship(
            'City', backref='states', cascade='all, delete-orphan')
