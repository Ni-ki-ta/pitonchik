import asyncio
import sys

import uvicorn
from fastapi import FastAPI
from routers.people import people_router
from routers.pets import pets_router

from src.database import async_engine_postgres, Base


app = FastAPI()
app.include_router(people_router)
app.include_router(pets_router)


async def create_tables():
    async with async_engine_postgres.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
        print("Tables in Base.metadata:", list(Base.metadata.tables.keys()))


if __name__ == "__main__":
    if sys.platform == 'win32':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    asyncio.run(create_tables())
    uvicorn.run("main:app", reload=True)
