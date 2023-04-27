from typing import Any
from sqlalchemy.ext.declarative import declarative_base, declared_attr, as_declarative


from pydantic import BaseModel
import datetime
from sqlalchemy import Column, DateTime
from sqlmodel import SQLModel, Field


# Base = declarative_base()


#change the class name to the name of the db
@as_declarative()
class Base:
    id: Any
    __name__:str

    @declared_attr
    def __tablename__(cls)->str:
        return cls.__name__.lower()+"s"
    created_at =  Column(DateTime, default=datetime.datetime.utcnow)
    modified_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)



# class TimeMixin(BaseModel):
#     created_at: datetime = Field(default_factory=datetime.now)
#     modified_at: datetime = Field(
#         sa_column = Column(
#             DateTime, default=datetime.now, onupdate=datetime.now, nullable=False
#         )
#     )