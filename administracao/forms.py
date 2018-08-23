from django import forms
from django.contrib.auth.models import User

from .models import *


class LoginForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ['username', 'password']
