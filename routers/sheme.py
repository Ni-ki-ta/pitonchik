from pydantic import BaseModel, EmailStr, ConfigDict
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


class UserSchema(BaseModel):
    model_config = ConfigDict(strict=True)

    username: str
    password: bytes
    email: EmailStr | None = None
    active: bool = True