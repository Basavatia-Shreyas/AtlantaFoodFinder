from django.db import models

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    cuisine_type = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    rating = models.FloatField()
    place_id = models.CharField(max_length=255)