#define DB connection here
import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://{}:{}@{}:{}/{}".format(os.environ.get("SQL_USER"),
                                                            os.environ.get("SQL_PASSWORD"),
                                                            os.environ.get("SQL_HOST"),
                                                            os.environ.get("SQL_PORT"),
                                                            os.environ.get("SQL_DATABASE"))

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()