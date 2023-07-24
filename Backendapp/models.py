from django.db import models

# Create your models here.
from django.db import models


class Categorydb(models.Model):
    Name = models.CharField(max_length=20, null=True, blank=True)
    Desc = models.CharField(max_length=30, null=True, blank=True)


class Productdb(models.Model):
    Category = models.CharField(max_length=20, null=True, blank=True)
    Product = models.CharField(max_length=30, null=True, blank=True)
    Price = models.IntegerField(null=True, blank=True)
    Description = models.CharField(max_length=30, null=True, blank=True)
    Image = models.ImageField(upload_to="profile", null=True, blank=True)
