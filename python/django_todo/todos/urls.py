from django.conf.urls import patterns, url
from todos.views import Index

urlpatterns = patterns(
    '',
    url(r'^$', Index.as_view(), name='index')
)
