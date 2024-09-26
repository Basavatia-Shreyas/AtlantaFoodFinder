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

class Restaurant(models.Model):
    place_id = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    # Add other fields as needed

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'restaurant')


