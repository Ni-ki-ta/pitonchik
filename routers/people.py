from fastapi import APIRouter, HTTPException, Depends
from routers.sheme import PeopleAddSchema, PeopleSchema
from dependencies import get_people_service
from crud.people import PeopleService
from typing import Annotated

people_router = APIRouter(prefix="/people", tags=["people"])


@people_router.post("", summary="Добавить человека")
async def add_person(
        data: PeopleAddSchema,
        people_crud: PeopleService = Depends(get_people_service)
):
    return await people_crud.create(data)


@people_router.get("", summary="Получить всех людей", response_model=list[PeopleSchema])
async def get_people(
        people_crud: Annotated[PeopleService, Depends(get_people_service)]
):
    return await people_crud.get_all()


@people_router.get("/{person_id}", summary="Получить конкретного человека", response_model=PeopleSchema)
async def get_person(
        person_id: int,
        people_crud: PeopleService = Depends(get_people_service)
):
    person = await people_crud.get_person(person_id)
    if not person:
        raise HTTPException(status_code=404, detail="Person wasn't found")
    return person
