__author__ = 'tylerkrebs'

from django.db import models
from geoposition.fields import GeopositionField


class Salon(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    zipcode = models.IntegerField(max_length=10)
    phone = models.IntegerField(max_length=14)
    website = models.CharField(max_length=100)
    yelp_url = models.CharField(max_length=100)
    yelp_rating = models.CharField(max_length=10)
    geo = GeopositionField()