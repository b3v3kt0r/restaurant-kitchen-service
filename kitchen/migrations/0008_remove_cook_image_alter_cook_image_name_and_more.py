# Generated by Django 4.2.14 on 2024-07-24 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("kitchen", "0007_alter_cook_image_alter_cook_image_name"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="cook",
            name="image",
        ),
        migrations.AlterField(
            model_name="cook",
            name="image_name",
            field=models.ImageField(blank=True, null=True, upload_to="media/"),
        ),
        migrations.AlterField(
            model_name="dish",
            name="image_name",
            field=models.ImageField(blank=True, null=True, upload_to="media/"),
        ),
    ]
