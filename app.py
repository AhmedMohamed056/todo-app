from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)

# اتصال بقاعدة البيانات
client = MongoClient("mongodb+srv://hamadarayyan056:Hamd056#@cluster1.nwa9q92.mongodb.net/?retryWrites=true&w=majority&appName=Cluster1")
db = client["todo_db"]
tasks_collection = db["tasks"]

@app.route('/')
def index():
    tasks = list(tasks_collection.find())
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add():
    title = request.form.get('task')
    status = request.form.get('status') or 'later'
    priority = request.form.get('priority') or 'Medium'
    due_date = request.form.get('due_date') or ''

    if title:
        tasks_collection.insert_one({
            'title': title,
            'status': status,
            'completed': False,
            'priority': priority,
            'due_date': due_date,
        })
    return redirect(url_for('index'))

@app.route('/delete/<task_id>', methods=['POST'])
def delete(task_id):
    tasks_collection.delete_one({'_id': ObjectId(task_id)})
    return redirect(url_for('index'))

@app.route('/toggle_complete/<task_id>', methods=['POST'])
def toggle_complete(task_id):
    task = tasks_collection.find_one({'_id': ObjectId(task_id)})
    if task:
        tasks_collection.update_one(
            {'_id': ObjectId(task_id)},
            {'$set': {'completed': not task['completed']}}
        )
    return redirect(url_for('index'))

@app.route('/change_status/<task_id>', methods=['POST'])
def change_status(task_id):
    task = tasks_collection.find_one({'_id': ObjectId(task_id)})
    if task:
        current = task['status']
        next_status = {'now': 'later', 'later': 'done', 'done': 'now'}[current]
        tasks_collection.update_one(
            {'_id': ObjectId(task_id)},
            {'$set': {'status': next_status}}
        )
    return redirect(url_for('index'))

@app.route('/edit/<task_id>', methods=['GET', 'POST'])
def edit(task_id):
    task = tasks_collection.find_one({'_id': ObjectId(task_id)})

    if not task:
        return redirect(url_for('index'))

    if request.method == 'POST':
        updated_task = {
            'title': request.form.get('task'),
            'status': request.form.get('status'),
            'priority': request.form.get('priority'),
            'due_date': request.form.get('due_date') or '',
            'completed': task['completed'],  # حافظ على الحالة القديمة
        }
        tasks_collection.update_one(
            {'_id': ObjectId(task_id)},
            {'$set': updated_task}
        )
        return redirect(url_for('index'))

    return render_template('edit.html', task=task, task_id=task_id)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

