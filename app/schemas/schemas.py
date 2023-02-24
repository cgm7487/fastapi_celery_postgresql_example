#define API schemas here
from typing import Dict, List, Optional, Union
from pydantic import BaseModel

class User(BaseModel):
    username: str
    password: str

class UserOut(BaseModel):
    username: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None