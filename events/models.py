from django.db import models
from django.utils import timezone
from datetime import datetime


class Event(models.Model):
    title = models.CharField(max_length=256)
    presenter = models.CharField(max_length=256, blank=True)
    time = models.DateTimeField(default=datetime.now(tz=timezone.utc))
    location = models.CharField(max_length=256, blank=True)
    coordinator = models.CharField(max_length=256, blank=True)
    description = models.TextField(blank=True)
