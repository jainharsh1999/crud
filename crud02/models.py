from django.db import models

# Create your models here.

class customer(models.Model):
  name = models.CharField(max_length=100, null=True, blank=False)
  Email = models.CharField(max_length=100, null=True, blank=False)
  password = models.CharField(max_length=255, null=True, blank=False)
  city = models.CharField(max_length=100, null=True, blank=False)
  address = models.CharField(max_length=250, null=True, blank=False)
  pincode = models.IntegerField(null=True, blank=False)
  
class login(models.Model):
    email = models.CharField(max_length=100, null=True, blank=False)
    password = models.CharField(max_length=100, null=True, blank=False)  
    
    def _str_(self) :
        return self.email
    
class Task(models.Model):
  title = models.CharField(max_length=200)
  completed = models.BooleanField(default=False, blank=True, null=True)
      
  def __str__(self):
    return self.title    
    
class vender(models.Model):
  name = models.CharField(max_length=100, null=True, blank=False)
  Email = models.CharField(max_length=100, null=True, blank=False)
  password = models.CharField(max_length=255, null=True, blank=False)
  city = models.CharField(max_length=100, null=True, blank=False)
  address = models.CharField(max_length=250, null=True, blank=False)
  pincode = models.IntegerField(null=True, blank=False) 