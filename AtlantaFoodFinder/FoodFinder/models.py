from django.db import models

# Create your models here.
class User(models.Model):
    user_name = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    # Figure out how to store the resturant - list of char, resturaunt objects, etc?
    #favorites = models 