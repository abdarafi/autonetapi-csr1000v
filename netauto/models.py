from django.db import models

# Create your models here.

class Device(models.Model):
    ip_address = models.CharField(max_length=200)
    hostname = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    ssh_port = models.IntegerField(default=22)

    def __str__(self):
        return "{}, {}".format(self.hostname, self.ip_address)

class Log(models.Model):
    target = models.CharField(max_length=200)
    action = models.CharField(max_length=200)
    status = models.CharField(max_length=200)
    messages = models.CharField(max_length=255, blank=True)
    time = models.DateTimeField(null=True)

    def __str__(self):
        return "{} - {} - {}".format(self.target, self.action, self.status)