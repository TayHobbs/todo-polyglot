from django.conf.urls import patterns, url
from todos.views import index, create, complete

urlpatterns = patterns(
    '',
    url(r'^$', index, name='index'),
    url(r'^create$', create, name='create'),
    url(r'^complete$', complete, name='complete')
)
