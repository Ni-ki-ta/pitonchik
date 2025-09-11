from fastapi import APIRouter, Depends

from dependencies.backend import authentication_backend
from routers.auth import http_bearer
from routers.shemas.user import UserRead, UserUpdate
from src.fastapi_users_rout import fastapi_users

users_router = APIRouter(
    prefix="/users",
    tags=["Users"],
    dependencies=[Depends(http_bearer)])

# /me
# /{id}
users_router.include_router(router=fastapi_users.get_users_router(UserRead, UserUpdate))
