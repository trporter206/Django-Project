from django import forms
from .models import Cocktail, UserProfile
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

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
            "public",
        ]

class UserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        ]

    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user

class EditProfileForm(UserChangeForm):

    class Meta:
        model = User
        fields = [
            'email',
            'first_name',
            'last_name',
            'password',
        ]
