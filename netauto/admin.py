from django.contrib import admin
from .models import Device, Log

admin.site.site_header = "AutonetAPI Administration"
admin.site.site_title = "AutonetAPI"
admin.site.index_title = "Site Administration"

# Register your models here.

admin.site.register(Device)
admin.site.register(Log)