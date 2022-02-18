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

    def __init__(self, task_name, datetime_creation, status):
        self.task_name = task_name
        self.datetime_creation = datetime_creation
        self.status = status


Base.metadata.create_all(engine)