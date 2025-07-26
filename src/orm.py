from sqlalchemy import select
from models import PeopleOrm, PetOrm, AnimalType#, metadata_obj,
#from database import engine, session_factory, Base
from database import engine_postgres, session_factory_postgres, Base


class SyncORM:
    @staticmethod
    def create_tables():
        engine_postgres.echo = False
        Base.metadata.drop_all(engine_postgres)
        Base.metadata.create_all(engine_postgres)
        engine_postgres.echo = True

    @staticmethod
    def insert_data():
        with session_factory_postgres() as session:
            person = PeopleOrm(
                name='Иван Иванов',
                age=30,
            )
            person_2 = PeopleOrm(
                name='Гена Букин',
                age=43,
                pets=[PetOrm(name="Kesha", animal_type=AnimalType.PARROT),
                      PetOrm(name="Murka", animal_type=AnimalType.CAT)
                      ]
            )

            session.add_all([person, person_2])
            session.flush()
            session.commit()

    @staticmethod
    def select_people():
        with session_factory_postgres() as session:
            query = select(PeopleOrm)
            result = session.execute(query)
            people = result.scalars().all()
            print(f"{people=}")

    @staticmethod
    def update_people(person_id: int = 2, new_name: str = "Ivan"):
        with session_factory_postgres() as session:
            person_ivan = session.get(PeopleOrm, person_id)
            person_ivan.name = new_name
            session.add(person_ivan)
            session.commit()
            session.refresh(person_ivan)

