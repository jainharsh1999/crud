from django.db import models

# Create your models here.

class customer(models.Model):
  name = models.CharField(max_length=100, null=True, blank=False)
  Email = models.CharField(max_length=100, null=True, blank=False)
  password = models.CharField(max_length=255, null=True, blank=False)
  city = models.CharField(max_length=100, null=True, blank=False)
  address = models.CharField(max_length=250, null=True, blank=False)
  pincode = models.IntegerField(max_length=7, null=True, blank=False)
  
class vender(models.Model):
  name = models.CharField(max_length=100, null=True, blank=False)
  Email = models.CharField(max_length=100, null=True, blank=False)
  password = models.CharField(max_length=255, null=True, blank=False)
  city = models.CharField(max_length=100, null=True, blank=False)
  address = models.CharField(max_length=250, null=True, blank=False)
  pincode = models.IntegerField(max_length=7, null=True, blank=False) 