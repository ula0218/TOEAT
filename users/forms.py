from django import forms
from .models import User
from django.contrib.auth.forms import AuthenticationForm

class CustomUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'height', 'weight', 'exercise']

class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(
        label='用戶名',
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