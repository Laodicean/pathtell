from django.db import models

# Create your models here.
class Alert(models.Model):
    event = models.ForeignKey('feed.Event')
    condition = models.CharField(max_length=30)

class Event(models.Model):
    result = models.BooleanField()
    condition = models.CharField(max_length=30)
    timestamp = models.CharField(max_length=30)
    event_graph = models.CharField(max_length=100000)

