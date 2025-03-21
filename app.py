from datetime import date

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

mysql_username="root"
mysql_password=""


# Configure MySQL database connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://'+mysql_username+':'+mysql_password+'@localhost/task_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Task Model
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200))
    due_date = db.Column(db.String(50), default=date.today().__str__())
    status = db.Column(db.String(20), default="Pending")


# Create tables
with app.app_context():
    db.create_all()

# Create a new task
@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.json
    new_task = Task(
        title=data.get('title', 'Untitled Task'),  # Default title if missing
        description=data.get('description', 'No description provided'),
        due_date=data.get('due_date', date.today().__str__()),
        status=data.get('status', 'Pending')
    )
    db.session.add(new_task)
    db.session.commit()
    return jsonify({"message": "Task created successfully!"}), 201

# get all tasks
@app.route('/tasks', methods=['GET'])
def get_tasks():
    try:
        tasks = Task.query.all()
        tasks_list = [{'id':t.id, 'title':t.title, 'description':t.description, 'due_date':t.due_date, 'status':t.status} for t in tasks]
        return jsonify(tasks_list), 200
    except:
        return jsonify("Task not found"), 404

# Get a single task
@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = Task.query.get(task_id)
    if not task:
        return jsonify({"error": "Task not found"}), 404
    return jsonify({"id": task.id, "title": task.title, "description": task.description, "due_date": task.due_date, "status": task.status})


# Update a task
@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = Task.query.get(task_id)
    if not task:
        return jsonify({"error": "Task not found"}), 404

    # fetching the request data
    data = request.json
    task.title = data.get('title', task.title)
    task.description = data.get('description', task.description)
    task.due_date = data.get('due_date', task.due_date)
    task.status = data.get('status', task.status)

    db.session.commit()
    return jsonify({"message": f"Task updated!"}), 201

# delete a task
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = Task.query.get(task_id)
    if not task:
        return jsonify({"message": "Task not found"}), 404
    db.session.delete(task)
    db.session.commit()
    return  jsonify({"message": "Task deleted successfully!"})


if __name__ == '__main__':
    app.run()