from django.urls import path

from kitchen.views import (
    index,
    DishTypeListView,
    DishListView,
    CookListView)

urlpatterns = [
    path("", index, name="index"),
    path("dish-types/", DishTypeListView.as_view(), name="dish_type_list"),
    path("dishes/", DishListView.as_view(), name="dish_list"),
    path("cooks/", CookListView.as_view(), name="cook_list")
]

app_name = "kitchen"
