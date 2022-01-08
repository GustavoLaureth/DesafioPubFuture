from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('cadastro/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard')
]