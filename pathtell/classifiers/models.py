from django.db import models
import datetime


class HeartBeatData(models.Model):
    person = models.ForeignKey('appauth.Person')
    rate = models.IntegerField()
    frequency = models.FloatField()
    beat_timestamp = models.DateTimeField() 
    beat_date = models.DateField()
    added_timestamp = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.beat_date = datetime.date(
                            year=self.beat_timestamp.year,
                            month=self.beat_timestamp.month,
                            day=self.beat_timestamp.day,
                        )
        super(HeartBeatData, self).save(*args, **kwargs)
