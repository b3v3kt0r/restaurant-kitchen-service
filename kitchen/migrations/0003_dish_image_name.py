# Generated by Django 4.1 on 2024-07-21 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("kitchen", "0002_alter_dish_options_alter_cook_years_of_experience_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="dish",
            name="image_name",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
