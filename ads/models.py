from django.db import models

class Ads(models.Model):
    name = models.CharField(max_length=250)
    author = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    is_published = models.BooleanField()

class Categories(models.Model):
    name = models.CharField(max_length=15)