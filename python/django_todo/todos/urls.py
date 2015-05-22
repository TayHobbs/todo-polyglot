from django.conf.urls import patterns, url
from todos.views import index

urlpatterns = patterns(
    '',
    url(r'^$', index, name='index')
)
