print('#' * 100)
print("Main2 urls")

from django.conf.urls import url, include

urlpatterns=[
    url(r'^', include('apps.random_word.urls'))
]