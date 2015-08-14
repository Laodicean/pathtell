from django.db import models
import json
import datetime

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
    timestamp = models.DateTimeField(auto_now_add=True)

    #y = [(i,x[i]) for i in range(len(x))]
    event_graph = models.TextField()
    getGraph = [(5*i+1,70 - i) for i in range(20)]

    """
    def getGraph(self, *args, **kwargs):
        x = json.loads(self.event_graph)
        #return [(5*i+1,x[i]) for i in range(len(x))]
        self.
        super(Event, self).getGraph [(i, 70 - i) for i in range(20)]


    def save(self, *args, **kwargs):
        self.beat_date = datetime.date(
                            year=self.beat_timestamp.year,
                            month=self.beat_timestamp.month,
                            day=self.beat_timestamp.day,
                        )
        super(HeartBeatData, self).save(*args, **kwargs)
        """

    datestamp = models.DateField() # Makes group_by queries on days easier

    def save(self, *args, **kwargs):
        self.result = False
        self.timestamp = datetime.datetime.now()
        self.datestamp = datetime.date(
                            year=self.timestamp.year,
                            month=self.timestamp.month,
                            day=self.timestamp.day,
                        )
        super(Event, self).save(*args, **kwargs)
