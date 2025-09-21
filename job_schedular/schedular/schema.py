from ninja import Schema
from typing import Optional
from django.utils import timezone

class JobIn(Schema):
    name: str
    interval_seconds: Optional[int] = 3600
    params: Optional[dict] = {}

class JobOut(Schema):
    id: int
    name: str
    last_run: Optional[timezone.datetime]
    next_run: Optional[timezone.datetime]
    interval_seconds: int
    params: dict
