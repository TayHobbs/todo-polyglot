from django.shortcuts import render
from django.views.generic import View

from todos.models import Todo


class Index(View):

    def get(self, request):
        todos = Todo.objects.all()
        return render(request, 'index.html', {'todos': todos})
