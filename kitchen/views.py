from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


from .models import DishType, Dish, Cook


def index(request: HttpRequest) -> HttpResponse:
    num_dishes = Dish.objects.count()
    num_dish_type = DishType.objects.count()
    num_cooks = Cook.objects.count()
    context = {
        "num_dishes": num_dishes,
        "num_dish_type": num_dish_type,
        "num_cooks": num_cooks
    }
    return render(request, "kitchen/index.html", context)
