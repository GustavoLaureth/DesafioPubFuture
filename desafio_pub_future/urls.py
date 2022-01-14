from django.urls import path
from . import views


urlpatterns = [
    path('', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    
    path('income_list/', views.IncomeListView.as_view(), name='income_list'),
    path('income_create/', views.IncomeCreateView.as_view(), name='income_create'),
    path('income_update/<pk>', views.IncomeUpdateView.as_view(), name='income_update'),
    path('income_delete/<pk>', views.IncomeDeleteView.as_view(), name='income_delete'),

    path('expense_list/', views.ExpenseListView.as_view(), name='expense_list'),
    path('expense_create/', views.ExpenseCreateView.as_view(), name='expense_create'),
    path('expense_update/<pk>', views.ExpenseUpdateView.as_view(), name='expense_update'),
    path('expense_delete/<pk>', views.ExpenseDeleteView.as_view(), name='expense_delete'),

    path('balance_list/', views.BalanceListView.as_view(), name='balance_list'),
    path('balance_create/', views.BalanceCreateView.as_view(), name='balance_create'),
    path('balance_update/<pk>', views.BalanceUpdateView.as_view(), name='balance_update'),
    path('balance_delete/<pk>', views.BalanceDeleteView.as_view(), name='balance_delete'),
]