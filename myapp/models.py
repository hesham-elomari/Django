from django.db import models
from django.contrib.auth.models import AbstractUser


class User1(AbstractUser):
    company_name = models.CharField(max_length=200)
    job = models.CharField(max_length=200)

    def __str__(self):
        return self.company_name

class Document(models.Model):
    user1 = models.ForeignKey(User1, on_delete=models.CASCADE, null=True)
    description = models.CharField(max_length=255, blank=False)
    document = models.FileField(upload_to='documents/%Y/%m/%d/')

    def __str__(self):
        return self.description



