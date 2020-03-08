from django.shortcuts import render, redirect, get_object_or_404
from .models import Device
import requests
import urllib3
import json

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

def add_ip(request):
    if request.method == "POST":
        
        interface = request.POST['interface']
        new_ip_addr = request.POST['ip_address']
        new_subnetmask = request.POST['subnetmask']

        selected_device_id = request.POST.getlist('device')
        for x in selected_device_id:    
            dev = get_object_or_404(Device, pk=x)
            def get_token():
                url = 'https://%s:55443/api/v1/auth/token-services' % dev.ip_address
                auth = (dev.username, dev.password) 
                headers = {'Content-Type':'application/json'}
                response = requests.post(url, auth=auth, headers=headers, verify=False)
                json_data = json.loads(response.text)
                token = json_data['token-id']
                return token

            def put_interface(token, interface):
                url = 'https://%s:55443/api/v1/interfaces/%s' % (dev.ip_address, interface)
                headers={ 'Content-Type': 'application/json', 'X-auth-token': token}

                payload = {
                    'type':'ethernet',
                    'if-name':interface,
                    'ip-address': new_ip_addr,
                    'subnet-mask': new_subnetmask,
                    'description': 'Configured via AUTONETAPI'
                    }

                response = requests.put(url, headers=headers, json=payload, verify=False)
                print('The router responds with status code: %s ' % response.status_code)

            # Disable unverified HTTPS request warnings.
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

            # Get token.
            token = get_token()

            # GET interface information.
            put_interface(token, interface)

        return redirect('home')
    else:
        all_devices = Device.objects.all()
        context = {
            'all_devices' : all_devices,
        }
        return render(request, 'netauto/add_ip.html', context)

def static_route(request):

    return render(request, 'netauto/static_route.html')


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