from django.urls import path

from kitchen.views import (
    index,
    DishTypeListView,
    DishTypeCreateView,
    DishTypeUpdateView,
    DishTypeDeleteView,
    DishListView,
    DishDetailView,
    CookListView,
    CookDetailView)

urlpatterns = [
    path("", index, name="index"),
    path("dish-types/", DishTypeListView.as_view(), name="dish_type_list"),
    path("dish-types/create/", DishTypeCreateView.as_view(), name="dish_type_create"),
    path("dish-types/<int:pk>/update/", DishTypeUpdateView.as_view(), name="dish_type_update"),
    path("dish-types/<int:pk>/delete/", DishTypeDeleteView.as_view(), name="dish_type_delete"),
    path("dishes/", DishListView.as_view(), name="dish_list"),
    path("dishes/<int:pk>/", DishDetailView.as_view(), name="dish_detail"),
    path("cooks/", CookListView.as_view(), name="cook_list"),
    path("cooks/<int:pk>/", CookDetailView.as_view(), name="cook_detail"),
]

app_name = "kitchen"
