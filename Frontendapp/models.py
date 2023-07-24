from django.db import models


class SignUp(models.Model):
    FirstName = models.CharField(max_length=20, null=True, blank=True)
    LastName = models.CharField(max_length=20, null=True, blank=True)
    Email = models.EmailField(max_length=20, null=True, blank=True)
    MobileNumber = models.IntegerField(null=True, blank=True)
    Password = models.CharField(max_length=20, null=True, blank=True)


class Cartdb(models.Model):
    Name = models.CharField(max_length=20, null=True, blank=True)
    Price = models.IntegerField(null=True, blank=True)
    Quantity = models.IntegerField(null=True, blank=True)
