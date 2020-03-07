from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('devices/', views.devices, name='devices'),
    path('configure/', views.configure, name='configure'),
    path('result/', views.show_config, name='result'),
    path('log/', views.log, name='log'),
]