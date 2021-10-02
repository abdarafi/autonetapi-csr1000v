from django.apps import AppConfig

from autonetapi import settings


class NetautoConfig(AppConfig):
    name = 'netauto'

    def ready(self):
        import netauto.signals
        from . import scheduler
        if settings.SCHEDULER_AUTOSTART:
            scheduler.start()
