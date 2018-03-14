from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^amadon/$', views.index),
    url(r'^amadon/index/$', views.index),
    url(r'^amadon/buy/(?P<prod_id>\d+)/$', views.buy),
    url(r'^amadon/checkout/$', views.checkout),
    url(r'^amadon/reset/$', views.reset)
]