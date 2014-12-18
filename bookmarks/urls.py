from django.conf.urls import patterns, url
from bookmarks import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<list_id>\d+)/$', views.detail, name='detail'),
)
