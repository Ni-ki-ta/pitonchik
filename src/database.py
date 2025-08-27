from fastapi import Depends
from sqlalchemy import create_engine
from typing import Annotated, AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import declarative_base

from sqlalchemy.orm import sessionmaker
from src.config import settings


# engine = create_engine(
#     url=settings.DATABASE_URL_psycopg,
#     echo=True,
#     #pool_size=5,
#     #max_overflow=10
# )
#
#session_factory = sessionmaker(engine)

# engine_postgres = create_engine(
#     url=settings.DATABASE_URL_psycopg_postgres,
#     echo=True,
# )

async_engine_postgres = create_async_engine(
    url=settings.DATABASE_URL_psycopg_postgres,
    echo=True,
)

#session_factory_postgres = sessionmaker(engine_postgres)

new_session = async_sessionmaker(async_engine_postgres)
async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with new_session() as session:
        yield session

SessionDep = Annotated[AsyncSession, Depends(get_async_session)]

Base = declarative_base()

