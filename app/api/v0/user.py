from fastapi import APIRouter, Depends, HTTPException, status

from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from app.db.models import crud
from app.schemas import schemas
from app import utils

from jose import jwt, JWTError

from sqlalchemy.orm import Session

from app import utils
from app.db.postgres.database import get_db

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/v0/user/token")

router = APIRouter()

async def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, utils.JWT_SECRET_KEY, algorithms=[utils.ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = schemas.TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = crud.get_user_by_name(db, user_name=token_data.username)
    if user is None:
        raise credentials_exception
    return user

@router.post("/user/signup", response_model=schemas.UserOut)
async def create_user(data: schemas.User, db: Session = Depends(get_db)):
    user = schemas.User(username = data.username,password = utils.get_hashed_password(data.password))
    user = crud.create_user(db, user)
    if user is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)

    return schemas.UserOut(username=user.username)

@router.post("/user/token", response_model=schemas.Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = crud.get_user_by_name(db, form_data.username)

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect username or password",
        )

    hased_password = user.password
    if not utils.verify_password(form_data.password, hased_password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect username or password",
        )

    return {"access_token": utils.create_access_token(user.username), "token_type": "bearer"}