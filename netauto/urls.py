from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('devices/', views.devices, name='devices'),
    path('add_ip/', views.add_ip, name='add_ip'),
    path('result/', views.show_config, name='result'),
    path('log/', views.log, name='log'),
    path('static_route/', views.static_route, name='static'),
    path('ospf/', views.ospf, name='ospf'),
    path('bgp/', views.bgp, name='bgp'),
]