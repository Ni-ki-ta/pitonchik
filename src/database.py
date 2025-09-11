from fastapi import Depends
from sqlalchemy import create_engine
from typing import Annotated, AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, declared_attr

from sqlalchemy.orm import sessionmaker
from src.config import settings
import re


def camel_case_to_snake_case(camel_case_str):
    snake_case_str = re.sub(r'(?<!^)(?=[A-Z])', '_', camel_case_str).lower()
    return snake_case_str

# engine = create_engine(
#     url=settings.DATABASE_URL_psycopg,
#     echo=True,
#     #pool_size=5,
#     #max_overflow=10
# )
#
#
# session_factory = sessionmaker(engine)
#
#
# engine_postgres = create_engine(
#     url=settings.DATABASE_URL_psycopg_postgres,
#     echo=True,
# )
#
# session_factory_postgres = sessionmaker(engine_postgres)


async_engine_postgres = create_async_engine(
    url=settings.DATABASE_URL_psycopg_postgres,
    echo=True,
)


new_session = async_sessionmaker(async_engine_postgres)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with new_session() as session:
        yield session

SessionDep = Annotated[AsyncSession, Depends(get_async_session)]


class Base(DeclarativeBase):
    __abstract__ = True

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return f"{camel_case_to_snake_case(cls.__name__)}s"