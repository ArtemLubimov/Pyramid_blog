import datetime #<- will be used to set default dates on models

from sqlalchemy import (
    Column,
    Integer,
    Unicode,     #<- will provide unicode field,
    UnicodeText, #<- will provide unicode text field,
    DateTime     #<- time abstraction field,
    )
from blojik_pyramid.models.meta import Base  #<- we need to import our sqlalchemy metadata for model classes to inherit from


class BlogRecord(Base):
    __tablename__ = 'entries'
    id = Column(Integer, primary_key=True)
    title = Column(Unicode(255), unique=True, nullable=False)
    body = Column(UnicodeText, default=u'')
    created = Column(DateTime, default=datetime.datetime.utcnow)
    edited = Column(DateTime, default=datetime.datetime.utcnow)
