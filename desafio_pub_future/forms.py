from django.forms import ModelForm, fields
from django import forms
from .models import Income
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.model import User

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    username = forms.Field(widget=forms.TextInput(attrs={
        'class': 'form-control mb-3', 'placeholder': 'Username'
    }))
    email = forms.Field(widget=forms.EmailInput(attrs={
        'class': 'form-control mb-3', 'placeholder': 'E-mail'
    }))
    password1 = forms.Field(widget=forms.PasswordInput(attrs={
        'class': 'form-control mb-3', 'placeholder': 'Senha'
    }))
    password2 = forms.Field(widget=forms.PasswordInput(attrs={
        'class': 'form-control mb-3', 'placeholder': 'Confirmar Senha'
    }))

    def save(self, commit=True):
        instance = super().save(commit=True)
        instance.username = instance.email
        if commit:
            instance.save()
        return instance

class DateInput(forms.DateInput):
    input_type = 'date'


class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = ['value','date','type','repetitive','repetition_interval','repetition_time', 'comment']
        widgets = {
            'date': DateInput()
        }
