# users/urls.py
from django.urls import path
from django.shortcuts import redirect
from . import views

urlpatterns = [
    path('login/', views.fake_login, name='login'),
    path('register/', views.user_register, name='register'),
    path('password-reset/', views.password_reset, name='password_reset'),
    path('dashboard/', views.dashboard, name='dashboard'),  # <--- aquí la ruta
]
