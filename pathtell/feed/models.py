from django.db import models

# Create your models here.
class Alert(models.Model):
    person = models.ForeignKey('appauth.Person')
    event = models.ForeignKey('feed.Event')
    condition = models.CharField(max_length=30)
    timestamp = models.DateTimeField(auto_now_add=True)


class Event(models.Model):
    person = models.ForeignKey('appauth.Person')
    result = models.BooleanField()
    condition = models.CharField(max_length=30)
    event_graph = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    datestamp = models.DateField() # Makes group_by queries on days easier

    def save(self, *args, **kwargs):
        self.datestamp = datetime.date(
                            year=self.timestamp.year,
                            month=self.timestamp.month,
                            day=self.timestamp.day,
                        )
        super(Event, self).save(*args, **kwargs)
