from django.db import models

class CustomModelName(models.Model):
     username = models.CharField(max_length=6)
     pass1 = models.CharField( max_length=8)
     name = models.CharField(max_length=50)

class add(models.Model):

     bookname = models.CharField(max_length=20)
     authorname = models.CharField(max_length=20)
     publishdate = models.CharField(max_length=20)

class abc(models.Model):
     a = models.CharField(max_length=12)
     b = models.CharField(max_length=22)

class admininfo(models.Model):
     username = models.CharField(max_length=10)
     firstname = models.CharField(max_length=20)
     lastname = models.CharField(max_length=20)
     email = models.CharField(max_length=50)
     password = models.CharField(max_length=20)


# Create your models here.
