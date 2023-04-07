
from pydantic import BaseModel
from datetime import datetime
from sqlalchemy import Column, DateTime
from sqlmodel import SQLModel, Field


class TimeMixin(BaseModel):
    created_at: datetime = Field(default_factory=datetime.now)
    modified_at: datetime = Field(
        sa_column = Column(
            DateTime, default=datetime.now, onupdate=datetime.now, nullable=False
        )
    )