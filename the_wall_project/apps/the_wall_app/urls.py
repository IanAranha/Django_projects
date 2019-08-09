from django.conf.urls import url
from . import views

def test(request):
    print('''
    ,----.    ,-.   ,----.,------. ,-.   ,-.,-. ,-.
    / ,-,_/  ,'  |  / /"P /`-, ,-','  |  / //  |/ /
   / / __  ,' ,| | / ,---'  / / ,' ,| | / // J P /
  / '-' /,' ,--. |/ /      / /,' ,--. |/ // /|  /
  `----''--'   `-'`'.--""""--.--'   `-'`' `' `-'
  nnnnnnnnnnnnnnnn,'.n*""""*N.`.#######################
  NNNNNNNNNNNNNNN/ J',n*""*n.`L \##### ### ### ### ####
                : J J___/\___L L :#####################
  nnnnnnnnnnnnnn{ [{ `.    ,' }] }## ### ### ### ### ##
  NNNNNNNNNNNNNN: T T /,'`.\ T J :#####################
                 \ L,`*n,,n*',J /
  nnnnnnnnnnnnnnnn`. *n,,,,n* ,'nnnnnnnnnnnnnnnnnnnnnnn
  NNNNNNNNNNNNNNNNNN`-..__..-'NNNNNNNNNNNNNNNNNNNNNNNNN
  ,-.    ,-.  ,-. ,----. ,----.,-. ,----.   ,-. 
  |  `.  \  `.|  \\  .--`\ \"L \\ \\ .-._\  |  `. o!0
  | |. `. \ \ ` L \\  __\ \ .  < \ \\ \  __ | |. `.
  | .--. `.\ \`-'\ \\ `---.\ \L `.\ \\ `-` \| .--. `. 
  `-'   `--``'    `-'`----' `-'`-' `' `----'`-'   `--'
   4 45
    ''')

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^dashboard$', views.dashboard),
    url(r'^postMessage$', views.postMessage),
    url(r'^postComment$', views.postComment)
]