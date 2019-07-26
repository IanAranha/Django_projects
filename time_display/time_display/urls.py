from django.conf.urls import url, include

print('&' * 50)
urlpatterns = [
    url(r'^', include('apps.time_display_app.urls')),
]

