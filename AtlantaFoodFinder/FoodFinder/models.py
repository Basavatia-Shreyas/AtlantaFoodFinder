from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    class Cuisine(models.TextChoices):
        Italian = "Italian"
        Chinese = "Chinese"
        Thai = "Thai"
        Indian = "Indian"
        Mexican = "Mexican"
        American = "American"
        Greek = "Greek"
        Korean = "Korean"
        Japanese = "Japanese"
        Vietnamese = "Vietnamese"

    favoriteCuisine = models.CharField(
        choices=Cuisine.choices,
        default=Cuisine.American,
        max_length=20,
    )

    favorites = models.CharField(max_length=280, null=True)

    def __str__(self):
        return str(self.user)