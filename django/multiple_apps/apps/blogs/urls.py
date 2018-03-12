# / - display "placeholder to later display all the list of blogs" via HttpResponse. Have this be handled by a method named 'index'
# /new - display "placeholder to display a new form to create a new blog" via HttpResponse. Have this be handled by a method named 'new'
# /create - Have this be handled by a method named 'create'.  For now, have this url redirect to /
# /{{number}} - display 'placeholder to display blog {{number}}'.  For example /15 should display a message 'placeholder to display blog 15'.  Have this be handled by a method named 'show'
# /{{number}}/edit - display 'placeholder to edit blog {{number}}.  Have this be handled by a method named 'edit'
# /{{number}}/delete - Have this be handled by a method named 'destroy'. For now, have this url redirect to /


from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^blogs/$', views.index),
    url(r'^blogs/new/$', views.new),
    url(r'^blogs/create/$', views.create),
    url(r'^blogs/(?P<number>\d+)/$', views.show),
    url(r'^blogs/(?P<number>\d+)/edit/$', views.edit),
    url(r'^blogs/(?P<number>\d+)/delete/$', views.destroy),
]

# Example:
# urlpatterns = [
#     url(r'^articles/2003/$', views.special_case_2003),
#     url(r'^articles/([0-9]{4})/$', views.year_archive),
#     url(r'^articles/([0-9]{4})/([0-9]{2})/$', views.month_archive),
#     url(r'^articles/([0-9]{4})/([0-9]{2})/([0-9]+)/$', views.article_detail),
#     url(r'^articles/(?P<year>[0-9]{4})/$', views.year_archive),
# ]