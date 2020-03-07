from django.contrib import admin
from .models import Device, Log

# Register your models here.

admin.site.register(Device)
admin.site.register(Log)