import sqlite3
from sqlalchemy.orm import sessionmaker
from create_table import Person, engine


from create_table import Person, engine, Search_output

# Создание сессии
Session = sessionmaker(bind=engine)
session = Session()
def person_add(name, res): # Добавление новой записи в базу данных
    new_person = Person(name=name)
    session.add(new_person)
    session.add(Search_output(text=res))
    session.commit()
    # Закрытие сессии
    session.close()

# # Создание новой сессии
# Session = sessionmaker(bind=engine)
# session = Session()
#
# # Извлечение всех записей из таблицы
# people = session.query(Person).all()
# for person in people:
#     print(person)
name = 'Азиз Антеев'
bithday = '09.08.1996'

connect = sqlite3.connect('../people.db')
cursor = connect.cursor()
cursor.execute(f"INSERT INTO people (id, name) VALUES (3, {name}) ")
connect.commit()
