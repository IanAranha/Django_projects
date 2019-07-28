from django.conf.urls import url
from . import views

urlpatterns=[
     url(r'^surveys$', views.index),
     url(r'^surveys/new$', views.new),
     # url(r'^surveys/create$', views.create),
     # url(r'^surveys/(?P<num>\d+)$', views.show),
     # url(r'^surveys/(?P<num>\d+)/edit$', views.edit),
     # url(r'^surveys/(?P<num>\d+)/delete$', views.destroy),
]