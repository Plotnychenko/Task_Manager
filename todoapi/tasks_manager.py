from flask import Flask, jsonify
from marshmallow import Schema, fields
import tasks_db

app = Flask(__name__)


class TasksSchema(Schema):
    class Meta:
        model = tasks_db.Tasks
        db_session = tasks_db.session
    tasks_db.Tasks.id = fields.Integer(dump_only=True)
    tasks_db.Tasks.task_name = fields.String()
    tasks_db.Tasks.status = fields.String()


@app.route('/add_task/<task_name>', methods=['POST'])
def add_task(task_name):
    new_task = tasks_db.Tasks(
        task_name=task_name,
        status="В работе"
    )
    tasks_db.session.add(new_task)
    tasks_db.session.commit()


@app.route('/modify_task/<int:task_id>', methods=['PUT'])
def modify_task(task_id):
    modifiable_task = tasks_db.session.query(tasks_db.Tasks).get(task_id)
    modifiable_task.status = "Завершено"
    tasks_db.session.add(modifiable_task)
    tasks_db.session.commit()


@app.route('/delete_task/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = tasks_db.session.query(tasks_db.Tasks).filter(tasks_db.Tasks.id == task_id).one()
    tasks_db.session.delete(task)
    tasks_db.session.commit()


@app.route('/list_tasks', methods=['GET'])
def list_task():
    task_schema = TasksSchema(many=True)
    task = tasks_db.session.query(tasks_db.Tasks).all()
    return jsonify(task_schema.dump(task))


if __name__ == "__main__":
    app.run()
