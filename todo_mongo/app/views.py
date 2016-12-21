from flask import render_template, request, redirect, url_for, flash
from app import app
from .models import Todo, TodoForm
import datetime

@app.route('/')
def index():
    form = TodoForm()
    todos = Todo.objects.order_by('-time')
    return render_template('index.html', todos=todos, form=form)

@app.route('/add', methods=['POST'])
def add():
    '''form = request.form
    content = form['content']
    todo = Todo(content=content)
    todo.save()
    return redirect('/')'''
    form = TodoForm(request.form)
    if form.validate():
        content = form.content.data
        print(content)
        todo = Todo(content=content, time=datetime.datetime.now())
        todo.save()
        flash('发表成功')
    # return redirect(url_for('index'))

    todos = Todo.objects.order_by('-time')
    return render_template('index.html', todos=todos, form=form)

@app.route('/done-or-undone/<string:todo_id>')
def done_or_undone(todo_id):
    # form = TodoForm()
    todo = Todo.objects.get_or_404(id=todo_id)
    # todo.status = 1
    todo.status = 0 if todo.status else 1
    todo.save()
    return redirect(url_for('index'))
    # todos = Todo.objects.all()
    # return render_template('index.html', todos=todos, form=form)

@app.route('/delete/<string:todo_id>')
def delete(todo_id):
    todo = Todo.objects.get_or_404(id=todo_id)
    todo.delete()
    return redirect(url_for('index'))

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html')


