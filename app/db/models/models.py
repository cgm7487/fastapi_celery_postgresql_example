#define data model here
from sqlalchemy import ARRAY, Boolean, Column, DateTime, Integer, JSON, String
from sqlalchemy.sql import func


from app.db.postgres.database import Base

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer(), primary_key=True, autoincrement = True)
    username = Column(String(32), unique=True, nullable=False)
    password = Column(String(256), nullable=False)
    disabled = Column(Boolean, default=False)
    date_created = Column(DateTime, server_default=func.now())
    date_modified = Column(DateTime, server_default=func.now())
