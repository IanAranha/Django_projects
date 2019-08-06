from django.conf.urls import url, include


def test(request):
    print("""
       /b_,dM\__,_
    _/MMMMMMMMMMMm,
   _YMMMMMMMMMMMM(
  `MMMMMM/   /   \   _   ,    
   MMM|  __  / __/  ( |_|
   YMM/_/# \__/# \    | |_)arry
   (.   \__/  \__/     ___  
     )       _,  |    '_|_)
_____/\     _   /       | otter
    \  `._____,'
     `..___(__
              ``-.
                  \
                   )""")

urlpatterns = [
    url(r'^', include('apps.login_reg_app.urls')),
]
