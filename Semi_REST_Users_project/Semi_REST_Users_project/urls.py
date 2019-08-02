
from django.conf.urls import url, include

urlpatterns = [
    url(r'^', include('apps.semirestful_users_app.urls')),
]
