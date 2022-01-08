from django.forms import ModelForm, fields
from django import forms
from django.forms.widgets import PasswordInput
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm

from .models import Account

class RegistrationForm(UserCreationForm):
    class Meta:
        model = Account
        # Campos que vão para o Register. (são do model Account em models.)
        fields = ['username', 'email', 'password1', 'password2']


class AccountAuthenticationForm(forms.ModelForm):

    password = forms.CharField(label='Passsword', widget=PasswordInput)

    class Meta:
        model = Account
        fields = ('email', 'password')

    def clean(self):
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']
        if not authenticate(email=email, password=password):
            raise forms.ValidationError('Login Inválido!')


class AccountUpdateForm(forms.ModelForm):

    class Meta:
        model = Account
        fields = ('email', 'username')
    
    def clean_email(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            try:
                account = Account.objects.exclude(pk=self.instance.pk).get(email=email)
            except Account.DoesNotExist:
                return email
            raise forms.ValidationError("Email '%s' is alredy in use." % email)
    def clean_username(self):
        if self.is_valid():
            username = self.cleaned_data['username']
            try:
                account = Account.objects.exclude(pk=self.instance.pk).get(username=username)
            except Account.DoesNotExist:
                return username
            raise forms.ValidationError("Username '%s' is alredy in use." % username)