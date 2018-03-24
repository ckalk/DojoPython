from django.conf.urls import url

from . import views

app_name = 'users'
urlpatterns = [
    url(r'^users/new$', views.new, name="my_new"),
    url(r'^users/create$', views.create, name="my_create"),
    url(r'^users/edit/(?P<id>\d+)$', views.edit, name="my_edit"),
    url(r'^users/update/(?P<id>\d+)$', views.update, name="my_update"),
    url(r'^users/show/(?P<id>\d+)$', views.show, name="my_show"),
    url(r'^users/destroy/(?P<id>\d+)$', views.destroy, name="my_destroy"),
]

