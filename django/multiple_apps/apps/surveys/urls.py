# /surveys - display "placeholder to display all the surveys created"
# /surveys/new - display "placeholder for users to add a new survey

from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^surveys/$', views.index),
    url(r'^surveys/new/$', views.new),
]
