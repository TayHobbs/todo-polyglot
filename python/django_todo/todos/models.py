from django.db import models


class Todo(models.Model):
    name = models.CharField()
    completed = models.BooleanField()
