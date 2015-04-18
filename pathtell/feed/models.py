from django.db import models

# Create your models here.
class Alert(models.Model):
    event = models.ForeignKey('feed.Event')
    condition = models.CharField(max_length=30)

class Event(models.Model):
    result = models.BooleanField()
    condition = models.CharField(max_length=30)
    event_graph = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

