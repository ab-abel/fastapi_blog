from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlmodel import SQLModel

from db.db_base import Base 
from db.schema.mixtime import TimeMixin

class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    firstname = Column(String, nullable=False)
    lastname = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True, index=False)
    password =Column(String, nullable=False)
    is_active = Column(Boolean, default=True)

