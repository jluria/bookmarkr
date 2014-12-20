from django.conf.urls import patterns, url
from accounts import views

urlpatterns = patterns('',
    url(r'^$', views.user_login, name='login'),
)
