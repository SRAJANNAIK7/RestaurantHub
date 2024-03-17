from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
class Contact2(models.Model):
    name2 = models.CharField(max_length=122)
    email2 = models.CharField(max_length=122)
    phone2 = models.CharField(max_length=12)
class Res(models.Model):
    Restaurant=models.CharField(max_length=122)

   
