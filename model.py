"""
Describing of User model in database.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    __allow_unmapped__ = True
    pass


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    fullname = Column(String(128), nullable=False)
    tg_id = Column(Integer, nullable=False)
    tg_name = Column(String(128), nullable=False)
