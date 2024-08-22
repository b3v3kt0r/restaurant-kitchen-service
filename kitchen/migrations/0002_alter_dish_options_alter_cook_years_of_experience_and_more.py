# Generated by Django 5.0.7 on 2024-07-19 15:35

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("kitchen", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="dish",
            options={"ordering": ["name"], "verbose_name_plural": "dishes"},
        ),
        migrations.AlterField(
            model_name="cook",
            name="years_of_experience",
            field=models.IntegerField(
                default=0, validators=[django.core.validators.MinValueValidator(0)]
            ),
        ),
        migrations.AlterField(
            model_name="dishtype",
            name="name",
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
