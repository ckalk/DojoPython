# /register - display 'placeholder for users to create a new user record'
# /login - display 'placeholder for users to login' 
# /users/new - have the same method that handles /register also handle the url request of /users/new
# /users - display 'placeholder to later display all the list of users'

from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^users/$', views.index),
    url(r'^users/new/$', views.new),
    url(r'^register/$', views.register),
    url(r'^login/$', views.login),
]
