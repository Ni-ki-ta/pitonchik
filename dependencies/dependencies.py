from typing import TYPE_CHECKING, Annotated

from fastapi import Depends
from fastapi_users.authentication.strategy import DatabaseStrategy

from src.config import settings
from src.database import get_async_session
from crud.people import PeopleService
from src.user_manager import UserManager
from sqlalchemy.ext.asyncio import AsyncSession
from src.models import User
from src.access_token import AccessToken
from fastapi_users.authentication.strategy import AccessTokenDatabase
if TYPE_CHECKING:
    from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase


async def get_people_service(
        session: AsyncSession = Depends(get_async_session)
) -> PeopleService:
    yield PeopleService(session)

# async def get_pets_service(session: AsyncSession = Depends(new_session)) -> PeopleService:
#     return PeopleService(session)


async def get_user_db(
        session: Annotated[
            AsyncSession,
            Depends(get_async_session)]):
    yield User.get_db(session=session)


async def get_access_token_db(
        session: Annotated[
            AsyncSession,
            Depends(get_async_session)]):
    yield AccessToken.get_db(session=session)


def get_database_strategy(
    access_token_db: Annotated[
        AccessTokenDatabase[AccessToken],
        Depends(get_access_token_db),
    ]
) -> DatabaseStrategy:
    return DatabaseStrategy(
        database=access_token_db,
        lifetime_seconds=settings.lifetime_seconds,
    )


async def get_user_manager(user_db: Annotated["SQLAlchemyUserDatabase", Depends(get_user_db)]):
    yield UserManager(user_db)
