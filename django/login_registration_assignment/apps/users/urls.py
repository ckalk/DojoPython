from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name="my_index"),
    url(r'^users/register$', views.register, name="my_register"),
    url(r'^users/login$', views.login, name="my_login"),
    url(r'^users/success$', views.success, name="my_success"),
]

