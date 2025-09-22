from django.db import models

# Create your models here.
from django.db import models


class Doctor(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    pwd = models.CharField(max_length=100)
    qualification = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=1000)


class Patient(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    pwd = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    age = models.CharField(max_length=20)
    healthissue = models.CharField(max_length=100)
    number = models.CharField(max_length=100)
    address = models.CharField(max_length=1000)
