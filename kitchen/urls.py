from django.urls import path

from kitchen.views import (
    index,
    DishTypeListView,
    DishTypeCreateView,
    DishTypeUpdateView,
    DishTypeDeleteView,
    DishListView,
    DishDetailView,
    DishCreateView,
    DishUpdateView,
    DishDeleteView,
    dish_remove_cook,
    dish_assign_cook,
    CookListView,
    CookDetailView,
    CookCreateView)

urlpatterns = [
    path("", index, name="index"),
    path("dish-types/", DishTypeListView.as_view(), name="dish_type_list"),
    path("dish-types/create/", DishTypeCreateView.as_view(), name="dish_type_create"),
    path("dish-types/<int:pk>/update/", DishTypeUpdateView.as_view(), name="dish_type_update"),
    path("dish-types/<int:pk>/delete/", DishTypeDeleteView.as_view(), name="dish_type_delete"),
    path("dishes/", DishListView.as_view(), name="dish_list"),
    path("dishes/create/", DishCreateView.as_view(), name="dish_create"),
    path("dishes/<int:pk>/", DishDetailView.as_view(), name="dish_detail"),
    path("dishes/<int:pk>/update/", DishUpdateView.as_view(), name="dish_update"),
    path("dishes/<int:pk>/delete/", DishDeleteView.as_view(), name="dish_delete"),
    path("dishes/<int:pk>/remove_cook/", dish_remove_cook, name="dish_remove_cook"),
    path("dishes/<int:pk>/assign_cook/", dish_assign_cook, name="dish_assign_cook"),
    path("cooks/", CookListView.as_view(), name="cook_list"),
    path("cooks/create", CookCreateView.as_view(), name="cook_create"),
    path("cooks/<int:pk>/", CookDetailView.as_view(), name="cook_detail"),
]

app_name = "kitchen"
