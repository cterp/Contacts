from django.db import models
import datetime
from django.utils import timezone
from django import forms


# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True) # not required
    email = models.EmailField() # makes sure the email is valid. e.g. 123@abc.com

    def __str__(self):
        return self.first_name + ' ' + self.last_name + ' \n(' + self.email + ')'