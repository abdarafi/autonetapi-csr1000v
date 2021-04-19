from apscheduler.triggers.cron import CronTrigger
from django.db.models.signals import post_save, pre_save, post_delete, pre_delete
from django.dispatch import receiver

from netauto.elasticclient import get_netflow_resampled
from netauto.models import Detector
from netauto.nescient import core
from netauto.scheduler import scheduler


def le_job(detector_instance: Detector):
    core(get_netflow_resampled(
        "now",
        detector_instance.sampling_interval,
        detector_instance.elastic_host,
        detector_instance.elastic_index
    ), detector_instance)


@receiver(pre_save, sender=Detector)
def upsert_jobs_on_save(sender, instance: Detector, **kwargs):
    scheduler.add_job(
        func=le_job,
        trigger=CronTrigger(second=instance.sampling_interval),
        args=[instance],
        id=instance.device_slug,
        max_instances=1,
        replace_existing=True
    )


@receiver(pre_delete, sender=Detector)
def delete_jobs_on_delete(sender, instance: Detector, **kwargs):
    scheduler.remove_job(instance.device_slug)
