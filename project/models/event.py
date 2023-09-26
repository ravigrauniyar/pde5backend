from django.db import models
from project.models.source import Source

class Event(models.Model):
    title = models.CharField(max_length=150)
    source = models.ForeignKey(Source, on_delete=models.DO_NOTHING)
    properties = models.JSONField(blank=True, null=True)
