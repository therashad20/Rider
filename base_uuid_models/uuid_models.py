
from sqlalchemy import Column, Integer, DateTime, String, ForeignKey, Boolean
from database_connection import Base
import uuid
import datetime


class Uuid_models(Base):
    __abstract__ = True 
    uuid = Column(String(255), default=lambda: str(uuid.uuid4()), unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow) 