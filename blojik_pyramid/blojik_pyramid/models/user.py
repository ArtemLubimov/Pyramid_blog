import datetime #<- will be used to set default dates on models

from sqlalchemy import (
    Column,
    Integer,
    Unicode,     #<- will provide unicode field,
    UnicodeText, #<- will provide unicode text field,
    DateTime     #<- time abstraction field,
    )
from blojik_pyramid.models.meta import Base  #<- we need to import our sqlalchemy metadata for model classes to inherit from


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(Unicode(255), unique=True, nullable=False)
    password = Column(Unicode(255), nullable=False)
    last_logged = Column(DateTime, default=datetime.datetime.utcnow)
