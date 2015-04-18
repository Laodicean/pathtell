from django.db import models


class HeartBeatData(models.Model):
    person = models.ForeignKey('appauth.Person')
    rate = models.IntegerField()
    frequency = models.FloatField()
    beat_timestamp = models.DateTimeField() 
    added_timestamp = models.DateTimeField(auto_now_add=True)
