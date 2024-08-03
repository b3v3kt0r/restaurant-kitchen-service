from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from kitchen.models import DishType, Cook, Dish

DISH_TYPE_URL = reverse("kitchen:dish_type_list")
DISH_URL = reverse("kitchen:dish_list")
COOK_URL = reverse("kitchen:cook_list")


class PublicDishTypeTest(TestCase):
    def test_login_required(self) -> None:
        res = self.client.get(DISH_TYPE_URL)
        self.assertNotEqual(res.status_code, 200)


class PrivateDishTypeTest(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="test",
            password="test123"
        )
        self.client.force_login(self.user)

    def test_retrieve_dish_types(self) -> None:
        DishType.objects.create(name="test1")
        DishType.objects.create(name="test2")
        response = self.client.get(DISH_TYPE_URL)
        self.assertEqual(response.status_code, 200)
        dish_types = DishType.objects.all()
        self.assertEqual(
            list(response.context["dish_type_list"]),
            list(dish_types)
        )
        self.assertTemplateUsed(response, "kitchen/dish_type_list.html")

    def test_search_dish_type(self) -> None:
        response = self.client.get(DISH_TYPE_URL, {"name": "Appetizer"})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Appetizer")


class PublicDishTest(TestCase):
    def test_login_required(self) -> None:
        res = self.client.get(DISH_URL)
        self.assertNotEqual(res.status_code, 200)


class PrivateDishTest(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="test",
            password="test123"
        )
        self.client.force_login(self.user)

    def test_retrieve_dish(self) -> None:
        dish_type = DishType.objects.create(name="test")
        Dish.objects.create(name="test1", dish_type=dish_type, price=5)
        Dish.objects.create(name="test2", dish_type=dish_type, price=6)
        response = self.client.get(DISH_URL)
        self.assertEqual(response.status_code, 200)
        dishes = Dish.objects.all()
        self.assertEqual(list(response.context["dish_list"]), list(dishes))
        self.assertTemplateUsed(response, "kitchen/dish_list.html")

    def test_search_dish(self) -> None:
        response = self.client.get(DISH_URL, {"name": "Apple pie"})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Apple pie")


class PublicCookTest(TestCase):
    def test_login_required(self) -> None:
        response = self.client.get(COOK_URL)
        self.assertNotEqual(response.status_code, 200)


class PrivateCookTest(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="test",
            password="test123"
        )
        self.client.force_login(self.user)

    def test_retrieve_cooks(self) -> None:
        response = self.client.get(COOK_URL)
        self.assertEqual(response.status_code, 200)
        cooks = Cook.objects.all()
        self.assertEqual(list(response.context["cook_list"]),
                         list(cooks))
        self.assertTemplateUsed(response, "kitchen/cook_list.html")

    def test_search_cooks_by_first_name(self) -> None:
        response = self.client.get(COOK_URL, {"first_name": "John"})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "John")

    def test_search_cooks_by_last_name(self) -> None:
        response = self.client.get(COOK_URL, {"last_name": "Doe"})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Doe")

    def test_search_cooks_by_username(self) -> None:
        response = self.client.get(COOK_URL, {"username": "admin"})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "admin")

    def test_search_cooks_by_years_of_experience(self) -> None:
        response = self.client.get(COOK_URL, {"username": "2"})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "2")
