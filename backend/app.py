from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:password@db:5432/todo'
db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = Task.query.all()
    return jsonify([{"id": t.id, "title": t.title} for t in tasks])

@app.route('/tasks', methods=['POST'])
def add_task():
    data = request.json
    task = Task(title=data['title'])
    db.session.add(task)
    db.session.commit()
    return jsonify({"message": "Task added"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
