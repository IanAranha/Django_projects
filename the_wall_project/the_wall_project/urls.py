from django.conf.urls import url, include

def test(request):
    print("""
   
    .--H--. ||                 |
    _//_||  ||                 |
   [    -|  |'--;--------------'
   '-()-()----()"()^^^^^^^()"()'
   
    """)

urlpatterns = [
    url(r'^', include('apps.the_wall_app.urls'))
]
