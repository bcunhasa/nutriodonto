from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.shortcuts import render
from django.views import View

from .models import *
from .forms import *


class IndexView(View):
    """Página inicial do site"""
    
    def get(self, request):
        return render(self.request, 'administracao/index.html')


class LoginRequired(LoginRequiredMixin):
    """Configurações para o login"""
    login_url = 'administracao/login/'
    redirect_field_name = 'next'


class LoginView(View):
    """Página para a autenticação do usuário"""
    
    def get(self, request):
        form = LoginForm()
        context = {'form': form}
        return render(self.request, 'administracao/login.html', context)
    
    def post(self, request):
        form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        usuario = authenticate(username=username, password=password)
        
        try:
            if username != 'admin':
                request.user.administrador
            
            if usuario is not None:
                login(request, usuario)
                return HttpResponseRedirect(reverse('administracao:visao_geral'))
            else:
                context = {'form': form}
                return render(self.request, 'administracao/login.html', context)
        except:
            context = {'form': form}
            return render(self.request, 'administracao/login.html', context)


class LogoutView(View):
    """Página para logout do usuário"""
    
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('administracao:index'))


class VisaoGeralView(LoginRequired, View):
    """Página de visão geral do site de administração"""
    
    def get(self, request):
        campanhas = Campanha.objects.count()
        acoes = Acao.objects.count()
        escolas = Escola.objects.count()
        alunos = Aluno.objects.count()
        questionarios = Questionario.objects.count()
        exames = Exame.objects.count()
        
        context = {
            'pagina_visao_geral': True,
            'campanhas': campanhas,
            'acoes': acoes,
            'escolas': escolas,
            'alunos': alunos,
            'questionarios': questionarios,
            'exames': exames,
        }
        return render(self.request, 'administracao/visao_geral.html', context)


class GraficosView(LoginRequired, View):
    """Página que exibe gráficos baseados nos dados já coletados"""
    
    def get(self, request):
        questionarios = Questionario.objects.order_by('-id')
        context = {'pagina_graficos': True, 'questionarios': questionarios}
        return render(self.request, 'administracao/graficos.html', context)


class UsuariosView(LoginRequired, View):
    """Página que lista os usuários cadastrados no sistema"""
    
    def get(self, request):
        usuarios = User.objects.order_by('-id')
        context = {'pagina_usuarios': True, 'usuarios': usuarios}
        return render(self.request, 'administracao/usuarios.html', context)


class CampanhasView(LoginRequired, View):
    """Página que lista as campanhas cadastradas no sistema"""
    
    def get(self, request):
        campanhas = Campanha.objects.order_by('-id')
        context = {'pagina_campanhas': True, 'campanhas': campanhas}
        return render(self.request, 'administracao/campanhas.html', context)


class AcoesView(LoginRequired, View):
    """Página que lista as ações cadastradas no sistema"""
    
    def get(self, request):
        acoes = Acao.objects.order_by('-id')
        context = {'pagina_acoes': True, 'acoes': acoes}
        return render(self.request, 'administracao/acoes.html', context)


class EscolasView(LoginRequired, View):
    """Página que lista as escolas cadastradas no sistema"""
    
    def get(self, request):
        escolas = Escola.objects.order_by('-id')
        context = {'pagina_escolas': True, 'escolas': escolas}
        return render(self.request, 'administracao/escolas.html', context)


class AlunosView(LoginRequired, View):
    """Página que lista os alunos cadastrados no sistema"""
    
    def get(self, request):
        alunos = Aluno.objects.order_by('-id')
        context = {'pagina_alunos': True, 'alunos': alunos}
        return render(self.request, 'administracao/alunos.html', context)


class QuestionariosView(LoginRequired, View):
    """Página que lista os questionários cadastrados no sistema"""
    
    def get(self, request):
        questionarios = Questionario.objects.order_by('-id')
        context = {'pagina_questionarios': True, 'questionarios': questionarios}
        return render(self.request, 'administracao/questionarios.html', context)


class ExamesView(LoginRequired, View):
    """Página que lista os exames cadastrados no sistema"""
    
    def get(self, request):
        exames = Exame.objects.order_by('-id')
        context = {'pagina_exames': True, 'exames': exames}
        return render(self.request, 'administracao/exames.html', context)
