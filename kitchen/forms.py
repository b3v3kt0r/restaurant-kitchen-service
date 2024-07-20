from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.core.exceptions import ValidationError

from kitchen.models import Cook, Dish


class CookCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Cook
        fields = UserCreationForm.Meta.fields + ("first_name", "last_name", "years_of_experience",)

    def clean_years_of_experience(self):
        return validate_years_of_experience(self.cleaned_data["years_of_experience"])


class CookYearsOfExperienceUpdateForm(forms.ModelForm):
    class Meta(UserCreationForm.Meta):
        model = Cook
        fields = ["years_of_experience"]

    def clean_years_of_experience(self):
        return validate_years_of_experience(self.cleaned_data["years_of_experience"])


def validate_years_of_experience(years_of_experience: int):
    if years_of_experience < 0:
        raise ValidationError("Years of experience must be positive number!")
    elif years_of_experience > 100:
        raise ValidationError("We don't like jokes here!")
    return years_of_experience


class DishForm(forms.ModelForm):
    cookers = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False)

    class Meta:
        model = Dish
        fields = "__all__"


class DishSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by name"})
    )


class DishTypeSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by name"})
    )


class CookSearchForm(forms.Form):
    first_name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by first name"})
    )
    last_name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by last name"})
    )
    username = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by username"})
    )
    years_of_experience = forms.IntegerField(
        required=False,
        label="",
        widget=forms.NumberInput(attrs={"placeholder": "Search by years of experience"})
    )
