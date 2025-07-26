from sqlalchemy import URL, text, insert
#from models import metadata_obj, people_table
from database import engine


# def create_tables():
#     engine.echo = False
#     metadata_obj.drop_all(engine)
#     metadata_obj.create_all(engine)
#     engine.echo = True
#
#
# def insert_data():
#     with engine.connect() as conn:
#         # statement = """INSERT INTO People (id, name, age, pet)
#         #             VALUES (1, 'Иван Иванов', 30, 1);"""
#         statement = insert(people_table).values(
#             id=1,
#             name='Иван Иванов',
#             age=30,
#             pet=1
#         )
#         #conn.execute(text(statement))
#         conn.execute(statement)
#         conn.commit()


