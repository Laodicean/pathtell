from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth import models as auth_models
from django.contrib.auth.models import User
import datetime


class Person(models.Model):
    user = models.OneToOneField('auth.User')
    dob = models.DateField(blank=True, null=True)

    def is_infant():
        """ An infant is a human that is less than one year of age from now
        """
        if (datetime.date.today() - self.dob) <= 365:
            return True
        return False


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Person.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)
