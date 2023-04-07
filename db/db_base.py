from typing import Any
from sqlalchemy.ext.declarative import declarative_base, declared_attr, as_declarative

# Base = declarative_base()


#change the class name to the name of the db
@as_declarative()
class Base:
    id: Any
    __name__:str

    @declared_attr
    def __tablename__(cls)->str:
        return cls.__name__.lower()+"s"

