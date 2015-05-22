from django.shortcuts import render, redirect

from todos.models import Todo


def index(request):
    todos = Todo.objects.all()
    return render(request, 'index.html', {'todos': todos})


def create(request):
    Todo.objects.create(name=request.POST['todo'], completed=False)
    return redirect('index')


def complete(request):
    todo = Todo.objects.get(pk=request.POST['id'])
    todo.completed = not todo.completed
    todo.save()
    return redirect('index')


def delete(request):
    Todo.objects.get(pk=request.POST['id']).delete()
    return redirect('index')


def edit(request):
    todo = Todo.objects.get(pk=request.POST['id'])
    todo.name = request.POST['todo']
    todo.save()
    return redirect('index')
