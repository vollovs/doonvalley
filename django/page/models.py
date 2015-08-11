from django.db import models
from calendar import weekday

class Event(models.Model):
    event_date = models.DateField()
    weekday = models.CharField(max_length=3, blank=False, null=False)
    time_range = models.CharField(max_length=22)
    active = models.BooleanField(default=False)
