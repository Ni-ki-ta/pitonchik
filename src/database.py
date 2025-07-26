from sqlalchemy import URL, create_engine, text
from sqlalchemy.orm import declarative_base

from sqlalchemy.orm import Session, sessionmaker
from src.config import settings


engine = create_engine(
    url=settings.DATABASE_URL_psycopg,
    echo=True,
    #pool_size=5,
    #max_overflow=10
)

session_factory = sessionmaker(engine)


# class Base(DeclarativeBase):
#     pass

Base = declarative_base()
