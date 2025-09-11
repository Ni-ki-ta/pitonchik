from typing import Annotated

from fastapi import APIRouter, Depends

from routers.shemas.user import UserRead
from src.fastapi_users_rout import current_active_user, current_active_super_user
from src.models import User

mess_router = APIRouter(
    prefix="/messages"
)


@mess_router.get("")
def get_user_messages(
        user: Annotated[
            User,
            Depends(current_active_user)
        ]
):
    return {
        "messages": {"m1", "m2", "m3"},
        "user": UserRead.model_validate(user)
    }


@mess_router.get("/secrets")
def get_superuser_messages(
        user: Annotated[
            User,
            Depends(current_active_super_user)
        ]
):
    return {
        "messages": {"secret-m1", "secret-m2", "secret-m3"},
        "user": UserRead.model_validate(user)
    }


def get_superuser_messages():
    pass
