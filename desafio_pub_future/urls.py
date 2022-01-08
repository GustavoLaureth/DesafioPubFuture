from django.urls import path
from . import views

urlpatterns = [
    path('', views.loginPage, name='login'),
    path('dashboard/', views.dashboard, name='dashboard')
]