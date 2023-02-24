from fastapi import APIRouter
from api.v0 import user

api_router = APIRouter(prefix="/v0")
api_router.include_router(user.router, tags=["user"])