from django.db import models
from django.contrib.auth import models as auth_models
import datetime


class Person(auth_models.):
    email = models.EmailField(unique=True)
    dob = models.DateField()

    USERNAME_FIELD = 'email'

    def is_infant():
        """ An infant is a human that is less than one year of age from now
        """
        if (datetime.date.today() - self.dob) <= 365:
            return True
        return False
