from datetime import date

import uvicorn
from fastapi import FastAPI, HTTPException
from psycopg.types import datetime
from sqlalchemy import select

from src.database import async_engine_postgres, Base, SessionDep
from src.models import PeopleOrm, PetOrm, AnimalType
from pydantic import BaseModel

app = FastAPI()

@app.post("/setup_database")
async def setup_database():
    async with async_engine_postgres.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
        print("Tables in Base.metadata:", list(Base.metadata.tables.keys()))

    return {"ok": True}


class PetAddSchema(BaseModel):
    name: str | None = None
    animal_type: AnimalType


class PetSchema(PetAddSchema):
    id: int
    owner_id: int

    class Config:
        from_attributes = True


class PeopleAddSchema(BaseModel):
    name: str
    age: int
    birthday: date | None = None


class PeopleSchema(PeopleAddSchema):
    id: int
    pets: list[PetSchema] = []

    class Config:
        from_attributes = True


@app.post(
    "/people",
    summary="Добавить человека",
    tags=["Люди"])
async def add_person(data: PeopleAddSchema, session: SessionDep):
    new_person = PeopleOrm(
        name=data.name,
        age=data.age,
        birthday=data.birthday
    )
    session.add(new_person)
    await session.commit()
    await session.refresh(new_person)
    return {"success": True, "message": "Человек успешно добавлен"}


@app.get(
    "/people",
    summary="Получить всех людей",
    tags=["Люди"])
async def get_people(session: SessionDep):
    query = select(PeopleOrm)
    result = await session.execute(query)
    return result.scalars().all()


@app.get(
    "/people/{person_id}",
    summary="Получить конкретного человека",
    tags=["Люди"],
    response_model=PeopleSchema)
async def ip(person_id: int, session: SessionDep):
    # person = await session.get(PeopleOrm, person_id)
    # if not person:
    #     raise HTTPException(status_code=404, detail="Человек не найден")
    result = await session.execute(select(PeopleOrm).where(PeopleOrm.id == person_id))
    person = result.scalars().first()
    if not person:
        raise HTTPException(status_code=404, detail="Человек не найден")
    return person


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
