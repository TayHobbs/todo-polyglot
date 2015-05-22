from django.shortcuts import render_to_response

from todos.models import Todo


def index(request):
    todos = Todo.objects.all()
    return render_to_response('index.html', {'todos': todos})
