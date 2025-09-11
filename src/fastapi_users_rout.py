import uuid

from fastapi import FastAPI
from fastapi_users import FastAPIUsers

from src.models import User, UserIdType
from dependencies.dependencies import get_user_manager
from dependencies.backend import authentication_backend

fastapi_users = FastAPIUsers[User, UserIdType](
    get_user_manager,
    [authentication_backend],
)

current_active_user = fastapi_users.current_user(active=True)
current_active_super_user = fastapi_users.current_user(active=True, superuser=True)
