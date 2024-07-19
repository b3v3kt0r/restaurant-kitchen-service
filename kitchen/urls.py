from django.urls import path

from kitchen.views import (
    index,
    DishTypeListView,
    DishListView,
    DishDetailView,
    CookListView,
    CookDetailView)

urlpatterns = [
    path("", index, name="index"),
    path("dish-types/", DishTypeListView.as_view(), name="dish_type_list"),
    path("dishes/", DishListView.as_view(), name="dish_list"),
    path("dishes/<int:pk>/", DishDetailView.as_view(), name="dish_detail"),
    path("cooks/", CookListView.as_view(), name="cook_list"),
    path("cooks/<int:pk>/", CookDetailView.as_view(), name="cook_detail"),
]

app_name = "kitchen"
