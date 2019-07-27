from django.conf.urls import url 
from . import views

urlpatterns=[
    url(r'^$', views.index),
    url(r'^addWordToSession$', views.addWordToSession),
    url(r'^show$', views.show),
    url(r'^clearSession$', views.clearSession)
]