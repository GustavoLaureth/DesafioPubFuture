from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import IncomeForm, CustomUserCreationForm
from django.contrib.auth import authenticate, login, logout
from .models import Income


def register(request):
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'pages/register.html', context)


def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    username = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Email ou senha invalida')

    return render(request, 'pages/login.html', context={'username': username})


def logout_view(request):
    logout(request)
    return redirect('login')


def dashboard(request):
    return render(request, 'pages/dashboard.html')


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

