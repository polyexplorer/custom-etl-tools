from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base
Base = declarative_base()


class DummyTable(Base):
    __tablename__ = 'dummy_table'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    gender = Column(String)