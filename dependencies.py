from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.database import get_async_session
from crud.people import PeopleService


async def get_people_service(session: AsyncSession = Depends(get_async_session)) -> PeopleService:
    yield PeopleService(session)

# async def get_pets_service(session: AsyncSession = Depends(new_session)) -> PeopleService:
#     return PeopleService(session)