from django.conf.urls import url, include


urlpatterns = [
    url(r'^', include('apps.session_words_app.urls')),
]
