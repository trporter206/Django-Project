from django import forms
from .models import Cocktail
from django.contrib.auth.models import User

class CocktailForm(forms.ModelForm):
    class Meta:
        model = Cocktail
        fields = [
            "cocktail_name",
            "cocktail_image",
            "cocktail_type",
            "cocktail_info",
            "cocktail_steps",
            "virgin",
        ]

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
        ]
