from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .models import Device, Log
import requests
import urllib3
import json
from datetime import datetime

# Create your views here.

def home(request):
    total_devices = Device.objects.all()
    last_event = Log.objects.all().order_by('-id')[:10]
    context = {
        'total_devices' : len(total_devices),
        'last_event': last_event,
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
            try:
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
                    if response.status_code >= 400:
                        message = json.loads(response.text)['error-message']
                    else:
                        message = 'Success'
                    return message

                # Disable unverified HTTPS request warnings.
                urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

                # Get token.
                token = get_token()

                # Put new interface.
                put_interface(token, interface)
                if put_interface(token,interface) == "Success":
                    log = Log(target=dev.ip_address, action="Modify IP Address", status="Successful", time= datetime.now(), messages='No Error')
                    log.save()
                else:
                    log = Log(target=dev.ip_address, action="Modify IP Address", status="Error", time= datetime.now(), messages=put_interface(token,interface))
                    log.save()
            except Exception as e:
                log = Log(target=dev.ip_address, action="Modify IP Address", status="Error", time= datetime.now(), messages=e)
                log.save()
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
            try:
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
                    if response.status_code >= 400:
                        message = json.loads(response.text)['error-message']
                    else:
                        message = 'Success'
                    return message

                # Disable unverified HTTPS request warnings.
                urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

                # Get token.
                token = get_token()

                # Post static route.
                hasil = post_static_route(token, outinterface)

                if hasil == "Success":
                    log = Log(target=dev.ip_address, action="Add Static Route", status="Successful", time= datetime.now(), messages='No Error')
                    log.save()
                else:
                    log = Log(target=dev.ip_address, action="Add Static Route", status="Error", time= datetime.now(), messages=post_static_route(token,outinterface))
                    log.save()
            except Exception as e:
                log = Log(target=dev.ip_address, action="Add Static Route", status="Error", time= datetime.now(), messages=e)
                log.save()
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
            try:
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
                def post_ospf(token):
                    url = 'https://%s:55443/api/v1/routing-svc/ospf/%s/networks' % (dev.ip_address, ospf_process_id)
                    headers = {'Content-Type':'application/json','Accept':'application/json','X-auth-token': token}
                    payload = {
                        "network" : network,
                        "area" : area
                    }
                    response = requests.post(url, headers=headers, json=payload, verify=False)
                    if response.status_code >= 400:
                        message = json.loads(response.text)['error-message']
                    else:
                        message = 'Success'
                    return message

                # Disable unverified HTTPS request warnings.
                urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

                # Get token.
                token = get_token()

                # Create OSPF Process ID
                create_ospf(token)

                # Post OSPF.
                hasil = post_ospf(token)
                if hasil == "Success":
                    log = Log(target=dev.ip_address, action="Add OSPF Route", status="Successful", time= datetime.now(), messages='No Error')
                    log.save()
                else:
                    log = Log(target=dev.ip_address, action="Add OSPF Route", status="Error", time= datetime.now(), messages=post_ospf(token))
                    log.save()
            except Exception as e:
                log = Log(target=dev.ip_address, action="Add OSPF Route", status="Error", time= datetime.now(), messages=e)
                log.save()

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
            try:
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
                def post_bgp(token):
                    url = 'https://%s:55443/api/v1/routing-svc/bgp/%s/networks' % (dev.ip_address, bgp_instance_id)
                    headers = {'Content-Type':'application/json','Accept':'application/json','X-auth-token': token}
                    payload = {
                        "network": network
                    }
                    response = requests.post(url, headers=headers, json=payload, verify=False)
                    if response.status_code >= 400:
                        message = json.loads(response.text)['error-message']
                    else:
                        message = 'Success'
                    return message
                
                # Disable unverified HTTPS request warnings.
                urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

                # Get token.
                token = get_token()

                # Create BGP ASN
                create_bgp(token)

                # Post BGP.
                hasil = post_bgp(token)
                if hasil == "Success":
                    log = Log(target=dev.ip_address, action="Add BGP Route", status="Successful", time= datetime.now(), messages='No Error')
                    log.save()
                else:
                    log = Log(target=dev.ip_address, action="Add BGP Route", status="Error", time= datetime.now(), messages=post_bgp(token))
                    log.save()
            except Exception as e:
                log = Log(target=dev.ip_address, action="Add BGP Route", status="Error", time= datetime.now(), messages=e)
                log.save()

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
        try:
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
                if response.status_code >= 400:
                    return (json_data['detail'], 'gabisa')
                else:
                    return (json_data['results'], 'bisa')

            # Disable unverified HTTPS request warnings.
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

            # Get token.
            token = get_token()

            # Put the CLI Command
            send_cli(token)
            if send_cli(token)[1] == "bisa":
                log = Log(target=dev.ip_address, action="Validate Configuration", status="Successful", time= datetime.now(), messages="No Error")
                log.save()
            else:
                log = Log(target=dev.ip_address, action="Validate Configuration", status="Error", time= datetime.now(), messages="Invalid Cisco Command")
                log.save()
        except Exception as e:
            log = Log(target=dev.ip_address, action="Validate Configuration", status="Error", time= datetime.now(), messages=e)
            log.save()
        context = {
            'head' : head,
            'status' : send_cli(token)[0],
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

def syslog(request):
    if request.method == "POST":
        selected_device_id = request.POST['router']
        dev = get_object_or_404(Device, pk=selected_device_id)
        try:
            def get_token():
                url = 'https://%s:55443/api/v1/auth/token-services' % dev.ip_address
                auth = (dev.username, dev.password) 
                headers = {'Content-Type':'application/json'}
                response = requests.post(url, auth=auth, headers=headers, verify=False)
                json_data = json.loads(response.text)
                token = json_data['token-id']
                return token
            def get_syslog(token):
                url = 'https://%s:55443/api/v1/global/syslog' % dev.ip_address
                headers = {'Accept':'application/json', 'X-auth-token':token} 
                response = requests.get(url, headers=headers, verify=False)
                json_data = json.loads(response.text)
                syslog = json_data['messages']
                return syslog
            # Disable unverified HTTPS request warnings.
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

            # Get token.
            token = get_token()

            get_syslog(token)
            log = Log(target=dev.ip_address, action="Export Syslog", status="Successful", time= datetime.now(), messages="No Error")
            log.save()
        except Exception as e:
            log = Log(target=dev.ip_address, action="Export Syslog", status="Error", time= datetime.now(), messages=e)
            log.save()
        
        filename = "syslog.txt"
        content = get_syslog(token)
        response = HttpResponse(content, content_type='text/plain')
        response['Content-Disposition'] = 'attachment; filename={0}'.format(filename)
        return response
    else:
        all_devices = Device.objects.all()
        context = {
            'all_devices': all_devices,
        }
        return render(request, 'netauto/syslog.html', context)

def log(request):
    logs = Log.objects.all().order_by('-id')
    context = {
        'logs': logs
    }
    return render(request, 'netauto/log.html', context)