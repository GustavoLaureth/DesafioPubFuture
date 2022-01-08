"""DesafioPubFuture URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from desafio_pub_future.views import (
    registerPage,
    logout_view,
    account_view,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('desafio_pub_future.urls')),
    path('register/', registerPage, name='register'),
    path('logout/', logout_view, name='logout'),
    path('account/', account_view, name='account'),
]
