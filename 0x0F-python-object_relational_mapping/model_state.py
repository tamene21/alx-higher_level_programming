#!/usr/bin/python3
"""Definition of the State class"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    """Class State"""

    __tablename__ = 'states'
    id = Colum(Integer, autoincrement=True,
               primary_key=True, nullable=False. unique=True)
    name = Column(string(128), nullable=False)
