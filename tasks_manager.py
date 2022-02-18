from flask import Flask, jsonify
import tasks_dp
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def add_task():
    new_task = tasks_dp.Tasks(input("Введите название задачи"), datetime_creation=datetime, status="В работе")
    tasks_dp.session.add(new_task)
    tasks_dp.session.commit()


@app.route('/')
def modify_task(task_id):
    modifiable_task = tasks_dp.session.query(tasks_dp.Tasks).get(task_id)
    if input("Задача решена? (да/нет)") == "да":
        modifiable_task.status = "Завершено"


@app.route('/')
def delete_task(task_name):
    pass


@app.route('/')
def list_task():
    pass