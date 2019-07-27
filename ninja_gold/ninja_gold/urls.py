from django.conf.urls import url, include

urlpatterns = [
    url(r'^', include('apps.ninja_gold_app.urls')),
]
