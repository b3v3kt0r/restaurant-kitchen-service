from django.test import TestCase

from kitchen.forms import CookCreationForm


class FormsTests(TestCase):
    def test_cook_creation_form_with_years_of_experience_first_last_name_is_valid(self) -> None:
        form_data = {
            "username": "test",
            "password1": "test123test",
            "password2": "test123test",
            "first_name": "Test first",
            "last_name": "Test last",
            "years_of_experience": 2
        }
        form = CookCreationForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)

    def test_driver_creation_form_with_invalid_license_number(self) -> None:
        form_data = {
            "username": "test",
            "password1": "test123test",
            "password2": "test123test",
            "first_name": "Test first",
            "last_name": "Test last",
            "years_of_experience": -1
        }
        form = CookCreationForm(data=form_data)
        self.assertFalse(form.is_valid())
