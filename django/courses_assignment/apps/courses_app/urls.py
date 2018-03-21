from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name="my_index"),
    url(r'^courses/create$', views.create, name="my_create"),
    url(r'^courses/(?P<id>\d+)/delete$', views.delete, name="my_delete"),
    url(r'^courses/destroy/(?P<id>\d+)$', views.destroy, name="my_destroy"),
]


