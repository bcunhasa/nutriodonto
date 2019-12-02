from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.views import View

from administracao.models import *


class LoginRequired(LoginRequiredMixin):
    """Configurações para o login"""
    login_url = 'administracao/login/'
    redirect_field_name = 'next'


class EscolasView(LoginRequired, View):
    """Página que carrega um mapa com as escolas"""
    
    def get(self, request):
        escolas = Escola.objects.order_by('-id')
        context = {'pagina_mapa_escolas': True, 'escolas': escolas}
        return render(self.request, 'mapas/escolas.html', context)
