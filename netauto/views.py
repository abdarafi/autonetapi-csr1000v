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
    if request.method == "POST":
        dest_network = request.POST['dest']
        next_hop =  request.POST['next_hop']
        outinterface = request.POST['outinterface']
        admin_distance = request.POST['admin_interface']

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
            def post_static_route(token):
                url = 'https://%s:55443/api/v1/routing-svc/static-routes' % dev.ip_address
                headers = {'Content-Type':'application/json','Accept':'application/json','X-auth-token': token}
                payload = {
                    "kind": "object#static-route",
                    "destination-network": dest_network,
                    "next-hop-router": next_hop,
                    "outgoing-interface": outinterface,
                    "admin-distance": admin_distance
                }
                response = requests.post(url, headers=headers, json=payload, verify=False)
                print('Status code : %s' %requests.status_codes )

            # Disable unverified HTTPS request warnings.
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

            # Get token.
            token = get_token()

            # GET interface information.
            put_interface(token, interface)

    else:
        all_devices = Device.objects.all()
        context = {
            'all_devices' : all_devices,
        }
        return render(request, 'netauto/static_route.html', context)

def ospf(request):
    if request.method == "POST":
        ospf_process_id = request.POST['ospf_process_id']
        network = request.POST['network']
        area = request.POST['area']
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
            def create_ospf(token):
                url = 'https://%s:55443/api/v1/routing-svc/ospf' % dev.ip_address
                headers = {'Content-Type':'application/json','Accept':'application/json','X-auth-token': token}
                payload = {
                    "routing-protocol-id": ospf_process_id
                }
                response = requests.post(url, headers=headers, json=payload, verify=False)
                print('Status code OSPF Process create : %s' %requests.status_codes )
            def post_ospf(token):
                url = 'https://%s:55443/api/v1/routing-svc/ospf/%s/networks' % (dev.ip_address, ospf_process_id)
                headers = {'Content-Type':'application/json','Accept':'application/json','X-auth-token': token}
                payload = {
                    "network" : network,
                    "area" : area
                }
                response = requests.post(url, headers=headers, json=payload, verify=False)
                print('Status code OSPF Create : %s' %requests.status_codes )
    else:
        all_devices = Device.objects.all()
        context = {
            'all_devices' : all_devices,
        }
        return render(request, 'netauto/ospf.html', context)

def bgp(request):
    if request.method == "POST":
        bgp_instance_id = request.POST['bgp_instance_id']
        bgp_asn = request.POST['bgp_asn']
        network = request.POST['network']
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
            def create_bgp(token):
                url = 'https://%s:55443//api/v1/routing-svc/bgp' % dev.ip_address
                headers = {'Content-Type':'application/json','Accept':'application/json','X-auth-token': token}
                payload = {
                    "routing-protocol-id": bgp_instance_id
                }
                response = requests.post(url, headers=headers, json=payload, verify=False)
                print('Status code BGP Process create : %s' %requests.status_codes )
            def post_bgp(token):
                url = 'https://%s:55443/api/v1/routing-svc/ospf/%s/networks' % (dev.ip_address, bgp_instance_id)
                headers = {'Content-Type':'application/json','Accept':'application/json','X-auth-token': token}
                payload = {
                    "kind": "object#bgp-network",
                    "routing-protocol-id": bgp_asn,
                    "network": network
                }
                response = requests.post(url, headers=headers, json=payload, verify=False)
                print('Status code BGP Create : %s' %requests.status_codes )
    else:
        all_devices = Device.objects.all()
        context = {
            'all_devices' : all_devices,
        }
        return render(request, 'netauto/bgp.html', context)


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