from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index ),
    url(r'^users$', views.show_all),
    url(r'^users/new$', views.new),
    url(r'^users/create$', views.create),
    url(r'^users/(?P<id>\d+)$', views.show_one),
    url(r'^users/(?P<id>\d+)/edit$', views.edit),
    url(r'^users/(?P<id>\d+)/destroy$', views.destroy),
]

