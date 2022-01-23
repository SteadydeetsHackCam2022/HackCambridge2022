"""backend URL Configuration

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
from django.urls import path
from rest_framework.authtoken import views as auth_views
from store import views as store_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('feed/', store_views.feed),
    path('login/', store_views.login),
    path('signup/', store_views.signup),
    path('search/', store_views.search),
    path('profile/', store_views.profile),
    path('products/add', store_views.product_add),
    path('products/save', store_views.product_save)
]
