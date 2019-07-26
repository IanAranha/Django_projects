from django.conf.urls import url, include

print("*" * 100)
print('inside the main urls')

urlpatterns = [
    url(r'^', include('apps.survey_app.urls')),
]
