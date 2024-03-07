from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import *

# Создание экземпляра базы данных
engine = create_engine('sqlite:///people.db', echo=True)
Base = declarative_base()

# Определение модели для хранения характеристик человека
class Person(Base):
    __tablename__ = 'people'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(Text, nullable=False)

class Search_output(Base):
    __tablename__ = 'search_output'

    id = Column(Integer, primary_key=True, autoincrement=True)
    text = Column(Text)


# Создание таблицы в базе данных
Base.metadata.create_all(engine)