from django.forms import ModelForm, fields
from django import forms
from .models import Income, Expense, Balance
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from datetime import date

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
        instance = super().save(commit=False)
        if commit:
            instance.save()
        return instance

class DateInput(forms.DateInput):
    input_type = 'date'


class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = ['value', 'date', 'type', 'comment']

    value = forms.DecimalField(initial=0.00)
    date = forms.DateField(widget=DateInput)
    type = forms.ChoiceField(choices=Income.ITypes.choices, initial =3)

    type.widget.attrs['class'] = 'form-control mb-4'

    def clean(self):
        cleaned_data = self.cleaned_data
        return cleaned_data
    
    def is_valid(self):
        is_valid = super(IncomeForm, self).is_valid()
        return is_valid

    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()
        return instance


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['value', 'date', 'type', 'comment']

    value = forms.DecimalField(initial=0.00)
    date = forms.DateField(widget=DateInput)
    type = forms.ChoiceField(choices=Expense.ETypes.choices, initial=5)

    type.widget.attrs['class'] = 'form-control mb-4'

    def is_valid(self):
        is_valid = super(ExpenseForm, self).is_valid()
        return is_valid

    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()
        return instance


class BalanceForm(forms.ModelForm):
    class Meta:
        model = Balance
        fields = ['value', 'date', 'type', 'comment']

    value = forms.DecimalField(initial=0.00)
    date = forms.DateField(widget=DateInput)
    type = forms.ChoiceField(choices=Balance.BType.choices, initial=1)

    type.widget.attrs['class'] = 'form-control mb-4'
