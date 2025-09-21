from django.db import models

class Job(models.Model):
    name = models.CharField(max_length=255)
    last_run = models.DateTimeField(null=True, blank=True)
    next_run = models.DateTimeField(null=True, blank=True)
    interval_seconds = models.PositiveIntegerField(default=3600)
    params = models.JSONField(default=dict)  # For dummy job customization
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"
