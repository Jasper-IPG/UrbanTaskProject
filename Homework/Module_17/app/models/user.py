from Homework.Module_17.app.backend.db import Base
from sqlalchemy import Column, ForeignKey, Boolean, Float, Integer, String
from sqlalchemy.orm import relationship
from Homework.Module_17.app.models import *


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    firstname = Column(String)
    lastname = Column(String)
    age = Column(Integer)
    slug = Column(String, unique=True, index=True)
    task = relationship('Task', back_populates='user')
