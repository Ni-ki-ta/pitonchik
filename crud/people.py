from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from src.models import PeopleOrm
from routers.sheme import PeopleAddSchema


class PeopleService:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_all(self) -> list[PeopleOrm]:
        query = select(PeopleOrm)
        result = await self.session.execute(query)
        return result.scalars().all()

    async def get_person(self, person_id: int) -> PeopleOrm | None:
        result = await self.session.execute(
            select(PeopleOrm).where(PeopleOrm.id == person_id)
        )
        return result.scalars().first()

    async def create(self, data: PeopleAddSchema) -> PeopleOrm:
        new_person = PeopleOrm(
            name=data.name,
            age=data.age,
            birthday=data.birthday
        )
        self.session.add(new_person)
        await self.session.commit()
        await self.session.refresh(new_person)
        print("Person was successfully added")
        return new_person

    class Config:
        from_attribures = True
