from fastapi import APIRouter, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import joinedload

from routers.shemas.sheme import PetAddSchema, PetSchema
from src.models import PetOrm, PeopleOrm
from src.database import SessionDep

pets_router = APIRouter(prefix="/pets", tags=["pets"])


@pets_router.post("/", response_model=PetSchema, summary="Добавить нового питомца")
async def add_pet(pet_data: PetAddSchema, session: SessionDep):
    owner = await session.get(PeopleOrm, pet_data.owner_id)
    if not owner:
        raise HTTPException(status_code=404, detail="Owner wasn't found")

    new_pet = PetOrm(
        name=pet_data.name,
        animal_type=pet_data.animal_type,
        owner_id=pet_data.owner_id
    )

    session.add(new_pet)
    await session.commit()
    await session.refresh(new_pet)

    return new_pet


@pets_router.get("/", response_model=list[PetSchema], summary="Получить всех питомцев")
async def get_all_pets(session: SessionDep):
    result = await session.execute(
        select(PetOrm)
        .options(joinedload(PetOrm.owner))
    )
    pets = result.scalars().all()
    return pets


@pets_router.get("/{pet_id}", response_model=PetSchema, summary="Получить питомца по id")
async def get_pet(pet_id: int, session: SessionDep):
    result = await session.execute(
        select(PetOrm)
        .options(joinedload(PetOrm.owner))
        .where(PetOrm.id == pet_id)
    )
    pet = result.scalars().first()

    if not pet:
        raise HTTPException(status_code=404, detail="Pet wasn't found")

    return pet
