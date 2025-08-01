import datetime
from typing import Optional, Annotated
from sqlalchemy import text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.database import Base
import enum

intpk = Annotated[int, mapped_column(primary_key=True)]


class PeopleOrm(Base):
    __tablename__ = "people"

    id: Mapped[intpk]
    name: Mapped[str]
    age: Mapped[int]
    birthday: Mapped[datetime.datetime] = mapped_column(server_default=text("CURRENT_TIMESTAMP"))
    pets: Mapped[list["PetOrm"]] = relationship(back_populates="owner")


class AnimalType(enum.Enum):
    CAT = "cat"
    DOG = "dog"
    PARROT = "parrot"


class PetOrm(Base):
    __tablename__ = "pet"
    id: Mapped[intpk]
    name: Mapped[Optional[str]]
    animal_type: Mapped[AnimalType]
    owner_id: Mapped[int] = mapped_column(ForeignKey("people.id"))
    owner: Mapped["PeopleOrm"] = relationship(back_populates="pets")





# metadata_obj = MetaData()
#
# people_table = Table(
#     "People",
#     metadata_obj,
#     Column("id", Integer, primary_key=True),
#     Column("name", String),
#     Column("age", Integer),
#     Column("pets", Integer),
# )
# pet_table = Table(
#     "Pet",
#     metadata_obj,
#     Column("id", Integer, primary_key=True),
#     Column("name", String),
#     Column("animal_type", Integer),
# )
