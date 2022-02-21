from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


Base = declarative_base()
engine = create_engine('sqlite:///tasks_list.db', echo=True)
Session = sessionmaker(bind=engine)
session = Session()


class Tasks(Base):
    __tablename__ = "Tasks"
    id = Column(Integer, primary_key=True)
    task_name = Column(String)
    status = Column(String)

    def __init__(self, task_name, status):
        self.task_name = task_name
        self.status = status


Base.metadata.create_all(engine)