from ninja import NinjaAPI, Query
from typing import List, Optional
from .models import Job
from .tasks import run_dummy_job
from django.shortcuts import get_object_or_404
from django.utils import timezone

from schedular.schema import JobIn, JobOut

api = NinjaAPI()

@api.get("/jobs", response=List[JobOut])
def list_jobs(request, limit: int = Query(10, ge=1, le=100), offset: int = Query(0, ge=0)):
    """
    List jobs with pagination.

    Args:
        request: HttpRequest object.
        limit (int): Maximum number of jobs to return (default 10, max 100).
        offset (int): Number of jobs to skip before returning results.

    Returns:
        List[JobOut]: A paginated list of jobs.
    """
    jobs = Job.objects.all().order_by("id")[offset:offset + limit]
    return list(jobs)

@api.get("/jobs/{job_id}", response=JobOut)
def get_job(request, job_id: int):
    """
    Retrieve a single job by its ID.

    Args:
        request: HttpRequest object.
        job_id (int): Primary key of the target job.

    Returns:
        JobOut: The requested job object.
    """
    job = get_object_or_404(Job, id=job_id)
    return job

@api.post("/jobs", response=JobOut)
def create_job(request, data: JobIn):
    """
    Create a new job and schedule its first run asynchronously.

    Args:
        request: HttpRequest object.
        data (JobIn): Data required to create the job.

    Returns:
        JobOut: The created job object.
    """
    job = Job.objects.create(
        name=data.name,
        interval_seconds=data.interval_seconds,
        params=data.params,
        next_run=timezone.now() + timezone.timedelta(seconds=data.interval_seconds)
    )
    # Schedule the first run asynchronously
    run_dummy_job.apply_async(args=[job.id], countdown=data.interval_seconds)
    return job
