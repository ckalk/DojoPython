from django.conf.urls import url

from . import views

app_name = 'dashboard'
urlpatterns = [
    url(r'^dashboard$', views.dashboard, name="my_dashboard"),
    url(r'^dashboard/admin$', views.admin, name="my_admin_dashboard"),
]

