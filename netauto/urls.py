from django.urls import path
from autonetapi import settings
from . import views
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('', views.home, name='home'),
    path('devices/', views.devices, name='devices'),
    path('add_ip/', views.add_ip, name='add_ip'),
    path('result/', views.show_config, name='result'),
    path('log/', views.log, name='log'),
    path('static_route/', views.static_route, name='static'),
    path('ospf/', views.ospf, name='ospf'),
    path('bgp/', views.bgp, name='bgp'),
    path('syslog/', views.syslog, name='syslog'),
    path('custom/', views.custom, name='custom'),
    path('detectors/', views.detectors, name='detectors'),
    path('login/', auth_views.LoginView.as_view(template_name="registration/login.html", redirect_authenticated_user=True), name='login'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)