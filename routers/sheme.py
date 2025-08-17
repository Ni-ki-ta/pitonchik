from pydantic import BaseModel
from src.models import AnimalType
from datetime import date

class PetAddSchema(BaseModel):
    name: str | None = None
    animal_type: AnimalType
    owner_id: int


class PetSchema(PetAddSchema):
    id: int

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