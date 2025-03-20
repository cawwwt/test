from django.db import models

# Create your models here.

class Doctor(models.Model):
    doctor = models.CharField(max_length = 30)
    field = models.CharField(max_length = 30)

class Patient(models.Model):
    name = models.CharField(max_length= 25)
    age = models.BigIntegerField
    illness = models.CharField(max_length=100)
    doctor = models.ForeignKey(Doctor, on_delete =models.CASCADE)
