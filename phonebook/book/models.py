from django.db import models


class PhoneRecord(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
