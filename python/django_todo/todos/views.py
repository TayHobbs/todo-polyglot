from django.shortcuts import render, redirect

from todos.models import Todo


def index(request):
    todos = Todo.objects.all()
    return render(request, 'index.html', {'todos': todos})


def create(request):
    Todo.objects.create(name=request.POST['todo'], completed=False)
    return redirect('index')
