from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MinValueValidator

from restaurant_kitchen_service import settings


class DishType(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    dish_type = models.ForeignKey(
        DishType, on_delete=models.CASCADE, related_name="dishes"
    )
    cooks = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="dishes")
    image_name = models.ImageField(null=True, blank=True)

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "dishes"

    def __str__(self):
        return f"{self.name} (price: {self.price}, dish type: {self.dish_type.name})"


class Cook(AbstractUser):
    years_of_experience = models.IntegerField(
        default=0, validators=[MinValueValidator(0)]
    )
    image_name = models.ImageField(null=True, blank=True)

    class Meta:
        ordering = ["username"]

    def __str__(self):
        return f"{self.username}: {self.first_name} {self.last_name}"
