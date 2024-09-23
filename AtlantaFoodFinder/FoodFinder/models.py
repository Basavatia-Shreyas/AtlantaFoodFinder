from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
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
        max_length=15,
    )

    def __str__(self):
        return str(self.user)

