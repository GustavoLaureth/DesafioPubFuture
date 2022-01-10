from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import RegistrationForm, AccountAuthenticationForm, AccountUpdateForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from time import sleep

from .forms import IncomeForm

from .models import Account, Income

def loginPage(request):
    context = {}
    user = request.user
    if user.is_authenticated:
        return redirect('dashboard')
    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                return redirect('dashboard')
        messages.add_message(request, messages.ERROR,
                             'Email ou Senha Inválido.')

        return redirect('login')

    else:
        form = AccountAuthenticationForm()

    context['login_form'] = form
    return render(request, 'pages/login.html', context)

def registerPage(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            return redirect('login')
        else:
            context['registration_form'] = form
    else:
        form = RegistrationForm()
        context['registration_form'] = form

    return render(request, 'pages/register.html', context)

def dashboard(request):
    return render(request, 'pages/dashboard.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def account_view(request):
    
    if not request.user.is_authenticated:
        return redirect('login')

    context = {}

    if request.POST:
        form = AccountUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.initial = {
                    'email': request.POST['email'],
                    'username': request.POST['username'],
            }
            form.save()
            return redirect('dashboard')
    else:
        form = AccountUpdateForm(
                initial= {
                    'email': request.user.email,
                    'username': request.user.username,
                }
            )
    context['account_form'] = form
    return render(request, 'pages/account.html', context)


class IncomeListView(ListView):
    model = Income
    paginate_by = 100


class IncomeDetailView(DetailView):
    model = Income


class IncomeCreateView(CreateView):
    model = Income
    form_class = IncomeForm
    success_url = reverse_lazy('income_list')


class IncomeUpdateView(UpdateView):
    model = Income
    form_class = IncomeForm
    success_url = reverse_lazy('income_list')


class IncomeDeleteView(DeleteView):
    model = Income
    success_url = reverse_lazy('income_list')

