from django import forms
from django.contrib.auth.forms import *
from django.contrib.auth.models import User


class SignupForm(UserCreationForm):
    

    class Meta:
        model = User
        fields =('username','email','password1','password2')

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'Your Username',
        'class':'w-1/2 py-4 px-6 rounded-xl'

    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder':'something@something.com',
        'class':'w-1/2 py-4 px-6 rounded-xl'

    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Choose a password',
        'class':'w-1/2 py-4 px-6 rounded-xl'

    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'',
        'class':'w-1/2 py-4 px-6 rounded-xl'

    }))

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'Enter your username',
        'class':'w-1/2 py-4 px-6 rounded-xl'

    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Enter your password',
        'class':'w-1/2 py-4 px-6 rounded-xl'

    }))
