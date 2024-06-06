from django import forms
from .models import Record
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm

class CustomUserForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ['name', 'height', 'weight', 'exercise']

class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(
        label='帳號',
        max_length=20,
        widget=forms.TextInput(attrs={
            'autofocus': True,
            })
    )
    password = forms.CharField(
        label='密碼',
        strip=False,
        widget=forms.PasswordInput()
    )
    
    error_messages = {
        'invalid_login': (
            "請輸入正確的帳號和密碼。注意！帳號和密碼都區分大小寫。")
    }

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(label='帳號', max_length=150)
    password1 = forms.CharField(label='密碼', widget=forms.PasswordInput)
    password2 = forms.CharField(label='確認密碼', widget=forms.PasswordInput)