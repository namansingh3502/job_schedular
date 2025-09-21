from celery import shared_task
from .models import Job
from django.utils import timezone

@shared_task
def run_dummy_job(job_id):
    job = Job.objects.get(id=job_id)

    job.last_run = timezone.now()
    job.next_run = timezone.now() + timezone.timedelta(seconds=job.interval_seconds)
    job.save()

