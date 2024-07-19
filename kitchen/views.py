from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import generic

from kitchen.models import DishType, Dish, Cook


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


class DishTypeListView(generic.ListView):
    model = DishType
    template_name = "kitchen/dish_type_list.html"
    context_object_name = "dish_type_list"


class DishListView(generic.ListView):
    model = Dish
    template_name = "kitchen/dish_list.html"


class CookListView(generic.ListView):
    model = Cook
    template_name = "kitchen/cook_list.html"