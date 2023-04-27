from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from db.db_base import Base 


class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    firstname = Column(String, nullable=False)
    lastname = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True, index=False)
    password =Column(String, nullable=False)
    is_active = Column(Boolean, default=True)

class Post(Base):
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    body = Column(String, nullable=False)
    owner_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates='posts')
    
    
    
    
