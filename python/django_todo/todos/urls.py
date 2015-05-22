from django.conf.urls import patterns, url
from todos.views import index, create, complete, delete, edit, active, completed, clear_completed

urlpatterns = patterns(
    '',
    url(r'^$', index, name='index'),
    url(r'^create$', create, name='create'),
    url(r'^complete$', complete, name='complete'),
    url(r'^delete$', delete, name='delete'),
    url(r'^edit$', edit, name='edit'),
    url(r'^active$', active, name='active'),
    url(r'^completed$', completed, name='completed'),
    url(r'^clear-completed$', clear_completed, name='clear_completed'),
)
