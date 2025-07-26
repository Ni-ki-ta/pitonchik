from sqlalchemy import create_engine
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

engine_postgres = create_engine(
    url=settings.DATABASE_URL_psycopg_postgres,
    echo=True,
)

session_factory_postgres = sessionmaker(engine_postgres)

Base = declarative_base()
