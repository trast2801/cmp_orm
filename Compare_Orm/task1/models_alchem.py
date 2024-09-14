from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer, String, Text


class Base(DeclarativeBase): pass

class A_Review(Base):
    __tablename__ = "task1_review"

    id = Column(Integer, primary_key=True)
    review = Column(Text)
    name = Column(String)
# Create your models here.

class A_Cinema(Base):
    __tablename__ = "task1_cinema"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    movie_duration = Column(String)
    movie_year = Column(Integer)
    genres = Column(String)
    countries = Column(String)


