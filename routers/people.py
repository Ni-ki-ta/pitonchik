from fastapi import APIRouter, HTTPException
from sqlalchemy import select
from routers.sheme import PeopleAddSchema, PeopleSchema
from src.models import PeopleOrm
from src.database import SessionDep

people_router = APIRouter(prefix="/people", tags=["people"])


@people_router.post("/", summary="Добавить человека")
async def add_person(data: PeopleAddSchema, session: SessionDep):
    new_person = PeopleOrm(
        name=data.name,
        age=data.age,
        birthday=data.birthday
    )
    session.add(new_person)
    await session.commit()
    await session.refresh(new_person)
    return {"success": True, "message": "Person was successfully added"}


@people_router.get("/", summary="Получить всех людей")
async def get_people(session: SessionDep):
    query = select(PeopleOrm)
    result = await session.execute(query)
    return result.scalars().all()


@people_router.get("/{person_id}", summary="Получить конкретного человека", response_model=PeopleSchema)
async def get_person(person_id: int, session: SessionDep):
    result = await session.execute(select(PeopleOrm).where(PeopleOrm.id == person_id))
    person = result.scalars().first()
    if not person:
        raise HTTPException(status_code=404, detail="Person wasn't found")
    return person