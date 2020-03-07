from django.shortcuts import render
from .models import Device

# Create your views here.

def home(request):
    total_devices = Device.objects.all()
    
    context = {
        'total_devices' : len(total_devices),
    }

    return render(request, 'netauto/home.html', context)

def devices(request):
    all_devices = Device.objects.all()

    context = {
        'all_devices' : all_devices,
    }
    return render(request, 'netauto/devices.html', context)

def configure(request):
    all_devices = Device.objects.all()

    context = {
        'all_devices' : all_devices,
        'mode' : "Configure",
    }
    return render(request, 'netauto/configure.html', context)

def show_config(request):
    if request.method == "POST":
        context = {
            'result' : "halo gan ini adalah contoh hasil dari konfigurasi perangkat router",  
        }
        return render(request, 'netauto/result.html', context)
    else:
        all_devices = Device.objects.all()
        context = {
            'all_devices' : all_devices,
            'mode' : "Show Configuration Result",
        }
        return render(request, 'netauto/configure.html', context)

def log(request):
    return render(request, 'netauto/log.html')