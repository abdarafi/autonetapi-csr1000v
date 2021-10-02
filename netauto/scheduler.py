import logging

from apscheduler.schedulers.background import BackgroundScheduler

from autonetapi import settings

scheduler = BackgroundScheduler(settings.SCHEDULER_CONFIG)


def start():
    if settings.DEBUG:
        logging.basicConfig()
        logging.getLogger('apscheduler').setLevel(logging.DEBUG)
    scheduler.start()
