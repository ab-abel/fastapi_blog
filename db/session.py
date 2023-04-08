from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from core.config import settings
from typing import Generator

SQL_DB_URL = settings.POSTGRES_URL

engine = create_engine(SQL_DB_URL)


sessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#depenencdy injection

def get_db() -> Generator:
    try:
        db=sessionLocal()
        yield db
    finally:
        db.close()