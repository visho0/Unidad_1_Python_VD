# users/forms.py
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm

class LoginForm(AuthenticationForm):
    username = forms.EmailField(label="Email")

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class CustomPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(label="Email")
