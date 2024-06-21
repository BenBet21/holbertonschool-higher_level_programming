#!/usr/bin/python3
"""Write a Python file similar to model_state.py named model_city.py\
    that contains the class definition of a City"""

from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    """Class City that inherits from Base (imported from model_state)"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
