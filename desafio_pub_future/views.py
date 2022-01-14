from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy, reverse
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import IncomeForm, ExpenseForm, BalanceForm, CustomUserCreationForm
from django.contrib.auth import authenticate, login, logout
from .models import Income, Expense, Balance
from django.http import HttpResponseRedirect
from datetime import date
from django.db.models import Sum


# --- ACCOUNT VIEW ---


def register(request):
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')

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


# --- DASHBOARD ---


def dashboard(request):
    last_balance = Balance.objects.filter(user=request.user, type=1).order_by('-date').first()
    last_income = Income.objects.filter(user=request.user).order_by('-date').first()
    last_expense = Expense.objects.filter(user=request.user).order_by('-date').first()
    if not last_balance:
        messages.warning(request, 'Nenhum saldo foi registrado. Adicione pelo menos um registro de saldo.')
        return render(request, 'pages/dashboard.html')

    today = date.today()
    # initialise total with sums of non repetitive incomes and
    total_income = Income.objects.filter(user=request.user, date__gte=last_balance.date, date__lte=today).aggregate(total=Sum('value'))['total']
    total_income = 0 if total_income is None else total_income
    total_expense = Expense.objects.filter(user=request.user, date__gte=last_balance.date, date__lte=today).aggregate(total=Sum('value'))['total']
    total_expense = 0 if total_expense is None else total_expense

    context = {
        'last_balance': last_balance,
        'last_income': last_income,
        'last_expense': last_expense,
        'estimated_balance': last_balance.value + total_income - total_expense,
        'total_income': total_income,
        'total_expense': total_expense
    }
    return render(request, 'pages/dashboard.html', context=context)


# --- INCOME VIEW ---


class IncomeListView(ListView):
    model = Income
    paginate_by = 100
    template_name = 'desafio_pub_future/balance_income_expense_list.html'
    extra_context = {'list_what': 'Income'}

    def get_queryset(self):
        user = self.request.user
        return Income.objects.filter(user=user)

class IncomeDetailView(DetailView):
    model = Income
    template_name = 'desafio_pub_future/balance_income_expense_detail.html'
    extra_context = {'detail_what': 'Income'}

    def get_queryset(self):
        user = self.request.user
        return Income.objects.filter(user=user)


class IncomeCreateView(CreateView):
    model = Income
    form_class = IncomeForm
    template_name = 'desafio_pub_future/balance_income_expense_form.html'
    extra_context = {'header_what': 'Receita'}

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse_lazy('income_list')


class IncomeUpdateView(UpdateView):
    model = Income
    form_class = IncomeForm
    template_name = 'desafio_pub_future/balance_income_expense_form.html'
    extra_context = {'header_what': 'Receita'}
    
    def get_queryset(self):
        user = self.request.user
        return Income.objects.filter(user=user)
    
    def get_success_url(self):
        return reverse('income_detail', kwargs={'pk': self.object.pk})


class IncomeDeleteView(DeleteView):
    model = Income
    success_url = reverse_lazy('income_list')
    template_name = 'desafio_pub_future/balance_income_expense_confirm_delete.html'
    extra_context = {'delete_what': 'Income'}

    def get_queryset(self):
        user = self.request.user
        return Income.objects.filter(user=user)


# --- EXPENSE VIEW ---


class ExpenseListView(ListView):
    model = Expense
    paginate_by = 100
    template_name = 'desafio_pub_future/balance_income_expense_list.html'
    extra_context = {'list_what': 'Expense'}

    def get_queryset(self):
        user = self.request.user
        return Expense.objects.filter(user=user)

class ExpenseDetailView(DetailView):
    model = Expense
    template_name = 'desafio_pub_future/balance_income_expense_detail.html'
    extra_context = {'detail_what': 'Expense'}

    def get_queryset(self):
        user = self.request.user
        return Expense.objects.filter(user=user)


class ExpenseCreateView(CreateView):
    model = Expense
    form_class = ExpenseForm
    template_name = 'desafio_pub_future/balance_income_expense_form.html'
    extra_context = {'header_what': 'Despesa'}

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse_lazy('expense_list')


class ExpenseUpdateView(UpdateView):
    model = Expense
    form_class = ExpenseForm
    template_name = 'desafio_pub_future/balance_income_expense_form.html'
    extra_context = {'header_what': 'Despesa'}
    
    def get_queryset(self):
        user = self.request.user
        return Expense.objects.filter(user=user)
    
    def get_success_url(self):
        return reverse('expense_detail', kwargs={'pk': self.object.pk})


class ExpenseDeleteView(DeleteView):
    model = Expense
    template_name = 'desafio_pub_future/balance_income_expense_confirm_delete.html'
    extra_context = {'delete_what': 'Expense'}

    def get_queryset(self):
        user = self.request.user
        return Expense.objects.filter(user=user)
    
    def get_success_url(self):
        return reverse_lazy('expense_list')


# BALANCE VIEW


class BalanceListView(ListView):
    model = Balance
    paginate_by = 100
    template_name = 'desafio_pub_future/balance_income_expense_list.html'
    extra_context = {'list_what': 'Balance'}

    def get_queryset(self):
        user = self.request.user
        return Balance.objects.filter(user=user)


class BalanceDetailView(DetailView):
    model = Balance
    template_name = 'desafio_pub_future/balance_income_expense_detail.html'
    extra_context = {'detail_what': 'Balance'}

    def get_queryset(self):
        user = self.request.user
        return Balance.objects.filter(user=user)


class BalanceCreateView(CreateView):
    model = Balance
    form_class = BalanceForm
    template_name = 'desafio_pub_future/balance_income_expense_form.html'
    extra_context = {'header_what': 'Saldo'}

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse_lazy('balance_list')


class BalanceUpdateView(UpdateView):
    model = Balance
    form_class = BalanceForm
    template_name = 'desafio_pub_future/balance_income_expense_form.html'
    extra_context = {'header_what': 'Saldo'}
    
    def get_queryset(self):
        user = self.request.user
        return Balance.objects.filter(user=user)
    
    def get_success_url(self):
        return reverse('balance_detail', kwargs={'pk': self.object.pk})


class BalanceDeleteView(DeleteView):
    model = Balance
    success_url = reverse_lazy('balance_list')
    template_name = 'desafio_pub_future/balance_income_expense_confirm_delete.html'
    extra_context = {'delete_what': 'Balance'}

    def get_queryset(self):
        user = self.request.user
        return Balance.objects.filter(user=user)
