# users/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, RegisterForm, CustomPasswordResetForm
from .models import Organization
from django.contrib import messages

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, "Usuario o contraseña incorrectos")
    else:
        form = LoginForm()
    return render(request, 'users/login.html', {'form': form})

def user_register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            Organization.objects.create(user=user, name=form.cleaned_data['username'])
            messages.success(request, "Registro exitoso. Puedes iniciar sesión.")
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {'form': form})

def password_reset(request):
    if request.method == 'POST':
        form = CustomPasswordResetForm(request.POST)
        if form.is_valid():
            # Aquí simulamos el envío de correo
            messages.success(request, "Se enviaron instrucciones al email proporcionado.")
            return redirect('login')
    else:
        form = CustomPasswordResetForm()
    return render(request, 'users/password_reset.html', {'form': form})

def fake_login(request):
    return render(request, 'users/login.html')

@login_required
def dashboard(request):
    return render(request, 'users/dashboard.html')
