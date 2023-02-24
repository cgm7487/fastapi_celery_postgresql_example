#define DB ORM here

from fastapi.encoders import jsonable_encoder

from app.schemas import schemas

from . import models

from sqlalchemy import desc
from sqlalchemy.orm import Session

def get_user_by_name(db: Session, user_name: str):
    return db.query(models.User).filter(models.User.username == user_name).first()

def create_user(db: Session, user: schemas.User):

    if get_user_by_name(db, user.username) is not None:
        return

    db_user = models.User(username=user.username, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
