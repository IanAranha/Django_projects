from django.conf.urls import url, include


urlpatterns = [
    url(r'^', include('apps.dojo_ninja_app.urls')),
    url(r'^', include('apps.book_author_app.urls')),
]
