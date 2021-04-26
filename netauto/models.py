import json
from datetime import datetime

import requests
import urllib3
from django.db import models

from netauto.utils import NetflowSlugs


class Device(models.Model):
    ip_address = models.CharField(max_length=200)
    hostname = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

    def get_token(self) -> str:
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        return json.loads(requests.post(
            url="https://{}:55443/api/v1/auth/token-services".format(self.ip_address),
            auth=(self.username, self.password),
            headers={"Content-Type": "application/json"},
            verify=False
        ).text)['token-id']

    def set_config(self, token: str, config: str) -> bool:
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        return requests.put(
            url="https://{}:55443/api/v1/global/cli".format(self.ip_address),
            headers={'Content-Type': 'application/json', 'X-auth-token': token},
            json={'config': config},
            verify=False).status_code <= 400

    def fire_exec(self, token: str, command: str) -> bool:
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        return requests.put(
            url="https://{}:55443/api/v1/global/cli".format(self.ip_address),
            headers={'Content-Type': 'application/json', 'X-auth-token': token},
            json={'exec': command},
            verify=False).status_code <= 400

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
    def device_slug(self) -> str:
        return "{}{}".format(self.device.hostname, self.device_interface)

    @property
    def netflow_slugs(self) -> NetflowSlugs:
        return NetflowSlugs(
            "{}Monitor".format(self.device_slug),
            "{}Record".format(self.device_slug),
            "{}Exporter".format(self.device_slug)
        )

    def add_netflow_config(self) -> bool:
        slugs = self.netflow_slugs
        token = self.device.get_token()
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
                        'do copy run start'.format(slugs.record_slug,
                                                   slugs.exporter_slug,
                                                   self.filebeat_host,
                                                   self.device_interface,
                                                   self.filebeat_port,
                                                   slugs.monitor_slug,
                                                   slugs.record_slug,
                                                   slugs.exporter_slug,
                                                   self.device_interface,
                                                   slugs.monitor_slug)
        return self.device.set_config(token, config_string)

    def remove_netflow_config(self) -> bool:
        config_string = 'int {}\n' \
                        'no ip flow monitor {} input' \
                        'exit' \
                        'no flow monitor {}\n' \
                        'no flow record {}\n' \
                        'no flow exporter {}\n' \
                        'do copy run start'.format(self.device_interface,
                                                   self.netflow_slugs.monitor_slug,
                                                   *self.netflow_slugs)
        return self.device.set_config(self.device.get_token(), config_string)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None, *args, **kwargs):
        if update_fields is not None:
            try:
                if self.remove_netflow_config():
                    log = Log(target=self.device.ip_address, action="[Nescient] Remove Netflow Config",
                              status="Successful",
                              time=datetime.now(), user='Anonymous', messages="No Error")
                    log.save()
                else:
                    log = Log(target=self.device.ip_address, action="[Nescient] Remove Netflow Config",
                              status="Error",
                              time=datetime.now(), user='Anonymous', messages="Invalid Script")
                    log.save()
            except Exception as e:
                log = Log(target=self.device.ip_address, action="[Nescient] Remove Netflow Config", status="Exception",
                          time=datetime.now(),
                          user='Anonymous', messages=e.__str__()[0:255])
                log.save()
        try:
            if self.add_netflow_config():
                super(Detector, self).save(*args, **kwargs)
                log = Log(target=self.device.ip_address, action="[Nescient] Add Netflow Config", status="Successful",
                          time=datetime.now(), user='Anonymous', messages="No Error")
                log.save()
            else:
                log = Log(target=self.device.ip_address, action="[Nescient] Add Netflow Config", status="Error",
                          time=datetime.now(),
                          user='Anonymous', messages="Invalid Script")
                log.save()

        except Exception as e:
            log = Log(target=self.device.ip_address, action="[Nescient] Add Netflow Config", status="Exception",
                      time=datetime.now(),
                      user='Anonymous', messages=e.__str__()[0:255])
            log.save()

    def delete(self, using=None, keep_parents=False, *args, **kwargs):
        try:
            if self.remove_netflow_config():
                log = Log(target=self.device.ip_address, action="[Nescient] Remove Netflow Config",
                          status="Successful",
                          time=datetime.now(), user='Anonymous', messages="No Error")
                log.save()
            else:
                log = Log(target=self.device.ip_address, action="[Nescient] Remove Netflow Config",
                          status="Error",
                          time=datetime.now(), user='Anonymous', messages="Invalid Script")
                log.save()
        except Exception as e:
            log = Log(target=self.device.ip_address, action="[Nescient] Remove Netflow Config", status="Exception",
                      time=datetime.now(),
                      user='Anonymous', messages=e.__str__()[0:255])
            log.save()
        super(Detector, self).delete(*args, **kwargs)

    def __str__(self):
        return "{} {} {} {}".format(
            self.device.hostname, self.device_interface, self.window_size, self.sampling_interval)
