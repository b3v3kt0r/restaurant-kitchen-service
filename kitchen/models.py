from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MinValueValidator

from restaurant_kitchen_service import settings


class DishType(models.Model):
    name = models.CharField(max_length=255)


class Dish(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    dish_type = models.ForeignKey(DishType,
                                  on_delete=models.CASCADE,
                                  related_name="dishes")
    cooks = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                   related_name="dishes")


class Cook(AbstractUser):
    years_of_experience = models.IntegerField(validators=[MinValueValidator(0)])
