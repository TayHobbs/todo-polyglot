from django.conf.url import patterns, url
from todos.views import Index

urlpatterns = patterns(
    '',
    url(r'^$', Index.as_view(), name='index')
)
