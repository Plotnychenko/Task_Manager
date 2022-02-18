from flask import Flask
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine('sqlite:///tasks_list.db', echo=True)
Session = sessionmaker(bind=engine)
session = Session()


class Tasks(Base):
    __tablename__ = "Tasks"
    id = Column(Integer, primary_key=True, autoincrement=True)
    task_name = Column(String)
    datetime_creation = Column(DateTime)
    status = Column(Enum("В работе", "Завершено"))
    datetime_complete = Column(DateTime)

    def __init__(self, task_name, datetime_creation, status, datetime_complete):
        self.task_name = task_name
        self.datetime_creation = datetime_creation
        self.status = status
        self.datetime_complete = datetime_complete


Base.metadata.create_all(engine)
