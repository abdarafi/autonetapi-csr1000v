import json
from datetime import datetime

import requests
import urllib3
from django.db import models

# Create your models here.
from django.db.models import Q


class Device(models.Model):
    ip_address = models.CharField(max_length=200)
    hostname = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

    def __str__(self):
        return "{}, {}".format(self.hostname, self.ip_address)


class Log(models.Model):
    target = models.CharField(max_length=200)
    action = models.CharField(max_length=200)
    status = models.CharField(max_length=200)
    messages = models.CharField(max_length=255, blank=True)
    time = models.DateTimeField(null=True)
    user = models.CharField(max_length=200, default='Anonymous')

    def __str__(self):
        return "{} - {} - {}".format(self.target, self.action, self.status)


class Detector(models.Model):
    device = models.OneToOneField(Device, on_delete=models.CASCADE, primary_key=True)
    device_interface = models.CharField(max_length=200)
    window_size = models.IntegerField()
    sampling_interval = models.IntegerField()
    elastic_host = models.GenericIPAddressField()
    elastic_index = models.CharField(max_length=255)
    filebeat_host = models.GenericIPAddressField()
    filebeat_port = models.BigIntegerField()

    @property
    def device_slug(self):
        return "{}{}".format(self.device.hostname, self.device_interface)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None, *args, **kwargs):
        try:
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
            device_token = json.loads(requests.post(
                url="https://{}:55443/api/v1/auth/token/token-services".format(self.device.ip_address),
                auth=(self.device.username, self.device.password),
                headers={"Content-Type": "application/json"},
                verify=False
            ).text)['token_id']
            record_slug = "{}{}Record".format(self.device.hostname, self.device_interface)
            monitor_slug = "{}{}Monitor".format(self.device.hostname, self.device_interface)
            export_slug = "{}{}Export".format(self.device.hostname, self.device_interface)
            config_string = 'flow record {}\n' \
                            'match ipv4 source address\n' \
                            'match ipv4 destination address\n' \
                            'match ipv4 protocol\n' \
                            'match transport source-port\n' \
                            'match transport destination-port\n' \
                            'match ipv4 tos\n' \
                            'match interface input\n' \
                            'collect interface output\n' \
                            'collect counter bytes\n' \
                            'collect counter packets\n' \
                            'collect timestamp sys-uptime first\n' \
                            'collect timestamp sys-uptime last\n' \
                            'collect application name\n' \
                            'collect routing source as\n' \
                            'collect routing destination as\n' \
                            'flow exporter {}\n' \
                            'destination {}\n' \
                            'source {}\n' \
                            'transport udp {}\n' \
                            'export-protocol netflow-v9\n' \
                            'template data timeout 60\n' \
                            'option application-table timeout 60\n' \
                            'option application-attributes timeout 300\n' \
                            'flow monitor {}\n' \
                            'record {}\n' \
                            'exporter {}\n' \
                            'cache timeout active 60\n' \
                            'cache timeout inactive 15\n' \
                            'exit\n' \
                            'interface {}\n' \
                            'ip flow monitor {} input\n' \
                            'exit\n' \
                            'do copy run start'.format(
                record_slug,
                export_slug,
                self.filebeat_host,
                self.device_interface,
                self.filebeat_port,
                monitor_slug,
                record_slug,
                export_slug,
                self.device_interface,
                monitor_slug
            )

            if requests.put(
                    url="https://{}:55443/api/v1/global/cli".format(self.device.ip_address),
                    headers={'Content-Type': 'application/json', 'X-auth-token': device_token},
                    json={'config': config_string},
                    verify=False).status_code >= 400:
                log = Log(target=self.device.ip_address, action="Configure Netflow", status="Error",
                          time=datetime.now(),
                          user=None, messages="Invalid Script")
                log.save()
            else:
                super(Detector, self).save(*args, **kwargs)
                log = Log(target=self.device.ip_address, action="Configure Netflow", status="Successful",
                          time=datetime.now(), user=None, messages="No Error")
                log.save()

        except Exception as e:
            log = Log(target=self.device.ip_address, action="Configure Netflow", status="Error",
                      time=datetime.now(),
                      user=None, messages="Failed establishing connection to device or requirements not match")
            log.save()

    def __str__(self):
        return "{} {} {} {}".format(
            self.device.hostname, self.device_interface, self.window_size, self.sampling_interval)
