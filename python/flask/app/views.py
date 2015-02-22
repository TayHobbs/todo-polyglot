from flask import render_template, request, redirect, url_for

from . import app, models
from .db import db


@app.route('/')
def index():
    todos = models.Todo.query.all()
    return render_template('index.html', todos=todos)


@app.route('/add-todo', methods=['POST'])
def add_todo():
    todo = models.Todo(name=request.form['todo'], completed=False)
    db.session.add(todo)
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/delete-todo', methods=['POST'])
def delete_todo():
    todo = models.Todo.query.get(request.form['id'])
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/edit-todo', methods=['POST'])
def edit_todo():
    todo = models.Todo.query.get(request.form['id'])
    todo.name = request.form['todo']
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/completed', methods=['GET', 'POST'])
def completed():
    if request.method == 'GET':
        todos = models.Todo.query.filter_by(completed=True)
        return render_template('completed.html', todos=todos)
    else:
        todo = models.Todo.query.get(request.form['id'])
        if todo.completed:
            todo.completed = False
        else:
            todo.completed = True
        db.session.commit()
        return redirect(url_for('index'))


@app.route('/active')
def active():
    todos = models.Todo.query.filter_by(completed=False)
    return render_template('active.html', todos=todos)


@app.route('/clear-completed', methods=['POST'])
def clear_completed():
    todos = models.Todo.query.filter_by(completed=True)
    for todo in todos:
        db.session.delete(todo)
        db.session.commit()
    return redirect(url_for('index'))
