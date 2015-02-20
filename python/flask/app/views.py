from flask import render_template, request, redirect, url_for

from . import app, models
from .db import db


@app.route('/')
def index():
    todos = models.Todo.query.all()
    return render_template('index.html', todos=todos)


@app.route('/add-todo', methods=['POST'])
def add_todo():
    todo = models.Todo(name=request.form['todo'])
    db.session.add(todo)
    db.session.commit()
    return redirect(url_for('index'))
