# Generated by Django 5.1 on 2024-10-01 00:36

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("FoodFinder", "0004_rename_favoriatecuisine_profile_favoritecuisine_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="favoriteCuisine",
            field=models.CharField(
                choices=[
                    ("Italian", "Italian"),
                    ("Chinese", "Chinese"),
                    ("Thai", "Thai"),
                    ("Indian", "Indian"),
                    ("Mexican", "Mexican"),
                    ("American", "American"),
                    ("Greek", "Greek"),
                    ("Korean", "Korean"),
                    ("Japanese", "Japanese"),
                    ("Vietnamese", "Vietnamese"),
                ],
                default="American",
                max_length=20,
            ),
        ),
    ]