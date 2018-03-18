from django.conf.urls import url
from . import views

urlpatterns = [
	url(r"^$", views.index, name="index"),
	url(r'^leagues/query/(?P<number>\d+)/$', views.query),
	url(r'^leagues/queryII/(?P<number>\d+)/$', views.queryII),
	url(r'^leagues/queryIII/(?P<number>\d+)/$', views.queryIII),
	url(r"^make_data/", views.make_data, name="make_data"),
]