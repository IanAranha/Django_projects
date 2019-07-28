from django.conf.urls import url, include


urlpatterns = [
    url(r'^', include('apps.blogs.urls')),
    url(r'^', include('apps.surveys.urls')),
    url(r'^', include('apps.users.urls')),
]

