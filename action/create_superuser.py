import asyncio
import contextlib
import sys
from os import getenv

from routers.shemas.user import UserCreate
from dependencies.dependencies import get_user_manager, get_user_db
from src.database import new_session
from src.models import User
from src.user_manager import UserManager

get_users_db_context = contextlib.asynccontextmanager(get_user_db)
get_user_manager_context = contextlib.asynccontextmanager(get_user_manager)

default_email = getenv("DEFAULT_EMAIL", "samsam@gmail.com")
default_password = getenv("DEFAULT_PASSWORD", "123123")
default_is_active = True
default_is_superuser = True
default_is_verified = True


async def create_user(
        user_manager: UserManager,
        user_create: UserCreate
) -> User:
    user = await user_manager.create(
        user_create=user_create,
        safe=False
    )
    return user


async def create_superuser(
        email: str = default_email,
        password: str = default_password,
        is_active: bool = default_is_active,
        is_superuser: bool = default_is_superuser,
        is_verified: bool = default_is_verified,
):
    user_create = UserCreate(
        email=email,
        password=password,
        is_active=is_active,
        is_superuser=is_superuser,
        is_verified=is_verified,
    )
    async with new_session() as session:
        async with get_users_db_context(session) as users_db:
            async with get_user_manager_context(users_db) as user_manager:
                return await create_user(
                    user_create=user_create,
                    user_manager=user_manager
                )


if __name__ == "__main__":
    if sys.platform == 'win32':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    asyncio.run(create_superuser())
