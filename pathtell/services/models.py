from django.db import models


class Service(models.Model):
    name = models.TextField()


"""
class Feature():
    name = models.TextField()
    sampling_rate = models.DoubleField()


class PersonFeatureData():
    user = models.ForeignKey('appauth.Person')
    service_connection = models.ForeignKey('service.PersonServiceConnection')

    datetime 
"""     

class PersonServiceConnection(models.Model):
    user = models.ForeignKey('appauth.Person')
    service = models.ForeignKey('services.Service')
    auth_token = models.TextField()
