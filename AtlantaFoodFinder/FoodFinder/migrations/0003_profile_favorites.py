# Generated by Django 5.1.1 on 2024-09-26 21:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("FoodFinder", "0002_profile_delete_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="favorites",
            field=models.CharField(max_length=280, null=True),
        ),
    ]
