#!/usr/bin/python3
"""
Define State class and a Base instance
"""


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """The state class definition."""
    __tablename__ = 'states'
    id = Column(Integer, autoincrement=True, unique=True, primary_key=True,
                nullable=False)
    name = Column(String(128), nullable=False)
