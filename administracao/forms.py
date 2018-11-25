from django import forms
from django.contrib.auth.models import User

from .models import *


class LoginForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ['username', 'password']


class CampanhaForm(forms.ModelForm):
    
    class Meta:
        model = Campanha
        fields = '__all__'


class AcaoForm(forms.ModelForm):
    
    class Meta:
        model = Acao
        fields = '__all__'


class EscolaForm(forms.ModelForm):
    
    class Meta:
        model = Escola
        fields = '__all__'


class AlunoForm(forms.ModelForm):
    
    class Meta:
        model = Aluno
        fields = '__all__'


class QuestionarioForm(forms.ModelForm):
    
    class Meta:
        model = Questionario
        fields = '__all__'


class ExameForm(forms.ModelForm):
    
    class Meta:
        model = Exame
        fields = '__all__'


class DiretorForm(forms.ModelForm):
    
    class Meta:
        model = Diretor
        fields = '__all__'
