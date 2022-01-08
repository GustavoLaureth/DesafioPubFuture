from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

from .models import Account

class RegistrationForm(UserCreationForm):
    class Meta:
        model = Account
        # Campos que vão para o Register. (são do model Account em models.)
        fields = ['username', 'email', 'password1', 'password2']
