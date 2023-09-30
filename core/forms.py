from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'w-full py-2 px-2 rounded-xl focus:outline-none'    
    }))
    
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'w-full py-2 px-2 rounded-xl focus:outline-none'    
    }))
    
class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'w-full py-2 px-2 rounded-xl focus:outline-none'    
    }))
    
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'w-full py-2 px-2 rounded-xl focus:outline-none'    
    }))
    
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'w-full py-2 px-2 rounded-xl focus:outline-none'    
    }))
    
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'w-full py-2 px-2 rounded-xl focus:outline-none'    
    }))