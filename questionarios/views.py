from django.shortcuts import render
from django.shortcuts import render
from django.views import View

from administracao.models import *
from administracao.forms import *


class DiretorView(View):
    """Permite que um diretor de escola responda o questionário"""
    
    def get(self, request):
        campanhas = Diretor.objects.order_by('-id')
        context = {'pagina_campanhas': True, 'campanhas': campanhas}
        return render(self.request, 'administracao/campanhas.html', context)


class AlunoView(View):
    """Permite que um aluno responda o questionário"""
    
    def get(self, request):
        campanhas = Campanha.objects.order_by('-id')
        context = {'pagina_campanhas': True, 'campanhas': campanhas}
        return render(self.request, 'administracao/campanhas.html', context)
