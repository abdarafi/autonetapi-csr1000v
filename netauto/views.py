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

            # Put new interface.
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
        dest_network = request.POST['dest']+ '/' + request.POST['prefix']
        next_hop =  request.POST['next_hop'] 
        outinterface = request.POST['outinterface']
        admin_distance = request.POST['admin_distance']

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
            def post_static_route(token, outinterface):
                url = 'https://%s:55443/api/v1/routing-svc/static-routes' % dev.ip_address
                headers = {'Content-Type':'application/json','Accept':'application/json','X-auth-token': token}
                payload = {
                    "destination-network": dest_network,
                    "next-hop-router": next_hop,
                    "outgoing-interface": outinterface,
                    "admin-distance": int(admin_distance)
                }
                
                response = requests.post(url, headers=headers, json=payload, verify=False)
                print('Status code for static route: %s' %response.status_code )

            # Disable unverified HTTPS request warnings.
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

            # Get token.
            token = get_token()

            # Post static route.
            post_static_route(token, outinterface)
        return redirect('home')


    else:
        all_devices = Device.objects.all()
        context = {
            'all_devices' : all_devices,
        }
        return render(request, 'netauto/static_route.html', context)

def ospf(request):
    if request.method == "POST":
        ospf_process_id = request.POST['ospf_process_id']
        network = request.POST['network'] + '/' + request.POST['prefix']
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
                print('Status code OSPF Process create : %s' % response.status_code )
            def post_ospf(token):
                url = 'https://%s:55443/api/v1/routing-svc/ospf/%s/networks' % (dev.ip_address, ospf_process_id)
                headers = {'Content-Type':'application/json','Accept':'application/json','X-auth-token': token}
                payload = {
                    "network" : network,
                    "area" : area
                }
                response = requests.post(url, headers=headers, json=payload, verify=False)
                print('Status code OSPF Create : %s' % response.status_code )

            # Disable unverified HTTPS request warnings.
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

            # Get token.
            token = get_token()

            # Create OSPF Process ID
            create_ospf(token)

            # Post OSPF.
            post_ospf(token)

        return redirect('home')

    else:
        all_devices = Device.objects.all()
        context = {
            'all_devices' : all_devices,
        }
        return render(request, 'netauto/ospf.html', context)

def bgp(request):
    if request.method == "POST":
        bgp_instance_id = request.POST['bgp_instance_id']
        network = request.POST['network'] + '/32'
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
                print('Status code BGP Process create : %s' % response.status_code )
            def post_bgp(token):
                url = 'https://%s:55443/api/v1/routing-svc/bgp/%s/networks' % (dev.ip_address, bgp_instance_id)
                headers = {'Content-Type':'application/json','Accept':'application/json','X-auth-token': token}
                payload = {
                    "network": network
                }
                response = requests.post(url, headers=headers, json=payload, verify=False)
                print('Status code BGP Create : %s' % response.status_code )
            
            # Disable unverified HTTPS request warnings.
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

            # Get token.
            token = get_token()

            # Create BGP ASN
            create_bgp(token)

            # Post BGP.
            post_bgp(token)

        return redirect('home')
    else:
        all_devices = Device.objects.all()
        context = {
            'all_devices' : all_devices,
        }
        return render(request, 'netauto/bgp.html', context)


def show_config(request):
    if request.method == "POST":
        head = 'The Configuration Result'
        cisco_command = request.POST['cisco_command']
        selected_device_id = request.POST['router']
        dev = get_object_or_404(Device, pk=selected_device_id)
        def get_token():
            url = 'https://%s:55443/api/v1/auth/token-services' % dev.ip_address
            auth = (dev.username, dev.password) 
            headers = {'Content-Type':'application/json'}
            response = requests.post(url, auth=auth, headers=headers, verify=False)
            json_data = json.loads(response.text)
            token = json_data['token-id']
            return token
        def send_cli(token):
            url = 'https://%s:55443/api/v1/global/cli' % dev.ip_address
            headers = {'Content-Type':'application/json','X-auth-token': token}
            payload = {
                "exec" : cisco_command
            }
            response = requests.put(url, headers=headers, json=payload, verify=False)
            json_data = json.loads(response.text)
            #print(json.dumps(json_data, indent=4, separators=(',', ': ')))
            return "Hasil response : \n " + json_data['results']

        # Disable unverified HTTPS request warnings.
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

        # Get token.
        token = get_token()

        # Put the CLI Command
        send_cli(token)
        context = {
            'head' : head,
            'status' : send_cli(token),
        }
        return render(request, 'netauto/result.html', context)
    else:
        head = 'Validate your configuration'
        all_devices = Device.objects.all()
        context = {
            'all_devices' : all_devices,
            'head' : head,
        }
        return render(request, 'netauto/validate.html', context)

def log(request):
    return render(request, 'netauto/log.html')