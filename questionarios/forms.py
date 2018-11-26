from django import forms
from django.contrib.auth.models import User

from administracao.models import *


class DiretorForm(forms.ModelForm):
    
    class Meta:
        model = Diretor
        exclude = ('data',)
