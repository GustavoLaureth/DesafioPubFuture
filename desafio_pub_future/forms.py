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
        fields = ['value', 'date', 'type', 'repetitive', 'repetition_interval', 'repetition_time', 'comment']

    date = forms.DateField(widget=DateInput, initial=date.today())

    def clean(self):
        cleaned_data = self.cleaned_data
        return cleaned_data
    
    def is_valid(self):
        is_valid = super(IncomeForm, self).is_valid()

        value = self.cleaned_data.get('value')
        value = self.cleaned_data.get('value')
        form_date = self.cleaned_data.get('date')
        repetitive = self.cleaned_data.get('repetitive')
        repetition_interval = self.cleaned_data.get('repetition_interval')
        repetition_time = self.cleaned_data.get('repetition_time')


        if value <= 0:
            self.add_error('value', 'O valor deve ser um número positivo')
            is_valid = False
        
        if repetition_interval == 4 and form_date.day > 28:
            self.add_error('date', 'Quando o intervalo de repetição é definido como MESES, a data não pode ser maior que 28')
            is_valid = False
        
        if repetitive:
            if repetition_interval == 1:
                self.add_error('repetition_interval', 'O intervalo de repetição não pode ser N/A quando a repetição é selecionada')
                is_valid = False
            if repetition_time == 0:
                self.add_error('repetition_time', 'O tempo de repetição não pode ser 0 quando a repetição é selecionada')
                is_valid = False
        else:
            if repetition_interval != 1:
                self.add_error('repetitive', 'Repetir precisa ser selecionado quando o intervalo de repetição não for N/A')
                is_valid = False

        if value <= 10:
            self.add_error('value', 'Não pode ser menor que 10')
            is_valid = False
        return is_valid

    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()
        return instance


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['value', 'date', 'type', 'repetitive', 'repetition_interval', 'repetition_time', 'comment']

    date = forms.DateField(widget=DateInput, initial=date.today())

    def is_valid(self):
        is_valid = super(ExpenseForm, self).is_valid()

        value = self.cleaned_data.get('value')
        value = self.cleaned_data.get('value')
        form_date = self.cleaned_data.get('date')
        repetitive = self.cleaned_data.get('repetitive')
        repetition_interval = self.cleaned_data.get('repetition_interval')
        repetition_time = self.cleaned_data.get('repetition_time')


        if value <= 0:
            self.add_error('value', 'O valor deve ser um número positivo')
            is_valid = False
        
        if repetition_interval == 4 and form_date.day > 28:
            self.add_error('date', 'Quando o intervalo de repetição é definido como MESES, a data não pode ser maior que 28')
            is_valid = False
        
        if repetitive:
            if repetition_interval == 1:
                self.add_error('repetition_interval', 'O intervalo de repetição não pode ser N/A quando a repetição é selecionada')
                is_valid = False
            if repetition_time == 0:
                self.add_error('repetition_time', 'O tempo de repetição não pode ser 0 quando a repetição é selecionada')
                is_valid = False
        else:
            if repetition_interval != 1:
                self.add_error('repetitive', 'Repetir precisa ser selecionado quando o intervalo de repetição não for N/A')
                is_valid = False

        if value <= 10:
            self.add_error('value', 'Não pode ser menor que 10')
            is_valid = False
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

    date = forms.DateField(widget=DateInput, initial=date.today())
