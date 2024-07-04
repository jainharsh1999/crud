from django.db import models

# Create your models here.

class customer(models.Model):
  name = models.CharField(max_length=100, null=True, blank=False)
  Email = models.CharField(max_length=100, null=True, blank=False)
  password = models.CharField(max_length=255, null=True, blank=False)
  city = models.CharField(max_length=100, null=True, blank=False)
  address = models.CharField(max_length=250, null=True, blank=False)
  pincode = models.IntegerField(null=True, blank=False)
    
class Employee(models.Model):
    emp_name = models.CharField(max_length=200)
    emp_email = models.EmailField()
    emp_contact = models.CharField(max_length=20)
    emp_role = models.CharField(max_length=200)
    emp_salary = models.IntegerField()
    id = models.AutoField(unique=True, primary_key=True)

    def __str__(self):
        return self.emp_name   
    
class vender(models.Model):
  name = models.CharField(max_length=100, null=True, blank=False)
  Email = models.CharField(max_length=100, null=True, blank=False)
  password = models.CharField(max_length=255, null=True, blank=False)
  city = models.CharField(max_length=100, null=True, blank=False)
  address = models.CharField(max_length=250, null=True, blank=False)
  pincode = models.IntegerField(null=True, blank=False) 