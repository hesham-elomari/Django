import datetime
from django.db import models
from django.utils import timezone
from django import forms
from django.contrib.auth.models import User



class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/%Y/%m/%d/')


class User1(User):
    company_name = models.CharField(max_length=200)
    Job = models.CharField(max_length=200)
    def __str__(self):
        return self.company_name
