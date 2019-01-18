from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.shortcuts import render
from django.views import View

from .models import *
from .forms import *
from .const import *


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
            if username != 'sadoadmin':
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
        return HttpResponseRedirect(reverse('portal:index'))


class VisaoGeralView(LoginRequired, View):
    """Acompanhamento da coleta dos dados"""
    
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


class InferenciaView(LoginRequired, View):
    """Exibe dados gerados após o processo de inferência estatística"""
    
    def get(self, request):
        alunos = Aluno.objects.all()
        
        # Dados sociais
        sexo = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
        sexo_esperado = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
        raca = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
        raca_esperado = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
        
        # Uso de cigarro
        questao_73 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        questao_73_esperado = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        questao_75 = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
        questao_75_esperado = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
        questao_79 = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
        questao_79_esperado = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
        
        # Consumo de bebida alcoólica
        questao_84 = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
        questao_84_esperado = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
        
        # Drogas ilícitas
        questao_92 = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
        questao_92_esperado = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
        
        # Saúde bucal
        questao_111 = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
        questao_111_esperado = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
        questao_113 = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
        questao_113_esperado = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
        
        # Frequência alimentar
        questao_25 = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
        questao_25_esperado = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
        questao_26 = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
        questao_26_esperado = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
        questao_27 = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
        questao_27_esperado = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
        questao_28 = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
        questao_28_esperado = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
        questao_29 = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
        questao_29_esperado = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
        questao_30 = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
        questao_30_esperado = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
        questao_31 = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
        questao_31_esperado = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
        questao_32 = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
        questao_32_esperado = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
        questao_33 = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
        questao_33_esperado = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
        questao_34 = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
        questao_34_esperado = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
        questao_35 = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
        questao_35_esperado = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
        questao_36 = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
        questao_36_esperado = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
        questao_37 = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
        questao_37_esperado = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
        questao_38 = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
        questao_38_esperado = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
        questao_39 = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
        questao_39_esperado = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
        questao_40 = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
        questao_40_esperado = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
        questao_41 = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
        questao_41_esperado = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
        questao_42 = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
        questao_42_esperado = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
        questao_43 = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
        questao_43_esperado = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
        questao_44 = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
        questao_44_esperado = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
        questao_45 = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
        questao_45_esperado = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
        questao_46 = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
        questao_46_esperado = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
        questao_47 = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
        questao_47_esperado = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
        questao_48 = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
        questao_48_esperado = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
        questao_49 = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
        questao_49_esperado = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
        questao_50 = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
        questao_50_esperado = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
        questao_51 = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
        questao_51_esperado = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
        questao_52 = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
        questao_52_esperado = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
        questao_53 = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
        questao_53_esperado = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
        questao_54 = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
        questao_54_esperado = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
        
        for aluno in alunos:
            try:
                exame = aluno.exame
            except Exame.DoesNotExist:
                pass
            else:
                if aluno.exame.carie_coroa_18 == 'B' or aluno.exame.carie_coroa_18 == '1' \
                   or aluno.exame.carie_coroa_17 == 'B' or aluno.exame.carie_coroa_17 == '1' \
                   or aluno.exame.carie_coroa_16 == 'B' or aluno.exame.carie_coroa_16 == '1' \
                   or aluno.exame.carie_coroa_15 == 'B' or aluno.exame.carie_coroa_15 == '1' \
                   or aluno.exame.carie_coroa_14 == 'B' or aluno.exame.carie_coroa_14 == '1' \
                   or aluno.exame.carie_coroa_13 == 'B' or aluno.exame.carie_coroa_13 == '1' \
                   or aluno.exame.carie_coroa_12 == 'B' or aluno.exame.carie_coroa_12 == '1' \
                   or aluno.exame.carie_coroa_11 == 'B' or aluno.exame.carie_coroa_11 == '1' \
                   or aluno.exame.carie_coroa_21 == 'B' or aluno.exame.carie_coroa_21 == '1' \
                   or aluno.exame.carie_coroa_22 == 'B' or aluno.exame.carie_coroa_22 == '1' \
                   or aluno.exame.carie_coroa_23 == 'B' or aluno.exame.carie_coroa_23 == '1' \
                   or aluno.exame.carie_coroa_24 == 'B' or aluno.exame.carie_coroa_24 == '1' \
                   or aluno.exame.carie_coroa_25 == 'B' or aluno.exame.carie_coroa_25 == '1' \
                   or aluno.exame.carie_coroa_26 == 'B' or aluno.exame.carie_coroa_26 == '1' \
                   or aluno.exame.carie_coroa_27 == 'B' or aluno.exame.carie_coroa_27 == '1' \
                   or aluno.exame.carie_coroa_28 == 'B' or aluno.exame.carie_coroa_28 == '1' \
                   or aluno.exame.carie_coroa_38 == 'B' or aluno.exame.carie_coroa_38 == '1' \
                   or aluno.exame.carie_coroa_37 == 'B' or aluno.exame.carie_coroa_37 == '1' \
                   or aluno.exame.carie_coroa_36 == 'B' or aluno.exame.carie_coroa_36 == '1' \
                   or aluno.exame.carie_coroa_35 == 'B' or aluno.exame.carie_coroa_35 == '1' \
                   or aluno.exame.carie_coroa_34 == 'B' or aluno.exame.carie_coroa_34 == '1' \
                   or aluno.exame.carie_coroa_33 == 'B' or aluno.exame.carie_coroa_33 == '1' \
                   or aluno.exame.carie_coroa_32 == 'B' or aluno.exame.carie_coroa_32 == '1' \
                   or aluno.exame.carie_coroa_31 == 'B' or aluno.exame.carie_coroa_31 == '1' \
                   or aluno.exame.carie_coroa_41 == 'B' or aluno.exame.carie_coroa_41 == '1' \
                   or aluno.exame.carie_coroa_42 == 'B' or aluno.exame.carie_coroa_42 == '1' \
                   or aluno.exame.carie_coroa_43 == 'B' or aluno.exame.carie_coroa_43 == '1' \
                   or aluno.exame.carie_coroa_44 == 'B' or aluno.exame.carie_coroa_44 == '1' \
                   or aluno.exame.carie_coroa_45 == 'B' or aluno.exame.carie_coroa_45 == '1' \
                   or aluno.exame.carie_coroa_46 == 'B' or aluno.exame.carie_coroa_46 == '1' \
                   or aluno.exame.carie_coroa_47 == 'B' or aluno.exame.carie_coroa_47 == '1' \
                   or aluno.exame.carie_coroa_48 == 'B' or aluno.exame.carie_coroa_48 == '1':
                    # Sexo
                    if aluno.sexo == '0': # masculino
                        sexo[0][0] += 1
                    elif aluno.sexo == '1': # feminino
                        sexo[1][0] += 1
                    elif aluno.sexo == '2': # outro
                        sexo[2][0] += 1
                    
                    # Raça
                    if aluno.raca == '0': # amarela
                        raca[0][0] += 1
                    elif aluno.raca == '1': # branca
                        raca[1][0] += 1
                    elif aluno.raca == '2': # indigena
                        raca[2][0] += 1
                    elif aluno.raca == '3': # parda
                        raca[3][0] += 1
                    elif aluno.raca == '4': # preta
                        raca[4][0] += 1
                    
                    try:
                        questionario = aluno.questionario
                    except Questionario.DoesNotExist:
                        pass
                    else:
                        # Questão 73
                        if aluno.questionario.questao_73 == '0': # Sim
                            questao_73[0][0] += 1
                        elif aluno.questionario.questao_73 == '1': # Não
                            questao_73[1][0] += 1
                        
                        # Questão 75
                        if aluno.questionario.questao_75 == '0': # Nenhum dia nos últimos 30 dias (0 dia)
                            questao_75[0][0] += 1
                        elif aluno.questionario.questao_75 == '1': # 1 ou 2 dias nos últimos 30 dias
                            questao_75[1][0] += 1
                        elif aluno.questionario.questao_75 == '2': # 3 a 5 dias nos últimos 30 dias
                            questao_75[2][0] += 1
                        elif aluno.questionario.questao_75 == '3': # 6 a 9 dias nos últimos 30 dias
                            questao_75[3][0] += 1
                        elif aluno.questionario.questao_75 == '4': # 10 a 19 dias nos últimos 30 dias
                            questao_75[4][0] += 1
                        elif aluno.questionario.questao_75 == '5': # 20 a 29 dias nos últimos 30 dias
                            questao_75[5][0] += 1
                        elif aluno.questionario.questao_75 == '6': # Todos os dias nos últimos 30 dias
                            questao_75[6][0] += 1
                        
                        # Questão 79
                        if aluno.questionario.questao_79 == '0': # Não usei nenhum produto do tabaco (os produtos do tabaco estão abaixo relacionados)
                            questao_79[0][0] += 1
                        elif aluno.questionario.questao_79 == '1': # Cigarros de cravo (conhecidos como cigarros de Bali).
                            questao_79[1][0] += 1
                        elif aluno.questionario.questao_79 == '2': # Cigarros enrolados à mão (conhecidos como cigarros de palha ou papel)
                            questao_79[2][0] += 1
                        elif aluno.questionario.questao_79 == '3': # Cigarrilhas
                            questao_79[3][0] += 1
                        elif aluno.questionario.questao_79 == '4': # Charutos, charutos pequenos.
                            questao_79[4][0] += 1
                        elif aluno.questionario.questao_79 == '5': # Fumo para mascar
                            questao_79[5][0] += 1
                        elif aluno.questionario.questao_79 == '6': # Narguilé (cachimbo de água)
                            questao_79[6][0] += 1
                        elif aluno.questionario.questao_79 == '7': # Cigarros indianos (bidis)
                            questao_79[7][0] += 1
                        elif aluno.questionario.questao_79 == '8': # Cigarro eletrônico (e-cigarette)
                            questao_79[8][0] += 1
                        elif aluno.questionario.questao_79 == '9': # Outros
                            questao_79[9][0] += 1
                        
                        # Questao_84
                        if aluno.questionario.questao_84 == '0': # Nenhum dia nos últimos 30 dias (0 dia)
                            questao_84[0][0] += 1
                        elif aluno.questionario.questao_84 == '1': # 1 ou 2 dias nos últimos 30 dias
                            questao_84[1][0] += 1
                        elif aluno.questionario.questao_84 == '2': # 3 a 5 dias nos últimos 30 dias
                            questao_84[2][0] += 1
                        elif aluno.questionario.questao_84 == '3': # 6 a 9 dias nos últimos 30 dias
                            questao_84[3][0] += 1
                        elif aluno.questionario.questao_84 == '4': # 10 a 19 dias nos últimos 30 dias
                            questao_84[4][0] += 1
                        elif aluno.questionario.questao_84 == '5': # 20 a 29 dias nos últimos 30 dias
                            questao_84[5][0] += 1
                        elif aluno.questionario.questao_84 == '6': # Todos os dias nos últimos 30 dias
                            questao_84[6][0] += 1
                        
                        # Questao_92
                        if aluno.questionario.questao_92 == '0': # Nenhum dia nos últimos 30 dias (0 dia)
                            questao_92[0][0] += 1
                        elif aluno.questionario.questao_92 == '1': # 1 ou 2 dias nos últimos 30 dias
                            questao_92[1][0] += 1
                        elif aluno.questionario.questao_92 == '2': # 3 a 5 dias nos últimos 30 dias
                            questao_92[2][0] += 1
                        elif aluno.questionario.questao_92 == '3': # 6 a 9 dias nos últimos 30 dias
                            questao_92[3][0] += 1
                        elif aluno.questionario.questao_92 == '4': # 10 ou mais dias nos últimos 30 dias
                            questao_92[4][0] += 1
                        
                        # Questao_111
                        if aluno.questionario.questao_111 == '0': # Não escovei meus dentes nos últimos 30 dias
                            questao_111[0][0] += 1
                        elif aluno.questionario.questao_111 == '1': # Não escovei meus dentes diariamente
                            questao_111[1][0] += 1
                        elif aluno.questionario.questao_111 == '2': # 1 vez por dia nos últimos 30 dias
                            questao_111[2][0] += 1
                        elif aluno.questionario.questao_111 == '3': # 2 vezes por dia nos últimos 30 dias
                            questao_111[3][0] += 1
                        elif aluno.questionario.questao_111 == '4': # 3 vezes por dia nos últimos 30 dias
                            questao_111[4][0] += 1
                        elif aluno.questionario.questao_111 == '5': # 4 ou mais vezes por dia nos últimos 30 dias
                            questao_111[5][0] += 1
                        
                        # Questao_113
                        if aluno.questionario.questao_113 == '0': # Nenhuma vez nos últimos 12 meses (0 vez)
                            questao_113[0][0] += 1
                        elif aluno.questionario.questao_113 == '1': # 1 vez nos últimos 12 meses
                            questao_113[1][0] += 1
                        elif aluno.questionario.questao_113 == '2': # 2 vezes nos últimos 12 meses
                            questao_113[2][0] += 1
                        elif aluno.questionario.questao_113 == '3': # 3 ou mais vezes nos últimos 12 meses
                            questao_113[3][0] += 1
                        
                        # Questão 25
                        if aluno.questionario.questao_25 == '0': # Nunca ou menos de uma vez por mês
                            questao_25[0][0] += 1
                        elif aluno.questionario.questao_25 == '1': # 1 a 3 vezes por mês
                            questao_25[1][0] += 1
                        elif aluno.questionario.questao_25 == '2': # 1 vez por semana
                            questao_25[2][0] += 1
                        elif aluno.questionario.questao_25 == '3': # 2 a 4 vezes por semana
                            questao_25[3][0] += 1
                        elif aluno.questionario.questao_25 == '4': # 6 a 8 vezes por semana
                            questao_25[4][0] += 1
                        elif aluno.questionario.questao_25 == '5': # 1 vez por dia
                            questao_25[5][0] += 1
                        elif aluno.questionario.questao_25 == '6': # 2 a 3 vezes por dia
                            questao_25[6][0] += 1
                        elif aluno.questionario.questao_25 == '7': # 4 a 6 vezes por dia
                            questao_25[7][0] += 1
                        elif aluno.questionario.questao_25 == '8': # Mais de 8 vezes por dia
                            questao_25[8][0] += 1
                        
                        # Questão 26
                        if aluno.questionario.questao_26 == '0': # Nunca ou menos de uma vez por mês
                            questao_26[0][0] += 1
                        elif aluno.questionario.questao_26 == '1': # 1 a 3 vezes por mês
                            questao_26[1][0] += 1
                        elif aluno.questionario.questao_26 == '2': # 1 vez por semana
                            questao_26[2][0] += 1
                        elif aluno.questionario.questao_26 == '3': # 2 a 4 vezes por semana
                            questao_26[3][0] += 1
                        elif aluno.questionario.questao_26 == '4': # 6 a 8 vezes por semana
                            questao_26[4][0] += 1
                        elif aluno.questionario.questao_26 == '5': # 1 vez por dia
                            questao_26[5][0] += 1
                        elif aluno.questionario.questao_26 == '6': # 2 a 3 vezes por dia
                            questao_26[6][0] += 1
                        elif aluno.questionario.questao_26 == '7': # 4 a 6 vezes por dia
                            questao_26[7][0] += 1
                        elif aluno.questionario.questao_26 == '8': # Mais de 8 vezes por dia
                            questao_26[8][0] += 1
                        
                        # Questão 27
                        if aluno.questionario.questao_27 == '0': # Nunca ou menos de uma vez por mês
                            questao_27[0][0] += 1
                        elif aluno.questionario.questao_27 == '1': # 1 a 3 vezes por mês
                            questao_27[1][0] += 1
                        elif aluno.questionario.questao_27 == '2': # 1 vez por semana
                            questao_27[2][0] += 1
                        elif aluno.questionario.questao_27 == '3': # 2 a 4 vezes por semana
                            questao_27[3][0] += 1
                        elif aluno.questionario.questao_27 == '4': # 6 a 8 vezes por semana
                            questao_27[4][0] += 1
                        elif aluno.questionario.questao_27 == '5': # 1 vez por dia
                            questao_27[5][0] += 1
                        elif aluno.questionario.questao_27 == '6': # 2 a 3 vezes por dia
                            questao_27[6][0] += 1
                        elif aluno.questionario.questao_27 == '7': # 4 a 6 vezes por dia
                            questao_27[7][0] += 1
                        elif aluno.questionario.questao_27 == '8': # Mais de 8 vezes por dia
                            questao_27[8][0] += 1
                        
                        # Questão 28
                        if aluno.questionario.questao_28 == '0': # Nunca ou menos de uma vez por mês
                            questao_28[0][0] += 1
                        elif aluno.questionario.questao_28 == '1': # 1 a 3 vezes por mês
                            questao_28[1][0] += 1
                        elif aluno.questionario.questao_28 == '2': # 1 vez por semana
                            questao_28[2][0] += 1
                        elif aluno.questionario.questao_28 == '3': # 2 a 4 vezes por semana
                            questao_28[3][0] += 1
                        elif aluno.questionario.questao_28 == '4': # 6 a 8 vezes por semana
                            questao_28[4][0] += 1
                        elif aluno.questionario.questao_28 == '5': # 1 vez por dia
                            questao_28[5][0] += 1
                        elif aluno.questionario.questao_28 == '6': # 2 a 3 vezes por dia
                            questao_28[6][0] += 1
                        elif aluno.questionario.questao_28 == '7': # 4 a 6 vezes por dia
                            questao_28[7][0] += 1
                        elif aluno.questionario.questao_28 == '8': # Mais de 8 vezes por dia
                            questao_28[8][0] += 1
                        
                        # Questão 29
                        if aluno.questionario.questao_29 == '0': # Nunca ou menos de uma vez por mês
                            questao_29[0][0] += 1
                        elif aluno.questionario.questao_29 == '1': # 1 a 3 vezes por mês
                            questao_29[1][0] += 1
                        elif aluno.questionario.questao_29 == '2': # 1 vez por semana
                            questao_29[2][0] += 1
                        elif aluno.questionario.questao_29 == '3': # 2 a 4 vezes por semana
                            questao_29[3][0] += 1
                        elif aluno.questionario.questao_29 == '4': # 6 a 8 vezes por semana
                            questao_29[4][0] += 1
                        elif aluno.questionario.questao_29 == '5': # 1 vez por dia
                            questao_29[5][0] += 1
                        elif aluno.questionario.questao_29 == '6': # 2 a 3 vezes por dia
                            questao_29[6][0] += 1
                        elif aluno.questionario.questao_29 == '7': # 4 a 6 vezes por dia
                            questao_29[7][0] += 1
                        elif aluno.questionario.questao_29 == '8': # Mais de 8 vezes por dia
                            questao_29[8][0] += 1
                        
                        # Questão 30
                        if aluno.questionario.questao_30 == '0': # Nunca ou menos de uma vez por mês
                            questao_30[0][0] += 1
                        elif aluno.questionario.questao_30 == '1': # 1 a 3 vezes por mês
                            questao_30[1][0] += 1
                        elif aluno.questionario.questao_30 == '2': # 1 vez por semana
                            questao_30[2][0] += 1
                        elif aluno.questionario.questao_30 == '3': # 2 a 4 vezes por semana
                            questao_30[3][0] += 1
                        elif aluno.questionario.questao_30 == '4': # 6 a 8 vezes por semana
                            questao_30[4][0] += 1
                        elif aluno.questionario.questao_30 == '5': # 1 vez por dia
                            questao_30[5][0] += 1
                        elif aluno.questionario.questao_30 == '6': # 2 a 3 vezes por dia
                            questao_30[6][0] += 1
                        elif aluno.questionario.questao_30 == '7': # 4 a 6 vezes por dia
                            questao_30[7][0] += 1
                        elif aluno.questionario.questao_30 == '8': # Mais de 8 vezes por dia
                            questao_30[8][0] += 1
                        
                        # Questão 31
                        if aluno.questionario.questao_31 == '0': # Nunca ou menos de uma vez por mês
                            questao_31[0][0] += 1
                        elif aluno.questionario.questao_31 == '1': # 1 a 3 vezes por mês
                            questao_31[1][0] += 1
                        elif aluno.questionario.questao_31 == '2': # 1 vez por semana
                            questao_31[2][0] += 1
                        elif aluno.questionario.questao_31 == '3': # 2 a 4 vezes por semana
                            questao_31[3][0] += 1
                        elif aluno.questionario.questao_31 == '4': # 6 a 8 vezes por semana
                            questao_31[4][0] += 1
                        elif aluno.questionario.questao_31 == '5': # 1 vez por dia
                            questao_31[5][0] += 1
                        elif aluno.questionario.questao_31 == '6': # 2 a 3 vezes por dia
                            questao_31[6][0] += 1
                        elif aluno.questionario.questao_31 == '7': # 4 a 6 vezes por dia
                            questao_31[7][0] += 1
                        elif aluno.questionario.questao_31 == '8': # Mais de 8 vezes por dia
                            questao_31[8][0] += 1
                        
                        # Questão 32
                        if aluno.questionario.questao_32 == '0': # Nunca ou menos de uma vez por mês
                            questao_32[0][0] += 1
                        elif aluno.questionario.questao_32 == '1': # 1 a 3 vezes por mês
                            questao_32[1][0] += 1
                        elif aluno.questionario.questao_32 == '2': # 1 vez por semana
                            questao_32[2][0] += 1
                        elif aluno.questionario.questao_32 == '3': # 2 a 4 vezes por semana
                            questao_32[3][0] += 1
                        elif aluno.questionario.questao_32 == '4': # 6 a 8 vezes por semana
                            questao_32[4][0] += 1
                        elif aluno.questionario.questao_32 == '5': # 1 vez por dia
                            questao_32[5][0] += 1
                        elif aluno.questionario.questao_32 == '6': # 2 a 3 vezes por dia
                            questao_32[6][0] += 1
                        elif aluno.questionario.questao_32 == '7': # 4 a 6 vezes por dia
                            questao_32[7][0] += 1
                        elif aluno.questionario.questao_32 == '8': # Mais de 8 vezes por dia
                            questao_32[8][0] += 1
                        
                        # Questão 33
                        if aluno.questionario.questao_33 == '0': # Nunca ou menos de uma vez por mês
                            questao_33[0][0] += 1
                        elif aluno.questionario.questao_33 == '1': # 1 a 3 vezes por mês
                            questao_33[1][0] += 1
                        elif aluno.questionario.questao_33 == '2': # 1 vez por semana
                            questao_33[2][0] += 1
                        elif aluno.questionario.questao_33 == '3': # 2 a 4 vezes por semana
                            questao_33[3][0] += 1
                        elif aluno.questionario.questao_33 == '4': # 6 a 8 vezes por semana
                            questao_33[4][0] += 1
                        elif aluno.questionario.questao_33 == '5': # 1 vez por dia
                            questao_33[5][0] += 1
                        elif aluno.questionario.questao_33 == '6': # 2 a 3 vezes por dia
                            questao_33[6][0] += 1
                        elif aluno.questionario.questao_33 == '7': # 4 a 6 vezes por dia
                            questao_33[7][0] += 1
                        elif aluno.questionario.questao_33 == '8': # Mais de 8 vezes por dia
                            questao_33[8][0] += 1
                        
                        # Questão 34
                        if aluno.questionario.questao_34 == '0': # Nunca ou menos de uma vez por mês
                            questao_34[0][0] += 1
                        elif aluno.questionario.questao_34 == '1': # 1 a 3 vezes por mês
                            questao_34[1][0] += 1
                        elif aluno.questionario.questao_34 == '2': # 1 vez por semana
                            questao_34[2][0] += 1
                        elif aluno.questionario.questao_34 == '3': # 2 a 4 vezes por semana
                            questao_34[3][0] += 1
                        elif aluno.questionario.questao_34 == '4': # 6 a 8 vezes por semana
                            questao_34[4][0] += 1
                        elif aluno.questionario.questao_34 == '5': # 1 vez por dia
                            questao_34[5][0] += 1
                        elif aluno.questionario.questao_34 == '6': # 2 a 3 vezes por dia
                            questao_34[6][0] += 1
                        elif aluno.questionario.questao_34 == '7': # 4 a 6 vezes por dia
                            questao_34[7][0] += 1
                        elif aluno.questionario.questao_34 == '8': # Mais de 8 vezes por dia
                            questao_34[8][0] += 1
                        
                        # Questão 35
                        if aluno.questionario.questao_35 == '0': # Nunca ou menos de uma vez por mês
                            questao_35[0][0] += 1
                        elif aluno.questionario.questao_35 == '1': # 1 a 3 vezes por mês
                            questao_35[1][0] += 1
                        elif aluno.questionario.questao_35 == '2': # 1 vez por semana
                            questao_35[2][0] += 1
                        elif aluno.questionario.questao_35 == '3': # 2 a 4 vezes por semana
                            questao_35[3][0] += 1
                        elif aluno.questionario.questao_35 == '4': # 6 a 8 vezes por semana
                            questao_35[4][0] += 1
                        elif aluno.questionario.questao_35 == '5': # 1 vez por dia
                            questao_35[5][0] += 1
                        elif aluno.questionario.questao_35 == '6': # 2 a 3 vezes por dia
                            questao_35[6][0] += 1
                        elif aluno.questionario.questao_35 == '7': # 4 a 6 vezes por dia
                            questao_35[7][0] += 1
                        elif aluno.questionario.questao_35 == '8': # Mais de 8 vezes por dia
                            questao_35[8][0] += 1
                        
                        # Questão 36
                        if aluno.questionario.questao_36 == '0': # Nunca ou menos de uma vez por mês
                            questao_36[0][0] += 1
                        elif aluno.questionario.questao_36 == '1': # 1 a 3 vezes por mês
                            questao_36[1][0] += 1
                        elif aluno.questionario.questao_36 == '2': # 1 vez por semana
                            questao_36[2][0] += 1
                        elif aluno.questionario.questao_36 == '3': # 2 a 4 vezes por semana
                            questao_36[3][0] += 1
                        elif aluno.questionario.questao_36 == '4': # 6 a 8 vezes por semana
                            questao_36[4][0] += 1
                        elif aluno.questionario.questao_36 == '5': # 1 vez por dia
                            questao_36[5][0] += 1
                        elif aluno.questionario.questao_36 == '6': # 2 a 3 vezes por dia
                            questao_36[6][0] += 1
                        elif aluno.questionario.questao_36 == '7': # 4 a 6 vezes por dia
                            questao_36[7][0] += 1
                        elif aluno.questionario.questao_36 == '8': # Mais de 8 vezes por dia
                            questao_36[8][0] += 1
                        
                        # Questão 37
                        if aluno.questionario.questao_37 == '0': # Nunca ou menos de uma vez por mês
                            questao_37[0][0] += 1
                        elif aluno.questionario.questao_37 == '1': # 1 a 3 vezes por mês
                            questao_37[1][0] += 1
                        elif aluno.questionario.questao_37 == '2': # 1 vez por semana
                            questao_37[2][0] += 1
                        elif aluno.questionario.questao_37 == '3': # 2 a 4 vezes por semana
                            questao_37[3][0] += 1
                        elif aluno.questionario.questao_37 == '4': # 6 a 8 vezes por semana
                            questao_37[4][0] += 1
                        elif aluno.questionario.questao_37 == '5': # 1 vez por dia
                            questao_37[5][0] += 1
                        elif aluno.questionario.questao_37 == '6': # 2 a 3 vezes por dia
                            questao_37[6][0] += 1
                        elif aluno.questionario.questao_37 == '7': # 4 a 6 vezes por dia
                            questao_37[7][0] += 1
                        elif aluno.questionario.questao_37 == '8': # Mais de 8 vezes por dia
                            questao_37[8][0] += 1
                        
                        # Questão 38
                        if aluno.questionario.questao_38 == '0': # Nunca ou menos de uma vez por mês
                            questao_38[0][0] += 1
                        elif aluno.questionario.questao_38 == '1': # 1 a 3 vezes por mês
                            questao_38[1][0] += 1
                        elif aluno.questionario.questao_38 == '2': # 1 vez por semana
                            questao_38[2][0] += 1
                        elif aluno.questionario.questao_38 == '3': # 2 a 4 vezes por semana
                            questao_38[3][0] += 1
                        elif aluno.questionario.questao_38 == '4': # 6 a 8 vezes por semana
                            questao_38[4][0] += 1
                        elif aluno.questionario.questao_38 == '5': # 1 vez por dia
                            questao_38[5][0] += 1
                        elif aluno.questionario.questao_38 == '6': # 2 a 3 vezes por dia
                            questao_38[6][0] += 1
                        elif aluno.questionario.questao_38 == '7': # 4 a 6 vezes por dia
                            questao_38[7][0] += 1
                        elif aluno.questionario.questao_38 == '8': # Mais de 8 vezes por dia
                            questao_38[8][0] += 1
                        
                        # Questão 39
                        if aluno.questionario.questao_39 == '0': # Nunca ou menos de uma vez por mês
                            questao_39[0][0] += 1
                        elif aluno.questionario.questao_39 == '1': # 1 a 3 vezes por mês
                            questao_39[1][0] += 1
                        elif aluno.questionario.questao_39 == '2': # 1 vez por semana
                            questao_39[2][0] += 1
                        elif aluno.questionario.questao_39 == '3': # 2 a 4 vezes por semana
                            questao_39[3][0] += 1
                        elif aluno.questionario.questao_39 == '4': # 6 a 8 vezes por semana
                            questao_39[4][0] += 1
                        elif aluno.questionario.questao_39 == '5': # 1 vez por dia
                            questao_39[5][0] += 1
                        elif aluno.questionario.questao_39 == '6': # 2 a 3 vezes por dia
                            questao_39[6][0] += 1
                        elif aluno.questionario.questao_39 == '7': # 4 a 6 vezes por dia
                            questao_39[7][0] += 1
                        elif aluno.questionario.questao_39 == '8': # Mais de 8 vezes por dia
                            questao_39[8][0] += 1
                        
                        # Questão 40
                        if aluno.questionario.questao_40 == '0': # Nunca ou menos de uma vez por mês
                            questao_40[0][0] += 1
                        elif aluno.questionario.questao_40 == '1': # 1 a 3 vezes por mês
                            questao_40[1][0] += 1
                        elif aluno.questionario.questao_40 == '2': # 1 vez por semana
                            questao_40[2][0] += 1
                        elif aluno.questionario.questao_40 == '3': # 2 a 4 vezes por semana
                            questao_40[3][0] += 1
                        elif aluno.questionario.questao_40 == '4': # 6 a 8 vezes por semana
                            questao_40[4][0] += 1
                        elif aluno.questionario.questao_40 == '5': # 1 vez por dia
                            questao_40[5][0] += 1
                        elif aluno.questionario.questao_40 == '6': # 2 a 3 vezes por dia
                            questao_40[6][0] += 1
                        elif aluno.questionario.questao_40 == '7': # 4 a 6 vezes por dia
                            questao_40[7][0] += 1
                        elif aluno.questionario.questao_40 == '8': # Mais de 8 vezes por dia
                            questao_40[8][0] += 1
                        
                        # Questão 41
                        if aluno.questionario.questao_41 == '0': # Nunca ou menos de uma vez por mês
                            questao_41[0][0] += 1
                        elif aluno.questionario.questao_41 == '1': # 1 a 3 vezes por mês
                            questao_41[1][0] += 1
                        elif aluno.questionario.questao_41 == '2': # 1 vez por semana
                            questao_41[2][0] += 1
                        elif aluno.questionario.questao_41 == '3': # 2 a 4 vezes por semana
                            questao_41[3][0] += 1
                        elif aluno.questionario.questao_41 == '4': # 6 a 8 vezes por semana
                            questao_41[4][0] += 1
                        elif aluno.questionario.questao_41 == '5': # 1 vez por dia
                            questao_41[5][0] += 1
                        elif aluno.questionario.questao_41 == '6': # 2 a 3 vezes por dia
                            questao_41[6][0] += 1
                        elif aluno.questionario.questao_41 == '7': # 4 a 6 vezes por dia
                            questao_41[7][0] += 1
                        elif aluno.questionario.questao_41 == '8': # Mais de 8 vezes por dia
                            questao_41[8][0] += 1
                        
                        # Questão 42
                        if aluno.questionario.questao_42 == '0': # Nunca ou menos de uma vez por mês
                            questao_42[0][0] += 1
                        elif aluno.questionario.questao_42 == '1': # 1 a 3 vezes por mês
                            questao_42[1][0] += 1
                        elif aluno.questionario.questao_42 == '2': # 1 vez por semana
                            questao_42[2][0] += 1
                        elif aluno.questionario.questao_42 == '3': # 2 a 4 vezes por semana
                            questao_42[3][0] += 1
                        elif aluno.questionario.questao_42 == '4': # 6 a 8 vezes por semana
                            questao_42[4][0] += 1
                        elif aluno.questionario.questao_42 == '5': # 1 vez por dia
                            questao_42[5][0] += 1
                        elif aluno.questionario.questao_42 == '6': # 2 a 3 vezes por dia
                            questao_42[6][0] += 1
                        elif aluno.questionario.questao_42 == '7': # 4 a 6 vezes por dia
                            questao_42[7][0] += 1
                        elif aluno.questionario.questao_42 == '8': # Mais de 8 vezes por dia
                            questao_42[8][0] += 1
                        
                        # Questão 43
                        if aluno.questionario.questao_43 == '0': # Nunca ou menos de uma vez por mês
                            questao_43[0][0] += 1
                        elif aluno.questionario.questao_43 == '1': # 1 a 3 vezes por mês
                            questao_43[1][0] += 1
                        elif aluno.questionario.questao_43 == '2': # 1 vez por semana
                            questao_43[2][0] += 1
                        elif aluno.questionario.questao_43 == '3': # 2 a 4 vezes por semana
                            questao_43[3][0] += 1
                        elif aluno.questionario.questao_43 == '4': # 6 a 8 vezes por semana
                            questao_43[4][0] += 1
                        elif aluno.questionario.questao_43 == '5': # 1 vez por dia
                            questao_43[5][0] += 1
                        elif aluno.questionario.questao_43 == '6': # 2 a 3 vezes por dia
                            questao_43[6][0] += 1
                        elif aluno.questionario.questao_43 == '7': # 4 a 6 vezes por dia
                            questao_43[7][0] += 1
                        elif aluno.questionario.questao_43 == '8': # Mais de 8 vezes por dia
                            questao_43[8][0] += 1
                        
                        # Questão 44
                        if aluno.questionario.questao_44 == '0': # Nunca ou menos de uma vez por mês
                            questao_44[0][0] += 1
                        elif aluno.questionario.questao_44 == '1': # 1 a 3 vezes por mês
                            questao_44[1][0] += 1
                        elif aluno.questionario.questao_44 == '2': # 1 vez por semana
                            questao_44[2][0] += 1
                        elif aluno.questionario.questao_44 == '3': # 2 a 4 vezes por semana
                            questao_44[3][0] += 1
                        elif aluno.questionario.questao_44 == '4': # 6 a 8 vezes por semana
                            questao_44[4][0] += 1
                        elif aluno.questionario.questao_44 == '5': # 1 vez por dia
                            questao_44[5][0] += 1
                        elif aluno.questionario.questao_44 == '6': # 2 a 3 vezes por dia
                            questao_44[6][0] += 1
                        elif aluno.questionario.questao_44 == '7': # 4 a 6 vezes por dia
                            questao_44[7][0] += 1
                        elif aluno.questionario.questao_44 == '8': # Mais de 8 vezes por dia
                            questao_44[8][0] += 1
                        
                        # Questão 45
                        if aluno.questionario.questao_45 == '0': # Nunca ou menos de uma vez por mês
                            questao_45[0][0] += 1
                        elif aluno.questionario.questao_45 == '1': # 1 a 3 vezes por mês
                            questao_45[1][0] += 1
                        elif aluno.questionario.questao_45 == '2': # 1 vez por semana
                            questao_45[2][0] += 1
                        elif aluno.questionario.questao_45 == '3': # 2 a 4 vezes por semana
                            questao_45[3][0] += 1
                        elif aluno.questionario.questao_45 == '4': # 6 a 8 vezes por semana
                            questao_45[4][0] += 1
                        elif aluno.questionario.questao_45 == '5': # 1 vez por dia
                            questao_45[5][0] += 1
                        elif aluno.questionario.questao_45 == '6': # 2 a 3 vezes por dia
                            questao_45[6][0] += 1
                        elif aluno.questionario.questao_45 == '7': # 4 a 6 vezes por dia
                            questao_45[7][0] += 1
                        elif aluno.questionario.questao_45 == '8': # Mais de 8 vezes por dia
                            questao_45[8][0] += 1
                        
                        # Questão 46
                        if aluno.questionario.questao_46 == '0': # Nunca ou menos de uma vez por mês
                            questao_46[0][0] += 1
                        elif aluno.questionario.questao_46 == '1': # 1 a 3 vezes por mês
                            questao_46[1][0] += 1
                        elif aluno.questionario.questao_46 == '2': # 1 vez por semana
                            questao_46[2][0] += 1
                        elif aluno.questionario.questao_46 == '3': # 2 a 4 vezes por semana
                            questao_46[3][0] += 1
                        elif aluno.questionario.questao_46 == '4': # 6 a 8 vezes por semana
                            questao_46[4][0] += 1
                        elif aluno.questionario.questao_46 == '5': # 1 vez por dia
                            questao_46[5][0] += 1
                        elif aluno.questionario.questao_46 == '6': # 2 a 3 vezes por dia
                            questao_46[6][0] += 1
                        elif aluno.questionario.questao_46 == '7': # 4 a 6 vezes por dia
                            questao_46[7][0] += 1
                        elif aluno.questionario.questao_46 == '8': # Mais de 8 vezes por dia
                            questao_46[8][0] += 1
                        
                        # Questão 47
                        if aluno.questionario.questao_47 == '0': # Nunca ou menos de uma vez por mês
                            questao_47[0][0] += 1
                        elif aluno.questionario.questao_47 == '1': # 1 a 3 vezes por mês
                            questao_47[1][0] += 1
                        elif aluno.questionario.questao_47 == '2': # 1 vez por semana
                            questao_47[2][0] += 1
                        elif aluno.questionario.questao_47 == '3': # 2 a 4 vezes por semana
                            questao_47[3][0] += 1
                        elif aluno.questionario.questao_47 == '4': # 6 a 8 vezes por semana
                            questao_47[4][0] += 1
                        elif aluno.questionario.questao_47 == '5': # 1 vez por dia
                            questao_47[5][0] += 1
                        elif aluno.questionario.questao_47 == '6': # 2 a 3 vezes por dia
                            questao_47[6][0] += 1
                        elif aluno.questionario.questao_47 == '7': # 4 a 6 vezes por dia
                            questao_47[7][0] += 1
                        elif aluno.questionario.questao_47 == '8': # Mais de 8 vezes por dia
                            questao_47[8][0] += 1
                        
                        # Questão 48
                        if aluno.questionario.questao_48 == '0': # Nunca ou menos de uma vez por mês
                            questao_48[0][0] += 1
                        elif aluno.questionario.questao_48 == '1': # 1 a 3 vezes por mês
                            questao_48[1][0] += 1
                        elif aluno.questionario.questao_48 == '2': # 1 vez por semana
                            questao_48[2][0] += 1
                        elif aluno.questionario.questao_48 == '3': # 2 a 4 vezes por semana
                            questao_48[3][0] += 1
                        elif aluno.questionario.questao_48 == '4': # 6 a 8 vezes por semana
                            questao_48[4][0] += 1
                        elif aluno.questionario.questao_48 == '5': # 1 vez por dia
                            questao_48[5][0] += 1
                        elif aluno.questionario.questao_48 == '6': # 2 a 3 vezes por dia
                            questao_48[6][0] += 1
                        elif aluno.questionario.questao_48 == '7': # 4 a 6 vezes por dia
                            questao_48[7][0] += 1
                        elif aluno.questionario.questao_48 == '8': # Mais de 8 vezes por dia
                            questao_48[8][0] += 1
                        
                        # Questão 49
                        if aluno.questionario.questao_49 == '0': # Nunca ou menos de uma vez por mês
                            questao_49[0][0] += 1
                        elif aluno.questionario.questao_49 == '1': # 1 a 3 vezes por mês
                            questao_49[1][0] += 1
                        elif aluno.questionario.questao_49 == '2': # 1 vez por semana
                            questao_49[2][0] += 1
                        elif aluno.questionario.questao_49 == '3': # 2 a 4 vezes por semana
                            questao_49[3][0] += 1
                        elif aluno.questionario.questao_49 == '4': # 6 a 8 vezes por semana
                            questao_49[4][0] += 1
                        elif aluno.questionario.questao_49 == '5': # 1 vez por dia
                            questao_49[5][0] += 1
                        elif aluno.questionario.questao_49 == '6': # 2 a 3 vezes por dia
                            questao_49[6][0] += 1
                        elif aluno.questionario.questao_49 == '7': # 4 a 6 vezes por dia
                            questao_49[7][0] += 1
                        elif aluno.questionario.questao_49 == '8': # Mais de 8 vezes por dia
                            questao_49[8][0] += 1
                        
                        # Questão 50
                        if aluno.questionario.questao_50 == '0': # Nunca ou menos de uma vez por mês
                            questao_50[0][0] += 1
                        elif aluno.questionario.questao_50 == '1': # 1 a 3 vezes por mês
                            questao_50[1][0] += 1
                        elif aluno.questionario.questao_50 == '2': # 1 vez por semana
                            questao_50[2][0] += 1
                        elif aluno.questionario.questao_50 == '3': # 2 a 4 vezes por semana
                            questao_50[3][0] += 1
                        elif aluno.questionario.questao_50 == '4': # 6 a 8 vezes por semana
                            questao_50[4][0] += 1
                        elif aluno.questionario.questao_50 == '5': # 1 vez por dia
                            questao_50[5][0] += 1
                        elif aluno.questionario.questao_50 == '6': # 2 a 3 vezes por dia
                            questao_50[6][0] += 1
                        elif aluno.questionario.questao_50 == '7': # 4 a 6 vezes por dia
                            questao_50[7][0] += 1
                        elif aluno.questionario.questao_50 == '8': # Mais de 8 vezes por dia
                            questao_50[8][0] += 1
                        
                        # Questão 51
                        if aluno.questionario.questao_51 == '0': # Nunca ou menos de uma vez por mês
                            questao_51[0][0] += 1
                        elif aluno.questionario.questao_51 == '1': # 1 a 3 vezes por mês
                            questao_51[1][0] += 1
                        elif aluno.questionario.questao_51 == '2': # 1 vez por semana
                            questao_51[2][0] += 1
                        elif aluno.questionario.questao_51 == '3': # 2 a 4 vezes por semana
                            questao_51[3][0] += 1
                        elif aluno.questionario.questao_51 == '4': # 6 a 8 vezes por semana
                            questao_51[4][0] += 1
                        elif aluno.questionario.questao_51 == '5': # 1 vez por dia
                            questao_51[5][0] += 1
                        elif aluno.questionario.questao_51 == '6': # 2 a 3 vezes por dia
                            questao_51[6][0] += 1
                        elif aluno.questionario.questao_51 == '7': # 4 a 6 vezes por dia
                            questao_51[7][0] += 1
                        elif aluno.questionario.questao_51 == '8': # Mais de 8 vezes por dia
                            questao_51[8][0] += 1
                        
                        # Questão 52
                        if aluno.questionario.questao_52 == '0': # Nunca ou menos de uma vez por mês
                            questao_52[0][0] += 1
                        elif aluno.questionario.questao_52 == '1': # 1 a 3 vezes por mês
                            questao_52[1][0] += 1
                        elif aluno.questionario.questao_52 == '2': # 1 vez por semana
                            questao_52[2][0] += 1
                        elif aluno.questionario.questao_52 == '3': # 2 a 4 vezes por semana
                            questao_52[3][0] += 1
                        elif aluno.questionario.questao_52 == '4': # 6 a 8 vezes por semana
                            questao_52[4][0] += 1
                        elif aluno.questionario.questao_52 == '5': # 1 vez por dia
                            questao_52[5][0] += 1
                        elif aluno.questionario.questao_52 == '6': # 2 a 3 vezes por dia
                            questao_52[6][0] += 1
                        elif aluno.questionario.questao_52 == '7': # 4 a 6 vezes por dia
                            questao_52[7][0] += 1
                        elif aluno.questionario.questao_52 == '8': # Mais de 8 vezes por dia
                            questao_52[8][0] += 1
                        
                        # Questão 53
                        if aluno.questionario.questao_53 == '0': # Nunca ou menos de uma vez por mês
                            questao_53[0][0] += 1
                        elif aluno.questionario.questao_53 == '1': # 1 a 3 vezes por mês
                            questao_53[1][0] += 1
                        elif aluno.questionario.questao_53 == '2': # 1 vez por semana
                            questao_53[2][0] += 1
                        elif aluno.questionario.questao_53 == '3': # 2 a 4 vezes por semana
                            questao_53[3][0] += 1
                        elif aluno.questionario.questao_53 == '4': # 6 a 8 vezes por semana
                            questao_53[4][0] += 1
                        elif aluno.questionario.questao_53 == '5': # 1 vez por dia
                            questao_53[5][0] += 1
                        elif aluno.questionario.questao_53 == '6': # 2 a 3 vezes por dia
                            questao_53[6][0] += 1
                        elif aluno.questionario.questao_53 == '7': # 4 a 6 vezes por dia
                            questao_53[7][0] += 1
                        elif aluno.questionario.questao_53 == '8': # Mais de 8 vezes por dia
                            questao_53[8][0] += 1
                        
                        # Questão 54
                        if aluno.questionario.questao_54 == '0': # Nunca ou menos de uma vez por mês
                            questao_54[0][0] += 1
                        elif aluno.questionario.questao_54 == '1': # 1 a 3 vezes por mês
                            questao_54[1][0] += 1
                        elif aluno.questionario.questao_54 == '2': # 1 vez por semana
                            questao_54[2][0] += 1
                        elif aluno.questionario.questao_54 == '3': # 2 a 4 vezes por semana
                            questao_54[3][0] += 1
                        elif aluno.questionario.questao_54 == '4': # 6 a 8 vezes por semana
                            questao_54[4][0] += 1
                        elif aluno.questionario.questao_54 == '5': # 1 vez por dia
                            questao_54[5][0] += 1
                        elif aluno.questionario.questao_54 == '6': # 2 a 3 vezes por dia
                            questao_54[6][0] += 1
                        elif aluno.questionario.questao_54 == '7': # 4 a 6 vezes por dia
                            questao_54[7][0] += 1
                        elif aluno.questionario.questao_54 == '8': # Mais de 8 vezes por dia
                            questao_54[8][0] += 1
                else:
                    # Sexo
                    if aluno.sexo == '0': # masculino
                        sexo[0][1] += 1
                    elif aluno.sexo == '1': # feminino
                        sexo[1][1] += 1
                    elif aluno.sexo == '2': # outro
                        sexo[2][1] += 1
                    
                    # Raça
                    if aluno.raca == '0': # amarela
                        raca[0][1] += 1
                    elif aluno.raca == '1': # branca
                        raca[1][1] += 1
                    elif aluno.raca == '2': # indigena
                        raca[2][1] += 1
                    elif aluno.raca == '3': # parda
                        raca[3][1] += 1
                    elif aluno.raca == '4': # preta
                        raca[4][1] += 1
                    
                    try:
                        questionario = aluno.questionario
                    except Questionario.DoesNotExist:
                        pass
                    else:
                        # Questão 73
                        if aluno.questionario.questao_73 == '0': # Sim
                            questao_73[0][1] += 1
                        elif aluno.questionario.questao_73 == '1': # Não
                            questao_73[1][1] += 1
                        
                        # Questão 75
                        if aluno.questionario.questao_75 == '0': # Nenhum dia nos últimos 30 dias (0 dia)
                            questao_75[0][1] += 1
                        elif aluno.questionario.questao_75 == '1': # 1 ou 2 dias nos últimos 30 dias
                            questao_75[1][1] += 1
                        elif aluno.questionario.questao_75 == '2': # 3 a 5 dias nos últimos 30 dias
                            questao_75[2][1] += 1
                        elif aluno.questionario.questao_75 == '3': # 6 a 9 dias nos últimos 30 dias
                            questao_75[3][1] += 1
                        elif aluno.questionario.questao_75 == '4': # 10 a 19 dias nos últimos 30 dias
                            questao_75[4][1] += 1
                        elif aluno.questionario.questao_75 == '5': # 20 a 29 dias nos últimos 30 dias
                            questao_75[5][1] += 1
                        elif aluno.questionario.questao_75 == '6': # Todos os dias nos últimos 30 dias
                            questao_75[6][1] += 1
                        
                        # Questão 79
                        if aluno.questionario.questao_79 == '0': # Não usei nenhum produto do tabaco (os produtos do tabaco estão abaixo relacionados)
                            questao_79[0][1] += 1
                        elif aluno.questionario.questao_79 == '1': # Cigarros de cravo (conhecidos como cigarros de Bali).
                            questao_79[1][1] += 1
                        elif aluno.questionario.questao_79 == '2': # Cigarros enrolados à mão (conhecidos como cigarros de palha ou papel)
                            questao_79[2][1] += 1
                        elif aluno.questionario.questao_79 == '3': # Cigarrilhas
                            questao_79[3][1] += 1
                        elif aluno.questionario.questao_79 == '4': # Charutos, charutos pequenos.
                            questao_79[4][1] += 1
                        elif aluno.questionario.questao_79 == '5': # Fumo para mascar
                            questao_79[5][1] += 1
                        elif aluno.questionario.questao_79 == '6': # Narguilé (cachimbo de água)
                            questao_79[6][1] += 1
                        elif aluno.questionario.questao_79 == '7': # Cigarros indianos (bidis)
                            questao_79[7][1] += 1
                        elif aluno.questionario.questao_79 == '8': # Cigarro eletrônico (e-cigarette)
                            questao_79[8][1] += 1
                        elif aluno.questionario.questao_79 == '9': # Outros
                            questao_79[9][1] += 1
                        
                        # Questao_84
                        if aluno.questionario.questao_84 == '0': # Nenhum dia nos últimos 30 dias (0 dia)
                            questao_84[0][1] += 1
                        elif aluno.questionario.questao_84 == '1': # 1 ou 2 dias nos últimos 30 dias
                            questao_84[1][1] += 1
                        elif aluno.questionario.questao_84 == '2': # 3 a 5 dias nos últimos 30 dias
                            questao_84[2][1] += 1
                        elif aluno.questionario.questao_84 == '3': # 6 a 9 dias nos últimos 30 dias
                            questao_84[3][1] += 1
                        elif aluno.questionario.questao_84 == '4': # 10 a 19 dias nos últimos 30 dias
                            questao_84[4][1] += 1
                        elif aluno.questionario.questao_84 == '5': # 20 a 29 dias nos últimos 30 dias
                            questao_84[5][1] += 1
                        elif aluno.questionario.questao_84 == '6': # Todos os dias nos últimos 30 dias
                            questao_84[6][1] += 1
                        
                        # Questao_92
                        if aluno.questionario.questao_92 == '0': # Nenhum dia nos últimos 30 dias (0 dia)
                            questao_92[0][1] += 1
                        elif aluno.questionario.questao_92 == '1': # 1 ou 2 dias nos últimos 30 dias
                            questao_92[1][1] += 1
                        elif aluno.questionario.questao_92 == '2': # 3 a 5 dias nos últimos 30 dias
                            questao_92[2][1] += 1
                        elif aluno.questionario.questao_92 == '3': # 6 a 9 dias nos últimos 30 dias
                            questao_92[3][1] += 1
                        elif aluno.questionario.questao_92 == '4': # 10 ou mais dias nos últimos 30 dias
                            questao_92[4][1] += 1
                        
                        # Questao_111
                        if aluno.questionario.questao_111 == '0': # Não escovei meus dentes nos últimos 30 dias
                            questao_111[0][1] += 1
                        elif aluno.questionario.questao_111 == '1': # Não escovei meus dentes diariamente
                            questao_111[1][1] += 1
                        elif aluno.questionario.questao_111 == '2': # 1 vez por dia nos últimos 30 dias
                            questao_111[2][1] += 1
                        elif aluno.questionario.questao_111 == '3': # 2 vezes por dia nos últimos 30 dias
                            questao_111[3][1] += 1
                        elif aluno.questionario.questao_111 == '4': # 3 vezes por dia nos últimos 30 dias
                            questao_111[4][1] += 1
                        elif aluno.questionario.questao_111 == '5': # 4 ou mais vezes por dia nos últimos 30 dias
                            questao_111[5][1] += 1
                        
                        # Questao_113
                        if aluno.questionario.questao_113 == '0': # Nenhuma vez nos últimos 12 meses (0 vez)
                            questao_113[0][1] += 1
                        elif aluno.questionario.questao_113 == '1': # 1 vez nos últimos 12 meses
                            questao_113[1][1] += 1
                        elif aluno.questionario.questao_113 == '2': # 2 vezes nos últimos 12 meses
                            questao_113[2][1] += 1
                        elif aluno.questionario.questao_113 == '3': # 3 ou mais vezes nos últimos 12 meses
                            questao_113[3][1] += 1
                        
                        # Questão 25
                        if aluno.questionario.questao_25 == '0': # Nunca ou menos de uma vez por mês
                            questao_25[0][1] += 1
                        elif aluno.questionario.questao_25 == '1': # 1 a 3 vezes por mês
                            questao_25[1][1] += 1
                        elif aluno.questionario.questao_25 == '2': # 1 vez por semana
                            questao_25[2][1] += 1
                        elif aluno.questionario.questao_25 == '3': # 2 a 4 vezes por semana
                            questao_25[3][1] += 1
                        elif aluno.questionario.questao_25 == '4': # 6 a 8 vezes por semana
                            questao_25[4][1] += 1
                        elif aluno.questionario.questao_25 == '5': # 1 vez por dia
                            questao_25[5][1] += 1
                        elif aluno.questionario.questao_25 == '6': # 2 a 3 vezes por dia
                            questao_25[6][1] += 1
                        elif aluno.questionario.questao_25 == '7': # 4 a 6 vezes por dia
                            questao_25[7][1] += 1
                        elif aluno.questionario.questao_25 == '8': # Mais de 8 vezes por dia
                            questao_25[8][1] += 1
                        
                        # Questão 26
                        if aluno.questionario.questao_26 == '0': # Nunca ou menos de uma vez por mês
                            questao_26[0][1] += 1
                        elif aluno.questionario.questao_26 == '1': # 1 a 3 vezes por mês
                            questao_26[1][1] += 1
                        elif aluno.questionario.questao_26 == '2': # 1 vez por semana
                            questao_26[2][1] += 1
                        elif aluno.questionario.questao_26 == '3': # 2 a 4 vezes por semana
                            questao_26[3][1] += 1
                        elif aluno.questionario.questao_26 == '4': # 6 a 8 vezes por semana
                            questao_26[4][1] += 1
                        elif aluno.questionario.questao_26 == '5': # 1 vez por dia
                            questao_26[5][1] += 1
                        elif aluno.questionario.questao_26 == '6': # 2 a 3 vezes por dia
                            questao_26[6][1] += 1
                        elif aluno.questionario.questao_26 == '7': # 4 a 6 vezes por dia
                            questao_26[7][1] += 1
                        elif aluno.questionario.questao_26 == '8': # Mais de 8 vezes por dia
                            questao_26[8][1] += 1
                        
                        # Questão 27
                        if aluno.questionario.questao_27 == '0': # Nunca ou menos de uma vez por mês
                            questao_27[0][1] += 1
                        elif aluno.questionario.questao_27 == '1': # 1 a 3 vezes por mês
                            questao_27[1][1] += 1
                        elif aluno.questionario.questao_27 == '2': # 1 vez por semana
                            questao_27[2][1] += 1
                        elif aluno.questionario.questao_27 == '3': # 2 a 4 vezes por semana
                            questao_27[3][1] += 1
                        elif aluno.questionario.questao_27 == '4': # 6 a 8 vezes por semana
                            questao_27[4][1] += 1
                        elif aluno.questionario.questao_27 == '5': # 1 vez por dia
                            questao_27[5][1] += 1
                        elif aluno.questionario.questao_27 == '6': # 2 a 3 vezes por dia
                            questao_27[6][1] += 1
                        elif aluno.questionario.questao_27 == '7': # 4 a 6 vezes por dia
                            questao_27[7][1] += 1
                        elif aluno.questionario.questao_27 == '8': # Mais de 8 vezes por dia
                            questao_27[8][1] += 1
                        
                        # Questão 28
                        if aluno.questionario.questao_28 == '0': # Nunca ou menos de uma vez por mês
                            questao_28[0][1] += 1
                        elif aluno.questionario.questao_28 == '1': # 1 a 3 vezes por mês
                            questao_28[1][1] += 1
                        elif aluno.questionario.questao_28 == '2': # 1 vez por semana
                            questao_28[2][1] += 1
                        elif aluno.questionario.questao_28 == '3': # 2 a 4 vezes por semana
                            questao_28[3][1] += 1
                        elif aluno.questionario.questao_28 == '4': # 6 a 8 vezes por semana
                            questao_28[4][1] += 1
                        elif aluno.questionario.questao_28 == '5': # 1 vez por dia
                            questao_28[5][1] += 1
                        elif aluno.questionario.questao_28 == '6': # 2 a 3 vezes por dia
                            questao_28[6][1] += 1
                        elif aluno.questionario.questao_28 == '7': # 4 a 6 vezes por dia
                            questao_28[7][1] += 1
                        elif aluno.questionario.questao_28 == '8': # Mais de 8 vezes por dia
                            questao_28[8][1] += 1
                        
                        # Questão 29
                        if aluno.questionario.questao_29 == '0': # Nunca ou menos de uma vez por mês
                            questao_29[0][1] += 1
                        elif aluno.questionario.questao_29 == '1': # 1 a 3 vezes por mês
                            questao_29[1][1] += 1
                        elif aluno.questionario.questao_29 == '2': # 1 vez por semana
                            questao_29[2][1] += 1
                        elif aluno.questionario.questao_29 == '3': # 2 a 4 vezes por semana
                            questao_29[3][1] += 1
                        elif aluno.questionario.questao_29 == '4': # 6 a 8 vezes por semana
                            questao_29[4][1] += 1
                        elif aluno.questionario.questao_29 == '5': # 1 vez por dia
                            questao_29[5][1] += 1
                        elif aluno.questionario.questao_29 == '6': # 2 a 3 vezes por dia
                            questao_29[6][1] += 1
                        elif aluno.questionario.questao_29 == '7': # 4 a 6 vezes por dia
                            questao_29[7][1] += 1
                        elif aluno.questionario.questao_29 == '8': # Mais de 8 vezes por dia
                            questao_29[8][1] += 1
                        
                        # Questão 30
                        if aluno.questionario.questao_30 == '0': # Nunca ou menos de uma vez por mês
                            questao_30[0][1] += 1
                        elif aluno.questionario.questao_30 == '1': # 1 a 3 vezes por mês
                            questao_30[1][1] += 1
                        elif aluno.questionario.questao_30 == '2': # 1 vez por semana
                            questao_30[2][1] += 1
                        elif aluno.questionario.questao_30 == '3': # 2 a 4 vezes por semana
                            questao_30[3][1] += 1
                        elif aluno.questionario.questao_30 == '4': # 6 a 8 vezes por semana
                            questao_30[4][1] += 1
                        elif aluno.questionario.questao_30 == '5': # 1 vez por dia
                            questao_30[5][1] += 1
                        elif aluno.questionario.questao_30 == '6': # 2 a 3 vezes por dia
                            questao_30[6][1] += 1
                        elif aluno.questionario.questao_30 == '7': # 4 a 6 vezes por dia
                            questao_30[7][1] += 1
                        elif aluno.questionario.questao_30 == '8': # Mais de 8 vezes por dia
                            questao_30[8][1] += 1
                        
                        # Questão 31
                        if aluno.questionario.questao_31 == '0': # Nunca ou menos de uma vez por mês
                            questao_31[0][1] += 1
                        elif aluno.questionario.questao_31 == '1': # 1 a 3 vezes por mês
                            questao_31[1][1] += 1
                        elif aluno.questionario.questao_31 == '2': # 1 vez por semana
                            questao_31[2][1] += 1
                        elif aluno.questionario.questao_31 == '3': # 2 a 4 vezes por semana
                            questao_31[3][1] += 1
                        elif aluno.questionario.questao_31 == '4': # 6 a 8 vezes por semana
                            questao_31[4][1] += 1
                        elif aluno.questionario.questao_31 == '5': # 1 vez por dia
                            questao_31[5][1] += 1
                        elif aluno.questionario.questao_31 == '6': # 2 a 3 vezes por dia
                            questao_31[6][1] += 1
                        elif aluno.questionario.questao_31 == '7': # 4 a 6 vezes por dia
                            questao_31[7][1] += 1
                        elif aluno.questionario.questao_31 == '8': # Mais de 8 vezes por dia
                            questao_31[8][1] += 1
                        
                        # Questão 32
                        if aluno.questionario.questao_32 == '0': # Nunca ou menos de uma vez por mês
                            questao_32[0][1] += 1
                        elif aluno.questionario.questao_32 == '1': # 1 a 3 vezes por mês
                            questao_32[1][1] += 1
                        elif aluno.questionario.questao_32 == '2': # 1 vez por semana
                            questao_32[2][1] += 1
                        elif aluno.questionario.questao_32 == '3': # 2 a 4 vezes por semana
                            questao_32[3][1] += 1
                        elif aluno.questionario.questao_32 == '4': # 6 a 8 vezes por semana
                            questao_32[4][1] += 1
                        elif aluno.questionario.questao_32 == '5': # 1 vez por dia
                            questao_32[5][1] += 1
                        elif aluno.questionario.questao_32 == '6': # 2 a 3 vezes por dia
                            questao_32[6][1] += 1
                        elif aluno.questionario.questao_32 == '7': # 4 a 6 vezes por dia
                            questao_32[7][1] += 1
                        elif aluno.questionario.questao_32 == '8': # Mais de 8 vezes por dia
                            questao_32[8][1] += 1
                        
                        # Questão 33
                        if aluno.questionario.questao_33 == '0': # Nunca ou menos de uma vez por mês
                            questao_33[0][1] += 1
                        elif aluno.questionario.questao_33 == '1': # 1 a 3 vezes por mês
                            questao_33[1][1] += 1
                        elif aluno.questionario.questao_33 == '2': # 1 vez por semana
                            questao_33[2][1] += 1
                        elif aluno.questionario.questao_33 == '3': # 2 a 4 vezes por semana
                            questao_33[3][1] += 1
                        elif aluno.questionario.questao_33 == '4': # 6 a 8 vezes por semana
                            questao_33[4][1] += 1
                        elif aluno.questionario.questao_33 == '5': # 1 vez por dia
                            questao_33[5][1] += 1
                        elif aluno.questionario.questao_33 == '6': # 2 a 3 vezes por dia
                            questao_33[6][1] += 1
                        elif aluno.questionario.questao_33 == '7': # 4 a 6 vezes por dia
                            questao_33[7][1] += 1
                        elif aluno.questionario.questao_33 == '8': # Mais de 8 vezes por dia
                            questao_33[8][1] += 1
                        
                        # Questão 34
                        if aluno.questionario.questao_34 == '0': # Nunca ou menos de uma vez por mês
                            questao_34[0][1] += 1
                        elif aluno.questionario.questao_34 == '1': # 1 a 3 vezes por mês
                            questao_34[1][1] += 1
                        elif aluno.questionario.questao_34 == '2': # 1 vez por semana
                            questao_34[2][1] += 1
                        elif aluno.questionario.questao_34 == '3': # 2 a 4 vezes por semana
                            questao_34[3][1] += 1
                        elif aluno.questionario.questao_34 == '4': # 6 a 8 vezes por semana
                            questao_34[4][1] += 1
                        elif aluno.questionario.questao_34 == '5': # 1 vez por dia
                            questao_34[5][1] += 1
                        elif aluno.questionario.questao_34 == '6': # 2 a 3 vezes por dia
                            questao_34[6][1] += 1
                        elif aluno.questionario.questao_34 == '7': # 4 a 6 vezes por dia
                            questao_34[7][1] += 1
                        elif aluno.questionario.questao_34 == '8': # Mais de 8 vezes por dia
                            questao_34[8][1] += 1
                        
                        # Questão 35
                        if aluno.questionario.questao_35 == '0': # Nunca ou menos de uma vez por mês
                            questao_35[0][1] += 1
                        elif aluno.questionario.questao_35 == '1': # 1 a 3 vezes por mês
                            questao_35[1][1] += 1
                        elif aluno.questionario.questao_35 == '2': # 1 vez por semana
                            questao_35[2][1] += 1
                        elif aluno.questionario.questao_35 == '3': # 2 a 4 vezes por semana
                            questao_35[3][1] += 1
                        elif aluno.questionario.questao_35 == '4': # 6 a 8 vezes por semana
                            questao_35[4][1] += 1
                        elif aluno.questionario.questao_35 == '5': # 1 vez por dia
                            questao_35[5][1] += 1
                        elif aluno.questionario.questao_35 == '6': # 2 a 3 vezes por dia
                            questao_35[6][1] += 1
                        elif aluno.questionario.questao_35 == '7': # 4 a 6 vezes por dia
                            questao_35[7][1] += 1
                        elif aluno.questionario.questao_35 == '8': # Mais de 8 vezes por dia
                            questao_35[8][1] += 1
                        
                        # Questão 36
                        if aluno.questionario.questao_36 == '0': # Nunca ou menos de uma vez por mês
                            questao_36[0][1] += 1
                        elif aluno.questionario.questao_36 == '1': # 1 a 3 vezes por mês
                            questao_36[1][1] += 1
                        elif aluno.questionario.questao_36 == '2': # 1 vez por semana
                            questao_36[2][1] += 1
                        elif aluno.questionario.questao_36 == '3': # 2 a 4 vezes por semana
                            questao_36[3][1] += 1
                        elif aluno.questionario.questao_36 == '4': # 6 a 8 vezes por semana
                            questao_36[4][1] += 1
                        elif aluno.questionario.questao_36 == '5': # 1 vez por dia
                            questao_36[5][1] += 1
                        elif aluno.questionario.questao_36 == '6': # 2 a 3 vezes por dia
                            questao_36[6][1] += 1
                        elif aluno.questionario.questao_36 == '7': # 4 a 6 vezes por dia
                            questao_36[7][1] += 1
                        elif aluno.questionario.questao_36 == '8': # Mais de 8 vezes por dia
                            questao_36[8][1] += 1
                        
                        # Questão 37
                        if aluno.questionario.questao_37 == '0': # Nunca ou menos de uma vez por mês
                            questao_37[0][1] += 1
                        elif aluno.questionario.questao_37 == '1': # 1 a 3 vezes por mês
                            questao_37[1][1] += 1
                        elif aluno.questionario.questao_37 == '2': # 1 vez por semana
                            questao_37[2][1] += 1
                        elif aluno.questionario.questao_37 == '3': # 2 a 4 vezes por semana
                            questao_37[3][1] += 1
                        elif aluno.questionario.questao_37 == '4': # 6 a 8 vezes por semana
                            questao_37[4][1] += 1
                        elif aluno.questionario.questao_37 == '5': # 1 vez por dia
                            questao_37[5][1] += 1
                        elif aluno.questionario.questao_37 == '6': # 2 a 3 vezes por dia
                            questao_37[6][1] += 1
                        elif aluno.questionario.questao_37 == '7': # 4 a 6 vezes por dia
                            questao_37[7][1] += 1
                        elif aluno.questionario.questao_37 == '8': # Mais de 8 vezes por dia
                            questao_37[8][1] += 1
                        
                        # Questão 38
                        if aluno.questionario.questao_38 == '0': # Nunca ou menos de uma vez por mês
                            questao_38[0][1] += 1
                        elif aluno.questionario.questao_38 == '1': # 1 a 3 vezes por mês
                            questao_38[1][1] += 1
                        elif aluno.questionario.questao_38 == '2': # 1 vez por semana
                            questao_38[2][1] += 1
                        elif aluno.questionario.questao_38 == '3': # 2 a 4 vezes por semana
                            questao_38[3][1] += 1
                        elif aluno.questionario.questao_38 == '4': # 6 a 8 vezes por semana
                            questao_38[4][1] += 1
                        elif aluno.questionario.questao_38 == '5': # 1 vez por dia
                            questao_38[5][1] += 1
                        elif aluno.questionario.questao_38 == '6': # 2 a 3 vezes por dia
                            questao_38[6][1] += 1
                        elif aluno.questionario.questao_38 == '7': # 4 a 6 vezes por dia
                            questao_38[7][1] += 1
                        elif aluno.questionario.questao_38 == '8': # Mais de 8 vezes por dia
                            questao_38[8][1] += 1
                        
                        # Questão 39
                        if aluno.questionario.questao_39 == '0': # Nunca ou menos de uma vez por mês
                            questao_39[0][1] += 1
                        elif aluno.questionario.questao_39 == '1': # 1 a 3 vezes por mês
                            questao_39[1][1] += 1
                        elif aluno.questionario.questao_39 == '2': # 1 vez por semana
                            questao_39[2][1] += 1
                        elif aluno.questionario.questao_39 == '3': # 2 a 4 vezes por semana
                            questao_39[3][1] += 1
                        elif aluno.questionario.questao_39 == '4': # 6 a 8 vezes por semana
                            questao_39[4][1] += 1
                        elif aluno.questionario.questao_39 == '5': # 1 vez por dia
                            questao_39[5][1] += 1
                        elif aluno.questionario.questao_39 == '6': # 2 a 3 vezes por dia
                            questao_39[6][1] += 1
                        elif aluno.questionario.questao_39 == '7': # 4 a 6 vezes por dia
                            questao_39[7][1] += 1
                        elif aluno.questionario.questao_39 == '8': # Mais de 8 vezes por dia
                            questao_39[8][1] += 1
                        
                        # Questão 40
                        if aluno.questionario.questao_40 == '0': # Nunca ou menos de uma vez por mês
                            questao_40[0][1] += 1
                        elif aluno.questionario.questao_40 == '1': # 1 a 3 vezes por mês
                            questao_40[1][1] += 1
                        elif aluno.questionario.questao_40 == '2': # 1 vez por semana
                            questao_40[2][1] += 1
                        elif aluno.questionario.questao_40 == '3': # 2 a 4 vezes por semana
                            questao_40[3][1] += 1
                        elif aluno.questionario.questao_40 == '4': # 6 a 8 vezes por semana
                            questao_40[4][1] += 1
                        elif aluno.questionario.questao_40 == '5': # 1 vez por dia
                            questao_40[5][1] += 1
                        elif aluno.questionario.questao_40 == '6': # 2 a 3 vezes por dia
                            questao_40[6][1] += 1
                        elif aluno.questionario.questao_40 == '7': # 4 a 6 vezes por dia
                            questao_40[7][1] += 1
                        elif aluno.questionario.questao_40 == '8': # Mais de 8 vezes por dia
                            questao_40[8][1] += 1
                        
                        # Questão 41
                        if aluno.questionario.questao_41 == '0': # Nunca ou menos de uma vez por mês
                            questao_41[0][1] += 1
                        elif aluno.questionario.questao_41 == '1': # 1 a 3 vezes por mês
                            questao_41[1][1] += 1
                        elif aluno.questionario.questao_41 == '2': # 1 vez por semana
                            questao_41[2][1] += 1
                        elif aluno.questionario.questao_41 == '3': # 2 a 4 vezes por semana
                            questao_41[3][1] += 1
                        elif aluno.questionario.questao_41 == '4': # 6 a 8 vezes por semana
                            questao_41[4][1] += 1
                        elif aluno.questionario.questao_41 == '5': # 1 vez por dia
                            questao_41[5][1] += 1
                        elif aluno.questionario.questao_41 == '6': # 2 a 3 vezes por dia
                            questao_41[6][1] += 1
                        elif aluno.questionario.questao_41 == '7': # 4 a 6 vezes por dia
                            questao_41[7][1] += 1
                        elif aluno.questionario.questao_41 == '8': # Mais de 8 vezes por dia
                            questao_41[8][1] += 1
                        
                        # Questão 42
                        if aluno.questionario.questao_42 == '0': # Nunca ou menos de uma vez por mês
                            questao_42[0][1] += 1
                        elif aluno.questionario.questao_42 == '1': # 1 a 3 vezes por mês
                            questao_42[1][1] += 1
                        elif aluno.questionario.questao_42 == '2': # 1 vez por semana
                            questao_42[2][1] += 1
                        elif aluno.questionario.questao_42 == '3': # 2 a 4 vezes por semana
                            questao_42[3][1] += 1
                        elif aluno.questionario.questao_42 == '4': # 6 a 8 vezes por semana
                            questao_42[4][1] += 1
                        elif aluno.questionario.questao_42 == '5': # 1 vez por dia
                            questao_42[5][1] += 1
                        elif aluno.questionario.questao_42 == '6': # 2 a 3 vezes por dia
                            questao_42[6][1] += 1
                        elif aluno.questionario.questao_42 == '7': # 4 a 6 vezes por dia
                            questao_42[7][1] += 1
                        elif aluno.questionario.questao_42 == '8': # Mais de 8 vezes por dia
                            questao_42[8][1] += 1
                        
                        # Questão 43
                        if aluno.questionario.questao_43 == '0': # Nunca ou menos de uma vez por mês
                            questao_43[0][1] += 1
                        elif aluno.questionario.questao_43 == '1': # 1 a 3 vezes por mês
                            questao_43[1][1] += 1
                        elif aluno.questionario.questao_43 == '2': # 1 vez por semana
                            questao_43[2][1] += 1
                        elif aluno.questionario.questao_43 == '3': # 2 a 4 vezes por semana
                            questao_43[3][1] += 1
                        elif aluno.questionario.questao_43 == '4': # 6 a 8 vezes por semana
                            questao_43[4][1] += 1
                        elif aluno.questionario.questao_43 == '5': # 1 vez por dia
                            questao_43[5][1] += 1
                        elif aluno.questionario.questao_43 == '6': # 2 a 3 vezes por dia
                            questao_43[6][1] += 1
                        elif aluno.questionario.questao_43 == '7': # 4 a 6 vezes por dia
                            questao_43[7][1] += 1
                        elif aluno.questionario.questao_43 == '8': # Mais de 8 vezes por dia
                            questao_43[8][1] += 1
                        
                        # Questão 44
                        if aluno.questionario.questao_44 == '0': # Nunca ou menos de uma vez por mês
                            questao_44[0][1] += 1
                        elif aluno.questionario.questao_44 == '1': # 1 a 3 vezes por mês
                            questao_44[1][1] += 1
                        elif aluno.questionario.questao_44 == '2': # 1 vez por semana
                            questao_44[2][1] += 1
                        elif aluno.questionario.questao_44 == '3': # 2 a 4 vezes por semana
                            questao_44[3][1] += 1
                        elif aluno.questionario.questao_44 == '4': # 6 a 8 vezes por semana
                            questao_44[4][1] += 1
                        elif aluno.questionario.questao_44 == '5': # 1 vez por dia
                            questao_44[5][1] += 1
                        elif aluno.questionario.questao_44 == '6': # 2 a 3 vezes por dia
                            questao_44[6][1] += 1
                        elif aluno.questionario.questao_44 == '7': # 4 a 6 vezes por dia
                            questao_44[7][1] += 1
                        elif aluno.questionario.questao_44 == '8': # Mais de 8 vezes por dia
                            questao_44[8][1] += 1
                        
                        # Questão 45
                        if aluno.questionario.questao_45 == '0': # Nunca ou menos de uma vez por mês
                            questao_45[0][1] += 1
                        elif aluno.questionario.questao_45 == '1': # 1 a 3 vezes por mês
                            questao_45[1][1] += 1
                        elif aluno.questionario.questao_45 == '2': # 1 vez por semana
                            questao_45[2][1] += 1
                        elif aluno.questionario.questao_45 == '3': # 2 a 4 vezes por semana
                            questao_45[3][1] += 1
                        elif aluno.questionario.questao_45 == '4': # 6 a 8 vezes por semana
                            questao_45[4][1] += 1
                        elif aluno.questionario.questao_45 == '5': # 1 vez por dia
                            questao_45[5][1] += 1
                        elif aluno.questionario.questao_45 == '6': # 2 a 3 vezes por dia
                            questao_45[6][1] += 1
                        elif aluno.questionario.questao_45 == '7': # 4 a 6 vezes por dia
                            questao_45[7][1] += 1
                        elif aluno.questionario.questao_45 == '8': # Mais de 8 vezes por dia
                            questao_45[8][1] += 1
                        
                        # Questão 46
                        if aluno.questionario.questao_46 == '0': # Nunca ou menos de uma vez por mês
                            questao_46[0][1] += 1
                        elif aluno.questionario.questao_46 == '1': # 1 a 3 vezes por mês
                            questao_46[1][1] += 1
                        elif aluno.questionario.questao_46 == '2': # 1 vez por semana
                            questao_46[2][1] += 1
                        elif aluno.questionario.questao_46 == '3': # 2 a 4 vezes por semana
                            questao_46[3][1] += 1
                        elif aluno.questionario.questao_46 == '4': # 6 a 8 vezes por semana
                            questao_46[4][1] += 1
                        elif aluno.questionario.questao_46 == '5': # 1 vez por dia
                            questao_46[5][1] += 1
                        elif aluno.questionario.questao_46 == '6': # 2 a 3 vezes por dia
                            questao_46[6][1] += 1
                        elif aluno.questionario.questao_46 == '7': # 4 a 6 vezes por dia
                            questao_46[7][1] += 1
                        elif aluno.questionario.questao_46 == '8': # Mais de 8 vezes por dia
                            questao_46[8][1] += 1
                        
                        # Questão 47
                        if aluno.questionario.questao_47 == '0': # Nunca ou menos de uma vez por mês
                            questao_47[0][1] += 1
                        elif aluno.questionario.questao_47 == '1': # 1 a 3 vezes por mês
                            questao_47[1][1] += 1
                        elif aluno.questionario.questao_47 == '2': # 1 vez por semana
                            questao_47[2][1] += 1
                        elif aluno.questionario.questao_47 == '3': # 2 a 4 vezes por semana
                            questao_47[3][1] += 1
                        elif aluno.questionario.questao_47 == '4': # 6 a 8 vezes por semana
                            questao_47[4][1] += 1
                        elif aluno.questionario.questao_47 == '5': # 1 vez por dia
                            questao_47[5][1] += 1
                        elif aluno.questionario.questao_47 == '6': # 2 a 3 vezes por dia
                            questao_47[6][1] += 1
                        elif aluno.questionario.questao_47 == '7': # 4 a 6 vezes por dia
                            questao_47[7][1] += 1
                        elif aluno.questionario.questao_47 == '8': # Mais de 8 vezes por dia
                            questao_47[8][1] += 1
                        
                        # Questão 48
                        if aluno.questionario.questao_48 == '0': # Nunca ou menos de uma vez por mês
                            questao_48[0][1] += 1
                        elif aluno.questionario.questao_48 == '1': # 1 a 3 vezes por mês
                            questao_48[1][1] += 1
                        elif aluno.questionario.questao_48 == '2': # 1 vez por semana
                            questao_48[2][1] += 1
                        elif aluno.questionario.questao_48 == '3': # 2 a 4 vezes por semana
                            questao_48[3][1] += 1
                        elif aluno.questionario.questao_48 == '4': # 6 a 8 vezes por semana
                            questao_48[4][1] += 1
                        elif aluno.questionario.questao_48 == '5': # 1 vez por dia
                            questao_48[5][1] += 1
                        elif aluno.questionario.questao_48 == '6': # 2 a 3 vezes por dia
                            questao_48[6][1] += 1
                        elif aluno.questionario.questao_48 == '7': # 4 a 6 vezes por dia
                            questao_48[7][1] += 1
                        elif aluno.questionario.questao_48 == '8': # Mais de 8 vezes por dia
                            questao_48[8][1] += 1
                        
                        # Questão 49
                        if aluno.questionario.questao_49 == '0': # Nunca ou menos de uma vez por mês
                            questao_49[0][1] += 1
                        elif aluno.questionario.questao_49 == '1': # 1 a 3 vezes por mês
                            questao_49[1][1] += 1
                        elif aluno.questionario.questao_49 == '2': # 1 vez por semana
                            questao_49[2][1] += 1
                        elif aluno.questionario.questao_49 == '3': # 2 a 4 vezes por semana
                            questao_49[3][1] += 1
                        elif aluno.questionario.questao_49 == '4': # 6 a 8 vezes por semana
                            questao_49[4][1] += 1
                        elif aluno.questionario.questao_49 == '5': # 1 vez por dia
                            questao_49[5][1] += 1
                        elif aluno.questionario.questao_49 == '6': # 2 a 3 vezes por dia
                            questao_49[6][1] += 1
                        elif aluno.questionario.questao_49 == '7': # 4 a 6 vezes por dia
                            questao_49[7][1] += 1
                        elif aluno.questionario.questao_49 == '8': # Mais de 8 vezes por dia
                            questao_49[8][1] += 1
                        
                        # Questão 50
                        if aluno.questionario.questao_50 == '0': # Nunca ou menos de uma vez por mês
                            questao_50[0][1] += 1
                        elif aluno.questionario.questao_50 == '1': # 1 a 3 vezes por mês
                            questao_50[1][1] += 1
                        elif aluno.questionario.questao_50 == '2': # 1 vez por semana
                            questao_50[2][1] += 1
                        elif aluno.questionario.questao_50 == '3': # 2 a 4 vezes por semana
                            questao_50[3][1] += 1
                        elif aluno.questionario.questao_50 == '4': # 6 a 8 vezes por semana
                            questao_50[4][1] += 1
                        elif aluno.questionario.questao_50 == '5': # 1 vez por dia
                            questao_50[5][1] += 1
                        elif aluno.questionario.questao_50 == '6': # 2 a 3 vezes por dia
                            questao_50[6][1] += 1
                        elif aluno.questionario.questao_50 == '7': # 4 a 6 vezes por dia
                            questao_50[7][1] += 1
                        elif aluno.questionario.questao_50 == '8': # Mais de 8 vezes por dia
                            questao_50[8][1] += 1
                        
                        # Questão 51
                        if aluno.questionario.questao_51 == '0': # Nunca ou menos de uma vez por mês
                            questao_51[0][1] += 1
                        elif aluno.questionario.questao_51 == '1': # 1 a 3 vezes por mês
                            questao_51[1][1] += 1
                        elif aluno.questionario.questao_51 == '2': # 1 vez por semana
                            questao_51[2][1] += 1
                        elif aluno.questionario.questao_51 == '3': # 2 a 4 vezes por semana
                            questao_51[3][1] += 1
                        elif aluno.questionario.questao_51 == '4': # 6 a 8 vezes por semana
                            questao_51[4][1] += 1
                        elif aluno.questionario.questao_51 == '5': # 1 vez por dia
                            questao_51[5][1] += 1
                        elif aluno.questionario.questao_51 == '6': # 2 a 3 vezes por dia
                            questao_51[6][1] += 1
                        elif aluno.questionario.questao_51 == '7': # 4 a 6 vezes por dia
                            questao_51[7][1] += 1
                        elif aluno.questionario.questao_51 == '8': # Mais de 8 vezes por dia
                            questao_51[8][1] += 1
                        
                        # Questão 52
                        if aluno.questionario.questao_52 == '0': # Nunca ou menos de uma vez por mês
                            questao_52[0][1] += 1
                        elif aluno.questionario.questao_52 == '1': # 1 a 3 vezes por mês
                            questao_52[1][1] += 1
                        elif aluno.questionario.questao_52 == '2': # 1 vez por semana
                            questao_52[2][1] += 1
                        elif aluno.questionario.questao_52 == '3': # 2 a 4 vezes por semana
                            questao_52[3][1] += 1
                        elif aluno.questionario.questao_52 == '4': # 6 a 8 vezes por semana
                            questao_52[4][1] += 1
                        elif aluno.questionario.questao_52 == '5': # 1 vez por dia
                            questao_52[5][1] += 1
                        elif aluno.questionario.questao_52 == '6': # 2 a 3 vezes por dia
                            questao_52[6][1] += 1
                        elif aluno.questionario.questao_52 == '7': # 4 a 6 vezes por dia
                            questao_52[7][1] += 1
                        elif aluno.questionario.questao_52 == '8': # Mais de 8 vezes por dia
                            questao_52[8][1] += 1
                        
                        # Questão 53
                        if aluno.questionario.questao_53 == '0': # Nunca ou menos de uma vez por mês
                            questao_53[0][1] += 1
                        elif aluno.questionario.questao_53 == '1': # 1 a 3 vezes por mês
                            questao_53[1][1] += 1
                        elif aluno.questionario.questao_53 == '2': # 1 vez por semana
                            questao_53[2][1] += 1
                        elif aluno.questionario.questao_53 == '3': # 2 a 4 vezes por semana
                            questao_53[3][1] += 1
                        elif aluno.questionario.questao_53 == '4': # 6 a 8 vezes por semana
                            questao_53[4][1] += 1
                        elif aluno.questionario.questao_53 == '5': # 1 vez por dia
                            questao_53[5][1] += 1
                        elif aluno.questionario.questao_53 == '6': # 2 a 3 vezes por dia
                            questao_53[6][1] += 1
                        elif aluno.questionario.questao_53 == '7': # 4 a 6 vezes por dia
                            questao_53[7][1] += 1
                        elif aluno.questionario.questao_53 == '8': # Mais de 8 vezes por dia
                            questao_53[8][1] += 1
                        
                        # Questão 54
                        if aluno.questionario.questao_54 == '0': # Nunca ou menos de uma vez por mês
                            questao_54[0][1] += 1
                        elif aluno.questionario.questao_54 == '1': # 1 a 3 vezes por mês
                            questao_54[1][1] += 1
                        elif aluno.questionario.questao_54 == '2': # 1 vez por semana
                            questao_54[2][1] += 1
                        elif aluno.questionario.questao_54 == '3': # 2 a 4 vezes por semana
                            questao_54[3][1] += 1
                        elif aluno.questionario.questao_54 == '4': # 6 a 8 vezes por semana
                            questao_54[4][1] += 1
                        elif aluno.questionario.questao_54 == '5': # 1 vez por dia
                            questao_54[5][1] += 1
                        elif aluno.questionario.questao_54 == '6': # 2 a 3 vezes por dia
                            questao_54[6][1] += 1
                        elif aluno.questionario.questao_54 == '7': # 4 a 6 vezes por dia
                            questao_54[7][1] += 1
                        elif aluno.questionario.questao_54 == '8': # Mais de 8 vezes por dia
                            questao_54[8][1] += 1
            
                # Totais da tabela sexo
                sexo[3][0] = sexo[0][0] + sexo[1][0] + sexo[2][0] # Total da coluna sim
                sexo[3][1] = sexo[0][1] + sexo[1][1] + sexo[2][1] # Total da coluna não
                sexo[3][2] = sexo[3][0] + sexo[3][1] # Total geral
                sexo[0][2] = sexo[0][0] + sexo[0][1] # Total da linha masculino
                sexo[1][2] = sexo[1][0] + sexo[1][1] # Total da linha feminino
                sexo[2][2] = sexo[2][0] + sexo[2][1] # Total da linha outro
                
                # Totais da tabela raça
                raca[5][0] = raca[0][0] + raca[1][0] + raca[2][0] + raca[3][0] + raca[4][0] # Total da coluna sim
                raca[5][1] = raca[0][1] + raca[1][1] + raca[2][1] + raca[3][1] + raca[4][1] # Total da coluna não
                raca[5][2] = raca[5][0] + raca[5][1] # Total geral
                raca[0][2] = raca[0][0] + raca[0][1] # Total da linha amarela
                raca[1][2] = raca[1][0] + raca[1][1] # Total da linha branca
                raca[2][2] = raca[2][0] + raca[2][1] # Total da linha indigena
                raca[3][2] = raca[3][0] + raca[3][1] # Total da linha parda
                raca[4][2] = raca[4][0] + raca[4][1] # Total da linha preta
                
                # Totais da tabela questão 73
                questao_73[2][0] = questao_73[0][0] + questao_73[1][0] # Total da coluna sim
                questao_73[2][1] = questao_73[0][1] + questao_73[1][1] # Total da coluna não
                questao_73[2][2] = questao_73[2][0] + questao_73[2][1] # Total geral
                questao_73[0][2] = questao_73[0][0] + questao_73[0][1] # Total da linha sim
                questao_73[1][2] = questao_73[1][0] + questao_73[1][1] # Total da linha não
                
                # Totais da tabela questão 75
                questao_75[7][0] = questao_75[0][0] + questao_75[1][0] + questao_75[2][0] + questao_75[3][0] + questao_75[4][0] + questao_75[5][0] + questao_75[6][0] # Total da coluna sim
                questao_75[7][1] = questao_75[0][1] + questao_75[1][1] + questao_75[2][1] + questao_75[3][1] + questao_75[4][1] + questao_75[5][1] + questao_75[6][1] # Total da coluna não
                questao_75[7][2] = questao_75[7][0] + questao_75[7][1] # Total geral
                questao_75[0][2] = questao_75[0][0] + questao_75[0][1] # Nenhum dia nos últimos 30 dias (0 dia)
                questao_75[1][2] = questao_75[1][0] + questao_75[1][1] # 1 ou 2 dias nos últimos 30 dias
                questao_75[2][2] = questao_75[2][0] + questao_75[2][1] # 3 a 5 dias nos últimos 30 dias
                questao_75[3][2] = questao_75[3][0] + questao_75[3][1] # 6 a 9 dias nos últimos 30 dias
                questao_75[4][2] = questao_75[4][0] + questao_75[4][1] # 10 a 19 dias nos últimos 30 dias
                questao_75[5][2] = questao_75[5][0] + questao_75[5][1] # 20 a 29 dias nos últimos 30 dias
                questao_75[6][2] = questao_75[6][0] + questao_75[6][1] # Todos os dias nos últimos 30 dias
                
                # Totais da tabela questão 79
                questao_79[10][0] = questao_79[0][0] + questao_79[1][0] + questao_79[2][0] + questao_79[3][0] + questao_79[4][0] + questao_79[5][0] + questao_79[6][0] + questao_79[7][0] + questao_79[8][0] + questao_79[9][0] # Total da coluna sim
                questao_79[10][1] = questao_79[0][1] + questao_79[1][1] + questao_79[2][1] + questao_79[3][1] + questao_79[4][1] + questao_79[5][1] + questao_79[6][1] + questao_79[7][1] + questao_79[8][1] + questao_79[9][1] # Total da coluna não
                questao_79[10][2] = questao_79[10][0] + questao_79[10][1] # Total geral
                questao_79[0][2] = questao_79[0][0] + questao_79[0][1] # Não usei nenhum produto do tabaco (os produtos do tabaco estão abaixo relacionados)
                questao_79[1][2] = questao_79[1][0] + questao_79[1][1] # Cigarros de cravo (conhecidos como cigarros de Bali).
                questao_79[2][2] = questao_79[2][0] + questao_79[2][1] # Cigarros enrolados à mão (conhecidos como cigarros de palha ou papel)
                questao_79[3][2] = questao_79[3][0] + questao_79[3][1] # Cigarrilhas
                questao_79[4][2] = questao_79[4][0] + questao_79[4][1] # Charutos, charutos pequenos.
                questao_79[5][2] = questao_79[5][0] + questao_79[5][1] # Fumo para mascar
                questao_79[6][2] = questao_79[6][0] + questao_79[6][1] # Narguilé (cachimbo de água)
                questao_79[7][2] = questao_79[7][0] + questao_79[7][1] # Cigarros indianos (bidis)
                questao_79[8][2] = questao_79[8][0] + questao_79[8][1] # Cigarro eletrônico (e-cigarette)
                questao_79[9][2] = questao_79[9][0] + questao_79[9][1] # Outros
                
                # Totais da tabela questão 84
                questao_84[7][0] = questao_84[0][0] + questao_84[1][0] + questao_84[2][0] + questao_84[3][0] + questao_84[4][0] + questao_84[5][0] + questao_84[6][0] # Total da coluna sim
                questao_84[7][1] = questao_84[0][1] + questao_84[1][1] + questao_84[2][1] + questao_84[3][1] + questao_84[4][1] + questao_84[5][1] + questao_84[6][1] # Total da coluna não
                questao_84[7][2] = questao_84[7][0] + questao_84[7][1] # Total geral
                questao_84[0][2] = questao_84[0][0] + questao_84[0][1] # Nenhum dia nos últimos 30 dias (0 dia)
                questao_84[1][2] = questao_84[1][0] + questao_84[1][1] # 1 ou 2 dias nos últimos 30 dias
                questao_84[2][2] = questao_84[2][0] + questao_84[2][1] # 3 a 5 dias nos últimos 30 dias
                questao_84[3][2] = questao_84[3][0] + questao_84[3][1] # 6 a 9 dias nos últimos 30 dias
                questao_84[4][2] = questao_84[4][0] + questao_84[4][1] # 10 a 19 dias nos últimos 30 dias
                questao_84[5][2] = questao_84[5][0] + questao_84[5][1] # 20 a 29 dias nos últimos 30 dias
                questao_84[6][2] = questao_84[6][0] + questao_84[6][1] # Todos os dias nos últimos 30 dias
                
                # Totais da tabela questão 92
                questao_92[5][0] = questao_92[0][0] + questao_92[1][0] + questao_92[2][0] + questao_92[3][0] + questao_92[4][0] # Total da coluna sim
                questao_92[5][1] = questao_92[0][1] + questao_92[1][1] + questao_92[2][1] + questao_92[3][1] + questao_92[4][1] # Total da coluna não
                questao_92[5][2] = questao_92[5][0] + questao_92[5][1] # Total geral
                questao_92[0][2] = questao_92[0][0] + questao_92[0][1] # Nenhum dia nos últimos 30 dias (0 dia)
                questao_92[1][2] = questao_92[1][0] + questao_92[1][1] # 1 ou 2 dias nos últimos 30 dias
                questao_92[2][2] = questao_92[2][0] + questao_92[2][1] # 3 a 5 dias nos últimos 30 dias
                questao_92[3][2] = questao_92[3][0] + questao_92[3][1] # 6 a 9 dias nos últimos 30 dias
                questao_92[4][2] = questao_92[4][0] + questao_92[4][1] # 10 ou mais dias nos últimos 30 dias
                
                # Totais da tabela questão 111
                questao_111[6][0] = questao_111[0][0] + questao_111[1][0] + questao_111[2][0] + questao_111[3][0] + questao_111[4][0] + questao_111[5][0] # Total da coluna sim
                questao_111[6][1] = questao_111[0][1] + questao_111[1][1] + questao_111[2][1] + questao_111[3][1] + questao_111[4][1] + questao_111[5][1] # Total da coluna não
                questao_111[6][2] = questao_111[6][0] + questao_111[6][1] # Total geral
                questao_111[0][2] = questao_111[0][0] + questao_111[0][1] # Não escovei meus dentes nos últimos 30 dias
                questao_111[1][2] = questao_111[1][0] + questao_111[1][1] # Não escovei meus dentes diariamente
                questao_111[2][2] = questao_111[2][0] + questao_111[2][1] # 1 vez por dia nos últimos 30 dias
                questao_111[3][2] = questao_111[3][0] + questao_111[3][1] # 2 vezes por dia nos últimos 30 dias
                questao_111[4][2] = questao_111[4][0] + questao_111[4][1] # 3 vezes por dia nos últimos 30 dias
                questao_111[5][2] = questao_111[5][0] + questao_111[5][1] # 4 ou mais vezes por dia nos últimos 30 dias
                
                # Totais da tabela questão 113
                questao_113[4][0] = questao_113[0][0] + questao_113[1][0] + questao_113[2][0] + questao_113[3][0] # Total da coluna sim
                questao_113[4][1] = questao_113[0][1] + questao_113[1][1] + questao_113[2][1] + questao_113[3][1] # Total da coluna não
                questao_113[4][2] = questao_113[4][0] + questao_113[4][1] # Total geral
                questao_113[0][2] = questao_113[0][0] + questao_113[0][1] # Nenhuma vez nos últimos 12 meses (0 vez)
                questao_113[1][2] = questao_113[1][0] + questao_113[1][1] # 1 vez nos últimos 12 meses
                questao_113[2][2] = questao_113[2][0] + questao_113[2][1] # 2 vezes nos últimos 12 meses
                questao_113[3][2] = questao_113[3][0] + questao_113[3][1] # 3 ou mais vezes nos últimos 12 meses
                
                # Totais da tabela questão 25
                questao_25[9][0] = questao_25[0][0] + questao_25[1][0] + questao_25[2][0] + questao_25[3][0] + questao_25[4][0] + questao_25[5][0] + questao_25[6][0] + questao_25[7][0] + questao_25[8][0] # Total da coluna sim
                questao_25[9][1] = questao_25[0][1] + questao_25[1][1] + questao_25[2][1] + questao_25[3][1] + questao_25[4][1] + questao_25[5][1] + questao_25[6][1] + questao_25[7][1] + questao_25[8][1] # Total da coluna não
                questao_25[9][2] = questao_25[9][0] + questao_25[9][1] # Total geral
                questao_25[0][2] = questao_25[0][0] + questao_25[0][1] # Nunca ou menos de uma vez por mês
                questao_25[1][2] = questao_25[1][0] + questao_25[1][1] # 1 a 3 vezes por mês
                questao_25[2][2] = questao_25[2][0] + questao_25[2][1] # 1 vez por semana
                questao_25[3][2] = questao_25[3][0] + questao_25[3][1] # 2 a 4 vezes por semana
                questao_25[4][2] = questao_25[4][0] + questao_25[4][1] # 6 a 8 vezes por semana
                questao_25[5][2] = questao_25[5][0] + questao_25[5][1] # 1 vez por dia
                questao_25[6][2] = questao_25[6][0] + questao_25[6][1] # 2 a 3 vezes por dia
                questao_25[7][2] = questao_25[7][0] + questao_25[7][1] # 4 a 6 vezes por dia
                questao_25[8][2] = questao_25[8][0] + questao_25[8][1] # Mais de 8 vezes por dia
                
                # Totais da tabela questão 26
                questao_26[9][0] = questao_26[0][0] + questao_26[1][0] + questao_26[2][0] + questao_26[3][0] + questao_26[4][0] + questao_26[5][0] + questao_26[6][0] + questao_26[7][0] + questao_26[8][0] # Total da coluna sim
                questao_26[9][1] = questao_26[0][1] + questao_26[1][1] + questao_26[2][1] + questao_26[3][1] + questao_26[4][1] + questao_26[5][1] + questao_26[6][1] + questao_26[7][1] + questao_26[8][1] # Total da coluna não
                questao_26[9][2] = questao_26[9][0] + questao_26[9][1] # Total geral
                questao_26[0][2] = questao_26[0][0] + questao_26[0][1] # Nunca ou menos de uma vez por mês
                questao_26[1][2] = questao_26[1][0] + questao_26[1][1] # 1 a 3 vezes por mês
                questao_26[2][2] = questao_26[2][0] + questao_26[2][1] # 1 vez por semana
                questao_26[3][2] = questao_26[3][0] + questao_26[3][1] # 2 a 4 vezes por semana
                questao_26[4][2] = questao_26[4][0] + questao_26[4][1] # 6 a 8 vezes por semana
                questao_26[5][2] = questao_26[5][0] + questao_26[5][1] # 1 vez por dia
                questao_26[6][2] = questao_26[6][0] + questao_26[6][1] # 2 a 3 vezes por dia
                questao_26[7][2] = questao_26[7][0] + questao_26[7][1] # 4 a 6 vezes por dia
                questao_26[8][2] = questao_26[8][0] + questao_26[8][1] # Mais de 8 vezes por dia
                
                # Totais da tabela questão 27
                questao_27[9][0] = questao_27[0][0] + questao_27[1][0] + questao_27[2][0] + questao_27[3][0] + questao_27[4][0] + questao_27[5][0] + questao_27[6][0] + questao_27[7][0] + questao_27[8][0] # Total da coluna sim
                questao_27[9][1] = questao_27[0][1] + questao_27[1][1] + questao_27[2][1] + questao_27[3][1] + questao_27[4][1] + questao_27[5][1] + questao_27[6][1] + questao_27[7][1] + questao_27[8][1] # Total da coluna não
                questao_27[9][2] = questao_27[9][0] + questao_27[9][1] # Total geral
                questao_27[0][2] = questao_27[0][0] + questao_27[0][1] # Nunca ou menos de uma vez por mês
                questao_27[1][2] = questao_27[1][0] + questao_27[1][1] # 1 a 3 vezes por mês
                questao_27[2][2] = questao_27[2][0] + questao_27[2][1] # 1 vez por semana
                questao_27[3][2] = questao_27[3][0] + questao_27[3][1] # 2 a 4 vezes por semana
                questao_27[4][2] = questao_27[4][0] + questao_27[4][1] # 6 a 8 vezes por semana
                questao_27[5][2] = questao_27[5][0] + questao_27[5][1] # 1 vez por dia
                questao_27[6][2] = questao_27[6][0] + questao_27[6][1] # 2 a 3 vezes por dia
                questao_27[7][2] = questao_27[7][0] + questao_27[7][1] # 4 a 6 vezes por dia
                questao_27[8][2] = questao_27[8][0] + questao_27[8][1] # Mais de 8 vezes por dia
                
                # Totais da tabela questão 28
                questao_28[9][0] = questao_28[0][0] + questao_28[1][0] + questao_28[2][0] + questao_28[3][0] + questao_28[4][0] + questao_28[5][0] + questao_28[6][0] + questao_28[7][0] + questao_28[8][0] # Total da coluna sim
                questao_28[9][1] = questao_28[0][1] + questao_28[1][1] + questao_28[2][1] + questao_28[3][1] + questao_28[4][1] + questao_28[5][1] + questao_28[6][1] + questao_28[7][1] + questao_28[8][1] # Total da coluna não
                questao_28[9][2] = questao_28[9][0] + questao_28[9][1] # Total geral
                questao_28[0][2] = questao_28[0][0] + questao_28[0][1] # Nunca ou menos de uma vez por mês
                questao_28[1][2] = questao_28[1][0] + questao_28[1][1] # 1 a 3 vezes por mês
                questao_28[2][2] = questao_28[2][0] + questao_28[2][1] # 1 vez por semana
                questao_28[3][2] = questao_28[3][0] + questao_28[3][1] # 2 a 4 vezes por semana
                questao_28[4][2] = questao_28[4][0] + questao_28[4][1] # 6 a 8 vezes por semana
                questao_28[5][2] = questao_28[5][0] + questao_28[5][1] # 1 vez por dia
                questao_28[6][2] = questao_28[6][0] + questao_28[6][1] # 2 a 3 vezes por dia
                questao_28[7][2] = questao_28[7][0] + questao_28[7][1] # 4 a 6 vezes por dia
                questao_28[8][2] = questao_28[8][0] + questao_28[8][1] # Mais de 8 vezes por dia
                
                # Totais da tabela questão 29
                questao_29[9][0] = questao_29[0][0] + questao_29[1][0] + questao_29[2][0] + questao_29[3][0] + questao_29[4][0] + questao_29[5][0] + questao_29[6][0] + questao_29[7][0] + questao_29[8][0] # Total da coluna sim
                questao_29[9][1] = questao_29[0][1] + questao_29[1][1] + questao_29[2][1] + questao_29[3][1] + questao_29[4][1] + questao_29[5][1] + questao_29[6][1] + questao_29[7][1] + questao_29[8][1] # Total da coluna não
                questao_29[9][2] = questao_29[9][0] + questao_29[9][1] # Total geral
                questao_29[0][2] = questao_29[0][0] + questao_29[0][1] # Nunca ou menos de uma vez por mês
                questao_29[1][2] = questao_29[1][0] + questao_29[1][1] # 1 a 3 vezes por mês
                questao_29[2][2] = questao_29[2][0] + questao_29[2][1] # 1 vez por semana
                questao_29[3][2] = questao_29[3][0] + questao_29[3][1] # 2 a 4 vezes por semana
                questao_29[4][2] = questao_29[4][0] + questao_29[4][1] # 6 a 8 vezes por semana
                questao_29[5][2] = questao_29[5][0] + questao_29[5][1] # 1 vez por dia
                questao_29[6][2] = questao_29[6][0] + questao_29[6][1] # 2 a 3 vezes por dia
                questao_29[7][2] = questao_29[7][0] + questao_29[7][1] # 4 a 6 vezes por dia
                questao_29[8][2] = questao_29[8][0] + questao_29[8][1] # Mais de 8 vezes por dia
                
                # Totais da tabela questão 30
                questao_30[9][0] = questao_30[0][0] + questao_30[1][0] + questao_30[2][0] + questao_30[3][0] + questao_30[4][0] + questao_30[5][0] + questao_30[6][0] + questao_30[7][0] + questao_30[8][0] # Total da coluna sim
                questao_30[9][1] = questao_30[0][1] + questao_30[1][1] + questao_30[2][1] + questao_30[3][1] + questao_30[4][1] + questao_30[5][1] + questao_30[6][1] + questao_30[7][1] + questao_30[8][1] # Total da coluna não
                questao_30[9][2] = questao_30[9][0] + questao_30[9][1] # Total geral
                questao_30[0][2] = questao_30[0][0] + questao_30[0][1] # Nunca ou menos de uma vez por mês
                questao_30[1][2] = questao_30[1][0] + questao_30[1][1] # 1 a 3 vezes por mês
                questao_30[2][2] = questao_30[2][0] + questao_30[2][1] # 1 vez por semana
                questao_30[3][2] = questao_30[3][0] + questao_30[3][1] # 2 a 4 vezes por semana
                questao_30[4][2] = questao_30[4][0] + questao_30[4][1] # 6 a 8 vezes por semana
                questao_30[5][2] = questao_30[5][0] + questao_30[5][1] # 1 vez por dia
                questao_30[6][2] = questao_30[6][0] + questao_30[6][1] # 2 a 3 vezes por dia
                questao_30[7][2] = questao_30[7][0] + questao_30[7][1] # 4 a 6 vezes por dia
                questao_30[8][2] = questao_30[8][0] + questao_30[8][1] # Mais de 8 vezes por dia
                
                # Totais da tabela questão 31
                questao_31[9][0] = questao_31[0][0] + questao_31[1][0] + questao_31[2][0] + questao_31[3][0] + questao_31[4][0] + questao_31[5][0] + questao_31[6][0] + questao_31[7][0] + questao_31[8][0] # Total da coluna sim
                questao_31[9][1] = questao_31[0][1] + questao_31[1][1] + questao_31[2][1] + questao_31[3][1] + questao_31[4][1] + questao_31[5][1] + questao_31[6][1] + questao_31[7][1] + questao_31[8][1] # Total da coluna não
                questao_31[9][2] = questao_31[9][0] + questao_31[9][1] # Total geral
                questao_31[0][2] = questao_31[0][0] + questao_31[0][1] # Nunca ou menos de uma vez por mês
                questao_31[1][2] = questao_31[1][0] + questao_31[1][1] # 1 a 3 vezes por mês
                questao_31[2][2] = questao_31[2][0] + questao_31[2][1] # 1 vez por semana
                questao_31[3][2] = questao_31[3][0] + questao_31[3][1] # 2 a 4 vezes por semana
                questao_31[4][2] = questao_31[4][0] + questao_31[4][1] # 6 a 8 vezes por semana
                questao_31[5][2] = questao_31[5][0] + questao_31[5][1] # 1 vez por dia
                questao_31[6][2] = questao_31[6][0] + questao_31[6][1] # 2 a 3 vezes por dia
                questao_31[7][2] = questao_31[7][0] + questao_31[7][1] # 4 a 6 vezes por dia
                questao_31[8][2] = questao_31[8][0] + questao_31[8][1] # Mais de 8 vezes por dia
                
                # Totais da tabela questão 32
                questao_32[9][0] = questao_32[0][0] + questao_32[1][0] + questao_32[2][0] + questao_32[3][0] + questao_32[4][0] + questao_32[5][0] + questao_32[6][0] + questao_32[7][0] + questao_32[8][0] # Total da coluna sim
                questao_32[9][1] = questao_32[0][1] + questao_32[1][1] + questao_32[2][1] + questao_32[3][1] + questao_32[4][1] + questao_32[5][1] + questao_32[6][1] + questao_32[7][1] + questao_32[8][1] # Total da coluna não
                questao_32[9][2] = questao_32[9][0] + questao_32[9][1] # Total geral
                questao_32[0][2] = questao_32[0][0] + questao_32[0][1] # Nunca ou menos de uma vez por mês
                questao_32[1][2] = questao_32[1][0] + questao_32[1][1] # 1 a 3 vezes por mês
                questao_32[2][2] = questao_32[2][0] + questao_32[2][1] # 1 vez por semana
                questao_32[3][2] = questao_32[3][0] + questao_32[3][1] # 2 a 4 vezes por semana
                questao_32[4][2] = questao_32[4][0] + questao_32[4][1] # 6 a 8 vezes por semana
                questao_32[5][2] = questao_32[5][0] + questao_32[5][1] # 1 vez por dia
                questao_32[6][2] = questao_32[6][0] + questao_32[6][1] # 2 a 3 vezes por dia
                questao_32[7][2] = questao_32[7][0] + questao_32[7][1] # 4 a 6 vezes por dia
                questao_32[8][2] = questao_32[8][0] + questao_32[8][1] # Mais de 8 vezes por dia
                
                # Totais da tabela questão 33
                questao_33[9][0] = questao_33[0][0] + questao_33[1][0] + questao_33[2][0] + questao_33[3][0] + questao_33[4][0] + questao_33[5][0] + questao_33[6][0] + questao_33[7][0] + questao_33[8][0] # Total da coluna sim
                questao_33[9][1] = questao_33[0][1] + questao_33[1][1] + questao_33[2][1] + questao_33[3][1] + questao_33[4][1] + questao_33[5][1] + questao_33[6][1] + questao_33[7][1] + questao_33[8][1] # Total da coluna não
                questao_33[9][2] = questao_33[9][0] + questao_33[9][1] # Total geral
                questao_33[0][2] = questao_33[0][0] + questao_33[0][1] # Nunca ou menos de uma vez por mês
                questao_33[1][2] = questao_33[1][0] + questao_33[1][1] # 1 a 3 vezes por mês
                questao_33[2][2] = questao_33[2][0] + questao_33[2][1] # 1 vez por semana
                questao_33[3][2] = questao_33[3][0] + questao_33[3][1] # 2 a 4 vezes por semana
                questao_33[4][2] = questao_33[4][0] + questao_33[4][1] # 6 a 8 vezes por semana
                questao_33[5][2] = questao_33[5][0] + questao_33[5][1] # 1 vez por dia
                questao_33[6][2] = questao_33[6][0] + questao_33[6][1] # 2 a 3 vezes por dia
                questao_33[7][2] = questao_33[7][0] + questao_33[7][1] # 4 a 6 vezes por dia
                questao_33[8][2] = questao_33[8][0] + questao_33[8][1] # Mais de 8 vezes por dia
                
                # Totais da tabela questão 34
                questao_34[9][0] = questao_34[0][0] + questao_34[1][0] + questao_34[2][0] + questao_34[3][0] + questao_34[4][0] + questao_34[5][0] + questao_34[6][0] + questao_34[7][0] + questao_34[8][0] # Total da coluna sim
                questao_34[9][1] = questao_34[0][1] + questao_34[1][1] + questao_34[2][1] + questao_34[3][1] + questao_34[4][1] + questao_34[5][1] + questao_34[6][1] + questao_34[7][1] + questao_34[8][1] # Total da coluna não
                questao_34[9][2] = questao_34[9][0] + questao_34[9][1] # Total geral
                questao_34[0][2] = questao_34[0][0] + questao_34[0][1] # Nunca ou menos de uma vez por mês
                questao_34[1][2] = questao_34[1][0] + questao_34[1][1] # 1 a 3 vezes por mês
                questao_34[2][2] = questao_34[2][0] + questao_34[2][1] # 1 vez por semana
                questao_34[3][2] = questao_34[3][0] + questao_34[3][1] # 2 a 4 vezes por semana
                questao_34[4][2] = questao_34[4][0] + questao_34[4][1] # 6 a 8 vezes por semana
                questao_34[5][2] = questao_34[5][0] + questao_34[5][1] # 1 vez por dia
                questao_34[6][2] = questao_34[6][0] + questao_34[6][1] # 2 a 3 vezes por dia
                questao_34[7][2] = questao_34[7][0] + questao_34[7][1] # 4 a 6 vezes por dia
                questao_34[8][2] = questao_34[8][0] + questao_34[8][1] # Mais de 8 vezes por dia
                
                # Totais da tabela questão 35
                questao_35[9][0] = questao_35[0][0] + questao_35[1][0] + questao_35[2][0] + questao_35[3][0] + questao_35[4][0] + questao_35[5][0] + questao_35[6][0] + questao_35[7][0] + questao_35[8][0] # Total da coluna sim
                questao_35[9][1] = questao_35[0][1] + questao_35[1][1] + questao_35[2][1] + questao_35[3][1] + questao_35[4][1] + questao_35[5][1] + questao_35[6][1] + questao_35[7][1] + questao_35[8][1] # Total da coluna não
                questao_35[9][2] = questao_35[9][0] + questao_35[9][1] # Total geral
                questao_35[0][2] = questao_35[0][0] + questao_35[0][1] # Nunca ou menos de uma vez por mês
                questao_35[1][2] = questao_35[1][0] + questao_35[1][1] # 1 a 3 vezes por mês
                questao_35[2][2] = questao_35[2][0] + questao_35[2][1] # 1 vez por semana
                questao_35[3][2] = questao_35[3][0] + questao_35[3][1] # 2 a 4 vezes por semana
                questao_35[4][2] = questao_35[4][0] + questao_35[4][1] # 6 a 8 vezes por semana
                questao_35[5][2] = questao_35[5][0] + questao_35[5][1] # 1 vez por dia
                questao_35[6][2] = questao_35[6][0] + questao_35[6][1] # 2 a 3 vezes por dia
                questao_35[7][2] = questao_35[7][0] + questao_35[7][1] # 4 a 6 vezes por dia
                questao_35[8][2] = questao_35[8][0] + questao_35[8][1] # Mais de 8 vezes por dia
                
                # Totais da tabela questão 36
                questao_36[9][0] = questao_36[0][0] + questao_36[1][0] + questao_36[2][0] + questao_36[3][0] + questao_36[4][0] + questao_36[5][0] + questao_36[6][0] + questao_36[7][0] + questao_36[8][0] # Total da coluna sim
                questao_36[9][1] = questao_36[0][1] + questao_36[1][1] + questao_36[2][1] + questao_36[3][1] + questao_36[4][1] + questao_36[5][1] + questao_36[6][1] + questao_36[7][1] + questao_36[8][1] # Total da coluna não
                questao_36[9][2] = questao_36[9][0] + questao_36[9][1] # Total geral
                questao_36[0][2] = questao_36[0][0] + questao_36[0][1] # Nunca ou menos de uma vez por mês
                questao_36[1][2] = questao_36[1][0] + questao_36[1][1] # 1 a 3 vezes por mês
                questao_36[2][2] = questao_36[2][0] + questao_36[2][1] # 1 vez por semana
                questao_36[3][2] = questao_36[3][0] + questao_36[3][1] # 2 a 4 vezes por semana
                questao_36[4][2] = questao_36[4][0] + questao_36[4][1] # 6 a 8 vezes por semana
                questao_36[5][2] = questao_36[5][0] + questao_36[5][1] # 1 vez por dia
                questao_36[6][2] = questao_36[6][0] + questao_36[6][1] # 2 a 3 vezes por dia
                questao_36[7][2] = questao_36[7][0] + questao_36[7][1] # 4 a 6 vezes por dia
                questao_36[8][2] = questao_36[8][0] + questao_36[8][1] # Mais de 8 vezes por dia
                
                # Totais da tabela questão 37
                questao_37[9][0] = questao_37[0][0] + questao_37[1][0] + questao_37[2][0] + questao_37[3][0] + questao_37[4][0] + questao_37[5][0] + questao_37[6][0] + questao_37[7][0] + questao_37[8][0] # Total da coluna sim
                questao_37[9][1] = questao_37[0][1] + questao_37[1][1] + questao_37[2][1] + questao_37[3][1] + questao_37[4][1] + questao_37[5][1] + questao_37[6][1] + questao_37[7][1] + questao_37[8][1] # Total da coluna não
                questao_37[9][2] = questao_37[9][0] + questao_37[9][1] # Total geral
                questao_37[0][2] = questao_37[0][0] + questao_37[0][1] # Nunca ou menos de uma vez por mês
                questao_37[1][2] = questao_37[1][0] + questao_37[1][1] # 1 a 3 vezes por mês
                questao_37[2][2] = questao_37[2][0] + questao_37[2][1] # 1 vez por semana
                questao_37[3][2] = questao_37[3][0] + questao_37[3][1] # 2 a 4 vezes por semana
                questao_37[4][2] = questao_37[4][0] + questao_37[4][1] # 6 a 8 vezes por semana
                questao_37[5][2] = questao_37[5][0] + questao_37[5][1] # 1 vez por dia
                questao_37[6][2] = questao_37[6][0] + questao_37[6][1] # 2 a 3 vezes por dia
                questao_37[7][2] = questao_37[7][0] + questao_37[7][1] # 4 a 6 vezes por dia
                questao_37[8][2] = questao_37[8][0] + questao_37[8][1] # Mais de 8 vezes por dia
                
                # Totais da tabela questão 38
                questao_38[9][0] = questao_38[0][0] + questao_38[1][0] + questao_38[2][0] + questao_38[3][0] + questao_38[4][0] + questao_38[5][0] + questao_38[6][0] + questao_38[7][0] + questao_38[8][0] # Total da coluna sim
                questao_38[9][1] = questao_38[0][1] + questao_38[1][1] + questao_38[2][1] + questao_38[3][1] + questao_38[4][1] + questao_38[5][1] + questao_38[6][1] + questao_38[7][1] + questao_38[8][1] # Total da coluna não
                questao_38[9][2] = questao_38[9][0] + questao_38[9][1] # Total geral
                questao_38[0][2] = questao_38[0][0] + questao_38[0][1] # Nunca ou menos de uma vez por mês
                questao_38[1][2] = questao_38[1][0] + questao_38[1][1] # 1 a 3 vezes por mês
                questao_38[2][2] = questao_38[2][0] + questao_38[2][1] # 1 vez por semana
                questao_38[3][2] = questao_38[3][0] + questao_38[3][1] # 2 a 4 vezes por semana
                questao_38[4][2] = questao_38[4][0] + questao_38[4][1] # 6 a 8 vezes por semana
                questao_38[5][2] = questao_38[5][0] + questao_38[5][1] # 1 vez por dia
                questao_38[6][2] = questao_38[6][0] + questao_38[6][1] # 2 a 3 vezes por dia
                questao_38[7][2] = questao_38[7][0] + questao_38[7][1] # 4 a 6 vezes por dia
                questao_38[8][2] = questao_38[8][0] + questao_38[8][1] # Mais de 8 vezes por dia
                
                # Totais da tabela questão 39
                questao_39[9][0] = questao_39[0][0] + questao_39[1][0] + questao_39[2][0] + questao_39[3][0] + questao_39[4][0] + questao_39[5][0] + questao_39[6][0] + questao_39[7][0] + questao_39[8][0] # Total da coluna sim
                questao_39[9][1] = questao_39[0][1] + questao_39[1][1] + questao_39[2][1] + questao_39[3][1] + questao_39[4][1] + questao_39[5][1] + questao_39[6][1] + questao_39[7][1] + questao_39[8][1] # Total da coluna não
                questao_39[9][2] = questao_39[9][0] + questao_39[9][1] # Total geral
                questao_39[0][2] = questao_39[0][0] + questao_39[0][1] # Nunca ou menos de uma vez por mês
                questao_39[1][2] = questao_39[1][0] + questao_39[1][1] # 1 a 3 vezes por mês
                questao_39[2][2] = questao_39[2][0] + questao_39[2][1] # 1 vez por semana
                questao_39[3][2] = questao_39[3][0] + questao_39[3][1] # 2 a 4 vezes por semana
                questao_39[4][2] = questao_39[4][0] + questao_39[4][1] # 6 a 8 vezes por semana
                questao_39[5][2] = questao_39[5][0] + questao_39[5][1] # 1 vez por dia
                questao_39[6][2] = questao_39[6][0] + questao_39[6][1] # 2 a 3 vezes por dia
                questao_39[7][2] = questao_39[7][0] + questao_39[7][1] # 4 a 6 vezes por dia
                questao_39[8][2] = questao_39[8][0] + questao_39[8][1] # Mais de 8 vezes por dia
                
                # Totais da tabela questão 40
                questao_40[9][0] = questao_40[0][0] + questao_40[1][0] + questao_40[2][0] + questao_40[3][0] + questao_40[4][0] + questao_40[5][0] + questao_40[6][0] + questao_40[7][0] + questao_40[8][0] # Total da coluna sim
                questao_40[9][1] = questao_40[0][1] + questao_40[1][1] + questao_40[2][1] + questao_40[3][1] + questao_40[4][1] + questao_40[5][1] + questao_40[6][1] + questao_40[7][1] + questao_40[8][1] # Total da coluna não
                questao_40[9][2] = questao_40[9][0] + questao_40[9][1] # Total geral
                questao_40[0][2] = questao_40[0][0] + questao_40[0][1] # Nunca ou menos de uma vez por mês
                questao_40[1][2] = questao_40[1][0] + questao_40[1][1] # 1 a 3 vezes por mês
                questao_40[2][2] = questao_40[2][0] + questao_40[2][1] # 1 vez por semana
                questao_40[3][2] = questao_40[3][0] + questao_40[3][1] # 2 a 4 vezes por semana
                questao_40[4][2] = questao_40[4][0] + questao_40[4][1] # 6 a 8 vezes por semana
                questao_40[5][2] = questao_40[5][0] + questao_40[5][1] # 1 vez por dia
                questao_40[6][2] = questao_40[6][0] + questao_40[6][1] # 2 a 3 vezes por dia
                questao_40[7][2] = questao_40[7][0] + questao_40[7][1] # 4 a 6 vezes por dia
                questao_40[8][2] = questao_40[8][0] + questao_40[8][1] # Mais de 8 vezes por dia
                
                # Totais da tabela questão 41
                questao_41[9][0] = questao_41[0][0] + questao_41[1][0] + questao_41[2][0] + questao_41[3][0] + questao_41[4][0] + questao_41[5][0] + questao_41[6][0] + questao_41[7][0] + questao_41[8][0] # Total da coluna sim
                questao_41[9][1] = questao_41[0][1] + questao_41[1][1] + questao_41[2][1] + questao_41[3][1] + questao_41[4][1] + questao_41[5][1] + questao_41[6][1] + questao_41[7][1] + questao_41[8][1] # Total da coluna não
                questao_41[9][2] = questao_41[9][0] + questao_41[9][1] # Total geral
                questao_41[0][2] = questao_41[0][0] + questao_41[0][1] # Nunca ou menos de uma vez por mês
                questao_41[1][2] = questao_41[1][0] + questao_41[1][1] # 1 a 3 vezes por mês
                questao_41[2][2] = questao_41[2][0] + questao_41[2][1] # 1 vez por semana
                questao_41[3][2] = questao_41[3][0] + questao_41[3][1] # 2 a 4 vezes por semana
                questao_41[4][2] = questao_41[4][0] + questao_41[4][1] # 6 a 8 vezes por semana
                questao_41[5][2] = questao_41[5][0] + questao_41[5][1] # 1 vez por dia
                questao_41[6][2] = questao_41[6][0] + questao_41[6][1] # 2 a 3 vezes por dia
                questao_41[7][2] = questao_41[7][0] + questao_41[7][1] # 4 a 6 vezes por dia
                questao_41[8][2] = questao_41[8][0] + questao_41[8][1] # Mais de 8 vezes por dia
                
                # Totais da tabela questão 42
                questao_42[9][0] = questao_42[0][0] + questao_42[1][0] + questao_42[2][0] + questao_42[3][0] + questao_42[4][0] + questao_42[5][0] + questao_42[6][0] + questao_42[7][0] + questao_42[8][0] # Total da coluna sim
                questao_42[9][1] = questao_42[0][1] + questao_42[1][1] + questao_42[2][1] + questao_42[3][1] + questao_42[4][1] + questao_42[5][1] + questao_42[6][1] + questao_42[7][1] + questao_42[8][1] # Total da coluna não
                questao_42[9][2] = questao_42[9][0] + questao_42[9][1] # Total geral
                questao_42[0][2] = questao_42[0][0] + questao_42[0][1] # Nunca ou menos de uma vez por mês
                questao_42[1][2] = questao_42[1][0] + questao_42[1][1] # 1 a 3 vezes por mês
                questao_42[2][2] = questao_42[2][0] + questao_42[2][1] # 1 vez por semana
                questao_42[3][2] = questao_42[3][0] + questao_42[3][1] # 2 a 4 vezes por semana
                questao_42[4][2] = questao_42[4][0] + questao_42[4][1] # 6 a 8 vezes por semana
                questao_42[5][2] = questao_42[5][0] + questao_42[5][1] # 1 vez por dia
                questao_42[6][2] = questao_42[6][0] + questao_42[6][1] # 2 a 3 vezes por dia
                questao_42[7][2] = questao_42[7][0] + questao_42[7][1] # 4 a 6 vezes por dia
                questao_42[8][2] = questao_42[8][0] + questao_42[8][1] # Mais de 8 vezes por dia
                
                # Totais da tabela questão 43
                questao_43[9][0] = questao_43[0][0] + questao_43[1][0] + questao_43[2][0] + questao_43[3][0] + questao_43[4][0] + questao_43[5][0] + questao_43[6][0] + questao_43[7][0] + questao_43[8][0] # Total da coluna sim
                questao_43[9][1] = questao_43[0][1] + questao_43[1][1] + questao_43[2][1] + questao_43[3][1] + questao_43[4][1] + questao_43[5][1] + questao_43[6][1] + questao_43[7][1] + questao_43[8][1] # Total da coluna não
                questao_43[9][2] = questao_43[9][0] + questao_43[9][1] # Total geral
                questao_43[0][2] = questao_43[0][0] + questao_43[0][1] # Nunca ou menos de uma vez por mês
                questao_43[1][2] = questao_43[1][0] + questao_43[1][1] # 1 a 3 vezes por mês
                questao_43[2][2] = questao_43[2][0] + questao_43[2][1] # 1 vez por semana
                questao_43[3][2] = questao_43[3][0] + questao_43[3][1] # 2 a 4 vezes por semana
                questao_43[4][2] = questao_43[4][0] + questao_43[4][1] # 6 a 8 vezes por semana
                questao_43[5][2] = questao_43[5][0] + questao_43[5][1] # 1 vez por dia
                questao_43[6][2] = questao_43[6][0] + questao_43[6][1] # 2 a 3 vezes por dia
                questao_43[7][2] = questao_43[7][0] + questao_43[7][1] # 4 a 6 vezes por dia
                questao_43[8][2] = questao_43[8][0] + questao_43[8][1] # Mais de 8 vezes por dia
                
                # Totais da tabela questão 44
                questao_44[9][0] = questao_44[0][0] + questao_44[1][0] + questao_44[2][0] + questao_44[3][0] + questao_44[4][0] + questao_44[5][0] + questao_44[6][0] + questao_44[7][0] + questao_44[8][0] # Total da coluna sim
                questao_44[9][1] = questao_44[0][1] + questao_44[1][1] + questao_44[2][1] + questao_44[3][1] + questao_44[4][1] + questao_44[5][1] + questao_44[6][1] + questao_44[7][1] + questao_44[8][1] # Total da coluna não
                questao_44[9][2] = questao_44[9][0] + questao_44[9][1] # Total geral
                questao_44[0][2] = questao_44[0][0] + questao_44[0][1] # Nunca ou menos de uma vez por mês
                questao_44[1][2] = questao_44[1][0] + questao_44[1][1] # 1 a 3 vezes por mês
                questao_44[2][2] = questao_44[2][0] + questao_44[2][1] # 1 vez por semana
                questao_44[3][2] = questao_44[3][0] + questao_44[3][1] # 2 a 4 vezes por semana
                questao_44[4][2] = questao_44[4][0] + questao_44[4][1] # 6 a 8 vezes por semana
                questao_44[5][2] = questao_44[5][0] + questao_44[5][1] # 1 vez por dia
                questao_44[6][2] = questao_44[6][0] + questao_44[6][1] # 2 a 3 vezes por dia
                questao_44[7][2] = questao_44[7][0] + questao_44[7][1] # 4 a 6 vezes por dia
                questao_44[8][2] = questao_44[8][0] + questao_44[8][1] # Mais de 8 vezes por dia
                
                # Totais da tabela questão 45
                questao_45[9][0] = questao_45[0][0] + questao_45[1][0] + questao_45[2][0] + questao_45[3][0] + questao_45[4][0] + questao_45[5][0] + questao_45[6][0] + questao_45[7][0] + questao_45[8][0] # Total da coluna sim
                questao_45[9][1] = questao_45[0][1] + questao_45[1][1] + questao_45[2][1] + questao_45[3][1] + questao_45[4][1] + questao_45[5][1] + questao_45[6][1] + questao_45[7][1] + questao_45[8][1] # Total da coluna não
                questao_45[9][2] = questao_45[9][0] + questao_45[9][1] # Total geral
                questao_45[0][2] = questao_45[0][0] + questao_45[0][1] # Nunca ou menos de uma vez por mês
                questao_45[1][2] = questao_45[1][0] + questao_45[1][1] # 1 a 3 vezes por mês
                questao_45[2][2] = questao_45[2][0] + questao_45[2][1] # 1 vez por semana
                questao_45[3][2] = questao_45[3][0] + questao_45[3][1] # 2 a 4 vezes por semana
                questao_45[4][2] = questao_45[4][0] + questao_45[4][1] # 6 a 8 vezes por semana
                questao_45[5][2] = questao_45[5][0] + questao_45[5][1] # 1 vez por dia
                questao_45[6][2] = questao_45[6][0] + questao_45[6][1] # 2 a 3 vezes por dia
                questao_45[7][2] = questao_45[7][0] + questao_45[7][1] # 4 a 6 vezes por dia
                questao_45[8][2] = questao_45[8][0] + questao_45[8][1] # Mais de 8 vezes por dia
                
                # Totais da tabela questão 46
                questao_46[9][0] = questao_46[0][0] + questao_46[1][0] + questao_46[2][0] + questao_46[3][0] + questao_46[4][0] + questao_46[5][0] + questao_46[6][0] + questao_46[7][0] + questao_46[8][0] # Total da coluna sim
                questao_46[9][1] = questao_46[0][1] + questao_46[1][1] + questao_46[2][1] + questao_46[3][1] + questao_46[4][1] + questao_46[5][1] + questao_46[6][1] + questao_46[7][1] + questao_46[8][1] # Total da coluna não
                questao_46[9][2] = questao_46[9][0] + questao_46[9][1] # Total geral
                questao_46[0][2] = questao_46[0][0] + questao_46[0][1] # Nunca ou menos de uma vez por mês
                questao_46[1][2] = questao_46[1][0] + questao_46[1][1] # 1 a 3 vezes por mês
                questao_46[2][2] = questao_46[2][0] + questao_46[2][1] # 1 vez por semana
                questao_46[3][2] = questao_46[3][0] + questao_46[3][1] # 2 a 4 vezes por semana
                questao_46[4][2] = questao_46[4][0] + questao_46[4][1] # 6 a 8 vezes por semana
                questao_46[5][2] = questao_46[5][0] + questao_46[5][1] # 1 vez por dia
                questao_46[6][2] = questao_46[6][0] + questao_46[6][1] # 2 a 3 vezes por dia
                questao_46[7][2] = questao_46[7][0] + questao_46[7][1] # 4 a 6 vezes por dia
                questao_46[8][2] = questao_46[8][0] + questao_46[8][1] # Mais de 8 vezes por dia
                
                # Totais da tabela questão 47
                questao_47[9][0] = questao_47[0][0] + questao_47[1][0] + questao_47[2][0] + questao_47[3][0] + questao_47[4][0] + questao_47[5][0] + questao_47[6][0] + questao_47[7][0] + questao_47[8][0] # Total da coluna sim
                questao_47[9][1] = questao_47[0][1] + questao_47[1][1] + questao_47[2][1] + questao_47[3][1] + questao_47[4][1] + questao_47[5][1] + questao_47[6][1] + questao_47[7][1] + questao_47[8][1] # Total da coluna não
                questao_47[9][2] = questao_47[9][0] + questao_47[9][1] # Total geral
                questao_47[0][2] = questao_47[0][0] + questao_47[0][1] # Nunca ou menos de uma vez por mês
                questao_47[1][2] = questao_47[1][0] + questao_47[1][1] # 1 a 3 vezes por mês
                questao_47[2][2] = questao_47[2][0] + questao_47[2][1] # 1 vez por semana
                questao_47[3][2] = questao_47[3][0] + questao_47[3][1] # 2 a 4 vezes por semana
                questao_47[4][2] = questao_47[4][0] + questao_47[4][1] # 6 a 8 vezes por semana
                questao_47[5][2] = questao_47[5][0] + questao_47[5][1] # 1 vez por dia
                questao_47[6][2] = questao_47[6][0] + questao_47[6][1] # 2 a 3 vezes por dia
                questao_47[7][2] = questao_47[7][0] + questao_47[7][1] # 4 a 6 vezes por dia
                questao_47[8][2] = questao_47[8][0] + questao_47[8][1] # Mais de 8 vezes por dia
                
                # Totais da tabela questão 48
                questao_48[9][0] = questao_48[0][0] + questao_48[1][0] + questao_48[2][0] + questao_48[3][0] + questao_48[4][0] + questao_48[5][0] + questao_48[6][0] + questao_48[7][0] + questao_48[8][0] # Total da coluna sim
                questao_48[9][1] = questao_48[0][1] + questao_48[1][1] + questao_48[2][1] + questao_48[3][1] + questao_48[4][1] + questao_48[5][1] + questao_48[6][1] + questao_48[7][1] + questao_48[8][1] # Total da coluna não
                questao_48[9][2] = questao_48[9][0] + questao_48[9][1] # Total geral
                questao_48[0][2] = questao_48[0][0] + questao_48[0][1] # Nunca ou menos de uma vez por mês
                questao_48[1][2] = questao_48[1][0] + questao_48[1][1] # 1 a 3 vezes por mês
                questao_48[2][2] = questao_48[2][0] + questao_48[2][1] # 1 vez por semana
                questao_48[3][2] = questao_48[3][0] + questao_48[3][1] # 2 a 4 vezes por semana
                questao_48[4][2] = questao_48[4][0] + questao_48[4][1] # 6 a 8 vezes por semana
                questao_48[5][2] = questao_48[5][0] + questao_48[5][1] # 1 vez por dia
                questao_48[6][2] = questao_48[6][0] + questao_48[6][1] # 2 a 3 vezes por dia
                questao_48[7][2] = questao_48[7][0] + questao_48[7][1] # 4 a 6 vezes por dia
                questao_48[8][2] = questao_48[8][0] + questao_48[8][1] # Mais de 8 vezes por dia
                
                # Totais da tabela questão 49
                questao_49[9][0] = questao_49[0][0] + questao_49[1][0] + questao_49[2][0] + questao_49[3][0] + questao_49[4][0] + questao_49[5][0] + questao_49[6][0] + questao_49[7][0] + questao_49[8][0] # Total da coluna sim
                questao_49[9][1] = questao_49[0][1] + questao_49[1][1] + questao_49[2][1] + questao_49[3][1] + questao_49[4][1] + questao_49[5][1] + questao_49[6][1] + questao_49[7][1] + questao_49[8][1] # Total da coluna não
                questao_49[9][2] = questao_49[9][0] + questao_49[9][1] # Total geral
                questao_49[0][2] = questao_49[0][0] + questao_49[0][1] # Nunca ou menos de uma vez por mês
                questao_49[1][2] = questao_49[1][0] + questao_49[1][1] # 1 a 3 vezes por mês
                questao_49[2][2] = questao_49[2][0] + questao_49[2][1] # 1 vez por semana
                questao_49[3][2] = questao_49[3][0] + questao_49[3][1] # 2 a 4 vezes por semana
                questao_49[4][2] = questao_49[4][0] + questao_49[4][1] # 6 a 8 vezes por semana
                questao_49[5][2] = questao_49[5][0] + questao_49[5][1] # 1 vez por dia
                questao_49[6][2] = questao_49[6][0] + questao_49[6][1] # 2 a 3 vezes por dia
                questao_49[7][2] = questao_49[7][0] + questao_49[7][1] # 4 a 6 vezes por dia
                questao_49[8][2] = questao_49[8][0] + questao_49[8][1] # Mais de 8 vezes por dia
                
                # Totais da tabela questão 50
                questao_50[9][0] = questao_50[0][0] + questao_50[1][0] + questao_50[2][0] + questao_50[3][0] + questao_50[4][0] + questao_50[5][0] + questao_50[6][0] + questao_50[7][0] + questao_50[8][0] # Total da coluna sim
                questao_50[9][1] = questao_50[0][1] + questao_50[1][1] + questao_50[2][1] + questao_50[3][1] + questao_50[4][1] + questao_50[5][1] + questao_50[6][1] + questao_50[7][1] + questao_50[8][1] # Total da coluna não
                questao_50[9][2] = questao_50[9][0] + questao_50[9][1] # Total geral
                questao_50[0][2] = questao_50[0][0] + questao_50[0][1] # Nunca ou menos de uma vez por mês
                questao_50[1][2] = questao_50[1][0] + questao_50[1][1] # 1 a 3 vezes por mês
                questao_50[2][2] = questao_50[2][0] + questao_50[2][1] # 1 vez por semana
                questao_50[3][2] = questao_50[3][0] + questao_50[3][1] # 2 a 4 vezes por semana
                questao_50[4][2] = questao_50[4][0] + questao_50[4][1] # 6 a 8 vezes por semana
                questao_50[5][2] = questao_50[5][0] + questao_50[5][1] # 1 vez por dia
                questao_50[6][2] = questao_50[6][0] + questao_50[6][1] # 2 a 3 vezes por dia
                questao_50[7][2] = questao_50[7][0] + questao_50[7][1] # 4 a 6 vezes por dia
                questao_50[8][2] = questao_50[8][0] + questao_50[8][1] # Mais de 8 vezes por dia
                
                # Totais da tabela questão 51
                questao_51[9][0] = questao_51[0][0] + questao_51[1][0] + questao_51[2][0] + questao_51[3][0] + questao_51[4][0] + questao_51[5][0] + questao_51[6][0] + questao_51[7][0] + questao_51[8][0] # Total da coluna sim
                questao_51[9][1] = questao_51[0][1] + questao_51[1][1] + questao_51[2][1] + questao_51[3][1] + questao_51[4][1] + questao_51[5][1] + questao_51[6][1] + questao_51[7][1] + questao_51[8][1] # Total da coluna não
                questao_51[9][2] = questao_51[9][0] + questao_51[9][1] # Total geral
                questao_51[0][2] = questao_51[0][0] + questao_51[0][1] # Nunca ou menos de uma vez por mês
                questao_51[1][2] = questao_51[1][0] + questao_51[1][1] # 1 a 3 vezes por mês
                questao_51[2][2] = questao_51[2][0] + questao_51[2][1] # 1 vez por semana
                questao_51[3][2] = questao_51[3][0] + questao_51[3][1] # 2 a 4 vezes por semana
                questao_51[4][2] = questao_51[4][0] + questao_51[4][1] # 6 a 8 vezes por semana
                questao_51[5][2] = questao_51[5][0] + questao_51[5][1] # 1 vez por dia
                questao_51[6][2] = questao_51[6][0] + questao_51[6][1] # 2 a 3 vezes por dia
                questao_51[7][2] = questao_51[7][0] + questao_51[7][1] # 4 a 6 vezes por dia
                questao_51[8][2] = questao_51[8][0] + questao_51[8][1] # Mais de 8 vezes por dia
                
                # Totais da tabela questão 52
                questao_52[9][0] = questao_52[0][0] + questao_52[1][0] + questao_52[2][0] + questao_52[3][0] + questao_52[4][0] + questao_52[5][0] + questao_52[6][0] + questao_52[7][0] + questao_52[8][0] # Total da coluna sim
                questao_52[9][1] = questao_52[0][1] + questao_52[1][1] + questao_52[2][1] + questao_52[3][1] + questao_52[4][1] + questao_52[5][1] + questao_52[6][1] + questao_52[7][1] + questao_52[8][1] # Total da coluna não
                questao_52[9][2] = questao_52[9][0] + questao_52[9][1] # Total geral
                questao_52[0][2] = questao_52[0][0] + questao_52[0][1] # Nunca ou menos de uma vez por mês
                questao_52[1][2] = questao_52[1][0] + questao_52[1][1] # 1 a 3 vezes por mês
                questao_52[2][2] = questao_52[2][0] + questao_52[2][1] # 1 vez por semana
                questao_52[3][2] = questao_52[3][0] + questao_52[3][1] # 2 a 4 vezes por semana
                questao_52[4][2] = questao_52[4][0] + questao_52[4][1] # 6 a 8 vezes por semana
                questao_52[5][2] = questao_52[5][0] + questao_52[5][1] # 1 vez por dia
                questao_52[6][2] = questao_52[6][0] + questao_52[6][1] # 2 a 3 vezes por dia
                questao_52[7][2] = questao_52[7][0] + questao_52[7][1] # 4 a 6 vezes por dia
                questao_52[8][2] = questao_52[8][0] + questao_52[8][1] # Mais de 8 vezes por dia
                
                # Totais da tabela questão 53
                questao_53[9][0] = questao_53[0][0] + questao_53[1][0] + questao_53[2][0] + questao_53[3][0] + questao_53[4][0] + questao_53[5][0] + questao_53[6][0] + questao_53[7][0] + questao_53[8][0] # Total da coluna sim
                questao_53[9][1] = questao_53[0][1] + questao_53[1][1] + questao_53[2][1] + questao_53[3][1] + questao_53[4][1] + questao_53[5][1] + questao_53[6][1] + questao_53[7][1] + questao_53[8][1] # Total da coluna não
                questao_53[9][2] = questao_53[9][0] + questao_53[9][1] # Total geral
                questao_53[0][2] = questao_53[0][0] + questao_53[0][1] # Nunca ou menos de uma vez por mês
                questao_53[1][2] = questao_53[1][0] + questao_53[1][1] # 1 a 3 vezes por mês
                questao_53[2][2] = questao_53[2][0] + questao_53[2][1] # 1 vez por semana
                questao_53[3][2] = questao_53[3][0] + questao_53[3][1] # 2 a 4 vezes por semana
                questao_53[4][2] = questao_53[4][0] + questao_53[4][1] # 6 a 8 vezes por semana
                questao_53[5][2] = questao_53[5][0] + questao_53[5][1] # 1 vez por dia
                questao_53[6][2] = questao_53[6][0] + questao_53[6][1] # 2 a 3 vezes por dia
                questao_53[7][2] = questao_53[7][0] + questao_53[7][1] # 4 a 6 vezes por dia
                questao_53[8][2] = questao_53[8][0] + questao_53[8][1] # Mais de 8 vezes por dia
                
                # Totais da tabela questão 54
                questao_54[9][0] = questao_54[0][0] + questao_54[1][0] + questao_54[2][0] + questao_54[3][0] + questao_54[4][0] + questao_54[5][0] + questao_54[6][0] + questao_54[7][0] + questao_54[8][0] # Total da coluna sim
                questao_54[9][1] = questao_54[0][1] + questao_54[1][1] + questao_54[2][1] + questao_54[3][1] + questao_54[4][1] + questao_54[5][1] + questao_54[6][1] + questao_54[7][1] + questao_54[8][1] # Total da coluna não
                questao_54[9][2] = questao_54[9][0] + questao_54[9][1] # Total geral
                questao_54[0][2] = questao_54[0][0] + questao_54[0][1] # Nunca ou menos de uma vez por mês
                questao_54[1][2] = questao_54[1][0] + questao_54[1][1] # 1 a 3 vezes por mês
                questao_54[2][2] = questao_54[2][0] + questao_54[2][1] # 1 vez por semana
                questao_54[3][2] = questao_54[3][0] + questao_54[3][1] # 2 a 4 vezes por semana
                questao_54[4][2] = questao_54[4][0] + questao_54[4][1] # 6 a 8 vezes por semana
                questao_54[5][2] = questao_54[5][0] + questao_54[5][1] # 1 vez por dia
                questao_54[6][2] = questao_54[6][0] + questao_54[6][1] # 2 a 3 vezes por dia
                questao_54[7][2] = questao_54[7][0] + questao_54[7][1] # 4 a 6 vezes por dia
                questao_54[8][2] = questao_54[8][0] + questao_54[8][1] # Mais de 8 vezes por dia
        
        
        # Montagem das tabelas de valores esperados
        sexo_esperado[0][0] = (sexo[0][2] / sexo[3][2]) * sexo[3][0] # masculino sim
        sexo_esperado[0][1] = (sexo[0][2] / sexo[3][2]) * sexo[3][1] # masculino não
        sexo_esperado[1][0] = (sexo[1][2] / sexo[3][2]) * sexo[3][0] # feminino sim
        sexo_esperado[1][1] = (sexo[1][2] / sexo[3][2]) * sexo[3][1] # feminino não
        sexo_esperado[2][0] = (sexo[2][2] / sexo[3][2]) * sexo[3][0] # outro sim
        sexo_esperado[2][1] = (sexo[2][2] / sexo[3][2]) * sexo[3][1] # outro não
        
        raca_esperado[0][0] = (raca[0][2] / raca[5][2]) * raca[5][0] # Amarela sim
        raca_esperado[0][1] = (raca[0][2] / raca[5][2]) * raca[5][1] # Amarela não
        raca_esperado[1][0] = (raca[1][2] / raca[5][2]) * raca[5][0] # Branca sim
        raca_esperado[1][1] = (raca[1][2] / raca[5][2]) * raca[5][1] # Branca não
        raca_esperado[2][0] = (raca[2][2] / raca[5][2]) * raca[5][0] # Indígena sim
        raca_esperado[2][1] = (raca[2][2] / raca[5][2]) * raca[5][1] # Indígena não
        raca_esperado[3][0] = (raca[3][2] / raca[5][2]) * raca[5][0] # Parda sim
        raca_esperado[3][1] = (raca[3][2] / raca[5][2]) * raca[5][1] # Parda não
        raca_esperado[4][0] = (raca[4][2] / raca[5][2]) * raca[5][0] # Preta sim
        raca_esperado[4][1] = (raca[4][2] / raca[5][2]) * raca[5][1] # Preta não
        
        questao_73_esperado[0][0] = (questao_73[0][2] / questao_73[2][2]) * questao_73[2][0] # Sim sim
        questao_73_esperado[0][1] = (questao_73[0][2] / questao_73[2][2]) * questao_73[2][1] # Não não
        questao_73_esperado[1][0] = (questao_73[1][2] / questao_73[2][2]) * questao_73[2][0] # Sim sim
        questao_73_esperado[1][1] = (questao_73[1][2] / questao_73[2][2]) * questao_73[2][1] # Não não
        
        questao_75_esperado[0][0] = (questao_75[0][2] / questao_75[7][2]) * questao_75[7][0] # Nenhum dia nos últimos 30 dias (0 dia) sim
        questao_75_esperado[0][1] = (questao_75[0][2] / questao_75[7][2]) * questao_75[7][1] # Nenhum dia nos últimos 30 dias (0 dia) não
        questao_75_esperado[1][0] = (questao_75[1][2] / questao_75[7][2]) * questao_75[7][0] # 1 ou 2 dias nos últimos 30 dias sim
        questao_75_esperado[1][1] = (questao_75[1][2] / questao_75[7][2]) * questao_75[7][1] # 1 ou 2 dias nos últimos 30 dias não
        questao_75_esperado[2][0] = (questao_75[2][2] / questao_75[7][2]) * questao_75[7][0] # 3 a 5 dias nos últimos 30 dias sim
        questao_75_esperado[2][1] = (questao_75[2][2] / questao_75[7][2]) * questao_75[7][1] # 3 a 5 dias nos últimos 30 dias não
        questao_75_esperado[3][0] = (questao_75[3][2] / questao_75[7][2]) * questao_75[7][0] # 6 a 9 dias nos últimos 30 dias sim
        questao_75_esperado[3][1] = (questao_75[3][2] / questao_75[7][2]) * questao_75[7][1] # 6 a 9 dias nos últimos 30 dias não
        questao_75_esperado[4][0] = (questao_75[4][2] / questao_75[7][2]) * questao_75[7][0] # 10 a 19 dias nos últimos 30 dias sim
        questao_75_esperado[4][1] = (questao_75[4][2] / questao_75[7][2]) * questao_75[7][1] # 10 a 19 dias nos últimos 30 dias não
        questao_75_esperado[5][0] = (questao_75[5][2] / questao_75[7][2]) * questao_75[7][0] # 20 a 29 dias nos últimos 30 dias sim
        questao_75_esperado[5][1] = (questao_75[5][2] / questao_75[7][2]) * questao_75[7][1] # 20 a 29 dias nos últimos 30 dias não
        questao_75_esperado[6][0] = (questao_75[6][2] / questao_75[7][2]) * questao_75[7][0] # Todos os dias nos últimos 30 dias sim
        questao_75_esperado[6][1] = (questao_75[6][2] / questao_75[7][2]) * questao_75[7][1] # Todos os dias nos últimos 30 dias não
        
        questao_79_esperado[0][0] = (questao_79[0][2] / questao_79[10][2]) * questao_79[10][0]
        questao_79_esperado[0][1] = (questao_79[0][2] / questao_79[10][2]) * questao_79[10][1]
        questao_79_esperado[1][0] = (questao_79[1][2] / questao_79[10][2]) * questao_79[10][0]
        questao_79_esperado[1][1] = (questao_79[1][2] / questao_79[10][2]) * questao_79[10][1]
        questao_79_esperado[2][0] = (questao_79[2][2] / questao_79[10][2]) * questao_79[10][0]
        questao_79_esperado[2][1] = (questao_79[2][2] / questao_79[10][2]) * questao_79[10][1]
        questao_79_esperado[3][0] = (questao_79[3][2] / questao_79[10][2]) * questao_79[10][0]
        questao_79_esperado[3][1] = (questao_79[3][2] / questao_79[10][2]) * questao_79[10][1]
        questao_79_esperado[4][0] = (questao_79[4][2] / questao_79[10][2]) * questao_79[10][0]
        questao_79_esperado[4][1] = (questao_79[4][2] / questao_79[10][2]) * questao_79[10][1]
        questao_79_esperado[5][0] = (questao_79[5][2] / questao_79[10][2]) * questao_79[10][0]
        questao_79_esperado[5][1] = (questao_79[5][2] / questao_79[10][2]) * questao_79[10][1]
        questao_79_esperado[6][0] = (questao_79[6][2] / questao_79[10][2]) * questao_79[10][0]
        questao_79_esperado[6][1] = (questao_79[6][2] / questao_79[10][2]) * questao_79[10][1]
        questao_79_esperado[7][0] = (questao_79[7][2] / questao_79[10][2]) * questao_79[10][0]
        questao_79_esperado[7][1] = (questao_79[7][2] / questao_79[10][2]) * questao_79[10][1]
        questao_79_esperado[8][0] = (questao_79[8][2] / questao_79[10][2]) * questao_79[10][0]
        questao_79_esperado[8][1] = (questao_79[8][2] / questao_79[10][2]) * questao_79[10][1]
        questao_79_esperado[9][0] = (questao_79[9][2] / questao_79[10][2]) * questao_79[10][0]
        questao_79_esperado[9][1] = (questao_79[9][2] / questao_79[10][2]) * questao_79[10][1]
        
        questao_84_esperado[0][0] = (questao_84[0][2] / questao_84[7][2]) * questao_84[7][0]
        questao_84_esperado[0][1] = (questao_84[0][2] / questao_84[7][2]) * questao_84[7][1]
        questao_84_esperado[1][0] = (questao_84[1][2] / questao_84[7][2]) * questao_84[7][0]
        questao_84_esperado[1][1] = (questao_84[1][2] / questao_84[7][2]) * questao_84[7][1]
        questao_84_esperado[2][0] = (questao_84[2][2] / questao_84[7][2]) * questao_84[7][0]
        questao_84_esperado[2][1] = (questao_84[2][2] / questao_84[7][2]) * questao_84[7][1]
        questao_84_esperado[3][0] = (questao_84[3][2] / questao_84[7][2]) * questao_84[7][0]
        questao_84_esperado[3][1] = (questao_84[3][2] / questao_84[7][2]) * questao_84[7][1]
        questao_84_esperado[4][0] = (questao_84[4][2] / questao_84[7][2]) * questao_84[7][0]
        questao_84_esperado[4][1] = (questao_84[4][2] / questao_84[7][2]) * questao_84[7][1]
        questao_84_esperado[5][0] = (questao_84[5][2] / questao_84[7][2]) * questao_84[7][0]
        questao_84_esperado[5][1] = (questao_84[5][2] / questao_84[7][2]) * questao_84[7][1]
        questao_84_esperado[6][0] = (questao_84[6][2] / questao_84[7][2]) * questao_84[7][0]
        questao_84_esperado[6][1] = (questao_84[6][2] / questao_84[7][2]) * questao_84[7][1]
        
        questao_92_esperado[0][0] = (questao_92[0][2] / questao_92[5][2]) * questao_92[5][0]
        questao_92_esperado[0][1] = (questao_92[0][2] / questao_92[5][2]) * questao_92[5][1]
        questao_92_esperado[1][0] = (questao_92[1][2] / questao_92[5][2]) * questao_92[5][0]
        questao_92_esperado[1][1] = (questao_92[1][2] / questao_92[5][2]) * questao_92[5][1]
        questao_92_esperado[2][0] = (questao_92[2][2] / questao_92[5][2]) * questao_92[5][0]
        questao_92_esperado[2][1] = (questao_92[2][2] / questao_92[5][2]) * questao_92[5][1]
        questao_92_esperado[3][0] = (questao_92[3][2] / questao_92[5][2]) * questao_92[5][0]
        questao_92_esperado[3][1] = (questao_92[3][2] / questao_92[5][2]) * questao_92[5][1]
        questao_92_esperado[4][0] = (questao_92[4][2] / questao_92[5][2]) * questao_92[5][0]
        questao_92_esperado[4][1] = (questao_92[4][2] / questao_92[5][2]) * questao_92[5][1]
        
        questao_111_esperado[0][0] = (questao_111[0][2] / questao_111[6][2]) * questao_111[6][0]
        questao_111_esperado[0][1] = (questao_111[0][2] / questao_111[6][2]) * questao_111[6][1]
        questao_111_esperado[1][0] = (questao_111[1][2] / questao_111[6][2]) * questao_111[6][0]
        questao_111_esperado[1][1] = (questao_111[1][2] / questao_111[6][2]) * questao_111[6][1]
        questao_111_esperado[2][0] = (questao_111[2][2] / questao_111[6][2]) * questao_111[6][0]
        questao_111_esperado[2][1] = (questao_111[2][2] / questao_111[6][2]) * questao_111[6][1]
        questao_111_esperado[3][0] = (questao_111[3][2] / questao_111[6][2]) * questao_111[6][0]
        questao_111_esperado[3][1] = (questao_111[3][2] / questao_111[6][2]) * questao_111[6][1]
        questao_111_esperado[4][0] = (questao_111[4][2] / questao_111[6][2]) * questao_111[6][0]
        questao_111_esperado[4][1] = (questao_111[4][2] / questao_111[6][2]) * questao_111[6][1]
        questao_111_esperado[5][0] = (questao_111[5][2] / questao_111[6][2]) * questao_111[6][0]
        questao_111_esperado[5][1] = (questao_111[5][2] / questao_111[6][2]) * questao_111[6][1]
        
        questao_113_esperado[0][0] = (questao_113[0][2] / questao_113[4][2]) * questao_113[4][0]
        questao_113_esperado[0][1] = (questao_113[0][2] / questao_113[4][2]) * questao_113[4][1]
        questao_113_esperado[1][0] = (questao_113[1][2] / questao_113[4][2]) * questao_113[4][0]
        questao_113_esperado[1][1] = (questao_113[1][2] / questao_113[4][2]) * questao_113[4][1]
        questao_113_esperado[2][0] = (questao_113[2][2] / questao_113[4][2]) * questao_113[4][0]
        questao_113_esperado[2][1] = (questao_113[2][2] / questao_113[4][2]) * questao_113[4][1]
        questao_113_esperado[3][0] = (questao_113[3][2] / questao_113[4][2]) * questao_113[4][0]
        questao_113_esperado[3][1] = (questao_113[3][2] / questao_113[4][2]) * questao_113[4][1]
        
        questao_25_esperado[0][0] = (questao_25[0][2] / questao_25[9][2]) * questao_25[9][0]
        questao_25_esperado[0][1] = (questao_25[0][2] / questao_25[9][2]) * questao_25[9][1]
        questao_25_esperado[1][0] = (questao_25[1][2] / questao_25[9][2]) * questao_25[9][0]
        questao_25_esperado[1][1] = (questao_25[1][2] / questao_25[9][2]) * questao_25[9][1]
        questao_25_esperado[2][0] = (questao_25[2][2] / questao_25[9][2]) * questao_25[9][0]
        questao_25_esperado[2][1] = (questao_25[2][2] / questao_25[9][2]) * questao_25[9][1]
        questao_25_esperado[3][0] = (questao_25[3][2] / questao_25[9][2]) * questao_25[9][0]
        questao_25_esperado[3][1] = (questao_25[3][2] / questao_25[9][2]) * questao_25[9][1]
        questao_25_esperado[4][0] = (questao_25[4][2] / questao_25[9][2]) * questao_25[9][0]
        questao_25_esperado[4][1] = (questao_25[4][2] / questao_25[9][2]) * questao_25[9][1]
        questao_25_esperado[5][0] = (questao_25[5][2] / questao_25[9][2]) * questao_25[9][0]
        questao_25_esperado[5][1] = (questao_25[5][2] / questao_25[9][2]) * questao_25[9][1]
        questao_25_esperado[6][0] = (questao_25[6][2] / questao_25[9][2]) * questao_25[9][0]
        questao_25_esperado[6][1] = (questao_25[6][2] / questao_25[9][2]) * questao_25[9][1]
        questao_25_esperado[7][0] = (questao_25[7][2] / questao_25[9][2]) * questao_25[9][0]
        questao_25_esperado[7][1] = (questao_25[7][2] / questao_25[9][2]) * questao_25[9][1]
        questao_25_esperado[8][0] = (questao_25[8][2] / questao_25[9][2]) * questao_25[9][0]
        questao_25_esperado[8][1] = (questao_25[8][2] / questao_25[9][2]) * questao_25[9][1]
        
        questao_26_esperado[0][0] = (questao_26[0][2] / questao_26[9][2]) * questao_26[9][0]
        questao_26_esperado[0][1] = (questao_26[0][2] / questao_26[9][2]) * questao_26[9][1]
        questao_26_esperado[1][0] = (questao_26[1][2] / questao_26[9][2]) * questao_26[9][0]
        questao_26_esperado[1][1] = (questao_26[1][2] / questao_26[9][2]) * questao_26[9][1]
        questao_26_esperado[2][0] = (questao_26[2][2] / questao_26[9][2]) * questao_26[9][0]
        questao_26_esperado[2][1] = (questao_26[2][2] / questao_26[9][2]) * questao_26[9][1]
        questao_26_esperado[3][0] = (questao_26[3][2] / questao_26[9][2]) * questao_26[9][0]
        questao_26_esperado[3][1] = (questao_26[3][2] / questao_26[9][2]) * questao_26[9][1]
        questao_26_esperado[4][0] = (questao_26[4][2] / questao_26[9][2]) * questao_26[9][0]
        questao_26_esperado[4][1] = (questao_26[4][2] / questao_26[9][2]) * questao_26[9][1]
        questao_26_esperado[5][0] = (questao_26[5][2] / questao_26[9][2]) * questao_26[9][0]
        questao_26_esperado[5][1] = (questao_26[5][2] / questao_26[9][2]) * questao_26[9][1]
        questao_26_esperado[6][0] = (questao_26[6][2] / questao_26[9][2]) * questao_26[9][0]
        questao_26_esperado[6][1] = (questao_26[6][2] / questao_26[9][2]) * questao_26[9][1]
        questao_26_esperado[7][0] = (questao_26[7][2] / questao_26[9][2]) * questao_26[9][0]
        questao_26_esperado[7][1] = (questao_26[7][2] / questao_26[9][2]) * questao_26[9][1]
        questao_26_esperado[8][0] = (questao_26[8][2] / questao_26[9][2]) * questao_26[9][0]
        questao_26_esperado[8][1] = (questao_26[8][2] / questao_26[9][2]) * questao_26[9][1]
        
        questao_27_esperado[0][0] = (questao_27[0][2] / questao_27[9][2]) * questao_27[9][0]
        questao_27_esperado[0][1] = (questao_27[0][2] / questao_27[9][2]) * questao_27[9][1]
        questao_27_esperado[1][0] = (questao_27[1][2] / questao_27[9][2]) * questao_27[9][0]
        questao_27_esperado[1][1] = (questao_27[1][2] / questao_27[9][2]) * questao_27[9][1]
        questao_27_esperado[2][0] = (questao_27[2][2] / questao_27[9][2]) * questao_27[9][0]
        questao_27_esperado[2][1] = (questao_27[2][2] / questao_27[9][2]) * questao_27[9][1]
        questao_27_esperado[3][0] = (questao_27[3][2] / questao_27[9][2]) * questao_27[9][0]
        questao_27_esperado[3][1] = (questao_27[3][2] / questao_27[9][2]) * questao_27[9][1]
        questao_27_esperado[4][0] = (questao_27[4][2] / questao_27[9][2]) * questao_27[9][0]
        questao_27_esperado[4][1] = (questao_27[4][2] / questao_27[9][2]) * questao_27[9][1]
        questao_27_esperado[5][0] = (questao_27[5][2] / questao_27[9][2]) * questao_27[9][0]
        questao_27_esperado[5][1] = (questao_27[5][2] / questao_27[9][2]) * questao_27[9][1]
        questao_27_esperado[6][0] = (questao_27[6][2] / questao_27[9][2]) * questao_27[9][0]
        questao_27_esperado[6][1] = (questao_27[6][2] / questao_27[9][2]) * questao_27[9][1]
        questao_27_esperado[7][0] = (questao_27[7][2] / questao_27[9][2]) * questao_27[9][0]
        questao_27_esperado[7][1] = (questao_27[7][2] / questao_27[9][2]) * questao_27[9][1]
        questao_27_esperado[8][0] = (questao_27[8][2] / questao_27[9][2]) * questao_27[9][0]
        questao_27_esperado[8][1] = (questao_27[8][2] / questao_27[9][2]) * questao_27[9][1]
        
        questao_28_esperado[0][0] = (questao_28[0][2] / questao_28[9][2]) * questao_28[9][0]
        questao_28_esperado[0][1] = (questao_28[0][2] / questao_28[9][2]) * questao_28[9][1]
        questao_28_esperado[1][0] = (questao_28[1][2] / questao_28[9][2]) * questao_28[9][0]
        questao_28_esperado[1][1] = (questao_28[1][2] / questao_28[9][2]) * questao_28[9][1]
        questao_28_esperado[2][0] = (questao_28[2][2] / questao_28[9][2]) * questao_28[9][0]
        questao_28_esperado[2][1] = (questao_28[2][2] / questao_28[9][2]) * questao_28[9][1]
        questao_28_esperado[3][0] = (questao_28[3][2] / questao_28[9][2]) * questao_28[9][0]
        questao_28_esperado[3][1] = (questao_28[3][2] / questao_28[9][2]) * questao_28[9][1]
        questao_28_esperado[4][0] = (questao_28[4][2] / questao_28[9][2]) * questao_28[9][0]
        questao_28_esperado[4][1] = (questao_28[4][2] / questao_28[9][2]) * questao_28[9][1]
        questao_28_esperado[5][0] = (questao_28[5][2] / questao_28[9][2]) * questao_28[9][0]
        questao_28_esperado[5][1] = (questao_28[5][2] / questao_28[9][2]) * questao_28[9][1]
        questao_28_esperado[6][0] = (questao_28[6][2] / questao_28[9][2]) * questao_28[9][0]
        questao_28_esperado[6][1] = (questao_28[6][2] / questao_28[9][2]) * questao_28[9][1]
        questao_28_esperado[7][0] = (questao_28[7][2] / questao_28[9][2]) * questao_28[9][0]
        questao_28_esperado[7][1] = (questao_28[7][2] / questao_28[9][2]) * questao_28[9][1]
        questao_28_esperado[8][0] = (questao_28[8][2] / questao_28[9][2]) * questao_28[9][0]
        questao_28_esperado[8][1] = (questao_28[8][2] / questao_28[9][2]) * questao_28[9][1]
        
        questao_29_esperado[0][0] = (questao_29[0][2] / questao_29[9][2]) * questao_29[9][0]
        questao_29_esperado[0][1] = (questao_29[0][2] / questao_29[9][2]) * questao_29[9][1]
        questao_29_esperado[1][0] = (questao_29[1][2] / questao_29[9][2]) * questao_29[9][0]
        questao_29_esperado[1][1] = (questao_29[1][2] / questao_29[9][2]) * questao_29[9][1]
        questao_29_esperado[2][0] = (questao_29[2][2] / questao_29[9][2]) * questao_29[9][0]
        questao_29_esperado[2][1] = (questao_29[2][2] / questao_29[9][2]) * questao_29[9][1]
        questao_29_esperado[3][0] = (questao_29[3][2] / questao_29[9][2]) * questao_29[9][0]
        questao_29_esperado[3][1] = (questao_29[3][2] / questao_29[9][2]) * questao_29[9][1]
        questao_29_esperado[4][0] = (questao_29[4][2] / questao_29[9][2]) * questao_29[9][0]
        questao_29_esperado[4][1] = (questao_29[4][2] / questao_29[9][2]) * questao_29[9][1]
        questao_29_esperado[5][0] = (questao_29[5][2] / questao_29[9][2]) * questao_29[9][0]
        questao_29_esperado[5][1] = (questao_29[5][2] / questao_29[9][2]) * questao_29[9][1]
        questao_29_esperado[6][0] = (questao_29[6][2] / questao_29[9][2]) * questao_29[9][0]
        questao_29_esperado[6][1] = (questao_29[6][2] / questao_29[9][2]) * questao_29[9][1]
        questao_29_esperado[7][0] = (questao_29[7][2] / questao_29[9][2]) * questao_29[9][0]
        questao_29_esperado[7][1] = (questao_29[7][2] / questao_29[9][2]) * questao_29[9][1]
        questao_29_esperado[8][0] = (questao_29[8][2] / questao_29[9][2]) * questao_29[9][0]
        questao_29_esperado[8][1] = (questao_29[8][2] / questao_29[9][2]) * questao_29[9][1]
        
        questao_30_esperado[0][0] = (questao_30[0][2] / questao_30[9][2]) * questao_30[9][0]
        questao_30_esperado[0][1] = (questao_30[0][2] / questao_30[9][2]) * questao_30[9][1]
        questao_30_esperado[1][0] = (questao_30[1][2] / questao_30[9][2]) * questao_30[9][0]
        questao_30_esperado[1][1] = (questao_30[1][2] / questao_30[9][2]) * questao_30[9][1]
        questao_30_esperado[2][0] = (questao_30[2][2] / questao_30[9][2]) * questao_30[9][0]
        questao_30_esperado[2][1] = (questao_30[2][2] / questao_30[9][2]) * questao_30[9][1]
        questao_30_esperado[3][0] = (questao_30[3][2] / questao_30[9][2]) * questao_30[9][0]
        questao_30_esperado[3][1] = (questao_30[3][2] / questao_30[9][2]) * questao_30[9][1]
        questao_30_esperado[4][0] = (questao_30[4][2] / questao_30[9][2]) * questao_30[9][0]
        questao_30_esperado[4][1] = (questao_30[4][2] / questao_30[9][2]) * questao_30[9][1]
        questao_30_esperado[5][0] = (questao_30[5][2] / questao_30[9][2]) * questao_30[9][0]
        questao_30_esperado[5][1] = (questao_30[5][2] / questao_30[9][2]) * questao_30[9][1]
        questao_30_esperado[6][0] = (questao_30[6][2] / questao_30[9][2]) * questao_30[9][0]
        questao_30_esperado[6][1] = (questao_30[6][2] / questao_30[9][2]) * questao_30[9][1]
        questao_30_esperado[7][0] = (questao_30[7][2] / questao_30[9][2]) * questao_30[9][0]
        questao_30_esperado[7][1] = (questao_30[7][2] / questao_30[9][2]) * questao_30[9][1]
        questao_30_esperado[8][0] = (questao_30[8][2] / questao_30[9][2]) * questao_30[9][0]
        questao_30_esperado[8][1] = (questao_30[8][2] / questao_30[9][2]) * questao_30[9][1]
        
        questao_31_esperado[0][0] = (questao_31[0][2] / questao_31[9][2]) * questao_31[9][0]
        questao_31_esperado[0][1] = (questao_31[0][2] / questao_31[9][2]) * questao_31[9][1]
        questao_31_esperado[1][0] = (questao_31[1][2] / questao_31[9][2]) * questao_31[9][0]
        questao_31_esperado[1][1] = (questao_31[1][2] / questao_31[9][2]) * questao_31[9][1]
        questao_31_esperado[2][0] = (questao_31[2][2] / questao_31[9][2]) * questao_31[9][0]
        questao_31_esperado[2][1] = (questao_31[2][2] / questao_31[9][2]) * questao_31[9][1]
        questao_31_esperado[3][0] = (questao_31[3][2] / questao_31[9][2]) * questao_31[9][0]
        questao_31_esperado[3][1] = (questao_31[3][2] / questao_31[9][2]) * questao_31[9][1]
        questao_31_esperado[4][0] = (questao_31[4][2] / questao_31[9][2]) * questao_31[9][0]
        questao_31_esperado[4][1] = (questao_31[4][2] / questao_31[9][2]) * questao_31[9][1]
        questao_31_esperado[5][0] = (questao_31[5][2] / questao_31[9][2]) * questao_31[9][0]
        questao_31_esperado[5][1] = (questao_31[5][2] / questao_31[9][2]) * questao_31[9][1]
        questao_31_esperado[6][0] = (questao_31[6][2] / questao_31[9][2]) * questao_31[9][0]
        questao_31_esperado[6][1] = (questao_31[6][2] / questao_31[9][2]) * questao_31[9][1]
        questao_31_esperado[7][0] = (questao_31[7][2] / questao_31[9][2]) * questao_31[9][0]
        questao_31_esperado[7][1] = (questao_31[7][2] / questao_31[9][2]) * questao_31[9][1]
        questao_31_esperado[8][0] = (questao_31[8][2] / questao_31[9][2]) * questao_31[9][0]
        questao_31_esperado[8][1] = (questao_31[8][2] / questao_31[9][2]) * questao_31[9][1]
        
        questao_32_esperado[0][0] = (questao_32[0][2] / questao_32[9][2]) * questao_32[9][0]
        questao_32_esperado[0][1] = (questao_32[0][2] / questao_32[9][2]) * questao_32[9][1]
        questao_32_esperado[1][0] = (questao_32[1][2] / questao_32[9][2]) * questao_32[9][0]
        questao_32_esperado[1][1] = (questao_32[1][2] / questao_32[9][2]) * questao_32[9][1]
        questao_32_esperado[2][0] = (questao_32[2][2] / questao_32[9][2]) * questao_32[9][0]
        questao_32_esperado[2][1] = (questao_32[2][2] / questao_32[9][2]) * questao_32[9][1]
        questao_32_esperado[3][0] = (questao_32[3][2] / questao_32[9][2]) * questao_32[9][0]
        questao_32_esperado[3][1] = (questao_32[3][2] / questao_32[9][2]) * questao_32[9][1]
        questao_32_esperado[4][0] = (questao_32[4][2] / questao_32[9][2]) * questao_32[9][0]
        questao_32_esperado[4][1] = (questao_32[4][2] / questao_32[9][2]) * questao_32[9][1]
        questao_32_esperado[5][0] = (questao_32[5][2] / questao_32[9][2]) * questao_32[9][0]
        questao_32_esperado[5][1] = (questao_32[5][2] / questao_32[9][2]) * questao_32[9][1]
        questao_32_esperado[6][0] = (questao_32[6][2] / questao_32[9][2]) * questao_32[9][0]
        questao_32_esperado[6][1] = (questao_32[6][2] / questao_32[9][2]) * questao_32[9][1]
        questao_32_esperado[7][0] = (questao_32[7][2] / questao_32[9][2]) * questao_32[9][0]
        questao_32_esperado[7][1] = (questao_32[7][2] / questao_32[9][2]) * questao_32[9][1]
        questao_32_esperado[8][0] = (questao_32[8][2] / questao_32[9][2]) * questao_32[9][0]
        questao_32_esperado[8][1] = (questao_32[8][2] / questao_32[9][2]) * questao_32[9][1]
        
        questao_33_esperado[0][0] = (questao_33[0][2] / questao_33[9][2]) * questao_33[9][0]
        questao_33_esperado[0][1] = (questao_33[0][2] / questao_33[9][2]) * questao_33[9][1]
        questao_33_esperado[1][0] = (questao_33[1][2] / questao_33[9][2]) * questao_33[9][0]
        questao_33_esperado[1][1] = (questao_33[1][2] / questao_33[9][2]) * questao_33[9][1]
        questao_33_esperado[2][0] = (questao_33[2][2] / questao_33[9][2]) * questao_33[9][0]
        questao_33_esperado[2][1] = (questao_33[2][2] / questao_33[9][2]) * questao_33[9][1]
        questao_33_esperado[3][0] = (questao_33[3][2] / questao_33[9][2]) * questao_33[9][0]
        questao_33_esperado[3][1] = (questao_33[3][2] / questao_33[9][2]) * questao_33[9][1]
        questao_33_esperado[4][0] = (questao_33[4][2] / questao_33[9][2]) * questao_33[9][0]
        questao_33_esperado[4][1] = (questao_33[4][2] / questao_33[9][2]) * questao_33[9][1]
        questao_33_esperado[5][0] = (questao_33[5][2] / questao_33[9][2]) * questao_33[9][0]
        questao_33_esperado[5][1] = (questao_33[5][2] / questao_33[9][2]) * questao_33[9][1]
        questao_33_esperado[6][0] = (questao_33[6][2] / questao_33[9][2]) * questao_33[9][0]
        questao_33_esperado[6][1] = (questao_33[6][2] / questao_33[9][2]) * questao_33[9][1]
        questao_33_esperado[7][0] = (questao_33[7][2] / questao_33[9][2]) * questao_33[9][0]
        questao_33_esperado[7][1] = (questao_33[7][2] / questao_33[9][2]) * questao_33[9][1]
        questao_33_esperado[8][0] = (questao_33[8][2] / questao_33[9][2]) * questao_33[9][0]
        questao_33_esperado[8][1] = (questao_33[8][2] / questao_33[9][2]) * questao_33[9][1]
        
        questao_34_esperado[0][0] = (questao_34[0][2] / questao_34[9][2]) * questao_34[9][0]
        questao_34_esperado[0][1] = (questao_34[0][2] / questao_34[9][2]) * questao_34[9][1]
        questao_34_esperado[1][0] = (questao_34[1][2] / questao_34[9][2]) * questao_34[9][0]
        questao_34_esperado[1][1] = (questao_34[1][2] / questao_34[9][2]) * questao_34[9][1]
        questao_34_esperado[2][0] = (questao_34[2][2] / questao_34[9][2]) * questao_34[9][0]
        questao_34_esperado[2][1] = (questao_34[2][2] / questao_34[9][2]) * questao_34[9][1]
        questao_34_esperado[3][0] = (questao_34[3][2] / questao_34[9][2]) * questao_34[9][0]
        questao_34_esperado[3][1] = (questao_34[3][2] / questao_34[9][2]) * questao_34[9][1]
        questao_34_esperado[4][0] = (questao_34[4][2] / questao_34[9][2]) * questao_34[9][0]
        questao_34_esperado[4][1] = (questao_34[4][2] / questao_34[9][2]) * questao_34[9][1]
        questao_34_esperado[5][0] = (questao_34[5][2] / questao_34[9][2]) * questao_34[9][0]
        questao_34_esperado[5][1] = (questao_34[5][2] / questao_34[9][2]) * questao_34[9][1]
        questao_34_esperado[6][0] = (questao_34[6][2] / questao_34[9][2]) * questao_34[9][0]
        questao_34_esperado[6][1] = (questao_34[6][2] / questao_34[9][2]) * questao_34[9][1]
        questao_34_esperado[7][0] = (questao_34[7][2] / questao_34[9][2]) * questao_34[9][0]
        questao_34_esperado[7][1] = (questao_34[7][2] / questao_34[9][2]) * questao_34[9][1]
        questao_34_esperado[8][0] = (questao_34[8][2] / questao_34[9][2]) * questao_34[9][0]
        questao_34_esperado[8][1] = (questao_34[8][2] / questao_34[9][2]) * questao_34[9][1]
        
        questao_35_esperado[0][0] = (questao_35[0][2] / questao_35[9][2]) * questao_35[9][0]
        questao_35_esperado[0][1] = (questao_35[0][2] / questao_35[9][2]) * questao_35[9][1]
        questao_35_esperado[1][0] = (questao_35[1][2] / questao_35[9][2]) * questao_35[9][0]
        questao_35_esperado[1][1] = (questao_35[1][2] / questao_35[9][2]) * questao_35[9][1]
        questao_35_esperado[2][0] = (questao_35[2][2] / questao_35[9][2]) * questao_35[9][0]
        questao_35_esperado[2][1] = (questao_35[2][2] / questao_35[9][2]) * questao_35[9][1]
        questao_35_esperado[3][0] = (questao_35[3][2] / questao_35[9][2]) * questao_35[9][0]
        questao_35_esperado[3][1] = (questao_35[3][2] / questao_35[9][2]) * questao_35[9][1]
        questao_35_esperado[4][0] = (questao_35[4][2] / questao_35[9][2]) * questao_35[9][0]
        questao_35_esperado[4][1] = (questao_35[4][2] / questao_35[9][2]) * questao_35[9][1]
        questao_35_esperado[5][0] = (questao_35[5][2] / questao_35[9][2]) * questao_35[9][0]
        questao_35_esperado[5][1] = (questao_35[5][2] / questao_35[9][2]) * questao_35[9][1]
        questao_35_esperado[6][0] = (questao_35[6][2] / questao_35[9][2]) * questao_35[9][0]
        questao_35_esperado[6][1] = (questao_35[6][2] / questao_35[9][2]) * questao_35[9][1]
        questao_35_esperado[7][0] = (questao_35[7][2] / questao_35[9][2]) * questao_35[9][0]
        questao_35_esperado[7][1] = (questao_35[7][2] / questao_35[9][2]) * questao_35[9][1]
        questao_35_esperado[8][0] = (questao_35[8][2] / questao_35[9][2]) * questao_35[9][0]
        questao_35_esperado[8][1] = (questao_35[8][2] / questao_35[9][2]) * questao_35[9][1]
        
        questao_36_esperado[0][0] = (questao_36[0][2] / questao_36[9][2]) * questao_36[9][0]
        questao_36_esperado[0][1] = (questao_36[0][2] / questao_36[9][2]) * questao_36[9][1]
        questao_36_esperado[1][0] = (questao_36[1][2] / questao_36[9][2]) * questao_36[9][0]
        questao_36_esperado[1][1] = (questao_36[1][2] / questao_36[9][2]) * questao_36[9][1]
        questao_36_esperado[2][0] = (questao_36[2][2] / questao_36[9][2]) * questao_36[9][0]
        questao_36_esperado[2][1] = (questao_36[2][2] / questao_36[9][2]) * questao_36[9][1]
        questao_36_esperado[3][0] = (questao_36[3][2] / questao_36[9][2]) * questao_36[9][0]
        questao_36_esperado[3][1] = (questao_36[3][2] / questao_36[9][2]) * questao_36[9][1]
        questao_36_esperado[4][0] = (questao_36[4][2] / questao_36[9][2]) * questao_36[9][0]
        questao_36_esperado[4][1] = (questao_36[4][2] / questao_36[9][2]) * questao_36[9][1]
        questao_36_esperado[5][0] = (questao_36[5][2] / questao_36[9][2]) * questao_36[9][0]
        questao_36_esperado[5][1] = (questao_36[5][2] / questao_36[9][2]) * questao_36[9][1]
        questao_36_esperado[6][0] = (questao_36[6][2] / questao_36[9][2]) * questao_36[9][0]
        questao_36_esperado[6][1] = (questao_36[6][2] / questao_36[9][2]) * questao_36[9][1]
        questao_36_esperado[7][0] = (questao_36[7][2] / questao_36[9][2]) * questao_36[9][0]
        questao_36_esperado[7][1] = (questao_36[7][2] / questao_36[9][2]) * questao_36[9][1]
        questao_36_esperado[8][0] = (questao_36[8][2] / questao_36[9][2]) * questao_36[9][0]
        questao_36_esperado[8][1] = (questao_36[8][2] / questao_36[9][2]) * questao_36[9][1]
        
        questao_37_esperado[0][0] = (questao_37[0][2] / questao_37[9][2]) * questao_37[9][0]
        questao_37_esperado[0][1] = (questao_37[0][2] / questao_37[9][2]) * questao_37[9][1]
        questao_37_esperado[1][0] = (questao_37[1][2] / questao_37[9][2]) * questao_37[9][0]
        questao_37_esperado[1][1] = (questao_37[1][2] / questao_37[9][2]) * questao_37[9][1]
        questao_37_esperado[2][0] = (questao_37[2][2] / questao_37[9][2]) * questao_37[9][0]
        questao_37_esperado[2][1] = (questao_37[2][2] / questao_37[9][2]) * questao_37[9][1]
        questao_37_esperado[3][0] = (questao_37[3][2] / questao_37[9][2]) * questao_37[9][0]
        questao_37_esperado[3][1] = (questao_37[3][2] / questao_37[9][2]) * questao_37[9][1]
        questao_37_esperado[4][0] = (questao_37[4][2] / questao_37[9][2]) * questao_37[9][0]
        questao_37_esperado[4][1] = (questao_37[4][2] / questao_37[9][2]) * questao_37[9][1]
        questao_37_esperado[5][0] = (questao_37[5][2] / questao_37[9][2]) * questao_37[9][0]
        questao_37_esperado[5][1] = (questao_37[5][2] / questao_37[9][2]) * questao_37[9][1]
        questao_37_esperado[6][0] = (questao_37[6][2] / questao_37[9][2]) * questao_37[9][0]
        questao_37_esperado[6][1] = (questao_37[6][2] / questao_37[9][2]) * questao_37[9][1]
        questao_37_esperado[7][0] = (questao_37[7][2] / questao_37[9][2]) * questao_37[9][0]
        questao_37_esperado[7][1] = (questao_37[7][2] / questao_37[9][2]) * questao_37[9][1]
        questao_37_esperado[8][0] = (questao_37[8][2] / questao_37[9][2]) * questao_37[9][0]
        questao_37_esperado[8][1] = (questao_37[8][2] / questao_37[9][2]) * questao_37[9][1]
        
        questao_38_esperado[0][0] = (questao_38[0][2] / questao_38[9][2]) * questao_38[9][0]
        questao_38_esperado[0][1] = (questao_38[0][2] / questao_38[9][2]) * questao_38[9][1]
        questao_38_esperado[1][0] = (questao_38[1][2] / questao_38[9][2]) * questao_38[9][0]
        questao_38_esperado[1][1] = (questao_38[1][2] / questao_38[9][2]) * questao_38[9][1]
        questao_38_esperado[2][0] = (questao_38[2][2] / questao_38[9][2]) * questao_38[9][0]
        questao_38_esperado[2][1] = (questao_38[2][2] / questao_38[9][2]) * questao_38[9][1]
        questao_38_esperado[3][0] = (questao_38[3][2] / questao_38[9][2]) * questao_38[9][0]
        questao_38_esperado[3][1] = (questao_38[3][2] / questao_38[9][2]) * questao_38[9][1]
        questao_38_esperado[4][0] = (questao_38[4][2] / questao_38[9][2]) * questao_38[9][0]
        questao_38_esperado[4][1] = (questao_38[4][2] / questao_38[9][2]) * questao_38[9][1]
        questao_38_esperado[5][0] = (questao_38[5][2] / questao_38[9][2]) * questao_38[9][0]
        questao_38_esperado[5][1] = (questao_38[5][2] / questao_38[9][2]) * questao_38[9][1]
        questao_38_esperado[6][0] = (questao_38[6][2] / questao_38[9][2]) * questao_38[9][0]
        questao_38_esperado[6][1] = (questao_38[6][2] / questao_38[9][2]) * questao_38[9][1]
        questao_38_esperado[7][0] = (questao_38[7][2] / questao_38[9][2]) * questao_38[9][0]
        questao_38_esperado[7][1] = (questao_38[7][2] / questao_38[9][2]) * questao_38[9][1]
        questao_38_esperado[8][0] = (questao_38[8][2] / questao_38[9][2]) * questao_38[9][0]
        questao_38_esperado[8][1] = (questao_38[8][2] / questao_38[9][2]) * questao_38[9][1]
        
        questao_39_esperado[0][0] = (questao_39[0][2] / questao_39[9][2]) * questao_39[9][0]
        questao_39_esperado[0][1] = (questao_39[0][2] / questao_39[9][2]) * questao_39[9][1]
        questao_39_esperado[1][0] = (questao_39[1][2] / questao_39[9][2]) * questao_39[9][0]
        questao_39_esperado[1][1] = (questao_39[1][2] / questao_39[9][2]) * questao_39[9][1]
        questao_39_esperado[2][0] = (questao_39[2][2] / questao_39[9][2]) * questao_39[9][0]
        questao_39_esperado[2][1] = (questao_39[2][2] / questao_39[9][2]) * questao_39[9][1]
        questao_39_esperado[3][0] = (questao_39[3][2] / questao_39[9][2]) * questao_39[9][0]
        questao_39_esperado[3][1] = (questao_39[3][2] / questao_39[9][2]) * questao_39[9][1]
        questao_39_esperado[4][0] = (questao_39[4][2] / questao_39[9][2]) * questao_39[9][0]
        questao_39_esperado[4][1] = (questao_39[4][2] / questao_39[9][2]) * questao_39[9][1]
        questao_39_esperado[5][0] = (questao_39[5][2] / questao_39[9][2]) * questao_39[9][0]
        questao_39_esperado[5][1] = (questao_39[5][2] / questao_39[9][2]) * questao_39[9][1]
        questao_39_esperado[6][0] = (questao_39[6][2] / questao_39[9][2]) * questao_39[9][0]
        questao_39_esperado[6][1] = (questao_39[6][2] / questao_39[9][2]) * questao_39[9][1]
        questao_39_esperado[7][0] = (questao_39[7][2] / questao_39[9][2]) * questao_39[9][0]
        questao_39_esperado[7][1] = (questao_39[7][2] / questao_39[9][2]) * questao_39[9][1]
        questao_39_esperado[8][0] = (questao_39[8][2] / questao_39[9][2]) * questao_39[9][0]
        questao_39_esperado[8][1] = (questao_39[8][2] / questao_39[9][2]) * questao_39[9][1]
        
        questao_40_esperado[0][0] = (questao_40[0][2] / questao_40[9][2]) * questao_40[9][0]
        questao_40_esperado[0][1] = (questao_40[0][2] / questao_40[9][2]) * questao_40[9][1]
        questao_40_esperado[1][0] = (questao_40[1][2] / questao_40[9][2]) * questao_40[9][0]
        questao_40_esperado[1][1] = (questao_40[1][2] / questao_40[9][2]) * questao_40[9][1]
        questao_40_esperado[2][0] = (questao_40[2][2] / questao_40[9][2]) * questao_40[9][0]
        questao_40_esperado[2][1] = (questao_40[2][2] / questao_40[9][2]) * questao_40[9][1]
        questao_40_esperado[3][0] = (questao_40[3][2] / questao_40[9][2]) * questao_40[9][0]
        questao_40_esperado[3][1] = (questao_40[3][2] / questao_40[9][2]) * questao_40[9][1]
        questao_40_esperado[4][0] = (questao_40[4][2] / questao_40[9][2]) * questao_40[9][0]
        questao_40_esperado[4][1] = (questao_40[4][2] / questao_40[9][2]) * questao_40[9][1]
        questao_40_esperado[5][0] = (questao_40[5][2] / questao_40[9][2]) * questao_40[9][0]
        questao_40_esperado[5][1] = (questao_40[5][2] / questao_40[9][2]) * questao_40[9][1]
        questao_40_esperado[6][0] = (questao_40[6][2] / questao_40[9][2]) * questao_40[9][0]
        questao_40_esperado[6][1] = (questao_40[6][2] / questao_40[9][2]) * questao_40[9][1]
        questao_40_esperado[7][0] = (questao_40[7][2] / questao_40[9][2]) * questao_40[9][0]
        questao_40_esperado[7][1] = (questao_40[7][2] / questao_40[9][2]) * questao_40[9][1]
        questao_40_esperado[8][0] = (questao_40[8][2] / questao_40[9][2]) * questao_40[9][0]
        questao_40_esperado[8][1] = (questao_40[8][2] / questao_40[9][2]) * questao_40[9][1]
        
        questao_41_esperado[0][0] = (questao_41[0][2] / questao_41[9][2]) * questao_41[9][0]
        questao_41_esperado[0][1] = (questao_41[0][2] / questao_41[9][2]) * questao_41[9][1]
        questao_41_esperado[1][0] = (questao_41[1][2] / questao_41[9][2]) * questao_41[9][0]
        questao_41_esperado[1][1] = (questao_41[1][2] / questao_41[9][2]) * questao_41[9][1]
        questao_41_esperado[2][0] = (questao_41[2][2] / questao_41[9][2]) * questao_41[9][0]
        questao_41_esperado[2][1] = (questao_41[2][2] / questao_41[9][2]) * questao_41[9][1]
        questao_41_esperado[3][0] = (questao_41[3][2] / questao_41[9][2]) * questao_41[9][0]
        questao_41_esperado[3][1] = (questao_41[3][2] / questao_41[9][2]) * questao_41[9][1]
        questao_41_esperado[4][0] = (questao_41[4][2] / questao_41[9][2]) * questao_41[9][0]
        questao_41_esperado[4][1] = (questao_41[4][2] / questao_41[9][2]) * questao_41[9][1]
        questao_41_esperado[5][0] = (questao_41[5][2] / questao_41[9][2]) * questao_41[9][0]
        questao_41_esperado[5][1] = (questao_41[5][2] / questao_41[9][2]) * questao_41[9][1]
        questao_41_esperado[6][0] = (questao_41[6][2] / questao_41[9][2]) * questao_41[9][0]
        questao_41_esperado[6][1] = (questao_41[6][2] / questao_41[9][2]) * questao_41[9][1]
        questao_41_esperado[7][0] = (questao_41[7][2] / questao_41[9][2]) * questao_41[9][0]
        questao_41_esperado[7][1] = (questao_41[7][2] / questao_41[9][2]) * questao_41[9][1]
        questao_41_esperado[8][0] = (questao_41[8][2] / questao_41[9][2]) * questao_41[9][0]
        questao_41_esperado[8][1] = (questao_41[8][2] / questao_41[9][2]) * questao_41[9][1]
        
        questao_42_esperado[0][0] = (questao_42[0][2] / questao_42[9][2]) * questao_42[9][0]
        questao_42_esperado[0][1] = (questao_42[0][2] / questao_42[9][2]) * questao_42[9][1]
        questao_42_esperado[1][0] = (questao_42[1][2] / questao_42[9][2]) * questao_42[9][0]
        questao_42_esperado[1][1] = (questao_42[1][2] / questao_42[9][2]) * questao_42[9][1]
        questao_42_esperado[2][0] = (questao_42[2][2] / questao_42[9][2]) * questao_42[9][0]
        questao_42_esperado[2][1] = (questao_42[2][2] / questao_42[9][2]) * questao_42[9][1]
        questao_42_esperado[3][0] = (questao_42[3][2] / questao_42[9][2]) * questao_42[9][0]
        questao_42_esperado[3][1] = (questao_42[3][2] / questao_42[9][2]) * questao_42[9][1]
        questao_42_esperado[4][0] = (questao_42[4][2] / questao_42[9][2]) * questao_42[9][0]
        questao_42_esperado[4][1] = (questao_42[4][2] / questao_42[9][2]) * questao_42[9][1]
        questao_42_esperado[5][0] = (questao_42[5][2] / questao_42[9][2]) * questao_42[9][0]
        questao_42_esperado[5][1] = (questao_42[5][2] / questao_42[9][2]) * questao_42[9][1]
        questao_42_esperado[6][0] = (questao_42[6][2] / questao_42[9][2]) * questao_42[9][0]
        questao_42_esperado[6][1] = (questao_42[6][2] / questao_42[9][2]) * questao_42[9][1]
        questao_42_esperado[7][0] = (questao_42[7][2] / questao_42[9][2]) * questao_42[9][0]
        questao_42_esperado[7][1] = (questao_42[7][2] / questao_42[9][2]) * questao_42[9][1]
        questao_42_esperado[8][0] = (questao_42[8][2] / questao_42[9][2]) * questao_42[9][0]
        questao_42_esperado[8][1] = (questao_42[8][2] / questao_42[9][2]) * questao_42[9][1]
        
        questao_43_esperado[0][0] = (questao_43[0][2] / questao_43[9][2]) * questao_43[9][0]
        questao_43_esperado[0][1] = (questao_43[0][2] / questao_43[9][2]) * questao_43[9][1]
        questao_43_esperado[1][0] = (questao_43[1][2] / questao_43[9][2]) * questao_43[9][0]
        questao_43_esperado[1][1] = (questao_43[1][2] / questao_43[9][2]) * questao_43[9][1]
        questao_43_esperado[2][0] = (questao_43[2][2] / questao_43[9][2]) * questao_43[9][0]
        questao_43_esperado[2][1] = (questao_43[2][2] / questao_43[9][2]) * questao_43[9][1]
        questao_43_esperado[3][0] = (questao_43[3][2] / questao_43[9][2]) * questao_43[9][0]
        questao_43_esperado[3][1] = (questao_43[3][2] / questao_43[9][2]) * questao_43[9][1]
        questao_43_esperado[4][0] = (questao_43[4][2] / questao_43[9][2]) * questao_43[9][0]
        questao_43_esperado[4][1] = (questao_43[4][2] / questao_43[9][2]) * questao_43[9][1]
        questao_43_esperado[5][0] = (questao_43[5][2] / questao_43[9][2]) * questao_43[9][0]
        questao_43_esperado[5][1] = (questao_43[5][2] / questao_43[9][2]) * questao_43[9][1]
        questao_43_esperado[6][0] = (questao_43[6][2] / questao_43[9][2]) * questao_43[9][0]
        questao_43_esperado[6][1] = (questao_43[6][2] / questao_43[9][2]) * questao_43[9][1]
        questao_43_esperado[7][0] = (questao_43[7][2] / questao_43[9][2]) * questao_43[9][0]
        questao_43_esperado[7][1] = (questao_43[7][2] / questao_43[9][2]) * questao_43[9][1]
        questao_43_esperado[8][0] = (questao_43[8][2] / questao_43[9][2]) * questao_43[9][0]
        questao_43_esperado[8][1] = (questao_43[8][2] / questao_43[9][2]) * questao_43[9][1]
        
        questao_44_esperado[0][0] = (questao_44[0][2] / questao_44[9][2]) * questao_44[9][0]
        questao_44_esperado[0][1] = (questao_44[0][2] / questao_44[9][2]) * questao_44[9][1]
        questao_44_esperado[1][0] = (questao_44[1][2] / questao_44[9][2]) * questao_44[9][0]
        questao_44_esperado[1][1] = (questao_44[1][2] / questao_44[9][2]) * questao_44[9][1]
        questao_44_esperado[2][0] = (questao_44[2][2] / questao_44[9][2]) * questao_44[9][0]
        questao_44_esperado[2][1] = (questao_44[2][2] / questao_44[9][2]) * questao_44[9][1]
        questao_44_esperado[3][0] = (questao_44[3][2] / questao_44[9][2]) * questao_44[9][0]
        questao_44_esperado[3][1] = (questao_44[3][2] / questao_44[9][2]) * questao_44[9][1]
        questao_44_esperado[4][0] = (questao_44[4][2] / questao_44[9][2]) * questao_44[9][0]
        questao_44_esperado[4][1] = (questao_44[4][2] / questao_44[9][2]) * questao_44[9][1]
        questao_44_esperado[5][0] = (questao_44[5][2] / questao_44[9][2]) * questao_44[9][0]
        questao_44_esperado[5][1] = (questao_44[5][2] / questao_44[9][2]) * questao_44[9][1]
        questao_44_esperado[6][0] = (questao_44[6][2] / questao_44[9][2]) * questao_44[9][0]
        questao_44_esperado[6][1] = (questao_44[6][2] / questao_44[9][2]) * questao_44[9][1]
        questao_44_esperado[7][0] = (questao_44[7][2] / questao_44[9][2]) * questao_44[9][0]
        questao_44_esperado[7][1] = (questao_44[7][2] / questao_44[9][2]) * questao_44[9][1]
        questao_44_esperado[8][0] = (questao_44[8][2] / questao_44[9][2]) * questao_44[9][0]
        questao_44_esperado[8][1] = (questao_44[8][2] / questao_44[9][2]) * questao_44[9][1]
        
        questao_45_esperado[0][0] = (questao_45[0][2] / questao_45[9][2]) * questao_45[9][0]
        questao_45_esperado[0][1] = (questao_45[0][2] / questao_45[9][2]) * questao_45[9][1]
        questao_45_esperado[1][0] = (questao_45[1][2] / questao_45[9][2]) * questao_45[9][0]
        questao_45_esperado[1][1] = (questao_45[1][2] / questao_45[9][2]) * questao_45[9][1]
        questao_45_esperado[2][0] = (questao_45[2][2] / questao_45[9][2]) * questao_45[9][0]
        questao_45_esperado[2][1] = (questao_45[2][2] / questao_45[9][2]) * questao_45[9][1]
        questao_45_esperado[3][0] = (questao_45[3][2] / questao_45[9][2]) * questao_45[9][0]
        questao_45_esperado[3][1] = (questao_45[3][2] / questao_45[9][2]) * questao_45[9][1]
        questao_45_esperado[4][0] = (questao_45[4][2] / questao_45[9][2]) * questao_45[9][0]
        questao_45_esperado[4][1] = (questao_45[4][2] / questao_45[9][2]) * questao_45[9][1]
        questao_45_esperado[5][0] = (questao_45[5][2] / questao_45[9][2]) * questao_45[9][0]
        questao_45_esperado[5][1] = (questao_45[5][2] / questao_45[9][2]) * questao_45[9][1]
        questao_45_esperado[6][0] = (questao_45[6][2] / questao_45[9][2]) * questao_45[9][0]
        questao_45_esperado[6][1] = (questao_45[6][2] / questao_45[9][2]) * questao_45[9][1]
        questao_45_esperado[7][0] = (questao_45[7][2] / questao_45[9][2]) * questao_45[9][0]
        questao_45_esperado[7][1] = (questao_45[7][2] / questao_45[9][2]) * questao_45[9][1]
        questao_45_esperado[8][0] = (questao_45[8][2] / questao_45[9][2]) * questao_45[9][0]
        questao_45_esperado[8][1] = (questao_45[8][2] / questao_45[9][2]) * questao_45[9][1]
        
        questao_46_esperado[0][0] = (questao_46[0][2] / questao_46[9][2]) * questao_46[9][0]
        questao_46_esperado[0][1] = (questao_46[0][2] / questao_46[9][2]) * questao_46[9][1]
        questao_46_esperado[1][0] = (questao_46[1][2] / questao_46[9][2]) * questao_46[9][0]
        questao_46_esperado[1][1] = (questao_46[1][2] / questao_46[9][2]) * questao_46[9][1]
        questao_46_esperado[2][0] = (questao_46[2][2] / questao_46[9][2]) * questao_46[9][0]
        questao_46_esperado[2][1] = (questao_46[2][2] / questao_46[9][2]) * questao_46[9][1]
        questao_46_esperado[3][0] = (questao_46[3][2] / questao_46[9][2]) * questao_46[9][0]
        questao_46_esperado[3][1] = (questao_46[3][2] / questao_46[9][2]) * questao_46[9][1]
        questao_46_esperado[4][0] = (questao_46[4][2] / questao_46[9][2]) * questao_46[9][0]
        questao_46_esperado[4][1] = (questao_46[4][2] / questao_46[9][2]) * questao_46[9][1]
        questao_46_esperado[5][0] = (questao_46[5][2] / questao_46[9][2]) * questao_46[9][0]
        questao_46_esperado[5][1] = (questao_46[5][2] / questao_46[9][2]) * questao_46[9][1]
        questao_46_esperado[6][0] = (questao_46[6][2] / questao_46[9][2]) * questao_46[9][0]
        questao_46_esperado[6][1] = (questao_46[6][2] / questao_46[9][2]) * questao_46[9][1]
        questao_46_esperado[7][0] = (questao_46[7][2] / questao_46[9][2]) * questao_46[9][0]
        questao_46_esperado[7][1] = (questao_46[7][2] / questao_46[9][2]) * questao_46[9][1]
        questao_46_esperado[8][0] = (questao_46[8][2] / questao_46[9][2]) * questao_46[9][0]
        questao_46_esperado[8][1] = (questao_46[8][2] / questao_46[9][2]) * questao_46[9][1]
        
        questao_47_esperado[0][0] = (questao_47[0][2] / questao_47[9][2]) * questao_47[9][0]
        questao_47_esperado[0][1] = (questao_47[0][2] / questao_47[9][2]) * questao_47[9][1]
        questao_47_esperado[1][0] = (questao_47[1][2] / questao_47[9][2]) * questao_47[9][0]
        questao_47_esperado[1][1] = (questao_47[1][2] / questao_47[9][2]) * questao_47[9][1]
        questao_47_esperado[2][0] = (questao_47[2][2] / questao_47[9][2]) * questao_47[9][0]
        questao_47_esperado[2][1] = (questao_47[2][2] / questao_47[9][2]) * questao_47[9][1]
        questao_47_esperado[3][0] = (questao_47[3][2] / questao_47[9][2]) * questao_47[9][0]
        questao_47_esperado[3][1] = (questao_47[3][2] / questao_47[9][2]) * questao_47[9][1]
        questao_47_esperado[4][0] = (questao_47[4][2] / questao_47[9][2]) * questao_47[9][0]
        questao_47_esperado[4][1] = (questao_47[4][2] / questao_47[9][2]) * questao_47[9][1]
        questao_47_esperado[5][0] = (questao_47[5][2] / questao_47[9][2]) * questao_47[9][0]
        questao_47_esperado[5][1] = (questao_47[5][2] / questao_47[9][2]) * questao_47[9][1]
        questao_47_esperado[6][0] = (questao_47[6][2] / questao_47[9][2]) * questao_47[9][0]
        questao_47_esperado[6][1] = (questao_47[6][2] / questao_47[9][2]) * questao_47[9][1]
        questao_47_esperado[7][0] = (questao_47[7][2] / questao_47[9][2]) * questao_47[9][0]
        questao_47_esperado[7][1] = (questao_47[7][2] / questao_47[9][2]) * questao_47[9][1]
        questao_47_esperado[8][0] = (questao_47[8][2] / questao_47[9][2]) * questao_47[9][0]
        questao_47_esperado[8][1] = (questao_47[8][2] / questao_47[9][2]) * questao_47[9][1]
        
        questao_48_esperado[0][0] = (questao_48[0][2] / questao_48[9][2]) * questao_48[9][0]
        questao_48_esperado[0][1] = (questao_48[0][2] / questao_48[9][2]) * questao_48[9][1]
        questao_48_esperado[1][0] = (questao_48[1][2] / questao_48[9][2]) * questao_48[9][0]
        questao_48_esperado[1][1] = (questao_48[1][2] / questao_48[9][2]) * questao_48[9][1]
        questao_48_esperado[2][0] = (questao_48[2][2] / questao_48[9][2]) * questao_48[9][0]
        questao_48_esperado[2][1] = (questao_48[2][2] / questao_48[9][2]) * questao_48[9][1]
        questao_48_esperado[3][0] = (questao_48[3][2] / questao_48[9][2]) * questao_48[9][0]
        questao_48_esperado[3][1] = (questao_48[3][2] / questao_48[9][2]) * questao_48[9][1]
        questao_48_esperado[4][0] = (questao_48[4][2] / questao_48[9][2]) * questao_48[9][0]
        questao_48_esperado[4][1] = (questao_48[4][2] / questao_48[9][2]) * questao_48[9][1]
        questao_48_esperado[5][0] = (questao_48[5][2] / questao_48[9][2]) * questao_48[9][0]
        questao_48_esperado[5][1] = (questao_48[5][2] / questao_48[9][2]) * questao_48[9][1]
        questao_48_esperado[6][0] = (questao_48[6][2] / questao_48[9][2]) * questao_48[9][0]
        questao_48_esperado[6][1] = (questao_48[6][2] / questao_48[9][2]) * questao_48[9][1]
        questao_48_esperado[7][0] = (questao_48[7][2] / questao_48[9][2]) * questao_48[9][0]
        questao_48_esperado[7][1] = (questao_48[7][2] / questao_48[9][2]) * questao_48[9][1]
        questao_48_esperado[8][0] = (questao_48[8][2] / questao_48[9][2]) * questao_48[9][0]
        questao_48_esperado[8][1] = (questao_48[8][2] / questao_48[9][2]) * questao_48[9][1]
        
        questao_49_esperado[0][0] = (questao_49[0][2] / questao_49[9][2]) * questao_49[9][0]
        questao_49_esperado[0][1] = (questao_49[0][2] / questao_49[9][2]) * questao_49[9][1]
        questao_49_esperado[1][0] = (questao_49[1][2] / questao_49[9][2]) * questao_49[9][0]
        questao_49_esperado[1][1] = (questao_49[1][2] / questao_49[9][2]) * questao_49[9][1]
        questao_49_esperado[2][0] = (questao_49[2][2] / questao_49[9][2]) * questao_49[9][0]
        questao_49_esperado[2][1] = (questao_49[2][2] / questao_49[9][2]) * questao_49[9][1]
        questao_49_esperado[3][0] = (questao_49[3][2] / questao_49[9][2]) * questao_49[9][0]
        questao_49_esperado[3][1] = (questao_49[3][2] / questao_49[9][2]) * questao_49[9][1]
        questao_49_esperado[4][0] = (questao_49[4][2] / questao_49[9][2]) * questao_49[9][0]
        questao_49_esperado[4][1] = (questao_49[4][2] / questao_49[9][2]) * questao_49[9][1]
        questao_49_esperado[5][0] = (questao_49[5][2] / questao_49[9][2]) * questao_49[9][0]
        questao_49_esperado[5][1] = (questao_49[5][2] / questao_49[9][2]) * questao_49[9][1]
        questao_49_esperado[6][0] = (questao_49[6][2] / questao_49[9][2]) * questao_49[9][0]
        questao_49_esperado[6][1] = (questao_49[6][2] / questao_49[9][2]) * questao_49[9][1]
        questao_49_esperado[7][0] = (questao_49[7][2] / questao_49[9][2]) * questao_49[9][0]
        questao_49_esperado[7][1] = (questao_49[7][2] / questao_49[9][2]) * questao_49[9][1]
        questao_49_esperado[8][0] = (questao_49[8][2] / questao_49[9][2]) * questao_49[9][0]
        questao_49_esperado[8][1] = (questao_49[8][2] / questao_49[9][2]) * questao_49[9][1]
        
        questao_50_esperado[0][0] = (questao_50[0][2] / questao_50[9][2]) * questao_50[9][0]
        questao_50_esperado[0][1] = (questao_50[0][2] / questao_50[9][2]) * questao_50[9][1]
        questao_50_esperado[1][0] = (questao_50[1][2] / questao_50[9][2]) * questao_50[9][0]
        questao_50_esperado[1][1] = (questao_50[1][2] / questao_50[9][2]) * questao_50[9][1]
        questao_50_esperado[2][0] = (questao_50[2][2] / questao_50[9][2]) * questao_50[9][0]
        questao_50_esperado[2][1] = (questao_50[2][2] / questao_50[9][2]) * questao_50[9][1]
        questao_50_esperado[3][0] = (questao_50[3][2] / questao_50[9][2]) * questao_50[9][0]
        questao_50_esperado[3][1] = (questao_50[3][2] / questao_50[9][2]) * questao_50[9][1]
        questao_50_esperado[4][0] = (questao_50[4][2] / questao_50[9][2]) * questao_50[9][0]
        questao_50_esperado[4][1] = (questao_50[4][2] / questao_50[9][2]) * questao_50[9][1]
        questao_50_esperado[5][0] = (questao_50[5][2] / questao_50[9][2]) * questao_50[9][0]
        questao_50_esperado[5][1] = (questao_50[5][2] / questao_50[9][2]) * questao_50[9][1]
        questao_50_esperado[6][0] = (questao_50[6][2] / questao_50[9][2]) * questao_50[9][0]
        questao_50_esperado[6][1] = (questao_50[6][2] / questao_50[9][2]) * questao_50[9][1]
        questao_50_esperado[7][0] = (questao_50[7][2] / questao_50[9][2]) * questao_50[9][0]
        questao_50_esperado[7][1] = (questao_50[7][2] / questao_50[9][2]) * questao_50[9][1]
        questao_50_esperado[8][0] = (questao_50[8][2] / questao_50[9][2]) * questao_50[9][0]
        questao_50_esperado[8][1] = (questao_50[8][2] / questao_50[9][2]) * questao_50[9][1]
        
        questao_51_esperado[0][0] = (questao_51[0][2] / questao_51[9][2]) * questao_51[9][0]
        questao_51_esperado[0][1] = (questao_51[0][2] / questao_51[9][2]) * questao_51[9][1]
        questao_51_esperado[1][0] = (questao_51[1][2] / questao_51[9][2]) * questao_51[9][0]
        questao_51_esperado[1][1] = (questao_51[1][2] / questao_51[9][2]) * questao_51[9][1]
        questao_51_esperado[2][0] = (questao_51[2][2] / questao_51[9][2]) * questao_51[9][0]
        questao_51_esperado[2][1] = (questao_51[2][2] / questao_51[9][2]) * questao_51[9][1]
        questao_51_esperado[3][0] = (questao_51[3][2] / questao_51[9][2]) * questao_51[9][0]
        questao_51_esperado[3][1] = (questao_51[3][2] / questao_51[9][2]) * questao_51[9][1]
        questao_51_esperado[4][0] = (questao_51[4][2] / questao_51[9][2]) * questao_51[9][0]
        questao_51_esperado[4][1] = (questao_51[4][2] / questao_51[9][2]) * questao_51[9][1]
        questao_51_esperado[5][0] = (questao_51[5][2] / questao_51[9][2]) * questao_51[9][0]
        questao_51_esperado[5][1] = (questao_51[5][2] / questao_51[9][2]) * questao_51[9][1]
        questao_51_esperado[6][0] = (questao_51[6][2] / questao_51[9][2]) * questao_51[9][0]
        questao_51_esperado[6][1] = (questao_51[6][2] / questao_51[9][2]) * questao_51[9][1]
        questao_51_esperado[7][0] = (questao_51[7][2] / questao_51[9][2]) * questao_51[9][0]
        questao_51_esperado[7][1] = (questao_51[7][2] / questao_51[9][2]) * questao_51[9][1]
        questao_51_esperado[8][0] = (questao_51[8][2] / questao_51[9][2]) * questao_51[9][0]
        questao_51_esperado[8][1] = (questao_51[8][2] / questao_51[9][2]) * questao_51[9][1]
        
        questao_52_esperado[0][0] = (questao_52[0][2] / questao_52[9][2]) * questao_52[9][0]
        questao_52_esperado[0][1] = (questao_52[0][2] / questao_52[9][2]) * questao_52[9][1]
        questao_52_esperado[1][0] = (questao_52[1][2] / questao_52[9][2]) * questao_52[9][0]
        questao_52_esperado[1][1] = (questao_52[1][2] / questao_52[9][2]) * questao_52[9][1]
        questao_52_esperado[2][0] = (questao_52[2][2] / questao_52[9][2]) * questao_52[9][0]
        questao_52_esperado[2][1] = (questao_52[2][2] / questao_52[9][2]) * questao_52[9][1]
        questao_52_esperado[3][0] = (questao_52[3][2] / questao_52[9][2]) * questao_52[9][0]
        questao_52_esperado[3][1] = (questao_52[3][2] / questao_52[9][2]) * questao_52[9][1]
        questao_52_esperado[4][0] = (questao_52[4][2] / questao_52[9][2]) * questao_52[9][0]
        questao_52_esperado[4][1] = (questao_52[4][2] / questao_52[9][2]) * questao_52[9][1]
        questao_52_esperado[5][0] = (questao_52[5][2] / questao_52[9][2]) * questao_52[9][0]
        questao_52_esperado[5][1] = (questao_52[5][2] / questao_52[9][2]) * questao_52[9][1]
        questao_52_esperado[6][0] = (questao_52[6][2] / questao_52[9][2]) * questao_52[9][0]
        questao_52_esperado[6][1] = (questao_52[6][2] / questao_52[9][2]) * questao_52[9][1]
        questao_52_esperado[7][0] = (questao_52[7][2] / questao_52[9][2]) * questao_52[9][0]
        questao_52_esperado[7][1] = (questao_52[7][2] / questao_52[9][2]) * questao_52[9][1]
        questao_52_esperado[8][0] = (questao_52[8][2] / questao_52[9][2]) * questao_52[9][0]
        questao_52_esperado[8][1] = (questao_52[8][2] / questao_52[9][2]) * questao_52[9][1]
        
        questao_53_esperado[0][0] = (questao_53[0][2] / questao_53[9][2]) * questao_53[9][0]
        questao_53_esperado[0][1] = (questao_53[0][2] / questao_53[9][2]) * questao_53[9][1]
        questao_53_esperado[1][0] = (questao_53[1][2] / questao_53[9][2]) * questao_53[9][0]
        questao_53_esperado[1][1] = (questao_53[1][2] / questao_53[9][2]) * questao_53[9][1]
        questao_53_esperado[2][0] = (questao_53[2][2] / questao_53[9][2]) * questao_53[9][0]
        questao_53_esperado[2][1] = (questao_53[2][2] / questao_53[9][2]) * questao_53[9][1]
        questao_53_esperado[3][0] = (questao_53[3][2] / questao_53[9][2]) * questao_53[9][0]
        questao_53_esperado[3][1] = (questao_53[3][2] / questao_53[9][2]) * questao_53[9][1]
        questao_53_esperado[4][0] = (questao_53[4][2] / questao_53[9][2]) * questao_53[9][0]
        questao_53_esperado[4][1] = (questao_53[4][2] / questao_53[9][2]) * questao_53[9][1]
        questao_53_esperado[5][0] = (questao_53[5][2] / questao_53[9][2]) * questao_53[9][0]
        questao_53_esperado[5][1] = (questao_53[5][2] / questao_53[9][2]) * questao_53[9][1]
        questao_53_esperado[6][0] = (questao_53[6][2] / questao_53[9][2]) * questao_53[9][0]
        questao_53_esperado[6][1] = (questao_53[6][2] / questao_53[9][2]) * questao_53[9][1]
        questao_53_esperado[7][0] = (questao_53[7][2] / questao_53[9][2]) * questao_53[9][0]
        questao_53_esperado[7][1] = (questao_53[7][2] / questao_53[9][2]) * questao_53[9][1]
        questao_53_esperado[8][0] = (questao_53[8][2] / questao_53[9][2]) * questao_53[9][0]
        questao_53_esperado[8][1] = (questao_53[8][2] / questao_53[9][2]) * questao_53[9][1]
        
        questao_54_esperado[0][0] = (questao_54[0][2] / questao_54[9][2]) * questao_54[9][0]
        questao_54_esperado[0][1] = (questao_54[0][2] / questao_54[9][2]) * questao_54[9][1]
        questao_54_esperado[1][0] = (questao_54[1][2] / questao_54[9][2]) * questao_54[9][0]
        questao_54_esperado[1][1] = (questao_54[1][2] / questao_54[9][2]) * questao_54[9][1]
        questao_54_esperado[2][0] = (questao_54[2][2] / questao_54[9][2]) * questao_54[9][0]
        questao_54_esperado[2][1] = (questao_54[2][2] / questao_54[9][2]) * questao_54[9][1]
        questao_54_esperado[3][0] = (questao_54[3][2] / questao_54[9][2]) * questao_54[9][0]
        questao_54_esperado[3][1] = (questao_54[3][2] / questao_54[9][2]) * questao_54[9][1]
        questao_54_esperado[4][0] = (questao_54[4][2] / questao_54[9][2]) * questao_54[9][0]
        questao_54_esperado[4][1] = (questao_54[4][2] / questao_54[9][2]) * questao_54[9][1]
        questao_54_esperado[5][0] = (questao_54[5][2] / questao_54[9][2]) * questao_54[9][0]
        questao_54_esperado[5][1] = (questao_54[5][2] / questao_54[9][2]) * questao_54[9][1]
        questao_54_esperado[6][0] = (questao_54[6][2] / questao_54[9][2]) * questao_54[9][0]
        questao_54_esperado[6][1] = (questao_54[6][2] / questao_54[9][2]) * questao_54[9][1]
        questao_54_esperado[7][0] = (questao_54[7][2] / questao_54[9][2]) * questao_54[9][0]
        questao_54_esperado[7][1] = (questao_54[7][2] / questao_54[9][2]) * questao_54[9][1]
        questao_54_esperado[8][0] = (questao_54[8][2] / questao_54[9][2]) * questao_54[9][0]
        questao_54_esperado[8][1] = (questao_54[8][2] / questao_54[9][2]) * questao_54[9][1]
        
        context = {
            'pagina_inferencia': True,
            'sexo': sexo,
            'raca': raca,
            'questao_73': questao_73,
            'questao_75': questao_75,
            'questao_79': questao_79,
            'questao_84': questao_84,
            'questao_92': questao_92,
            'questao_111': questao_111,
            'questao_113': questao_113,
            'questao_25': questao_25,
            'questao_26': questao_26,
            'questao_27': questao_27,
            'questao_28': questao_28,
            'questao_29': questao_29,
            'questao_30': questao_30,
            'questao_31': questao_31,
            'questao_32': questao_32,
            'questao_33': questao_33,
            'questao_34': questao_34,
            'questao_35': questao_35,
            'questao_36': questao_36,
            'questao_37': questao_37,
            'questao_38': questao_38,
            'questao_39': questao_39,
            'questao_40': questao_40,
            'questao_41': questao_41,
            'questao_42': questao_42,
            'questao_43': questao_43,
            'questao_44': questao_44,
            'questao_45': questao_45,
            'questao_46': questao_46,
            'questao_47': questao_47,
            'questao_48': questao_48,
            'questao_49': questao_49,
            'questao_50': questao_50,
            'questao_51': questao_51,
            'questao_52': questao_52,
            'questao_53': questao_53,
            'questao_54': questao_54,
            
            'sexo_esperado': sexo_esperado,
            'raca_esperado': raca_esperado,
            'questao_73_esperado': questao_73_esperado,
            'questao_75_esperado': questao_75_esperado,
            'questao_79_esperado': questao_79_esperado,
            'questao_84_esperado': questao_84_esperado,
            'questao_92_esperado': questao_92_esperado,
            'questao_111_esperado': questao_111_esperado,
            'questao_113_esperado': questao_113_esperado,
            'questao_25_esperado': questao_25_esperado,
            'questao_26_esperado': questao_26_esperado,
            'questao_27_esperado': questao_27_esperado,
            'questao_28_esperado': questao_28_esperado,
            'questao_29_esperado': questao_29_esperado,
            'questao_30_esperado': questao_30_esperado,
            'questao_31_esperado': questao_31_esperado,
            'questao_32_esperado': questao_32_esperado,
            'questao_33_esperado': questao_33_esperado,
            'questao_34_esperado': questao_34_esperado,
            'questao_35_esperado': questao_35_esperado,
            'questao_36_esperado': questao_36_esperado,
            'questao_37_esperado': questao_37_esperado,
            'questao_38_esperado': questao_38_esperado,
            'questao_39_esperado': questao_39_esperado,
            'questao_40_esperado': questao_40_esperado,
            'questao_41_esperado': questao_41_esperado,
            'questao_42_esperado': questao_42_esperado,
            'questao_43_esperado': questao_43_esperado,
            'questao_44_esperado': questao_44_esperado,
            'questao_45_esperado': questao_45_esperado,
            'questao_46_esperado': questao_46_esperado,
            'questao_47_esperado': questao_47_esperado,
            'questao_48_esperado': questao_48_esperado,
            'questao_49_esperado': questao_49_esperado,
            'questao_50_esperado': questao_50_esperado,
            'questao_51_esperado': questao_51_esperado,
            'questao_52_esperado': questao_52_esperado,
            'questao_53_esperado': questao_53_esperado,
            'questao_54_esperado': questao_54_esperado,
        }
        
        return render(self.request, 'administracao/inferencia.html', context)


class GraficosAlunosView(LoginRequired, View):
    """Página que exibe gráficos baseados nos dados dos alunos"""
    
    def get(self, request):
        alunos = Aluno.objects.order_by('-id')
        
        aluno_por_escola = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for aluno in alunos:
            if aluno.escola.nome == "Escola municipal Antônio Carlos Jobim":
                aluno_por_escola[0] = aluno_por_escola[0] + 1
            elif aluno.escola.nome == "Escola municipal Antônio G. de Carvalho Filho":
                aluno_por_escola[1] = aluno_por_escola[1] + 1
            elif aluno.escola.nome == "Escola municipal Anne Frank":
                aluno_por_escola[2] = aluno_por_escola[2] + 1
            elif aluno.escola.nome == "Escola municipal Darcy Ribeiro":
                aluno_por_escola[3] = aluno_por_escola[3] + 1
            elif aluno.escola.nome == "Escola municipal Henrique Talone Pinheiro":
                aluno_por_escola[4] = aluno_por_escola[4] + 1
            elif aluno.escola.nome == "Escola municipal de T.I. Vinícius de Moraes":
                aluno_por_escola[5] = aluno_por_escola[5] + 1
            elif aluno.escola.nome == "Escola municipal Beatriz Rodrigues da Silva":
                aluno_por_escola[6] = aluno_por_escola[6] + 1
            elif aluno.escola.nome == "Escola municipal Mestre Pacífico S. Campos":
                aluno_por_escola[7] = aluno_por_escola[7] + 1
            elif aluno.escola.nome == "Escola municipal Luiz Gonzaga":
                aluno_por_escola[8] = aluno_por_escola[8] + 1
            elif aluno.escola.nome == "Escola municipal de T.I. Padre Josimo M. Tavares":
                aluno_por_escola[9] = aluno_por_escola[9] + 1
            elif aluno.escola.nome == "Escola municipal de T.I. Daniel Batista":
                aluno_por_escola[10] = aluno_por_escola[10] + 1
            elif aluno.escola.nome == "Escola municipal de T.I. Monsenhor Pedro P. Piagem":
                aluno_por_escola[11] = aluno_por_escola[11] + 1
            elif aluno.escola.nome == "Escola municipal Jorge Amado":
                aluno_por_escola[12] = aluno_por_escola[12] + 1
            elif aluno.escola.nome == "Escola municipal Maria Rosa de Castro Sales":
                aluno_por_escola[13] = aluno_por_escola[13] + 1
            elif aluno.escola.nome == "Escola municipal Professor Sávia F. Jacome":
                aluno_por_escola[14] = aluno_por_escola[14] + 1
            elif aluno.escola.nome == "Escola municipal de T.I. Caroline C. C. da Silva":
                aluno_por_escola[15] = aluno_por_escola[15] + 1
            elif aluno.escola.nome == "Escola municipal Aurélio Buarque de Holanda":
                aluno_por_escola[16] = aluno_por_escola[16] + 1
            elif aluno.escola.nome == "Escola municipal Maria Júlia Amorim Rodrigues":
                aluno_por_escola[17] = aluno_por_escola[17] + 1
            elif aluno.escola.nome == "Escola municipal Thiago Barbosa":
                aluno_por_escola[18] = aluno_por_escola[18] + 1
            elif aluno.escola.nome == "Escola municipal de T.I. Euridice F. de Mello":
                aluno_por_escola[19] = aluno_por_escola[19] + 1
            elif aluno.escola.nome == "Escola municipal de T.I. Margarida Gonçalves":
                aluno_por_escola[20] = aluno_por_escola[20] + 1
            elif aluno.escola.nome == "Escola municipal Crispim Pereira de Alencar":
                aluno_por_escola[21] = aluno_por_escola[21] + 1
            elif aluno.escola.nome == "Escola municipal de T.I. Aprigio T. de Matos":
                aluno_por_escola[22] = aluno_por_escola[22] + 1
            elif aluno.escola.nome == "Escola municipal de T.I. João Beltrão":
                aluno_por_escola[23] = aluno_por_escola[23] + 1
            elif aluno.escola.nome == "Escola municipal de T.I. Luiz Nunes de Oliveira":
                aluno_por_escola[24] = aluno_por_escola[24] + 1
            elif aluno.escola.nome == "Escola municipal de T.I. Sueli Pereira A. Reche":
                aluno_por_escola[25] = aluno_por_escola[25] + 1
        
        sexo = [0, 0, 0, 0, 0]
        for aluno in alunos:
            if aluno.sexo == '0':
                sexo[0] += 1
            elif aluno.sexo == '1':
                sexo[1] += 1
            elif aluno.sexo == '2':
                sexo[2] += 1
            elif aluno.sexo == '3':
                sexo[3] += 1
            else:
                sexo[4] += 1
        
        participacao = [0, 0, 0, 0]
        tem_questionario = False
        tem_exame = False
        
        for aluno in alunos:
            try:
                questionario = aluno.questionario
            except Questionario.DoesNotExist:
                tem_questionario = False
            else:
                tem_questionario = True
            
            try:
                exame = aluno.exame
            except Exame.DoesNotExist:
                tem_exame = False
            else:
                tem_exame = True
            
            if tem_questionario and tem_exame:
                participacao[2] = participacao[2] + 1
            elif not tem_questionario and not tem_exame:
                participacao[3] = participacao[3] + 1
            elif tem_questionario:
                participacao[0] = participacao[0] + 1
            else:
                participacao[1] = participacao[1] + 1
        
        raca = [0, 0, 0, 0, 0, 0]
        for aluno in alunos:
            if aluno.raca == '0':
                raca[0] += 1
            elif aluno.raca == '1':
                raca[1] += 1
            elif aluno.raca == '2':
                raca[2] += 1
            elif aluno.raca == '3':
                raca[3] += 1
            elif aluno.raca == '4':
                raca[4] += 1
            else:
                raca[5] += 1
        
        print(raca)
        
        context = {
            'pagina_graficos': True,
            'pagina_graficos_alunos': True,
            'alunos': alunos,
            'aluno_por_escola': aluno_por_escola,
            'sexo': sexo,
            'raca': raca,
            'participacao': participacao,
        }
        
        return render(self.request, 'administracao/graficos_alunos.html', context)


class GraficosQuestionariosView(LoginRequired, View):
    """Página que exibe gráficos baseados nos dados dos questionários"""
    
    def get(self, request):
        questionarios = Questionario.objects.order_by('-id')
        
        questao_1 = self.iniciaQuestao(len(ALUNO_1) + 1)
        questao_2 = self.iniciaQuestao(len(ALUNO_2) + 1)
        questao_3 = self.iniciaQuestao(len(ALUNO_3) + 1)
        questao_4 = self.iniciaQuestao(len(ALUNO_4) + 1)
        questao_5 = self.iniciaQuestao(len(ALUNO_5) + 1)
        questao_6 = self.iniciaQuestao(len(ALUNO_6) + 1)
        questao_7 = self.iniciaQuestao(len(ALUNO_7) + 1)
        questao_8 = self.iniciaQuestao(len(ALUNO_8) + 1)
        questao_9 = self.iniciaQuestao(len(ALUNO_9) + 1)
        questao_10 = self.iniciaQuestao(len(ALUNO_10) + 1)
        questao_11 = self.iniciaQuestao(len(ALUNO_11) + 1)
        questao_12 = self.iniciaQuestao(len(ALUNO_12) + 1)
        questao_13 = self.iniciaQuestao(len(ALUNO_13) + 1)
        questao_14 = self.iniciaQuestao(len(ALUNO_14) + 1)
        questao_15 = self.iniciaQuestao(len(ALUNO_15) + 1)
        questao_16 = self.iniciaQuestao(len(ALUNO_16) + 1)
        questao_17 = self.iniciaQuestao(len(ALUNO_17) + 1)
        questao_18 = self.iniciaQuestao(len(ALUNO_18) + 1)
        questao_19 = self.iniciaQuestao(len(ALUNO_19) + 1)
        questao_20 = self.iniciaQuestao(len(ALUNO_20) + 1)
        questao_21 = self.iniciaQuestao(len(ALUNO_21) + 1)
        questao_22 = self.iniciaQuestao(len(ALUNO_22) + 1)
        questao_23 = self.iniciaQuestao(len(ALUNO_23) + 1)
        questao_24 = self.iniciaQuestao(len(ALUNO_24) + 1)
        questao_25 = self.iniciaQuestao(len(ALUNO_25) + 1)
        questao_26 = self.iniciaQuestao(len(ALUNO_26) + 1)
        questao_27 = self.iniciaQuestao(len(ALUNO_27) + 1)
        questao_28 = self.iniciaQuestao(len(ALUNO_28) + 1)
        questao_29 = self.iniciaQuestao(len(ALUNO_29) + 1)
        questao_30 = self.iniciaQuestao(len(ALUNO_30) + 1)
        questao_31 = self.iniciaQuestao(len(ALUNO_31) + 1)
        questao_32 = self.iniciaQuestao(len(ALUNO_32) + 1)
        questao_33 = self.iniciaQuestao(len(ALUNO_33) + 1)
        questao_34 = self.iniciaQuestao(len(ALUNO_34) + 1)
        questao_35 = self.iniciaQuestao(len(ALUNO_35) + 1)
        questao_36 = self.iniciaQuestao(len(ALUNO_36) + 1)
        questao_37 = self.iniciaQuestao(len(ALUNO_37) + 1)
        questao_38 = self.iniciaQuestao(len(ALUNO_38) + 1)
        questao_39 = self.iniciaQuestao(len(ALUNO_39) + 1)
        questao_40 = self.iniciaQuestao(len(ALUNO_40) + 1)
        questao_41 = self.iniciaQuestao(len(ALUNO_41) + 1)
        questao_42 = self.iniciaQuestao(len(ALUNO_42) + 1)
        questao_43 = self.iniciaQuestao(len(ALUNO_43) + 1)
        questao_44 = self.iniciaQuestao(len(ALUNO_44) + 1)
        questao_45 = self.iniciaQuestao(len(ALUNO_45) + 1)
        questao_46 = self.iniciaQuestao(len(ALUNO_46) + 1)
        questao_47 = self.iniciaQuestao(len(ALUNO_47) + 1)
        questao_48 = self.iniciaQuestao(len(ALUNO_48) + 1)
        questao_49 = self.iniciaQuestao(len(ALUNO_49) + 1)
        questao_50 = self.iniciaQuestao(len(ALUNO_50) + 1)
        questao_51 = self.iniciaQuestao(len(ALUNO_51) + 1)
        questao_52 = self.iniciaQuestao(len(ALUNO_52) + 1)
        questao_53 = self.iniciaQuestao(len(ALUNO_53) + 1)
        questao_54 = self.iniciaQuestao(len(ALUNO_54) + 1)
        questao_55 = self.iniciaQuestao(len(ALUNO_55) + 1)
        questao_56 = self.iniciaQuestao(len(ALUNO_56) + 1)
        questao_57 = self.iniciaQuestao(len(ALUNO_57) + 1)
        questao_58 = self.iniciaQuestao(len(ALUNO_58) + 1)
        questao_59 = self.iniciaQuestao(len(ALUNO_59) + 1)
        questao_60 = self.iniciaQuestao(len(ALUNO_60) + 1)
        questao_61 = self.iniciaQuestao(len(ALUNO_61) + 1)
        questao_62 = self.iniciaQuestao(len(ALUNO_62) + 1)
        questao_63 = self.iniciaQuestao(len(ALUNO_63) + 1)
        questao_64 = self.iniciaQuestao(len(ALUNO_64) + 1)
        questao_65 = self.iniciaQuestao(len(ALUNO_65) + 1)
        questao_66 = self.iniciaQuestao(len(ALUNO_66) + 1)
        questao_67 = self.iniciaQuestao(len(ALUNO_67) + 1)
        questao_68 = self.iniciaQuestao(len(ALUNO_68) + 1)
        questao_69 = self.iniciaQuestao(len(ALUNO_69) + 1)
        questao_70 = self.iniciaQuestao(len(ALUNO_70) + 1)
        questao_71 = self.iniciaQuestao(len(ALUNO_71) + 1)
        questao_72 = self.iniciaQuestao(len(ALUNO_72) + 1)
        questao_73 = self.iniciaQuestao(len(ALUNO_73) + 1)
        questao_74 = self.iniciaQuestao(len(ALUNO_74) + 1)
        questao_75 = self.iniciaQuestao(len(ALUNO_75) + 1)
        questao_76 = self.iniciaQuestao(len(ALUNO_76) + 1)
        questao_77 = self.iniciaQuestao(len(ALUNO_77) + 1)
        questao_78 = self.iniciaQuestao(len(ALUNO_78) + 1)
        questao_79 = self.iniciaQuestao(len(ALUNO_79) + 1)
        questao_80 = self.iniciaQuestao(len(ALUNO_80) + 1)
        questao_81 = self.iniciaQuestao(len(ALUNO_81) + 1)
        questao_82 = self.iniciaQuestao(len(ALUNO_82) + 1)
        questao_83 = self.iniciaQuestao(len(ALUNO_83) + 1)
        questao_84 = self.iniciaQuestao(len(ALUNO_84) + 1)
        questao_85 = self.iniciaQuestao(len(ALUNO_85) + 1)
        questao_86 = self.iniciaQuestao(len(ALUNO_86) + 1)
        questao_87 = self.iniciaQuestao(len(ALUNO_87) + 1)
        questao_88 = self.iniciaQuestao(len(ALUNO_88) + 1)
        questao_89 = self.iniciaQuestao(len(ALUNO_89) + 1)
        questao_90 = self.iniciaQuestao(len(ALUNO_90) + 1)
        questao_91 = self.iniciaQuestao(len(ALUNO_91) + 1)
        questao_92 = self.iniciaQuestao(len(ALUNO_92) + 1)
        questao_93 = self.iniciaQuestao(len(ALUNO_93) + 1)
        questao_94 = self.iniciaQuestao(len(ALUNO_94) + 1)
        questao_95 = self.iniciaQuestao(len(ALUNO_95) + 1)
        questao_96 = self.iniciaQuestao(len(ALUNO_96) + 1)
        questao_97 = self.iniciaQuestao(len(ALUNO_97) + 1)
        questao_98 = self.iniciaQuestao(len(ALUNO_98) + 1)
        questao_99 = self.iniciaQuestao(len(ALUNO_99) + 1)
        questao_100 = self.iniciaQuestao(len(ALUNO_100) + 1)
        questao_101 = self.iniciaQuestao(len(ALUNO_101) + 1)
        questao_102 = self.iniciaQuestao(len(ALUNO_102) + 1)
        questao_103 = self.iniciaQuestao(len(ALUNO_103) + 1)
        questao_104 = self.iniciaQuestao(len(ALUNO_104) + 1)
        questao_105 = self.iniciaQuestao(len(ALUNO_105) + 1)
        questao_106 = self.iniciaQuestao(len(ALUNO_106) + 1)
        questao_107 = self.iniciaQuestao(len(ALUNO_107) + 1)
        questao_108 = self.iniciaQuestao(len(ALUNO_108) + 1)
        questao_109 = self.iniciaQuestao(len(ALUNO_109) + 1)
        questao_110 = self.iniciaQuestao(len(ALUNO_110) + 1)
        questao_111 = self.iniciaQuestao(len(ALUNO_111) + 1)
        questao_112 = self.iniciaQuestao(len(ALUNO_112) + 1)
        questao_113 = self.iniciaQuestao(len(ALUNO_113) + 1)
        questao_114 = self.iniciaQuestao(len(ALUNO_114) + 1)
        questao_115 = self.iniciaQuestao(len(ALUNO_115) + 1)
        questao_116 = self.iniciaQuestao(len(ALUNO_116) + 1)
        questao_117 = self.iniciaQuestao(len(ALUNO_117) + 1)
        questao_118 = self.iniciaQuestao(len(ALUNO_118) + 1)
        questao_119 = self.iniciaQuestao(len(ALUNO_119) + 1)
        questao_120 = self.iniciaQuestao(len(ALUNO_120) + 1)
        questao_121 = self.iniciaQuestao(len(ALUNO_121) + 1)
        questao_122 = self.iniciaQuestao(len(ALUNO_122) + 1)
        questao_123 = self.iniciaQuestao(len(ALUNO_123) + 1)
        questao_124 = self.iniciaQuestao(len(ALUNO_124) + 1)
        questao_125 = self.iniciaQuestao(len(ALUNO_125) + 1)
        questao_126 = self.iniciaQuestao(len(ALUNO_126) + 1)
        questao_127 = self.iniciaQuestao(len(ALUNO_127) + 1)
        questao_128 = self.iniciaQuestao(len(ALUNO_128) + 1)
        questao_129 = self.iniciaQuestao(len(ALUNO_129) + 1)
        questao_130 = self.iniciaQuestao(len(ALUNO_130) + 1)
        questao_131 = self.iniciaQuestao(len(ALUNO_131) + 1)
        questao_132 = self.iniciaQuestao(len(ALUNO_132) + 1)
        questao_133 = self.iniciaQuestao(len(ALUNO_133) + 1)
        questao_134 = self.iniciaQuestao(len(ALUNO_134) + 1)
        questao_135 = self.iniciaQuestao(len(ALUNO_135) + 1)
        questao_136 = self.iniciaQuestao(len(ALUNO_136) + 1)
        questao_137 = self.iniciaQuestao(len(ALUNO_137) + 1)
        questao_138 = self.iniciaQuestao(len(ALUNO_138) + 1)
        questao_139 = self.iniciaQuestao(len(ALUNO_139) + 1)
        questao_140 = self.iniciaQuestao(len(ALUNO_140) + 1)
        questao_141 = self.iniciaQuestao(len(ALUNO_141) + 1)
        questao_142 = self.iniciaQuestao(len(ALUNO_142) + 1)
        questao_143 = self.iniciaQuestao(len(ALUNO_143) + 1)
        questao_144 = self.iniciaQuestao(len(ALUNO_144) + 1)
        questao_145 = self.iniciaQuestao(len(ALUNO_145) + 1)
        questao_146 = self.iniciaQuestao(len(ALUNO_146) + 1)
        
        for questionario in questionarios:
            if questionario.questao_1 == None:
                questao_1[len(ALUNO_1)] = questao_1[len(ALUNO_1)] + 1
            else:
                questao_1[int(questionario.questao_1)] = questao_1[int(questionario.questao_1)] + 1
            if questionario.questao_2 == None:
                questao_2[len(ALUNO_2)] = questao_2[len(ALUNO_2)] + 1
            else:
                questao_2[int(questionario.questao_2)] = questao_2[int(questionario.questao_2)] + 1
            if questionario.questao_3 == None:
                questao_3[len(ALUNO_3)] = questao_3[len(ALUNO_3)] + 1
            else:
                questao_3[int(questionario.questao_3)] = questao_3[int(questionario.questao_3)] + 1
            if questionario.questao_4 == None:
                questao_4[len(ALUNO_4)] = questao_4[len(ALUNO_4)] + 1
            else:
                questao_4[int(questionario.questao_4)] = questao_4[int(questionario.questao_4)] + 1
            if questionario.questao_5 == None:
                questao_5[len(ALUNO_5)] = questao_5[len(ALUNO_5)] + 1
            else:
                questao_5[int(questionario.questao_5)] = questao_5[int(questionario.questao_5)] + 1
            if questionario.questao_6 == None:
                questao_6[len(ALUNO_6)] = questao_6[len(ALUNO_6)] + 1
            else:
                questao_6[int(questionario.questao_6)] = questao_6[int(questionario.questao_6)] + 1
            if questionario.questao_7 == None:
                questao_7[len(ALUNO_7)] = questao_7[len(ALUNO_7)] + 1
            else:
                questao_7[int(questionario.questao_7)] = questao_7[int(questionario.questao_7)] + 1
            if questionario.questao_8 == None:
                questao_8[len(ALUNO_8)] = questao_8[len(ALUNO_8)] + 1
            else:
                questao_8[int(questionario.questao_8)] = questao_8[int(questionario.questao_8)] + 1
            if questionario.questao_9 == None:
                questao_9[len(ALUNO_9)] = questao_9[len(ALUNO_9)] + 1
            else:
                questao_9[int(questionario.questao_9)] = questao_9[int(questionario.questao_9)] + 1
            if questionario.questao_10 == None:
                questao_10[len(ALUNO_10)] = questao_10[len(ALUNO_10)] + 1
            else:
                questao_10[int(questionario.questao_10)] = questao_10[int(questionario.questao_10)] + 1
            if questionario.questao_11 == None:
                questao_11[len(ALUNO_11)] = questao_11[len(ALUNO_11)] + 1
            else:
                questao_11[int(questionario.questao_11)] = questao_11[int(questionario.questao_11)] + 1
            if questionario.questao_12 == None:
                questao_12[len(ALUNO_12)] = questao_12[len(ALUNO_12)] + 1
            else:
                questao_12[int(questionario.questao_12)] = questao_12[int(questionario.questao_12)] + 1
            if questionario.questao_13 == None:
                questao_13[len(ALUNO_13)] = questao_13[len(ALUNO_13)] + 1
            else:
                questao_13[int(questionario.questao_13)] = questao_13[int(questionario.questao_13)] + 1
            if questionario.questao_14 == None:
                questao_14[len(ALUNO_14)] = questao_14[len(ALUNO_14)] + 1
            else:
                questao_14[int(questionario.questao_14)] = questao_14[int(questionario.questao_14)] + 1
            if questionario.questao_15 == None:
                questao_15[len(ALUNO_15)] = questao_15[len(ALUNO_15)] + 1
            else:
                questao_15[int(questionario.questao_15)] = questao_15[int(questionario.questao_15)] + 1
            if questionario.questao_16 == None:
                questao_16[len(ALUNO_16)] = questao_16[len(ALUNO_16)] + 1
            else:
                questao_16[int(questionario.questao_16)] = questao_16[int(questionario.questao_16)] + 1
            if questionario.questao_17 == None:
                questao_17[len(ALUNO_17)] = questao_17[len(ALUNO_17)] + 1
            else:
                questao_17[int(questionario.questao_17)] = questao_17[int(questionario.questao_17)] + 1
            if questionario.questao_18 == None:
                questao_18[len(ALUNO_18)] = questao_18[len(ALUNO_18)] + 1
            else:
                questao_18[int(questionario.questao_18)] = questao_18[int(questionario.questao_18)] + 1
            if questionario.questao_19 == None:
                questao_19[len(ALUNO_19)] = questao_19[len(ALUNO_19)] + 1
            else:
                questao_19[int(questionario.questao_19)] = questao_19[int(questionario.questao_19)] + 1
            if questionario.questao_20 == None:
                questao_20[len(ALUNO_20)] = questao_20[len(ALUNO_20)] + 1
            else:
                questao_20[int(questionario.questao_20)] = questao_20[int(questionario.questao_20)] + 1
            if questionario.questao_21 == None:
                questao_21[len(ALUNO_21)] = questao_21[len(ALUNO_21)] + 1
            else:
                questao_21[int(questionario.questao_21)] = questao_21[int(questionario.questao_21)] + 1
            if questionario.questao_22 == None:
                questao_22[len(ALUNO_22)] = questao_22[len(ALUNO_22)] + 1
            else:
                questao_22[int(questionario.questao_22)] = questao_22[int(questionario.questao_22)] + 1
            if questionario.questao_23 == None:
                questao_23[len(ALUNO_23)] = questao_23[len(ALUNO_23)] + 1
            else:
                questao_23[int(questionario.questao_23)] = questao_23[int(questionario.questao_23)] + 1
            if questionario.questao_24 == None:
                questao_24[len(ALUNO_24)] = questao_24[len(ALUNO_24)] + 1
            else:
                questao_24[int(questionario.questao_24)] = questao_24[int(questionario.questao_24)] + 1
            if questionario.questao_25 == None:
                questao_25[len(ALUNO_25)] = questao_25[len(ALUNO_25)] + 1
            else:
                questao_25[int(questionario.questao_25)] = questao_25[int(questionario.questao_25)] + 1
            if questionario.questao_26 == None:
                questao_26[len(ALUNO_26)] = questao_26[len(ALUNO_26)] + 1
            else:
                questao_26[int(questionario.questao_26)] = questao_26[int(questionario.questao_26)] + 1
            if questionario.questao_27 == None:
                questao_27[len(ALUNO_27)] = questao_27[len(ALUNO_27)] + 1
            else:
                questao_27[int(questionario.questao_27)] = questao_27[int(questionario.questao_27)] + 1
            if questionario.questao_28 == None:
                questao_28[len(ALUNO_28)] = questao_28[len(ALUNO_28)] + 1
            else:
                questao_28[int(questionario.questao_28)] = questao_28[int(questionario.questao_28)] + 1
            if questionario.questao_29 == None:
                questao_29[len(ALUNO_29)] = questao_29[len(ALUNO_29)] + 1
            else:
                questao_29[int(questionario.questao_29)] = questao_29[int(questionario.questao_29)] + 1
            if questionario.questao_30 == None:
                questao_30[len(ALUNO_30)] = questao_30[len(ALUNO_30)] + 1
            else:
                questao_30[int(questionario.questao_30)] = questao_30[int(questionario.questao_30)] + 1
            if questionario.questao_31 == None:
                questao_31[len(ALUNO_31)] = questao_31[len(ALUNO_31)] + 1
            else:
                questao_31[int(questionario.questao_31)] = questao_31[int(questionario.questao_31)] + 1
            if questionario.questao_32 == None:
                questao_32[len(ALUNO_32)] = questao_32[len(ALUNO_32)] + 1
            else:
                questao_32[int(questionario.questao_32)] = questao_32[int(questionario.questao_32)] + 1
            if questionario.questao_33 == None:
                questao_33[len(ALUNO_33)] = questao_33[len(ALUNO_33)] + 1
            else:
                questao_33[int(questionario.questao_33)] = questao_33[int(questionario.questao_33)] + 1
            if questionario.questao_34 == None:
                questao_34[len(ALUNO_34)] = questao_34[len(ALUNO_34)] + 1
            else:
                questao_34[int(questionario.questao_34)] = questao_34[int(questionario.questao_34)] + 1
            if questionario.questao_35 == None:
                questao_35[len(ALUNO_35)] = questao_35[len(ALUNO_35)] + 1
            else:
                questao_35[int(questionario.questao_35)] = questao_35[int(questionario.questao_35)] + 1
            if questionario.questao_36 == None:
                questao_36[len(ALUNO_36)] = questao_36[len(ALUNO_36)] + 1
            else:
                questao_36[int(questionario.questao_36)] = questao_36[int(questionario.questao_36)] + 1
            if questionario.questao_37 == None:
                questao_37[len(ALUNO_37)] = questao_37[len(ALUNO_37)] + 1
            else:
                questao_37[int(questionario.questao_37)] = questao_37[int(questionario.questao_37)] + 1
            if questionario.questao_38 == None:
                questao_38[len(ALUNO_38)] = questao_38[len(ALUNO_38)] + 1
            else:
                questao_38[int(questionario.questao_38)] = questao_38[int(questionario.questao_38)] + 1
            if questionario.questao_39 == None:
                questao_39[len(ALUNO_39)] = questao_39[len(ALUNO_39)] + 1
            else:
                questao_39[int(questionario.questao_39)] = questao_39[int(questionario.questao_39)] + 1
            if questionario.questao_40 == None:
                questao_40[len(ALUNO_40)] = questao_40[len(ALUNO_40)] + 1
            else:
                questao_40[int(questionario.questao_40)] = questao_40[int(questionario.questao_40)] + 1
            if questionario.questao_41 == None:
                questao_41[len(ALUNO_41)] = questao_41[len(ALUNO_41)] + 1
            else:
                questao_41[int(questionario.questao_41)] = questao_41[int(questionario.questao_41)] + 1
            if questionario.questao_42 == None:
                questao_42[len(ALUNO_42)] = questao_42[len(ALUNO_42)] + 1
            else:
                questao_42[int(questionario.questao_42)] = questao_42[int(questionario.questao_42)] + 1
            if questionario.questao_43 == None:
                questao_43[len(ALUNO_43)] = questao_43[len(ALUNO_43)] + 1
            else:
                questao_43[int(questionario.questao_43)] = questao_43[int(questionario.questao_43)] + 1
            if questionario.questao_44 == None:
                questao_44[len(ALUNO_44)] = questao_44[len(ALUNO_44)] + 1
            else:
                questao_44[int(questionario.questao_44)] = questao_44[int(questionario.questao_44)] + 1
            if questionario.questao_45 == None:
                questao_45[len(ALUNO_45)] = questao_45[len(ALUNO_45)] + 1
            else:
                questao_45[int(questionario.questao_45)] = questao_45[int(questionario.questao_45)] + 1
            if questionario.questao_46 == None:
                questao_46[len(ALUNO_46)] = questao_46[len(ALUNO_46)] + 1
            else:
                questao_46[int(questionario.questao_46)] = questao_46[int(questionario.questao_46)] + 1
            if questionario.questao_47 == None:
                questao_47[len(ALUNO_47)] = questao_47[len(ALUNO_47)] + 1
            else:
                questao_47[int(questionario.questao_47)] = questao_47[int(questionario.questao_47)] + 1
            if questionario.questao_48 == None:
                questao_48[len(ALUNO_48)] = questao_48[len(ALUNO_48)] + 1
            else:
                questao_48[int(questionario.questao_48)] = questao_48[int(questionario.questao_48)] + 1
            if questionario.questao_49 == None:
                questao_49[len(ALUNO_49)] = questao_49[len(ALUNO_49)] + 1
            else:
                questao_49[int(questionario.questao_49)] = questao_49[int(questionario.questao_49)] + 1
            if questionario.questao_50 == None:
                questao_50[len(ALUNO_50)] = questao_50[len(ALUNO_50)] + 1
            else:
                questao_50[int(questionario.questao_50)] = questao_50[int(questionario.questao_50)] + 1
            if questionario.questao_51 == None:
                questao_51[len(ALUNO_51)] = questao_51[len(ALUNO_51)] + 1
            else:
                questao_51[int(questionario.questao_51)] = questao_51[int(questionario.questao_51)] + 1
            if questionario.questao_52 == None:
                questao_52[len(ALUNO_52)] = questao_52[len(ALUNO_52)] + 1
            else:
                questao_52[int(questionario.questao_52)] = questao_52[int(questionario.questao_52)] + 1
            if questionario.questao_53 == None:
                questao_53[len(ALUNO_53)] = questao_53[len(ALUNO_53)] + 1
            else:
                questao_53[int(questionario.questao_53)] = questao_53[int(questionario.questao_53)] + 1
            if questionario.questao_54 == None:
                questao_54[len(ALUNO_54)] = questao_54[len(ALUNO_54)] + 1
            else:
                questao_54[int(questionario.questao_54)] = questao_54[int(questionario.questao_54)] + 1
            if questionario.questao_55 == None:
                questao_55[len(ALUNO_55)] = questao_55[len(ALUNO_55)] + 1
            else:
                questao_55[int(questionario.questao_55)] = questao_55[int(questionario.questao_55)] + 1
            if questionario.questao_56 == None:
                questao_56[len(ALUNO_56)] = questao_56[len(ALUNO_56)] + 1
            else:
                questao_56[int(questionario.questao_56)] = questao_56[int(questionario.questao_56)] + 1
            if questionario.questao_57 == None:
                questao_57[len(ALUNO_57)] = questao_57[len(ALUNO_57)] + 1
            else:
                questao_57[int(questionario.questao_57)] = questao_57[int(questionario.questao_57)] + 1
            if questionario.questao_58 == None:
                questao_58[len(ALUNO_58)] = questao_58[len(ALUNO_58)] + 1
            else:
                questao_58[int(questionario.questao_58)] = questao_58[int(questionario.questao_58)] + 1
            if questionario.questao_59 == None:
                questao_59[len(ALUNO_59)] = questao_59[len(ALUNO_59)] + 1
            else:
                questao_59[int(questionario.questao_59)] = questao_59[int(questionario.questao_59)] + 1
            if questionario.questao_60 == None:
                questao_60[len(ALUNO_60)] = questao_60[len(ALUNO_60)] + 1
            else:
                for escolhas in questionario.questao_60:
                    for escolha in escolhas:
                        questao_60[int(escolha)] = questao_60[int(escolha)] + 1
            if questionario.questao_61 == None:
                questao_61[len(ALUNO_61)] = questao_61[len(ALUNO_61)] + 1
            else:
                questao_61[int(questionario.questao_61)] = questao_61[int(questionario.questao_61)] + 1
            if questionario.questao_62 == None:
                questao_62[len(ALUNO_62)] = questao_62[len(ALUNO_62)] + 1
            else:
                questao_62[int(questionario.questao_62)] = questao_62[int(questionario.questao_62)] + 1
            if questionario.questao_63 == None:
                questao_63[len(ALUNO_63)] = questao_63[len(ALUNO_63)] + 1
            else:
                questao_63[int(questionario.questao_63)] = questao_63[int(questionario.questao_63)] + 1
            if questionario.questao_64 == None:
                questao_64[len(ALUNO_64)] = questao_64[len(ALUNO_64)] + 1
            else:
                questao_64[int(questionario.questao_64)] = questao_64[int(questionario.questao_64)] + 1
            if questionario.questao_65 == None:
                questao_65[len(ALUNO_65)] = questao_65[len(ALUNO_65)] + 1
            else:
                questao_65[int(questionario.questao_65)] = questao_65[int(questionario.questao_65)] + 1
            if questionario.questao_66 == None:
                questao_66[len(ALUNO_66)] = questao_66[len(ALUNO_66)] + 1
            else:
                questao_66[int(questionario.questao_66)] = questao_66[int(questionario.questao_66)] + 1
            if questionario.questao_67 == None:
                questao_67[len(ALUNO_67)] = questao_67[len(ALUNO_67)] + 1
            else:
                questao_67[int(questionario.questao_67)] = questao_67[int(questionario.questao_67)] + 1
            if questionario.questao_68 == None:
                questao_68[len(ALUNO_68)] = questao_68[len(ALUNO_68)] + 1
            else:
                questao_68[int(questionario.questao_68)] = questao_68[int(questionario.questao_68)] + 1
            if questionario.questao_69 == None:
                questao_69[len(ALUNO_69)] = questao_69[len(ALUNO_69)] + 1
            else:
                questao_69[int(questionario.questao_69)] = questao_69[int(questionario.questao_69)] + 1
            if questionario.questao_70 == None:
                questao_70[len(ALUNO_70)] = questao_70[len(ALUNO_70)] + 1
            else:
                questao_70[int(questionario.questao_70)] = questao_70[int(questionario.questao_70)] + 1
            if questionario.questao_71 == None:
                questao_71[len(ALUNO_71)] = questao_71[len(ALUNO_71)] + 1
            else:
                questao_71[int(questionario.questao_71)] = questao_71[int(questionario.questao_71)] + 1
            if questionario.questao_72 == None:
                questao_72[len(ALUNO_72)] = questao_72[len(ALUNO_72)] + 1
            else:
                questao_72[int(questionario.questao_72)] = questao_72[int(questionario.questao_72)] + 1
            if questionario.questao_73 == None:
                questao_73[len(ALUNO_73)] = questao_73[len(ALUNO_73)] + 1
            else:
                questao_73[int(questionario.questao_73)] = questao_73[int(questionario.questao_73)] + 1
            if questionario.questao_74 == None:
                questao_74[len(ALUNO_74)] = questao_74[len(ALUNO_74)] + 1
            else:
                questao_74[int(questionario.questao_74)] = questao_74[int(questionario.questao_74)] + 1
            if questionario.questao_75 == None:
                questao_75[len(ALUNO_75)] = questao_75[len(ALUNO_75)] + 1
            else:
                questao_75[int(questionario.questao_75)] = questao_75[int(questionario.questao_75)] + 1
            if questionario.questao_76 == None:
                questao_76[len(ALUNO_76)] = questao_76[len(ALUNO_76)] + 1
            else:
                questao_76[int(questionario.questao_76)] = questao_76[int(questionario.questao_76)] + 1
            if questionario.questao_77 == None:
                questao_77[len(ALUNO_77)] = questao_77[len(ALUNO_77)] + 1
            else:
                questao_77[int(questionario.questao_77)] = questao_77[int(questionario.questao_77)] + 1
            if questionario.questao_78 == None:
                questao_78[len(ALUNO_78)] = questao_78[len(ALUNO_78)] + 1
            else:
                questao_78[int(questionario.questao_78)] = questao_78[int(questionario.questao_78)] + 1
            if questionario.questao_79 == None:
                questao_79[len(ALUNO_79)] = questao_79[len(ALUNO_79)] + 1
            else:
                questao_79[int(questionario.questao_79)] = questao_79[int(questionario.questao_79)] + 1
            if questionario.questao_80 == None:
                questao_80[len(ALUNO_80)] = questao_80[len(ALUNO_80)] + 1
            else:
                questao_80[int(questionario.questao_80)] = questao_80[int(questionario.questao_80)] + 1
            if questionario.questao_81 == None:
                questao_81[len(ALUNO_81)] = questao_81[len(ALUNO_81)] + 1
            else:
                questao_81[int(questionario.questao_81)] = questao_81[int(questionario.questao_81)] + 1
            if questionario.questao_82 == None:
                questao_82[len(ALUNO_82)] = questao_82[len(ALUNO_82)] + 1
            else:
                questao_82[int(questionario.questao_82)] = questao_82[int(questionario.questao_82)] + 1
            if questionario.questao_83 == None:
                questao_83[len(ALUNO_83)] = questao_83[len(ALUNO_83)] + 1
            else:
                questao_83[int(questionario.questao_83)] = questao_83[int(questionario.questao_83)] + 1
            if questionario.questao_84 == None:
                questao_84[len(ALUNO_84)] = questao_84[len(ALUNO_84)] + 1
            else:
                questao_84[int(questionario.questao_84)] = questao_84[int(questionario.questao_84)] + 1
            if questionario.questao_85 == None:
                questao_85[len(ALUNO_85)] = questao_85[len(ALUNO_85)] + 1
            else:
                questao_85[int(questionario.questao_85)] = questao_85[int(questionario.questao_85)] + 1
            if questionario.questao_86 == None:
                questao_86[len(ALUNO_86)] = questao_86[len(ALUNO_86)] + 1
            else:
                questao_86[int(questionario.questao_86)] = questao_86[int(questionario.questao_86)] + 1
            if questionario.questao_87 == None:
                questao_87[len(ALUNO_87)] = questao_87[len(ALUNO_87)] + 1
            else:
                questao_87[int(questionario.questao_87)] = questao_87[int(questionario.questao_87)] + 1
            if questionario.questao_88 == None:
                questao_88[len(ALUNO_88)] = questao_88[len(ALUNO_88)] + 1
            else:
                questao_88[int(questionario.questao_88)] = questao_88[int(questionario.questao_88)] + 1
            if questionario.questao_89 == None:
                questao_89[len(ALUNO_89)] = questao_89[len(ALUNO_89)] + 1
            else:
                questao_89[int(questionario.questao_89)] = questao_89[int(questionario.questao_89)] + 1
            if questionario.questao_90 == None:
                questao_90[len(ALUNO_90)] = questao_90[len(ALUNO_90)] + 1
            else:
                questao_90[int(questionario.questao_90)] = questao_90[int(questionario.questao_90)] + 1
            if questionario.questao_91 == None:
                questao_91[len(ALUNO_91)] = questao_91[len(ALUNO_91)] + 1
            else:
                questao_91[int(questionario.questao_91)] = questao_91[int(questionario.questao_91)] + 1
            if questionario.questao_92 == None:
                questao_92[len(ALUNO_92)] = questao_92[len(ALUNO_92)] + 1
            else:
                questao_92[int(questionario.questao_92)] = questao_92[int(questionario.questao_92)] + 1
            if questionario.questao_93 == None:
                questao_93[len(ALUNO_93)] = questao_93[len(ALUNO_93)] + 1
            else:
                questao_93[int(questionario.questao_93)] = questao_93[int(questionario.questao_93)] + 1
            if questionario.questao_94 == None:
                questao_94[len(ALUNO_94)] = questao_94[len(ALUNO_94)] + 1
            else:
                questao_94[int(questionario.questao_94)] = questao_94[int(questionario.questao_94)] + 1
            if questionario.questao_95 == None:
                questao_95[len(ALUNO_95)] = questao_95[len(ALUNO_95)] + 1
            else:
                questao_95[int(questionario.questao_95)] = questao_95[int(questionario.questao_95)] + 1
            if questionario.questao_96 == None:
                questao_96[len(ALUNO_96)] = questao_96[len(ALUNO_96)] + 1
            else:
                questao_96[int(questionario.questao_96)] = questao_96[int(questionario.questao_96)] + 1
            if questionario.questao_97 == None:
                questao_97[len(ALUNO_97)] = questao_97[len(ALUNO_97)] + 1
            else:
                questao_97[int(questionario.questao_97)] = questao_97[int(questionario.questao_97)] + 1
            if questionario.questao_98 == None:
                questao_98[len(ALUNO_98)] = questao_98[len(ALUNO_98)] + 1
            else:
                questao_98[int(questionario.questao_98)] = questao_98[int(questionario.questao_98)] + 1
            if questionario.questao_99 == None:
                questao_99[len(ALUNO_99)] = questao_99[len(ALUNO_99)] + 1
            else:
                questao_99[int(questionario.questao_99)] = questao_99[int(questionario.questao_99)] + 1
            if questionario.questao_100 == None:
                questao_100[len(ALUNO_100)] = questao_100[len(ALUNO_100)] + 1
            else:
                questao_100[int(questionario.questao_100)] = questao_100[int(questionario.questao_100)] + 1
            if questionario.questao_101 == None:
                questao_101[len(ALUNO_101)] = questao_101[len(ALUNO_101)] + 1
            else:
                questao_101[int(questionario.questao_101)] = questao_101[int(questionario.questao_101)] + 1
            if questionario.questao_102 == None:
                questao_102[len(ALUNO_102)] = questao_102[len(ALUNO_102)] + 1
            else:
                questao_102[int(questionario.questao_102)] = questao_102[int(questionario.questao_102)] + 1
            if questionario.questao_103 == None:
                questao_103[len(ALUNO_103)] = questao_103[len(ALUNO_103)] + 1
            else:
                questao_103[int(questionario.questao_103)] = questao_103[int(questionario.questao_103)] + 1
            if questionario.questao_104 == None:
                questao_104[len(ALUNO_104)] = questao_104[len(ALUNO_104)] + 1
            else:
                questao_104[int(questionario.questao_104)] = questao_104[int(questionario.questao_104)] + 1
            if questionario.questao_105 == None:
                questao_105[len(ALUNO_105)] = questao_105[len(ALUNO_105)] + 1
            else:
                questao_105[int(questionario.questao_105)] = questao_105[int(questionario.questao_105)] + 1
            if questionario.questao_106 == None:
                questao_106[len(ALUNO_106)] = questao_106[len(ALUNO_106)] + 1
            else:
                questao_106[int(questionario.questao_106)] = questao_106[int(questionario.questao_106)] + 1
            if questionario.questao_107 == None:
                questao_107[len(ALUNO_107)] = questao_107[len(ALUNO_107)] + 1
            else:
                questao_107[int(questionario.questao_107)] = questao_107[int(questionario.questao_107)] + 1
            if questionario.questao_108 == None:
                questao_108[len(ALUNO_108)] = questao_108[len(ALUNO_108)] + 1
            else:
                questao_108[int(questionario.questao_108)] = questao_108[int(questionario.questao_108)] + 1
            if questionario.questao_109 == None:
                questao_109[len(ALUNO_109)] = questao_109[len(ALUNO_109)] + 1
            else:
                questao_109[int(questionario.questao_109)] = questao_109[int(questionario.questao_109)] + 1
            if questionario.questao_110 == None:
                questao_110[len(ALUNO_110)] = questao_110[len(ALUNO_110)] + 1
            else:
                questao_110[int(questionario.questao_110)] = questao_110[int(questionario.questao_110)] + 1
            if questionario.questao_111 == None:
                questao_111[len(ALUNO_111)] = questao_111[len(ALUNO_111)] + 1
            else:
                questao_111[int(questionario.questao_111)] = questao_111[int(questionario.questao_111)] + 1
            if questionario.questao_112 == None:
                questao_112[len(ALUNO_112)] = questao_112[len(ALUNO_112)] + 1
            else:
                questao_112[int(questionario.questao_112)] = questao_112[int(questionario.questao_112)] + 1
            if questionario.questao_113 == None:
                questao_113[len(ALUNO_113)] = questao_113[len(ALUNO_113)] + 1
            else:
                questao_113[int(questionario.questao_113)] = questao_113[int(questionario.questao_113)] + 1
            if questionario.questao_114 == None:
                questao_114[len(ALUNO_114)] = questao_114[len(ALUNO_114)] + 1
            else:
                questao_114[int(questionario.questao_114)] = questao_114[int(questionario.questao_114)] + 1
            if questionario.questao_115 == None:
                questao_115[len(ALUNO_115)] = questao_115[len(ALUNO_115)] + 1
            else:
                questao_115[int(questionario.questao_115)] = questao_115[int(questionario.questao_115)] + 1
            if questionario.questao_116 == None:
                questao_116[len(ALUNO_116)] = questao_116[len(ALUNO_116)] + 1
            else:
                questao_116[int(questionario.questao_116)] = questao_116[int(questionario.questao_116)] + 1
            if questionario.questao_117 == None:
                questao_117[len(ALUNO_117)] = questao_117[len(ALUNO_117)] + 1
            else:
                questao_117[int(questionario.questao_117)] = questao_117[int(questionario.questao_117)] + 1
            if questionario.questao_118 == None:
                questao_118[len(ALUNO_118)] = questao_118[len(ALUNO_118)] + 1
            else:
                questao_118[int(questionario.questao_118)] = questao_118[int(questionario.questao_118)] + 1
            if questionario.questao_119 == None:
                questao_119[len(ALUNO_119)] = questao_119[len(ALUNO_119)] + 1
            else:
                questao_119[int(questionario.questao_119)] = questao_119[int(questionario.questao_119)] + 1
            if questionario.questao_120 == None:
                questao_120[len(ALUNO_120)] = questao_120[len(ALUNO_120)] + 1
            else:
                questao_120[int(questionario.questao_120)] = questao_120[int(questionario.questao_120)] + 1
            if questionario.questao_121 == None:
                questao_121[len(ALUNO_121)] = questao_121[len(ALUNO_121)] + 1
            else:
                questao_121[int(questionario.questao_121)] = questao_121[int(questionario.questao_121)] + 1
            if questionario.questao_122 == None:
                questao_122[len(ALUNO_122)] = questao_122[len(ALUNO_122)] + 1
            else:
                questao_122[int(questionario.questao_122)] = questao_122[int(questionario.questao_122)] + 1
            if questionario.questao_123 == None:
                questao_123[len(ALUNO_123)] = questao_123[len(ALUNO_123)] + 1
            else:
                questao_123[int(questionario.questao_123)] = questao_123[int(questionario.questao_123)] + 1
            if questionario.questao_124 == None:
                questao_124[len(ALUNO_124)] = questao_124[len(ALUNO_124)] + 1
            else:
                questao_124[int(questionario.questao_124)] = questao_124[int(questionario.questao_124)] + 1
            if questionario.questao_125 == None:
                questao_125[len(ALUNO_125)] = questao_125[len(ALUNO_125)] + 1
            else:
                questao_125[int(questionario.questao_125)] = questao_125[int(questionario.questao_125)] + 1
            if questionario.questao_126 == None:
                questao_126[len(ALUNO_126)] = questao_126[len(ALUNO_126)] + 1
            else:
                questao_126[int(questionario.questao_126)] = questao_126[int(questionario.questao_126)] + 1
            if questionario.questao_127 == None:
                questao_127[len(ALUNO_127)] = questao_127[len(ALUNO_127)] + 1
            else:
                questao_127[int(questionario.questao_127)] = questao_127[int(questionario.questao_127)] + 1
            if questionario.questao_128 == None:
                questao_128[len(ALUNO_128)] = questao_128[len(ALUNO_128)] + 1
            else:
                questao_128[int(questionario.questao_128)] = questao_128[int(questionario.questao_128)] + 1
            if questionario.questao_129 == None:
                questao_129[len(ALUNO_129)] = questao_129[len(ALUNO_129)] + 1
            else:
                questao_129[int(questionario.questao_129)] = questao_129[int(questionario.questao_129)] + 1
            if questionario.questao_130 == None:
                questao_130[len(ALUNO_130)] = questao_130[len(ALUNO_130)] + 1
            else:
                questao_130[int(questionario.questao_130)] = questao_130[int(questionario.questao_130)] + 1
            if questionario.questao_131 == None:
                questao_131[len(ALUNO_131)] = questao_131[len(ALUNO_131)] + 1
            else:
                questao_131[int(questionario.questao_131)] = questao_131[int(questionario.questao_131)] + 1
            if questionario.questao_132 == None:
                questao_132[len(ALUNO_132)] = questao_132[len(ALUNO_132)] + 1
            else:
                questao_132[int(questionario.questao_132)] = questao_132[int(questionario.questao_132)] + 1
            if questionario.questao_133 == None:
                questao_133[len(ALUNO_133)] = questao_133[len(ALUNO_133)] + 1
            else:
                questao_133[int(questionario.questao_133)] = questao_133[int(questionario.questao_133)] + 1
            if questionario.questao_134 == None:
                questao_134[len(ALUNO_134)] = questao_134[len(ALUNO_134)] + 1
            else:
                questao_134[int(questionario.questao_134)] = questao_134[int(questionario.questao_134)] + 1
            if questionario.questao_135 == None:
                questao_135[len(ALUNO_135)] = questao_135[len(ALUNO_135)] + 1
            else:
                questao_135[int(questionario.questao_135)] = questao_135[int(questionario.questao_135)] + 1
            if questionario.questao_136 == None:
                questao_136[len(ALUNO_136)] = questao_136[len(ALUNO_136)] + 1
            else:
                questao_136[int(questionario.questao_136)] = questao_136[int(questionario.questao_136)] + 1
            if questionario.questao_137 == None:
                questao_137[len(ALUNO_137)] = questao_137[len(ALUNO_137)] + 1
            else:
                questao_137[int(questionario.questao_137)] = questao_137[int(questionario.questao_137)] + 1
            if questionario.questao_138 == None:
                questao_138[len(ALUNO_138)] = questao_138[len(ALUNO_138)] + 1
            else:
                questao_138[int(questionario.questao_138)] = questao_138[int(questionario.questao_138)] + 1
            if questionario.questao_139 == None:
                questao_139[len(ALUNO_139)] = questao_139[len(ALUNO_139)] + 1
            else:
                questao_139[int(questionario.questao_139)] = questao_139[int(questionario.questao_139)] + 1
            if questionario.questao_140 == None:
                questao_140[len(ALUNO_140)] = questao_140[len(ALUNO_140)] + 1
            else:
                questao_140[int(questionario.questao_140)] = questao_140[int(questionario.questao_140)] + 1
            if questionario.questao_141 == None:
                questao_141[len(ALUNO_141)] = questao_141[len(ALUNO_141)] + 1
            else:
                questao_141[int(questionario.questao_141)] = questao_141[int(questionario.questao_141)] + 1
            if questionario.questao_142 == None:
                questao_142[len(ALUNO_142)] = questao_142[len(ALUNO_142)] + 1
            else:
                questao_142[int(questionario.questao_142)] = questao_142[int(questionario.questao_142)] + 1
            if questionario.questao_143 == None:
                questao_143[len(ALUNO_143)] = questao_143[len(ALUNO_143)] + 1
            else:
                questao_143[int(questionario.questao_143)] = questao_143[int(questionario.questao_143)] + 1
            if questionario.questao_144 == None:
                questao_144[len(ALUNO_144)] = questao_144[len(ALUNO_144)] + 1
            else:
                questao_144[int(questionario.questao_144)] = questao_144[int(questionario.questao_144)] + 1
            if questionario.questao_145 == None:
                questao_145[len(ALUNO_145)] = questao_145[len(ALUNO_145)] + 1
            else:
                questao_145[int(questionario.questao_145)] = questao_145[int(questionario.questao_145)] + 1
            if questionario.questao_146 == None:
                questao_146[len(ALUNO_146)] = questao_146[len(ALUNO_146)] + 1
            else:
                for escolhas in questionario.questao_146:
                    for escolha in escolhas:
                        questao_146[int(escolha)] = questao_146[int(escolha)] + 1
        
        context = {
            'pagina_graficos': True,
            'pagina_graficos_questionarios': True,
            'questionarios': questionarios,
            'questao_1': questao_1,
            'questao_2': questao_2,
            'questao_3': questao_3,
            'questao_4': questao_4,
            'questao_5': questao_5,
            'questao_6': questao_6,
            'questao_7': questao_7,
            'questao_8': questao_8,
            'questao_9': questao_9,
            'questao_10': questao_10,
            'questao_11': questao_11,
            'questao_12': questao_12,
            'questao_13': questao_13,
            'questao_14': questao_14,
            'questao_15': questao_15,
            'questao_16': questao_16,
            'questao_17': questao_17,
            'questao_18': questao_18,
            'questao_19': questao_19,
            'questao_20': questao_20,
            'questao_21': questao_21,
            'questao_22': questao_22,
            'questao_23': questao_23,
            'questao_24': questao_24,
            'questao_25': questao_25,
            'questao_26': questao_26,
            'questao_27': questao_27,
            'questao_28': questao_28,
            'questao_29': questao_29,
            'questao_30': questao_30,
            'questao_31': questao_31,
            'questao_32': questao_32,
            'questao_33': questao_33,
            'questao_34': questao_34,
            'questao_35': questao_35,
            'questao_36': questao_36,
            'questao_37': questao_37,
            'questao_38': questao_38,
            'questao_39': questao_39,
            'questao_40': questao_40,
            'questao_41': questao_41,
            'questao_42': questao_42,
            'questao_43': questao_43,
            'questao_44': questao_44,
            'questao_45': questao_45,
            'questao_46': questao_46,
            'questao_47': questao_47,
            'questao_48': questao_48,
            'questao_49': questao_49,
            'questao_50': questao_50,
            'questao_51': questao_51,
            'questao_52': questao_52,
            'questao_53': questao_53,
            'questao_54': questao_54,
            'questao_55': questao_55,
            'questao_56': questao_56,
            'questao_57': questao_57,
            'questao_58': questao_58,
            'questao_59': questao_59,
            'questao_60': questao_60,
            'questao_61': questao_61,
            'questao_62': questao_62,
            'questao_63': questao_63,
            'questao_64': questao_64,
            'questao_65': questao_65,
            'questao_66': questao_66,
            'questao_67': questao_67,
            'questao_68': questao_68,
            'questao_69': questao_69,
            'questao_70': questao_70,
            'questao_71': questao_71,
            'questao_72': questao_72,
            'questao_73': questao_73,
            'questao_74': questao_74,
            'questao_75': questao_75,
            'questao_76': questao_76,
            'questao_77': questao_77,
            'questao_78': questao_78,
            'questao_79': questao_79,
            'questao_80': questao_80,
            'questao_81': questao_81,
            'questao_82': questao_82,
            'questao_83': questao_83,
            'questao_84': questao_84,
            'questao_85': questao_85,
            'questao_86': questao_86,
            'questao_87': questao_87,
            'questao_88': questao_88,
            'questao_89': questao_89,
            'questao_90': questao_90,
            'questao_91': questao_91,
            'questao_92': questao_92,
            'questao_93': questao_93,
            'questao_94': questao_94,
            'questao_95': questao_95,
            'questao_96': questao_96,
            'questao_97': questao_97,
            'questao_98': questao_98,
            'questao_99': questao_99,
            'questao_100': questao_100,
            'questao_101': questao_101,
            'questao_102': questao_102,
            'questao_103': questao_103,
            'questao_104': questao_104,
            'questao_105': questao_105,
            'questao_106': questao_106,
            'questao_107': questao_107,
            'questao_108': questao_108,
            'questao_109': questao_109,
            'questao_110': questao_110,
            'questao_111': questao_111,
            'questao_112': questao_112,
            'questao_113': questao_113,
            'questao_114': questao_114,
            'questao_115': questao_115,
            'questao_116': questao_116,
            'questao_117': questao_117,
            'questao_118': questao_118,
            'questao_119': questao_119,
            'questao_120': questao_120,
            'questao_121': questao_121,
            'questao_122': questao_122,
            'questao_123': questao_123,
            'questao_124': questao_124,
            'questao_125': questao_125,
            'questao_126': questao_126,
            'questao_127': questao_127,
            'questao_128': questao_128,
            'questao_129': questao_129,
            'questao_130': questao_130,
            'questao_131': questao_131,
            'questao_132': questao_132,
            'questao_133': questao_133,
            'questao_134': questao_134,
            'questao_135': questao_135,
            'questao_136': questao_136,
            'questao_137': questao_137,
            'questao_138': questao_138,
            'questao_139': questao_139,
            'questao_140': questao_140,
            'questao_141': questao_141,
            'questao_142': questao_142,
            'questao_143': questao_143,
            'questao_144': questao_144,
            'questao_145': questao_145,
            'questao_146': questao_146,
        }
        
        return render(self.request, 'administracao/graficos_questionarios.html', context)
    
    def iniciaQuestao(self, maximo):
        questao = []
        for i in range(maximo):
            questao.append(0)
        return questao


class GraficosExamesView(LoginRequired, View):
    """Página que exibe gráficos baseados nos dados dos exames"""
    
    def get(self, request):
        exames = Exame.objects.order_by('-id')
        
        situacao_coroa = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        sem_problemas_coroa = True
        for exame in exames:
            tem_problema_coroa = [False, False, False, False, False, False, False, False, False, False]
            
            if exame.carie_coroa_18 != None and exame.carie_coroa_18 == 'T': tem_problema_coroa[9] = True; sem_problemas_coroa = False
            if exame.carie_coroa_18 != None and exame.carie_coroa_18 != '0' and exame.carie_coroa_18 != 'A' and exame.carie_coroa_18 != 'T' and exame.carie_coroa_18 != '9': tem_problema_coroa[int(self.letra_para_numero(exame.carie_coroa_18))] = True; sem_problemas_coroa = False
            
            if exame.carie_coroa_17 != None and exame.carie_coroa_17 == 'T': tem_problema_coroa[9] = True; sem_problemas_coroa = False
            if exame.carie_coroa_17 != None and exame.carie_coroa_17 != '0' and exame.carie_coroa_17 != 'A' and exame.carie_coroa_17 != 'T' and exame.carie_coroa_17 != '9': tem_problema_coroa[int(self.letra_para_numero(exame.carie_coroa_17))] = True; sem_problemas_coroa = False
            
            if exame.carie_coroa_16 != None and exame.carie_coroa_16 == 'T': tem_problema_coroa[9] = True; sem_problemas_coroa = False
            if exame.carie_coroa_16 != None and exame.carie_coroa_16 != '0' and exame.carie_coroa_16 != 'A' and exame.carie_coroa_16 != 'T' and exame.carie_coroa_16 != '9': tem_problema_coroa[int(self.letra_para_numero(exame.carie_coroa_16))] = True; sem_problemas_coroa = False
            
            if exame.carie_coroa_15 != None and exame.carie_coroa_15 == 'T': tem_problema_coroa[9] = True; sem_problemas_coroa = False
            if exame.carie_coroa_15 != None and exame.carie_coroa_15 != '0' and exame.carie_coroa_15 != 'A' and exame.carie_coroa_15 != 'T' and exame.carie_coroa_15 != '9': tem_problema_coroa[int(self.letra_para_numero(exame.carie_coroa_15))] = True; sem_problemas_coroa = False
            
            if exame.carie_coroa_14 != None and exame.carie_coroa_14 == 'T': tem_problema_coroa[9] = True; sem_problemas_coroa = False
            if exame.carie_coroa_14 != None and exame.carie_coroa_14 != '0' and exame.carie_coroa_14 != 'A' and exame.carie_coroa_14 != 'T' and exame.carie_coroa_14 != '9': tem_problema_coroa[int(self.letra_para_numero(exame.carie_coroa_14))] = True; sem_problemas_coroa = False
            
            if exame.carie_coroa_13 != None and exame.carie_coroa_13 == 'T': tem_problema_coroa[9] = True; sem_problemas_coroa = False
            if exame.carie_coroa_13 != None and exame.carie_coroa_13 != '0' and exame.carie_coroa_13 != 'A' and exame.carie_coroa_13 != 'T' and exame.carie_coroa_13 != '9': tem_problema_coroa[int(self.letra_para_numero(exame.carie_coroa_13))] = True; sem_problemas_coroa = False
            
            if exame.carie_coroa_12 != None and exame.carie_coroa_12 == 'T': tem_problema_coroa[9] = True; sem_problemas_coroa = False
            if exame.carie_coroa_12 != None and exame.carie_coroa_12 != '0' and exame.carie_coroa_12 != 'A' and exame.carie_coroa_12 != 'T' and exame.carie_coroa_12 != '9': tem_problema_coroa[int(self.letra_para_numero(exame.carie_coroa_12))] = True; sem_problemas_coroa = False
            
            if exame.carie_coroa_11 != None and exame.carie_coroa_11 == 'T': tem_problema_coroa[9] = True; sem_problemas_coroa = False
            if exame.carie_coroa_11 != None and exame.carie_coroa_11 != '0' and exame.carie_coroa_11 != 'A' and exame.carie_coroa_11 != 'T' and exame.carie_coroa_11 != '9': tem_problema_coroa[int(self.letra_para_numero(exame.carie_coroa_11))] = True; sem_problemas_coroa = False
            
            
            if exame.carie_coroa_21 != None and exame.carie_coroa_21 == 'T': tem_problema_coroa[9] = True; sem_problemas_coroa = False
            if exame.carie_coroa_21 != None and exame.carie_coroa_21 != '0' and exame.carie_coroa_21 != 'A' and exame.carie_coroa_21 != 'T' and exame.carie_coroa_21 != '9': tem_problema_coroa[int(self.letra_para_numero(exame.carie_coroa_21))] = True; sem_problemas_coroa = False
            
            if exame.carie_coroa_22 != None and exame.carie_coroa_22 == 'T': tem_problema_coroa[9] = True; sem_problemas_coroa = False
            if exame.carie_coroa_22 != None and exame.carie_coroa_22 != '0' and exame.carie_coroa_22 != 'A' and exame.carie_coroa_22 != 'T' and exame.carie_coroa_22 != '9': tem_problema_coroa[int(self.letra_para_numero(exame.carie_coroa_22))] = True; sem_problemas_coroa = False
            
            if exame.carie_coroa_23 != None and exame.carie_coroa_23 == 'T': tem_problema_coroa[9] = True; sem_problemas_coroa = False
            if exame.carie_coroa_23 != None and exame.carie_coroa_23 != '0' and exame.carie_coroa_23 != 'A' and exame.carie_coroa_23 != 'T' and exame.carie_coroa_23 != '9': tem_problema_coroa[int(self.letra_para_numero(exame.carie_coroa_23))] = True; sem_problemas_coroa = False
            
            if exame.carie_coroa_24 != None and exame.carie_coroa_24 == 'T': tem_problema_coroa[9] = True; sem_problemas_coroa = False
            if exame.carie_coroa_24 != None and exame.carie_coroa_24 != '0' and exame.carie_coroa_24 != 'A' and exame.carie_coroa_24 != 'T' and exame.carie_coroa_24 != '9': tem_problema_coroa[int(self.letra_para_numero(exame.carie_coroa_24))] = True; sem_problemas_coroa = False
            
            if exame.carie_coroa_25 != None and exame.carie_coroa_25 == 'T': tem_problema_coroa[9] = True; sem_problemas_coroa = False
            if exame.carie_coroa_25 != None and exame.carie_coroa_25 != '0' and exame.carie_coroa_25 != 'A' and exame.carie_coroa_25 != 'T' and exame.carie_coroa_25 != '9': tem_problema_coroa[int(self.letra_para_numero(exame.carie_coroa_25))] = True; sem_problemas_coroa = False
            
            if exame.carie_coroa_26 != None and exame.carie_coroa_26 == 'T': tem_problema_coroa[9] = True; sem_problemas_coroa = False
            if exame.carie_coroa_26 != None and exame.carie_coroa_26 != '0' and exame.carie_coroa_26 != 'A' and exame.carie_coroa_26 != 'T' and exame.carie_coroa_26 != '9': tem_problema_coroa[int(self.letra_para_numero(exame.carie_coroa_26))] = True; sem_problemas_coroa = False
            
            if exame.carie_coroa_27 != None and exame.carie_coroa_27 == 'T': tem_problema_coroa[9] = True; sem_problemas_coroa = False
            if exame.carie_coroa_27 != None and exame.carie_coroa_27 != '0' and exame.carie_coroa_27 != 'A' and exame.carie_coroa_27 != 'T' and exame.carie_coroa_27 != '9': tem_problema_coroa[int(self.letra_para_numero(exame.carie_coroa_27))] = True; sem_problemas_coroa = False
            
            if exame.carie_coroa_28 != None and exame.carie_coroa_28 == 'T': tem_problema_coroa[9] = True; sem_problemas_coroa = False
            if exame.carie_coroa_28 != None and exame.carie_coroa_28 != '0' and exame.carie_coroa_28 != 'A' and exame.carie_coroa_28 != 'T' and exame.carie_coroa_28 != '9': tem_problema_coroa[int(self.letra_para_numero(exame.carie_coroa_28))] = True; sem_problemas_coroa = False
            
            
            if exame.carie_coroa_38 != None and exame.carie_coroa_38 == 'T': tem_problema_coroa[9] = True; sem_problemas_coroa = False
            if exame.carie_coroa_38 != None and exame.carie_coroa_38 != '0' and exame.carie_coroa_38 != 'A' and exame.carie_coroa_38 != 'T' and exame.carie_coroa_38 != '9': tem_problema_coroa[int(self.letra_para_numero(exame.carie_coroa_38))] = True; sem_problemas_coroa = False
            
            if exame.carie_coroa_37 != None and exame.carie_coroa_37 == 'T': tem_problema_coroa[9] = True; sem_problemas_coroa = False
            if exame.carie_coroa_37 != None and exame.carie_coroa_37 != '0' and exame.carie_coroa_37 != 'A' and exame.carie_coroa_37 != 'T' and exame.carie_coroa_37 != '9': tem_problema_coroa[int(self.letra_para_numero(exame.carie_coroa_37))] = True; sem_problemas_coroa = False
            
            if exame.carie_coroa_36 != None and exame.carie_coroa_36 == 'T': tem_problema_coroa[9] = True; sem_problemas_coroa = False
            if exame.carie_coroa_36 != None and exame.carie_coroa_36 != '0' and exame.carie_coroa_36 != 'A' and exame.carie_coroa_36 != 'T' and exame.carie_coroa_36 != '9': tem_problema_coroa[int(self.letra_para_numero(exame.carie_coroa_36))] = True; sem_problemas_coroa = False
            
            if exame.carie_coroa_35 != None and exame.carie_coroa_35 == 'T': tem_problema_coroa[9] = True; sem_problemas_coroa = False
            if exame.carie_coroa_35 != None and exame.carie_coroa_35 != '0' and exame.carie_coroa_35 != 'A' and exame.carie_coroa_35 != 'T' and exame.carie_coroa_35 != '9': tem_problema_coroa[int(self.letra_para_numero(exame.carie_coroa_35))] = True; sem_problemas_coroa = False
            
            if exame.carie_coroa_34 != None and exame.carie_coroa_34 == 'T': tem_problema_coroa[9] = True; sem_problemas_coroa = False
            if exame.carie_coroa_34 != None and exame.carie_coroa_34 != '0' and exame.carie_coroa_34 != 'A' and exame.carie_coroa_34 != 'T' and exame.carie_coroa_34 != '9': tem_problema_coroa[int(self.letra_para_numero(exame.carie_coroa_34))] = True; sem_problemas_coroa = False
            
            if exame.carie_coroa_33 != None and exame.carie_coroa_33 == 'T': tem_problema_coroa[9] = True; sem_problemas_coroa = False
            if exame.carie_coroa_33 != None and exame.carie_coroa_33 != '0' and exame.carie_coroa_33 != 'A' and exame.carie_coroa_33 != 'T' and exame.carie_coroa_33 != '9': tem_problema_coroa[int(self.letra_para_numero(exame.carie_coroa_33))] = True; sem_problemas_coroa = False
            
            if exame.carie_coroa_32 != None and exame.carie_coroa_32 == 'T': tem_problema_coroa[9] = True; sem_problemas_coroa = False
            if exame.carie_coroa_32 != None and exame.carie_coroa_32 != '0' and exame.carie_coroa_32 != 'A' and exame.carie_coroa_32 != 'T' and exame.carie_coroa_32 != '9': tem_problema_coroa[int(self.letra_para_numero(exame.carie_coroa_32))] = True; sem_problemas_coroa = False
            
            if exame.carie_coroa_31 != None and exame.carie_coroa_31 == 'T': tem_problema_coroa[9] = True; sem_problemas_coroa = False
            if exame.carie_coroa_31 != None and exame.carie_coroa_31 != '0' and exame.carie_coroa_31 != 'A' and exame.carie_coroa_31 != 'T' and exame.carie_coroa_31 != '9': tem_problema_coroa[int(self.letra_para_numero(exame.carie_coroa_31))] = True; sem_problemas_coroa = False
            
            
            if exame.carie_coroa_41 != None and exame.carie_coroa_41 == 'T': tem_problema_coroa[9] = True; sem_problemas_coroa = False
            if exame.carie_coroa_41 != None and exame.carie_coroa_41 != '0' and exame.carie_coroa_41 != 'A' and exame.carie_coroa_41 != 'T' and exame.carie_coroa_41 != '9': tem_problema_coroa[int(self.letra_para_numero(exame.carie_coroa_41))] = True; sem_problemas_coroa = False
            
            if exame.carie_coroa_42 != None and exame.carie_coroa_42 == 'T': tem_problema_coroa[9] = True; sem_problemas_coroa = False
            if exame.carie_coroa_42 != None and exame.carie_coroa_42 != '0' and exame.carie_coroa_42 != 'A' and exame.carie_coroa_42 != 'T' and exame.carie_coroa_42 != '9': tem_problema_coroa[int(self.letra_para_numero(exame.carie_coroa_42))] = True; sem_problemas_coroa = False
            
            if exame.carie_coroa_43 != None and exame.carie_coroa_43 == 'T': tem_problema_coroa[9] = True; sem_problemas_coroa = False
            if exame.carie_coroa_43 != None and exame.carie_coroa_43 != '0' and exame.carie_coroa_43 != 'A' and exame.carie_coroa_43 != 'T' and exame.carie_coroa_43 != '9': tem_problema_coroa[int(self.letra_para_numero(exame.carie_coroa_43))] = True; sem_problemas_coroa = False
            
            if exame.carie_coroa_44 != None and exame.carie_coroa_44 == 'T': tem_problema_coroa[9] = True; sem_problemas_coroa = False
            if exame.carie_coroa_44 != None and exame.carie_coroa_44 != '0' and exame.carie_coroa_44 != 'A' and exame.carie_coroa_44 != 'T' and exame.carie_coroa_44 != '9': tem_problema_coroa[int(self.letra_para_numero(exame.carie_coroa_44))] = True; sem_problemas_coroa = False
            
            if exame.carie_coroa_45 != None and exame.carie_coroa_45 == 'T': tem_problema_coroa[9] = True; sem_problemas_coroa = False
            if exame.carie_coroa_45 != None and exame.carie_coroa_45 != '0' and exame.carie_coroa_45 != 'A' and exame.carie_coroa_45 != 'T' and exame.carie_coroa_45 != '9': tem_problema_coroa[int(self.letra_para_numero(exame.carie_coroa_45))] = True; sem_problemas_coroa = False
            
            if exame.carie_coroa_46 != None and exame.carie_coroa_46 == 'T': tem_problema_coroa[9] = True; sem_problemas_coroa = False
            if exame.carie_coroa_46 != None and exame.carie_coroa_46 != '0' and exame.carie_coroa_46 != 'A' and exame.carie_coroa_46 != 'T' and exame.carie_coroa_46 != '9': tem_problema_coroa[int(self.letra_para_numero(exame.carie_coroa_46))] = True; sem_problemas_coroa = False
            
            if exame.carie_coroa_47 != None and exame.carie_coroa_47 == 'T': tem_problema_coroa[9] = True; sem_problemas_coroa = False
            if exame.carie_coroa_47 != None and exame.carie_coroa_47 != '0' and exame.carie_coroa_47 != 'A' and exame.carie_coroa_47 != 'T' and exame.carie_coroa_47 != '9': tem_problema_coroa[int(self.letra_para_numero(exame.carie_coroa_47))] = True; sem_problemas_coroa = False
            
            if exame.carie_coroa_48 != None and exame.carie_coroa_48 == 'T': tem_problema_coroa[9] = True; sem_problemas_coroa = False
            if exame.carie_coroa_48 != None and exame.carie_coroa_48 != '0' and exame.carie_coroa_48 != 'A' and exame.carie_coroa_48 != 'T' and exame.carie_coroa_48 != '9': tem_problema_coroa[int(self.letra_para_numero(exame.carie_coroa_48))] = True; sem_problemas_coroa = False
            
            if sem_problemas_coroa: tem_problema_coroa[0] = True
            else: sem_problemas_coroa = True
            
            if tem_problema_coroa[0]: situacao_coroa[0] += 1
            if tem_problema_coroa[1]: situacao_coroa[1] += 1
            if tem_problema_coroa[2]: situacao_coroa[2] += 1
            if tem_problema_coroa[3]: situacao_coroa[3] += 1
            if tem_problema_coroa[4]: situacao_coroa[4] += 1
            if tem_problema_coroa[5]: situacao_coroa[5] += 1
            if tem_problema_coroa[6]: situacao_coroa[6] += 1
            if tem_problema_coroa[7]: situacao_coroa[7] += 1
            if tem_problema_coroa[8]: situacao_coroa[8] += 1
            if tem_problema_coroa[9]: situacao_coroa[9] += 1
        
        tratamento_necessario = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        sem_tratamento_indicado = True
        for exame in exames:
            tratamento_foi_indicado = [False, False, False, False, False, False, False, False, False]
            
            if exame.carie_tratamento_18 != None and exame.carie_tratamento_18 != '0' and exame.carie_tratamento_18 != '9': tratamento_foi_indicado[int(exame.carie_tratamento_18)] = True; sem_tratamento_indicado = False
            if exame.carie_tratamento_17 != None and exame.carie_tratamento_17 != '0' and exame.carie_tratamento_17 != '9': tratamento_foi_indicado[int(exame.carie_tratamento_17)] = True; sem_tratamento_indicado = False
            if exame.carie_tratamento_16 != None and exame.carie_tratamento_16 != '0' and exame.carie_tratamento_16 != '9': tratamento_foi_indicado[int(exame.carie_tratamento_16)] = True; sem_tratamento_indicado = False
            if exame.carie_tratamento_15 != None and exame.carie_tratamento_15 != '0' and exame.carie_tratamento_15 != '9': tratamento_foi_indicado[int(exame.carie_tratamento_15)] = True; sem_tratamento_indicado = False
            if exame.carie_tratamento_14 != None and exame.carie_tratamento_14 != '0' and exame.carie_tratamento_14 != '9': tratamento_foi_indicado[int(exame.carie_tratamento_14)] = True; sem_tratamento_indicado = False
            if exame.carie_tratamento_13 != None and exame.carie_tratamento_13 != '0' and exame.carie_tratamento_13 != '9': tratamento_foi_indicado[int(exame.carie_tratamento_13)] = True; sem_tratamento_indicado = False
            if exame.carie_tratamento_12 != None and exame.carie_tratamento_12 != '0' and exame.carie_tratamento_12 != '9': tratamento_foi_indicado[int(exame.carie_tratamento_12)] = True; sem_tratamento_indicado = False
            if exame.carie_tratamento_11 != None and exame.carie_tratamento_11 != '0' and exame.carie_tratamento_11 != '9': tratamento_foi_indicado[int(exame.carie_tratamento_11)] = True; sem_tratamento_indicado = False
            
            if exame.carie_tratamento_21 != None and exame.carie_tratamento_21 != '0' and exame.carie_tratamento_21 != '9': tratamento_foi_indicado[int(exame.carie_tratamento_21)] = True; sem_tratamento_indicado = False
            if exame.carie_tratamento_22 != None and exame.carie_tratamento_22 != '0' and exame.carie_tratamento_22 != '9': tratamento_foi_indicado[int(exame.carie_tratamento_22)] = True; sem_tratamento_indicado = False
            if exame.carie_tratamento_23 != None and exame.carie_tratamento_23 != '0' and exame.carie_tratamento_23 != '9': tratamento_foi_indicado[int(exame.carie_tratamento_23)] = True; sem_tratamento_indicado = False
            if exame.carie_tratamento_24 != None and exame.carie_tratamento_24 != '0' and exame.carie_tratamento_24 != '9': tratamento_foi_indicado[int(exame.carie_tratamento_24)] = True; sem_tratamento_indicado = False
            if exame.carie_tratamento_25 != None and exame.carie_tratamento_25 != '0' and exame.carie_tratamento_25 != '9': tratamento_foi_indicado[int(exame.carie_tratamento_25)] = True; sem_tratamento_indicado = False
            if exame.carie_tratamento_26 != None and exame.carie_tratamento_26 != '0' and exame.carie_tratamento_26 != '9': tratamento_foi_indicado[int(exame.carie_tratamento_26)] = True; sem_tratamento_indicado = False
            if exame.carie_tratamento_27 != None and exame.carie_tratamento_27 != '0' and exame.carie_tratamento_27 != '9': tratamento_foi_indicado[int(exame.carie_tratamento_27)] = True; sem_tratamento_indicado = False
            if exame.carie_tratamento_28 != None and exame.carie_tratamento_28 != '0' and exame.carie_tratamento_28 != '9': tratamento_foi_indicado[int(exame.carie_tratamento_28)] = True; sem_tratamento_indicado = False
            
            if exame.carie_tratamento_38 != None and exame.carie_tratamento_38 != '0' and exame.carie_tratamento_38 != '9': tratamento_foi_indicado[int(exame.carie_tratamento_38)] = True; sem_tratamento_indicado = False
            if exame.carie_tratamento_37 != None and exame.carie_tratamento_37 != '0' and exame.carie_tratamento_37 != '9': tratamento_foi_indicado[int(exame.carie_tratamento_37)] = True; sem_tratamento_indicado = False
            if exame.carie_tratamento_36 != None and exame.carie_tratamento_36 != '0' and exame.carie_tratamento_36 != '9': tratamento_foi_indicado[int(exame.carie_tratamento_36)] = True; sem_tratamento_indicado = False
            if exame.carie_tratamento_35 != None and exame.carie_tratamento_35 != '0' and exame.carie_tratamento_35 != '9': tratamento_foi_indicado[int(exame.carie_tratamento_35)] = True; sem_tratamento_indicado = False
            if exame.carie_tratamento_34 != None and exame.carie_tratamento_34 != '0' and exame.carie_tratamento_34 != '9': tratamento_foi_indicado[int(exame.carie_tratamento_34)] = True; sem_tratamento_indicado = False
            if exame.carie_tratamento_33 != None and exame.carie_tratamento_33 != '0' and exame.carie_tratamento_33 != '9': tratamento_foi_indicado[int(exame.carie_tratamento_33)] = True; sem_tratamento_indicado = False
            if exame.carie_tratamento_32 != None and exame.carie_tratamento_32 != '0' and exame.carie_tratamento_32 != '9': tratamento_foi_indicado[int(exame.carie_tratamento_32)] = True; sem_tratamento_indicado = False
            if exame.carie_tratamento_31 != None and exame.carie_tratamento_31 != '0' and exame.carie_tratamento_31 != '9': tratamento_foi_indicado[int(exame.carie_tratamento_31)] = True; sem_tratamento_indicado = False
            
            if exame.carie_tratamento_41 != None and exame.carie_tratamento_41 != '0' and exame.carie_tratamento_41 != '9': tratamento_foi_indicado[int(exame.carie_tratamento_41)] = True; sem_tratamento_indicado = False
            if exame.carie_tratamento_42 != None and exame.carie_tratamento_42 != '0' and exame.carie_tratamento_42 != '9': tratamento_foi_indicado[int(exame.carie_tratamento_42)] = True; sem_tratamento_indicado = False
            if exame.carie_tratamento_43 != None and exame.carie_tratamento_43 != '0' and exame.carie_tratamento_43 != '9': tratamento_foi_indicado[int(exame.carie_tratamento_43)] = True; sem_tratamento_indicado = False
            if exame.carie_tratamento_44 != None and exame.carie_tratamento_44 != '0' and exame.carie_tratamento_44 != '9': tratamento_foi_indicado[int(exame.carie_tratamento_44)] = True; sem_tratamento_indicado = False
            if exame.carie_tratamento_45 != None and exame.carie_tratamento_45 != '0' and exame.carie_tratamento_45 != '9': tratamento_foi_indicado[int(exame.carie_tratamento_45)] = True; sem_tratamento_indicado = False
            if exame.carie_tratamento_46 != None and exame.carie_tratamento_46 != '0' and exame.carie_tratamento_46 != '9': tratamento_foi_indicado[int(exame.carie_tratamento_46)] = True; sem_tratamento_indicado = False
            if exame.carie_tratamento_47 != None and exame.carie_tratamento_47 != '0' and exame.carie_tratamento_47 != '9': tratamento_foi_indicado[int(exame.carie_tratamento_47)] = True; sem_tratamento_indicado = False
            if exame.carie_tratamento_48 != None and exame.carie_tratamento_48 != '0' and exame.carie_tratamento_48 != '9': tratamento_foi_indicado[int(exame.carie_tratamento_48)] = True; sem_tratamento_indicado = False
            
            if sem_tratamento_indicado: tratamento_foi_indicado[0] = True
            else: sem_tratamento_indicado = True
            
            if tratamento_foi_indicado[0]: tratamento_necessario[0] += 1
            if tratamento_foi_indicado[1]: tratamento_necessario[1] += 1
            if tratamento_foi_indicado[2]: tratamento_necessario[2] += 1
            if tratamento_foi_indicado[3]: tratamento_necessario[3] += 1
            if tratamento_foi_indicado[4]: tratamento_necessario[4] += 1
            if tratamento_foi_indicado[5]: tratamento_necessario[5] += 1
            if tratamento_foi_indicado[6]: tratamento_necessario[6] += 1
            if tratamento_foi_indicado[7]: tratamento_necessario[7] += 1
            if tratamento_foi_indicado[8]: tratamento_necessario[8] += 1
            
        condicao_periodontal = [0, 0, 0, 0]
        sem_problema_periodontal = True
        for exame in exames:
            tem_problema_periodontal = [False, False, False, False]
            
            if exame.periodontal_sangramento_1716 != None:
                if exame.periodontal_sangramento_1716 != '0' and exame.periodontal_sangramento_1716 != '9' and exame.periodontal_sangramento_1716 != 'X': tem_problema_periodontal[1] = True; sem_problema_periodontal = False
            if exame.periodontal_sangramento_11 != None:
                if exame.periodontal_sangramento_11 != '0' and exame.periodontal_sangramento_11 != '9' and exame.periodontal_sangramento_11 != 'X': tem_problema_periodontal[1] = True; sem_problema_periodontal = False
            if exame.periodontal_sangramento_2627 != None:
                if exame.periodontal_sangramento_2627 != '0' and exame.periodontal_sangramento_2627 != '9' and exame.periodontal_sangramento_2627 != 'X': tem_problema_periodontal[1] = True; sem_problema_periodontal = False
            if exame.periodontal_sangramento_3736 != None:
                if exame.periodontal_sangramento_3736 != '0' and exame.periodontal_sangramento_3736 != '9' and exame.periodontal_sangramento_3736 != 'X': tem_problema_periodontal[1] = True; sem_problema_periodontal = False
            if exame.periodontal_sangramento_31 != None:
                if exame.periodontal_sangramento_31 != '0' and exame.periodontal_sangramento_31 != '9' and exame.periodontal_sangramento_31 != 'X': tem_problema_periodontal[1] = True; sem_problema_periodontal = False
            if exame.periodontal_sangramento_4647 != None:
                if exame.periodontal_sangramento_4647 != '0' and exame.periodontal_sangramento_4647 != '9' and exame.periodontal_sangramento_4647 != 'X': tem_problema_periodontal[1] = True; sem_problema_periodontal = False
            
            if exame.periodontal_calculo_1716 != None:
                if exame.periodontal_calculo_1716 != '0' and exame.periodontal_calculo_1716 != '9' and exame.periodontal_calculo_1716 != 'X': tem_problema_periodontal[2] = True; sem_problema_periodontal = False
            if exame.periodontal_calculo_11 != None:
                if exame.periodontal_calculo_11 != '0' and exame.periodontal_calculo_11 != '9' and exame.periodontal_calculo_11 != 'X': tem_problema_periodontal[2] = True; sem_problema_periodontal = False
            if exame.periodontal_calculo_2627 != None:
                if exame.periodontal_calculo_2627 != '0' and exame.periodontal_calculo_2627 != '9' and exame.periodontal_calculo_2627 != 'X': tem_problema_periodontal[2] = True; sem_problema_periodontal = False
            if exame.periodontal_calculo_3736 != None:
                if exame.periodontal_calculo_3736 != '0' and exame.periodontal_calculo_3736 != '9' and exame.periodontal_calculo_3736 != 'X': tem_problema_periodontal[2] = True; sem_problema_periodontal = False
            if exame.periodontal_calculo_31 != None:
                if exame.periodontal_calculo_31 != '0' and exame.periodontal_calculo_31 != '9' and exame.periodontal_calculo_31 != 'X': tem_problema_periodontal[2] = True; sem_problema_periodontal = False
            if exame.periodontal_calculo_4647 != None:
                if exame.periodontal_calculo_4647 != '0' and exame.periodontal_calculo_4647 != '9' and exame.periodontal_calculo_4647 != 'X': tem_problema_periodontal[2] = True; sem_problema_periodontal = False
            
            if exame.periodontal_bolsa_1716 != None:
                if exame.periodontal_bolsa_1716 != '0' and exame.periodontal_bolsa_1716 != '9' and exame.periodontal_bolsa_1716 != 'X': tem_problema_periodontal[3] = True; sem_problema_periodontal = False
            if exame.periodontal_bolsa_11 != None:
                if exame.periodontal_bolsa_11 != '0' and exame.periodontal_bolsa_11 != '9' and exame.periodontal_bolsa_11 != 'X': tem_problema_periodontal[3] = True; sem_problema_periodontal = False
            if exame.periodontal_bolsa_2627 != None:
                if exame.periodontal_bolsa_2627 != '0' and exame.periodontal_bolsa_2627 != '9' and exame.periodontal_bolsa_2627 != 'X': tem_problema_periodontal[3] = True; sem_problema_periodontal = False
            if exame.periodontal_bolsa_3736 != None:
                if exame.periodontal_bolsa_3736 != '0' and exame.periodontal_bolsa_3736 != '9' and exame.periodontal_bolsa_3736 != 'X': tem_problema_periodontal[3] = True; sem_problema_periodontal = False
            if exame.periodontal_bolsa_31 != None:
                if exame.periodontal_bolsa_31 != '0' and exame.periodontal_bolsa_31 != '9' and exame.periodontal_bolsa_31 != 'X': tem_problema_periodontal[3] = True; sem_problema_periodontal = False
            if exame.periodontal_bolsa_4647 != None:
                if exame.periodontal_bolsa_4647 != '0' and exame.periodontal_bolsa_4647 != '9' and exame.periodontal_bolsa_4647 != 'X': tem_problema_periodontal[3] = True; sem_problema_periodontal = False
            
            if sem_problema_periodontal: tem_problema_periodontal[0] = True
            else: sem_problema_periodontal = True
            
            if tem_problema_periodontal[0]: condicao_periodontal[0] += 1
            if tem_problema_periodontal[1]: condicao_periodontal[1] += 1
            if tem_problema_periodontal[2]: condicao_periodontal[2] += 1
            if tem_problema_periodontal[3]: condicao_periodontal[3] += 1
        
        context = {
            'pagina_graficos': True,
            'pagina_graficos_exames': True,
            'exames': exames,
            'situacao_coroa': situacao_coroa,
            'tratamento_necessario': tratamento_necessario,
            'condicao_periodontal': condicao_periodontal,
        }
        
        return render(self.request, 'administracao/graficos_exames.html', context)
    
    def letra_para_numero(self, letra):
        if letra == 'B' or letra == 'b':
            return '1'
        elif letra == 'C' or letra == 'c':
            return '2'
        elif letra == 'D' or letra == 'd':
            return '3'
        elif letra == 'E' or letra == 'e':
            return '4'
        elif letra == 'F' or letra == 'f':
            return '5'
        elif letra == 'G' or letra == 'g':
            return '6'
        elif letra == 'H' or letra == 'h':
            return '7'
        elif letra == 'K' or letra == 'k':
            return '8'
        elif letra == 'T' or letra == 't':
            return 'T'
        elif letra == 'L' or letra == 'l':
            return '9'
        else:
            return letra


class GraficosDiretoresView(LoginRequired, View):
    """Página que exibe gráficos baseados nos dados dos questionários dos diretores"""
    
    def get(self, request):
        diretores = Diretor.objects.order_by('-id')
        
        questao_1 = self.iniciaQuestao(len(DIRETOR_1) + 1)
        questao_2 = self.iniciaQuestao(len(DIRETOR_2) + 1)
        questao_3 = self.iniciaQuestao(len(DIRETOR_3) + 1)
        questao_4 = self.iniciaQuestao(len(DIRETOR_4) + 1)
        questao_5 = self.iniciaQuestao(len(DIRETOR_5) + 1)
        questao_6 = self.iniciaQuestao(len(DIRETOR_6) + 1)
        questao_7 = self.iniciaQuestao(len(DIRETOR_7) + 1)
        questao_8 = self.iniciaQuestao(len(DIRETOR_8) + 1)
        questao_9 = self.iniciaQuestao(len(DIRETOR_9) + 1)
        questao_10 = self.iniciaQuestao(len(DIRETOR_10) + 1)
        questao_11 = self.iniciaQuestao(len(DIRETOR_11) + 1)
        questao_12 = self.iniciaQuestao(len(DIRETOR_12) + 1)
        questao_13 = self.iniciaQuestao(len(DIRETOR_13) + 1)
        questao_14 = self.iniciaQuestao(len(DIRETOR_14) + 1)
        questao_15 = self.iniciaQuestao(len(DIRETOR_15) + 1)
        questao_16 = self.iniciaQuestao(len(DIRETOR_16) + 1)
        questao_17 = self.iniciaQuestao(len(DIRETOR_17) + 1)
        questao_18 = self.iniciaQuestao(len(DIRETOR_18) + 1)
        questao_19 = self.iniciaQuestao(len(DIRETOR_19) + 1)
        questao_20 = self.iniciaQuestao(len(DIRETOR_20) + 1)
        questao_21 = self.iniciaQuestao(len(DIRETOR_21) + 1)
        questao_22 = self.iniciaQuestao(len(DIRETOR_22) + 1)
        questao_23 = self.iniciaQuestao(len(DIRETOR_23) + 1)
        questao_24 = self.iniciaQuestao(len(DIRETOR_24) + 1)
        questao_25 = self.iniciaQuestao(len(DIRETOR_25) + 1)
        questao_26 = self.iniciaQuestao(len(DIRETOR_26) + 1)
        questao_27 = self.iniciaQuestao(len(DIRETOR_27) + 1)
        questao_28 = self.iniciaQuestao(len(DIRETOR_28) + 1)
        questao_29 = self.iniciaQuestao(len(DIRETOR_29) + 1)
        questao_30 = self.iniciaQuestao(len(DIRETOR_30) + 1)
        questao_31 = self.iniciaQuestao(len(DIRETOR_31) + 1)
        questao_32 = self.iniciaQuestao(len(DIRETOR_32) + 1)
        questao_33 = self.iniciaQuestao(len(DIRETOR_33) + 1)
        questao_34 = self.iniciaQuestao(len(DIRETOR_34) + 1)
        questao_35 = self.iniciaQuestao(len(DIRETOR_35) + 1)
        questao_36 = self.iniciaQuestao(len(DIRETOR_36) + 1)
        questao_37 = self.iniciaQuestao(len(DIRETOR_37) + 1)
        questao_38 = self.iniciaQuestao(len(DIRETOR_38) + 1)
        questao_39 = self.iniciaQuestao(len(DIRETOR_39) + 1)
        questao_40 = self.iniciaQuestao(len(DIRETOR_40) + 1)
        questao_41 = self.iniciaQuestao(len(DIRETOR_41) + 1)
        questao_42 = self.iniciaQuestao(len(DIRETOR_42) + 1)
        questao_43 = self.iniciaQuestao(len(DIRETOR_43) + 1)
        questao_44 = self.iniciaQuestao(len(DIRETOR_44) + 1)
        questao_45 = self.iniciaQuestao(len(DIRETOR_45) + 1)
        questao_46 = self.iniciaQuestao(len(DIRETOR_46) + 1)
        questao_47 = self.iniciaQuestao(len(DIRETOR_47) + 1)
        questao_48 = self.iniciaQuestao(len(DIRETOR_48) + 1)
        questao_49 = self.iniciaQuestao(len(DIRETOR_49) + 1)
        questao_50 = self.iniciaQuestao(len(DIRETOR_50) + 1)
        questao_51 = self.iniciaQuestao(len(DIRETOR_51) + 1)
        questao_52 = self.iniciaQuestao(len(DIRETOR_52) + 1)
        questao_53 = self.iniciaQuestao(len(DIRETOR_53) + 1)
        questao_54 = self.iniciaQuestao(len(DIRETOR_54) + 1)
        questao_55 = self.iniciaQuestao(len(DIRETOR_55) + 1)
        questao_56 = self.iniciaQuestao(len(DIRETOR_56) + 1)
        questao_57 = self.iniciaQuestao(len(DIRETOR_57) + 1)
        questao_58 = self.iniciaQuestao(len(DIRETOR_58) + 1)
        questao_59 = self.iniciaQuestao(len(DIRETOR_59) + 1)
        questao_60 = self.iniciaQuestao(len(DIRETOR_60) + 1)
        questao_61 = self.iniciaQuestao(len(DIRETOR_61) + 1)
        questao_62 = self.iniciaQuestao(len(DIRETOR_62) + 1)
        questao_63 = self.iniciaQuestao(len(DIRETOR_63) + 1)
        questao_64 = self.iniciaQuestao(len(DIRETOR_64) + 1)
        questao_65 = self.iniciaQuestao(len(DIRETOR_65) + 1)
        questao_66 = self.iniciaQuestao(len(DIRETOR_66) + 1)
        questao_67 = self.iniciaQuestao(len(DIRETOR_67) + 1)
        questao_68 = self.iniciaQuestao(len(DIRETOR_68) + 1)
        questao_69 = self.iniciaQuestao(len(DIRETOR_69) + 1)
        questao_70 = self.iniciaQuestao(len(DIRETOR_70) + 1)
        questao_71 = self.iniciaQuestao(len(DIRETOR_71) + 1)
        questao_72 = self.iniciaQuestao(len(DIRETOR_72) + 1)
        questao_73 = self.iniciaQuestao(len(DIRETOR_73) + 1)
        questao_74 = self.iniciaQuestao(len(DIRETOR_74) + 1)
        questao_75 = self.iniciaQuestao(len(DIRETOR_75) + 1)
        questao_76 = self.iniciaQuestao(len(DIRETOR_76) + 1)
        questao_77 = self.iniciaQuestao(len(DIRETOR_77) + 1)
        questao_78 = self.iniciaQuestao(len(DIRETOR_78) + 1)
        questao_79 = self.iniciaQuestao(len(DIRETOR_79) + 1)
        questao_80 = self.iniciaQuestao(len(DIRETOR_80) + 1)
        questao_81 = self.iniciaQuestao(len(DIRETOR_81) + 1)
        questao_82 = self.iniciaQuestao(len(DIRETOR_82) + 1)
        questao_83 = self.iniciaQuestao(len(DIRETOR_83) + 1)
        questao_84 = self.iniciaQuestao(len(DIRETOR_84) + 1)
        
        for diretor in diretores:
            if diretor.questao_1 == None:
                questao_1[len(DIRETOR_1)] = questao_1[len(DIRETOR_1)] + 1
            else:
                for escolhas in diretor.questao_1:
                    for escolha in escolhas:
                        questao_1[int(escolha)] = questao_1[int(escolha)] + 1
            if diretor.questao_2 == None:
                questao_2[len(DIRETOR_2)] = questao_2[len(DIRETOR_2)] + 1
            else:
                questao_2[int(diretor.questao_2)] = questao_2[int(diretor.questao_2)] + 1
            if diretor.questao_3 == None:
                questao_3[len(DIRETOR_3)] = questao_3[len(DIRETOR_3)] + 1
            else:
                for escolhas in diretor.questao_3:
                    for escolha in escolhas:
                        questao_3[int(escolha)] = questao_3[int(escolha)] + 1
            if diretor.questao_4 == None:
                questao_4[len(DIRETOR_4)] = questao_4[len(DIRETOR_4)] + 1
            else:
                questao_4[int(diretor.questao_4)] = questao_4[int(diretor.questao_4)] + 1
            if diretor.questao_5 == None:
                questao_5[len(DIRETOR_5)] = questao_5[len(DIRETOR_5)] + 1
            else:
                questao_5[int(diretor.questao_5)] = questao_5[int(diretor.questao_5)] + 1
            if diretor.questao_6 == None:
                questao_6[len(DIRETOR_6)] = questao_6[len(DIRETOR_6)] + 1
            else:
                questao_6[int(diretor.questao_6)] = questao_6[int(diretor.questao_6)] + 1
            if diretor.questao_7 == None:
                questao_7[len(DIRETOR_7)] = questao_7[len(DIRETOR_7)] + 1
            else:
                questao_7[int(diretor.questao_7)] = questao_7[int(diretor.questao_7)] + 1
            if diretor.questao_8 == None:
                questao_8[len(DIRETOR_8)] = questao_8[len(DIRETOR_8)] + 1
            else:
                questao_8[int(diretor.questao_8)] = questao_8[int(diretor.questao_8)] + 1
            if diretor.questao_9 == None:
                questao_9[len(DIRETOR_9)] = questao_9[len(DIRETOR_9)] + 1
            else:
                questao_9[int(diretor.questao_9)] = questao_9[int(diretor.questao_9)] + 1
            if diretor.questao_10 == None:
                questao_10[len(DIRETOR_10)] = questao_10[len(DIRETOR_10)] + 1
            else:
                questao_10[int(diretor.questao_10)] = questao_10[int(diretor.questao_10)] + 1
            if diretor.questao_11 == None:
                questao_11[len(DIRETOR_11)] = questao_11[len(DIRETOR_11)] + 1
            else:
                questao_11[int(diretor.questao_11)] = questao_11[int(diretor.questao_11)] + 1
            if diretor.questao_12 == None:
                questao_12[len(DIRETOR_12)] = questao_12[len(DIRETOR_12)] + 1
            else:
                questao_12[int(diretor.questao_12)] = questao_12[int(diretor.questao_12)] + 1
            if diretor.questao_13 == None:
                questao_13[len(DIRETOR_13)] = questao_13[len(DIRETOR_13)] + 1
            else:
                questao_13[int(diretor.questao_13)] = questao_13[int(diretor.questao_13)] + 1
            if diretor.questao_14 == None:
                questao_14[len(DIRETOR_14)] = questao_14[len(DIRETOR_14)] + 1
            else:
                questao_14[int(diretor.questao_14)] = questao_14[int(diretor.questao_14)] + 1
            if diretor.questao_15 == None:
                questao_15[len(DIRETOR_15)] = questao_15[len(DIRETOR_15)] + 1
            else:
                questao_15[int(diretor.questao_15)] = questao_15[int(diretor.questao_15)] + 1
            if diretor.questao_16 == None:
                questao_16[len(DIRETOR_16)] = questao_16[len(DIRETOR_16)] + 1
            else:
                questao_16[int(diretor.questao_16)] = questao_16[int(diretor.questao_16)] + 1
            if diretor.questao_17 == None:
                questao_17[len(DIRETOR_17)] = questao_17[len(DIRETOR_17)] + 1
            else:
                questao_17[int(diretor.questao_17)] = questao_17[int(diretor.questao_17)] + 1
            if diretor.questao_18 == None:
                questao_18[len(DIRETOR_18)] = questao_18[len(DIRETOR_18)] + 1
            else:
                questao_18[int(diretor.questao_18)] = questao_18[int(diretor.questao_18)] + 1
            if diretor.questao_19 == None:
                questao_19[len(DIRETOR_19)] = questao_19[len(DIRETOR_19)] + 1
            else:
                questao_19[int(diretor.questao_19)] = questao_19[int(diretor.questao_19)] + 1
            if diretor.questao_20 == None:
                questao_20[len(DIRETOR_20)] = questao_20[len(DIRETOR_20)] + 1
            else:
                questao_20[int(diretor.questao_20)] = questao_20[int(diretor.questao_20)] + 1
            if diretor.questao_21 == None:
                questao_21[len(DIRETOR_21)] = questao_21[len(DIRETOR_21)] + 1
            else:
                questao_21[int(diretor.questao_21)] = questao_21[int(diretor.questao_21)] + 1
            if diretor.questao_22 == None:
                questao_22[len(DIRETOR_22)] = questao_22[len(DIRETOR_22)] + 1
            else:
                questao_22[int(diretor.questao_22)] = questao_22[int(diretor.questao_22)] + 1
            if diretor.questao_23 == None:
                questao_23[len(DIRETOR_23)] = questao_23[len(DIRETOR_23)] + 1
            else:
                questao_23[int(diretor.questao_23)] = questao_23[int(diretor.questao_23)] + 1
            if diretor.questao_24 == None:
                questao_24[len(DIRETOR_24)] = questao_24[len(DIRETOR_24)] + 1
            else:
                questao_24[int(diretor.questao_24)] = questao_24[int(diretor.questao_24)] + 1
            if diretor.questao_25 == None:
                questao_25[len(DIRETOR_25)] = questao_25[len(DIRETOR_25)] + 1
            else:
                questao_25[int(diretor.questao_25)] = questao_25[int(diretor.questao_25)] + 1
            if diretor.questao_26 == None:
                questao_26[len(DIRETOR_26)] = questao_26[len(DIRETOR_26)] + 1
            else:
                questao_26[int(diretor.questao_26)] = questao_26[int(diretor.questao_26)] + 1
            if diretor.questao_27 == None:
                questao_27[len(DIRETOR_27)] = questao_27[len(DIRETOR_27)] + 1
            else:
                questao_27[int(diretor.questao_27)] = questao_27[int(diretor.questao_27)] + 1
            if diretor.questao_28 == None:
                questao_28[len(DIRETOR_28)] = questao_28[len(DIRETOR_28)] + 1
            else:
                for escolhas in diretor.questao_28:
                    for escolha in escolhas:
                        questao_28[int(escolha)] = questao_28[int(escolha)] + 1
            if diretor.questao_29 == None:
                questao_29[len(DIRETOR_29)] = questao_29[len(DIRETOR_29)] + 1
            else:
                questao_29[int(diretor.questao_29)] = questao_29[int(diretor.questao_29)] + 1
            if diretor.questao_30 == None:
                questao_30[len(DIRETOR_30)] = questao_30[len(DIRETOR_30)] + 1
            else:
                questao_30[int(diretor.questao_30)] = questao_30[int(diretor.questao_30)] + 1
            if diretor.questao_31 == None:
                questao_31[len(DIRETOR_31)] = questao_31[len(DIRETOR_31)] + 1
            else:
                for escolhas in diretor.questao_31:
                    for escolha in escolhas:
                        questao_31[int(escolha)] = questao_31[int(escolha)] + 1
            if diretor.questao_32 == None:
                questao_32[len(DIRETOR_32)] = questao_32[len(DIRETOR_32)] + 1
            else:
                questao_32[int(diretor.questao_32)] = questao_32[int(diretor.questao_32)] + 1
            if diretor.questao_33 == None:
                questao_33[len(DIRETOR_33)] = questao_33[len(DIRETOR_33)] + 1
            else:
                for escolhas in diretor.questao_33:
                    for escolha in escolhas:
                        questao_33[int(escolha)] = questao_33[int(escolha)] + 1
            if diretor.questao_34 == None:
                questao_34[len(DIRETOR_34)] = questao_34[len(DIRETOR_34)] + 1
            else:
                questao_34[int(diretor.questao_34)] = questao_34[int(diretor.questao_34)] + 1
            if diretor.questao_35 == None:
                questao_35[len(DIRETOR_35)] = questao_35[len(DIRETOR_35)] + 1
            else:
                questao_35[int(diretor.questao_35)] = questao_35[int(diretor.questao_35)] + 1
            if diretor.questao_36 == None:
                questao_36[len(DIRETOR_36)] = questao_36[len(DIRETOR_36)] + 1
            else:
                questao_36[int(diretor.questao_36)] = questao_36[int(diretor.questao_36)] + 1
            if diretor.questao_37 == None:
                questao_37[len(DIRETOR_37)] = questao_37[len(DIRETOR_37)] + 1
            else:
                for escolhas in diretor.questao_37:
                    for escolha in escolhas:
                        questao_37[int(escolha)] = questao_37[int(escolha)] + 1
            if diretor.questao_38 == None:
                questao_38[len(DIRETOR_38)] = questao_38[len(DIRETOR_38)] + 1
            else:
                questao_38[int(diretor.questao_38)] = questao_38[int(diretor.questao_38)] + 1
            if diretor.questao_39 == None:
                questao_39[len(DIRETOR_39)] = questao_39[len(DIRETOR_39)] + 1
            else:
                for escolhas in diretor.questao_39:
                    for escolha in escolhas:
                        questao_39[int(escolha)] = questao_39[int(escolha)] + 1
            if diretor.questao_40 == None:
                questao_40[len(DIRETOR_40)] = questao_40[len(DIRETOR_40)] + 1
            else:
                questao_40[int(diretor.questao_40)] = questao_40[int(diretor.questao_40)] + 1
            if diretor.questao_41 == None:
                questao_41[len(DIRETOR_41)] = questao_41[len(DIRETOR_41)] + 1
            else:
                questao_41[int(diretor.questao_41)] = questao_41[int(diretor.questao_41)] + 1
            if diretor.questao_42 == None:
                questao_42[len(DIRETOR_42)] = questao_42[len(DIRETOR_42)] + 1
            else:
                questao_42[int(diretor.questao_42)] = questao_42[int(diretor.questao_42)] + 1
            if diretor.questao_43 == None:
                questao_43[len(DIRETOR_43)] = questao_43[len(DIRETOR_43)] + 1
            else:
                questao_43[int(diretor.questao_43)] = questao_43[int(diretor.questao_43)] + 1
            if diretor.questao_44 == None:
                questao_44[len(DIRETOR_44)] = questao_44[len(DIRETOR_44)] + 1
            else:
                questao_44[int(diretor.questao_44)] = questao_44[int(diretor.questao_44)] + 1
            if diretor.questao_45 == None:
                questao_45[len(DIRETOR_45)] = questao_45[len(DIRETOR_45)] + 1
            else:
                questao_45[int(diretor.questao_45)] = questao_45[int(diretor.questao_45)] + 1
            if diretor.questao_46 == None:
                questao_46[len(DIRETOR_46)] = questao_46[len(DIRETOR_46)] + 1
            else:
                questao_46[int(diretor.questao_46)] = questao_46[int(diretor.questao_46)] + 1
            if diretor.questao_47 == None:
                questao_47[len(DIRETOR_47)] = questao_47[len(DIRETOR_47)] + 1
            else:
                questao_47[int(diretor.questao_47)] = questao_47[int(diretor.questao_47)] + 1
            if diretor.questao_48 == None:
                questao_48[len(DIRETOR_48)] = questao_48[len(DIRETOR_48)] + 1
            else:
                questao_48[int(diretor.questao_48)] = questao_48[int(diretor.questao_48)] + 1
            if diretor.questao_49 == None:
                questao_49[len(DIRETOR_49)] = questao_49[len(DIRETOR_49)] + 1
            else:
                questao_49[int(diretor.questao_49)] = questao_49[int(diretor.questao_49)] + 1
            if diretor.questao_50 == None:
                questao_50[len(DIRETOR_50)] = questao_50[len(DIRETOR_50)] + 1
            else:
                questao_50[int(diretor.questao_50)] = questao_50[int(diretor.questao_50)] + 1
            if diretor.questao_51 == None:
                questao_51[len(DIRETOR_51)] = questao_51[len(DIRETOR_51)] + 1
            else:
                questao_51[int(diretor.questao_51)] = questao_51[int(diretor.questao_51)] + 1
            if diretor.questao_52 == None:
                questao_52[len(DIRETOR_52)] = questao_52[len(DIRETOR_52)] + 1
            else:
                questao_52[int(diretor.questao_52)] = questao_52[int(diretor.questao_52)] + 1
            if diretor.questao_53 == None:
                questao_53[len(DIRETOR_53)] = questao_53[len(DIRETOR_53)] + 1
            else:
                questao_53[int(diretor.questao_53)] = questao_53[int(diretor.questao_53)] + 1
            if diretor.questao_54 == None:
                questao_54[len(DIRETOR_54)] = questao_54[len(DIRETOR_54)] + 1
            else:
                questao_54[int(diretor.questao_54)] = questao_54[int(diretor.questao_54)] + 1
            if diretor.questao_55 == None:
                questao_55[len(DIRETOR_55)] = questao_55[len(DIRETOR_55)] + 1
            else:
                questao_55[int(diretor.questao_55)] = questao_55[int(diretor.questao_55)] + 1
            if diretor.questao_56 == None:
                questao_56[len(DIRETOR_56)] = questao_56[len(DIRETOR_56)] + 1
            else:
                questao_56[int(diretor.questao_56)] = questao_56[int(diretor.questao_56)] + 1
            if diretor.questao_57 == None:
                questao_57[len(DIRETOR_57)] = questao_57[len(DIRETOR_57)] + 1
            else:
                questao_57[int(diretor.questao_57)] = questao_57[int(diretor.questao_57)] + 1
            if diretor.questao_58 == None:
                questao_58[len(DIRETOR_58)] = questao_58[len(DIRETOR_58)] + 1
            else:
                questao_58[int(diretor.questao_58)] = questao_58[int(diretor.questao_58)] + 1
            if diretor.questao_59 == None:
                questao_59[len(DIRETOR_59)] = questao_59[len(DIRETOR_59)] + 1
            else:
                questao_59[int(diretor.questao_59)] = questao_59[int(diretor.questao_59)] + 1
            if diretor.questao_60 == None:
                questao_60[len(DIRETOR_60)] = questao_60[len(DIRETOR_60)] + 1
            else:
                questao_60[int(diretor.questao_60)] = questao_60[int(diretor.questao_60)] + 1
            if diretor.questao_61 == None:
                questao_61[len(DIRETOR_61)] = questao_61[len(DIRETOR_61)] + 1
            else:
                questao_61[int(diretor.questao_61)] = questao_61[int(diretor.questao_61)] + 1
            if diretor.questao_62 == None:
                questao_62[len(DIRETOR_62)] = questao_62[len(DIRETOR_62)] + 1
            else:
                questao_62[int(diretor.questao_62)] = questao_62[int(diretor.questao_62)] + 1
            if diretor.questao_63 == None:
                questao_63[len(DIRETOR_63)] = questao_63[len(DIRETOR_63)] + 1
            else:
                questao_63[int(diretor.questao_63)] = questao_63[int(diretor.questao_63)] + 1
            if diretor.questao_64 == None:
                questao_64[len(DIRETOR_64)] = questao_64[len(DIRETOR_64)] + 1
            else:
                questao_64[int(diretor.questao_64)] = questao_64[int(diretor.questao_64)] + 1
            if diretor.questao_65 == None:
                questao_65[len(DIRETOR_65)] = questao_65[len(DIRETOR_65)] + 1
            else:
                questao_65[int(diretor.questao_65)] = questao_65[int(diretor.questao_65)] + 1
            if diretor.questao_66 == None:
                questao_66[len(DIRETOR_66)] = questao_66[len(DIRETOR_66)] + 1
            else:
                questao_66[int(diretor.questao_66)] = questao_66[int(diretor.questao_66)] + 1
            if diretor.questao_67 == None:
                questao_67[len(DIRETOR_67)] = questao_67[len(DIRETOR_67)] + 1
            else:
                questao_67[int(diretor.questao_67)] = questao_67[int(diretor.questao_67)] + 1
            if diretor.questao_68 == None:
                questao_68[len(DIRETOR_68)] = questao_68[len(DIRETOR_68)] + 1
            else:
                questao_68[int(diretor.questao_68)] = questao_68[int(diretor.questao_68)] + 1
            if diretor.questao_69 == None:
                questao_69[len(DIRETOR_69)] = questao_69[len(DIRETOR_69)] + 1
            else:
                questao_69[int(diretor.questao_69)] = questao_69[int(diretor.questao_69)] + 1
            if diretor.questao_70 == None:
                questao_70[len(DIRETOR_70)] = questao_70[len(DIRETOR_70)] + 1
            else:
                questao_70[int(diretor.questao_70)] = questao_70[int(diretor.questao_70)] + 1
            if diretor.questao_71 == None:
                questao_71[len(DIRETOR_71)] = questao_71[len(DIRETOR_71)] + 1
            else:
                questao_71[int(diretor.questao_71)] = questao_71[int(diretor.questao_71)] + 1
            if diretor.questao_72 == None:
                questao_72[len(DIRETOR_72)] = questao_72[len(DIRETOR_72)] + 1
            else:
                questao_72[int(diretor.questao_72)] = questao_72[int(diretor.questao_72)] + 1
            if diretor.questao_73 == None:
                questao_73[len(DIRETOR_73)] = questao_73[len(DIRETOR_73)] + 1
            else:
                questao_73[int(diretor.questao_73)] = questao_73[int(diretor.questao_73)] + 1
            if diretor.questao_74 == None:
                questao_74[len(DIRETOR_74)] = questao_74[len(DIRETOR_74)] + 1
            else:
                questao_74[int(diretor.questao_74)] = questao_74[int(diretor.questao_74)] + 1
            if diretor.questao_75 == None:
                questao_75[len(DIRETOR_75)] = questao_75[len(DIRETOR_75)] + 1
            else:
                questao_75[int(diretor.questao_75)] = questao_75[int(diretor.questao_75)] + 1
            if diretor.questao_76 == None:
                questao_76[len(DIRETOR_76)] = questao_76[len(DIRETOR_76)] + 1
            else:
                questao_76[int(diretor.questao_76)] = questao_76[int(diretor.questao_76)] + 1
            if diretor.questao_77 == None:
                questao_77[len(DIRETOR_77)] = questao_77[len(DIRETOR_77)] + 1
            else:
                questao_77[int(diretor.questao_77)] = questao_77[int(diretor.questao_77)] + 1
            if diretor.questao_78 == None:
                questao_78[len(DIRETOR_78)] = questao_78[len(DIRETOR_78)] + 1
            else:
                questao_78[int(diretor.questao_78)] = questao_78[int(diretor.questao_78)] + 1
            if diretor.questao_79 == None:
                questao_79[len(DIRETOR_79)] = questao_79[len(DIRETOR_79)] + 1
            else:
                questao_79[int(diretor.questao_79)] = questao_79[int(diretor.questao_79)] + 1
            if diretor.questao_80 == None:
                questao_80[len(DIRETOR_80)] = questao_80[len(DIRETOR_80)] + 1
            else:
                questao_80[int(diretor.questao_80)] = questao_80[int(diretor.questao_80)] + 1
            if diretor.questao_81 == None:
                questao_81[len(DIRETOR_81)] = questao_81[len(DIRETOR_81)] + 1
            else:
                questao_81[int(diretor.questao_81)] = questao_81[int(diretor.questao_81)] + 1
            if diretor.questao_82 == None:
                questao_82[len(DIRETOR_82)] = questao_82[len(DIRETOR_82)] + 1
            else:
                questao_82[int(diretor.questao_82)] = questao_82[int(diretor.questao_82)] + 1
            if diretor.questao_83 == None:
                questao_83[len(DIRETOR_83)] = questao_83[len(DIRETOR_83)] + 1
            else:
                questao_83[int(diretor.questao_83)] = questao_83[int(diretor.questao_83)] + 1
            if diretor.questao_84 == None:
                questao_84[len(DIRETOR_84)] = questao_84[len(DIRETOR_84)] + 1
            else:
                questao_84[int(diretor.questao_84)] = questao_84[int(diretor.questao_84)] + 1
        
        context = {
            'pagina_graficos': True,
            'pagina_graficos_diretores': True,
            'diretores': diretores,
            'questao_1': questao_1,
            'questao_2': questao_2,
            'questao_3': questao_3,
            'questao_4': questao_4,
            'questao_5': questao_5,
            'questao_6': questao_6,
            'questao_7': questao_7,
            'questao_8': questao_8,
            'questao_9': questao_9,
            'questao_10': questao_10,
            'questao_11': questao_11,
            'questao_12': questao_12,
            'questao_13': questao_13,
            'questao_14': questao_14,
            'questao_15': questao_15,
            'questao_16': questao_16,
            'questao_17': questao_17,
            'questao_18': questao_18,
            'questao_19': questao_19,
            'questao_20': questao_20,
            'questao_21': questao_21,
            'questao_22': questao_22,
            'questao_23': questao_23,
            'questao_24': questao_24,
            'questao_25': questao_25,
            'questao_26': questao_26,
            'questao_27': questao_27,
            'questao_28': questao_28,
            'questao_29': questao_29,
            'questao_30': questao_30,
            'questao_31': questao_31,
            'questao_32': questao_32,
            'questao_33': questao_33,
            'questao_34': questao_34,
            'questao_35': questao_35,
            'questao_36': questao_36,
            'questao_37': questao_37,
            'questao_38': questao_38,
            'questao_39': questao_39,
            'questao_40': questao_40,
            'questao_41': questao_41,
            'questao_42': questao_42,
            'questao_43': questao_43,
            'questao_44': questao_44,
            'questao_45': questao_45,
            'questao_46': questao_46,
            'questao_47': questao_47,
            'questao_48': questao_48,
            'questao_49': questao_49,
            'questao_50': questao_50,
            'questao_51': questao_51,
            'questao_52': questao_52,
            'questao_53': questao_53,
            'questao_54': questao_54,
            'questao_55': questao_55,
            'questao_56': questao_56,
            'questao_57': questao_57,
            'questao_58': questao_58,
            'questao_59': questao_59,
            'questao_60': questao_60,
            'questao_61': questao_61,
            'questao_62': questao_62,
            'questao_63': questao_63,
            'questao_64': questao_64,
            'questao_65': questao_65,
            'questao_66': questao_66,
            'questao_67': questao_67,
            'questao_68': questao_68,
            'questao_69': questao_69,
            'questao_70': questao_70,
            'questao_71': questao_71,
            'questao_72': questao_72,
            'questao_73': questao_73,
            'questao_74': questao_74,
            'questao_75': questao_75,
            'questao_76': questao_76,
            'questao_77': questao_77,
            'questao_78': questao_78,
            'questao_79': questao_79,
            'questao_80': questao_80,
            'questao_81': questao_81,
            'questao_82': questao_82,
            'questao_83': questao_83,
            'questao_84': questao_84,
        }
        
        return render(self.request, 'administracao/graficos_diretores.html', context)
    
    def iniciaQuestao(self, maximo):
        questao = []
        for i in range(maximo):
            questao.append(0)
        return questao


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


class DetalhesCampanhaView(LoginRequired, View):
    """Página com as informações sobre uma campanha"""
    
    def get(self, request, campanha_id):
        campanha = Campanha.objects.get(id=campanha_id)
        form = CampanhaForm(instance=campanha)
        context = {'pagina_campanhas': True, 'campanha': campanha, 'form': form}
        return render(self.request, 'administracao/campanha.html', context)


class CriaCampanhaView(LoginRequired, View):
    """Cadastra as informações de uma nova campanha"""
    
    def get(self, request):
        form = CampanhaForm()
        context = {'pagina_campanhas': True, 'form': form}
        return render(self.request, 'administracao/novo_elemento.html', context)
    
    def post(self, request):
        form = CampanhaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('administracao:campanhas'))
        context = {'pagina_campanhas': True, 'form': form}
        return render(self.request, 'administracao/novo_elemento.html', context)


class EditaCampanhaView(LoginRequired, View):
    """Altera as informações de uma campanha"""
    
    def get(self, request, campanha_id):
        campanha = Campanha.objects.get(id=campanha_id)
        form = CampanhaForm(instance=campanha)
        context = {'pagina_campanhas': True, 'campanha': campanha, 'form': form}
        return render(self.request, 'administracao/edita_elemento.html', context)
    
    def post(self, request, campanha_id):
        campanha = Campanha.objects.get(id=campanha_id)
        form = CampanhaForm(request.POST, request.FILES, instance=campanha)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('administracao:campanhas'))
        context = {'pagina_campanhas': True, 'campanha': campanha, 'form': form}
        return render(self.request, 'administracao/edita_elemento.html', context)


class RemoveCampanhaView(LoginRequired, View):
    """Remove uma campanha"""
    
    def get(self, request, campanha_id):
        campanha = Campanha.objects.get(id=campanha_id)
        context = {'pagina_campanhas': True, 'campanha': campanha}
        return render(self.request, 'administracao/remove_elemento.html', context)
        
    def post(self, request, campanha_id):
        campanha = Campanha.objects.get(id=campanha_id)
        campanha.delete()
        return HttpResponseRedirect(reverse('administracao:campanhas'))


class AcoesView(LoginRequired, View):
    """Página que lista as ações cadastradas no sistema"""
    
    def get(self, request):
        acoes = Acao.objects.order_by('-id')
        context = {'pagina_acoes': True, 'acoes': acoes}
        return render(self.request, 'administracao/acoes.html', context)


class DetalhesAcaoView(LoginRequired, View):
    """Página com as informações sobre uma ação"""
    
    def get(self, request, acao_id):
        acao = Acao.objects.get(id=acao_id)
        form = AcaoForm(instance=acao)
        context = {'pagina_acoes': True, 'acao': acao, 'form': form}
        return render(self.request, 'administracao/acao.html', context)


class CriaAcaoView(LoginRequired, View):
    """Cadastra as informações de uma nova ação"""
    
    def get(self, request):
        form = AcaoForm()
        context = {'pagina_acoes': True, 'form': form}
        return render(self.request, 'administracao/novo_elemento.html', context)
    
    def post(self, request):
        form = AcaoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('administracao:acoes'))
        context = {'pagina_acoes': True, 'form': form}
        return render(self.request, 'administracao/novo_elemento.html', context)


class EditaAcaoView(LoginRequired, View):
    """Altera as informações de uma ação"""
    
    def get(self, request, acao_id):
        acao = Acao.objects.get(id=acao_id)
        form = AcaoForm(instance=acao)
        context = {'pagina_acoes': True, 'acao': acao, 'form': form}
        return render(self.request, 'administracao/edita_elemento.html', context)
    
    def post(self, request, acao_id):
        acao = Acao.objects.get(id=acao_id)
        form = AcaoForm(request.POST, request.FILES, instance=acao)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('administracao:acoes'))
        context = {'pagina_acoes': True, 'acao': acao, 'form': form}
        return render(self.request, 'administracao/edita_elemento.html', context)


class RemoveAcaoView(LoginRequired, View):
    """Remove uma ação"""
    
    def get(self, request, acao_id):
        acao = Acao.objects.get(id=acao_id)
        context = {'pagina_acoes': True, 'acao': acao}
        return render(self.request, 'administracao/remove_elemento.html', context)
        
    def post(self, request, acao_id):
        acao = Acao.objects.get(id=acao_id)
        acao.delete()
        return HttpResponseRedirect(reverse('administracao:acoes'))


class EscolasView(LoginRequired, View):
    """Página que lista as escolas cadastradas no sistema"""
    
    def get(self, request):
        escolas = Escola.objects.order_by('-id')
        context = {'pagina_escolas': True, 'escolas': escolas}
        return render(self.request, 'administracao/escolas.html', context)


class DetalhesEscolaView(LoginRequired, View):
    """Página com as informações sobre uma escola"""
    
    def get(self, request, escola_id):
        escola = Escola.objects.get(id=escola_id)
        form = EscolaForm(instance=escola)
        context = {'pagina_escolas': True, 'escola': escola, 'form': form}
        return render(self.request, 'administracao/escola.html', context)


class CriaEscolaView(LoginRequired, View):
    """Cadastra as informações de uma nova escola"""
    
    def get(self, request):
        form = EscolaForm()
        context = {'pagina_escolas': True, 'form': form}
        return render(self.request, 'administracao/novo_elemento.html', context)
    
    def post(self, request):
        form = EscolaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('administracao:escolas'))
        context = {'pagina_escolas': True, 'form': form}
        return render(self.request, 'administracao/novo_elemento.html', context)


class EditaEscolaView(LoginRequired, View):
    """Altera as informações de uma escola"""
    
    def get(self, request, escola_id):
        escola = Escola.objects.get(id=escola_id)
        form = EscolaForm(instance=escola)
        context = {'pagina_escolas': True, 'escola': escola, 'form': form}
        return render(self.request, 'administracao/edita_elemento.html', context)
    
    def post(self, request, escola_id):
        escola = Escola.objects.get(id=escola_id)
        form = EscolaForm(request.POST, request.FILES, instance=escola)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('administracao:escolas'))
        context = {'pagina_escolas': True, 'escola': escola, 'form': form}
        return render(self.request, 'administracao/edita_elemento.html', context)


class RemoveEscolaView(LoginRequired, View):
    """Remove uma escola"""
    
    def get(self, request, escola_id):
        escola = Escola.objects.get(id=escola_id)
        context = {'pagina_escolas': True, 'escola': escola}
        return render(self.request, 'administracao/remove_elemento.html', context)
        
    def post(self, request, escola_id):
        escola = Escola.objects.get(id=escola_id)
        escola.delete()
        return HttpResponseRedirect(reverse('administracao:escolas'))


class AlunosView(LoginRequired, View):
    """Página que lista os alunos cadastrados no sistema"""
    
    def get(self, request):
        alunos = Aluno.objects.order_by('-id')
        context = {'pagina_alunos': True, 'alunos': alunos}
        return render(self.request, 'administracao/alunos.html', context)


class DetalhesAlunoView(LoginRequired, View):
    """Página com as informações sobre um aluno"""
    
    def get(self, request, aluno_id):
        aluno = Aluno.objects.get(id=aluno_id)
        form = AlunoForm(instance=aluno)
        context = {'pagina_alunos': True, 'aluno': aluno, 'form': form}
        return render(self.request, 'administracao/aluno.html', context)


class CriaAlunoView(LoginRequired, View):
    """Cadastra as informações de um novo aluno"""
    
    def get(self, request):
        form = AlunoForm()
        context = {'pagina_alunos': True, 'form': form}
        return render(self.request, 'administracao/novo_elemento.html', context)
    
    def post(self, request):
        form = AlunoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('administracao:alunos'))
        context = {'pagina_alunos': True, 'form': form}
        return render(self.request, 'administracao/novo_elemento.html', context)


class EditaAlunoView(LoginRequired, View):
    """Altera as informações de um aluno"""
    
    def get(self, request, aluno_id):
        aluno = Aluno.objects.get(id=aluno_id)
        form = AlunoForm(instance=aluno)
        context = {'pagina_alunos': True, 'aluno': aluno, 'form': form}
        return render(self.request, 'administracao/edita_elemento.html', context)
    
    def post(self, request, aluno_id):
        aluno = Aluno.objects.get(id=aluno_id)
        form = AlunoForm(request.POST, request.FILES, instance=aluno)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('administracao:alunos'))
        context = {'pagina_alunos': True, 'aluno': aluno, 'form': form}
        return render(self.request, 'administracao/edita_elemento.html', context)


class RemoveAlunoView(LoginRequired, View):
    """Remove um aluno"""
    
    def get(self, request, aluno_id):
        aluno = Aluno.objects.get(id=aluno_id)
        context = {'pagina_alunos': True, 'aluno': aluno}
        return render(self.request, 'administracao/remove_elemento.html', context)
        
    def post(self, request, aluno_id):
        aluno = Aluno.objects.get(id=aluno_id)
        aluno.delete()
        return HttpResponseRedirect(reverse('administracao:alunos'))


class QuestionariosView(LoginRequired, View):
    """Página que lista os questionários cadastrados no sistema"""
    
    def get(self, request):
        questionarios = Questionario.objects.order_by('-id')
        context = {'pagina_questionarios': True, 'questionarios': questionarios}
        return render(self.request, 'administracao/questionarios.html', context)


class DetalhesQuestionarioView(LoginRequired, View):
    """Página com as informações sobre um questionário"""
    
    def get(self, request, questionario_id):
        questionario = Questionario.objects.get(id=questionario_id)
        form = QuestionarioForm(instance=questionario)
        context = {'pagina_questionarios': True, 'questionario': questionario, 'form': form}
        return render(self.request, 'administracao/questionario.html', context)


class CriaQuestionarioView(LoginRequired, View):
    """Cadastra as informações de um novo questionário"""
    
    def get(self, request):
        form = QuestionarioForm()
        context = {'pagina_questionarios': True, 'form': form}
        return render(self.request, 'administracao/novo_elemento.html', context)
    
    def post(self, request):
        form = QuestionarioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('administracao:questionarios'))
        context = {'pagina_questionarios': True, 'form': form}
        return render(self.request, 'administracao/novo_elemento.html', context)


class EditaQuestionarioView(LoginRequired, View):
    """Altera as informações de um questionário"""
    
    def get(self, request, questionario_id):
        questionario = Questionario.objects.get(id=questionario_id)
        form = QuestionarioForm(instance=questionario)
        context = {'pagina_questionarios': True, 'questionario': questionario, 'form': form}
        return render(self.request, 'administracao/edita_elemento.html', context)
    
    def post(self, request, questionario_id):
        questionario = Questionario.objects.get(id=questionario_id)
        form = QuestionarioForm(request.POST, request.FILES, instance=questionario)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('administracao:questionarios'))
        context = {'pagina_questionarios': True, 'questionario': questionario, 'form': form}
        return render(self.request, 'administracao/edita_elemento.html', context)


class RemoveQuestionarioView(LoginRequired, View):
    """Remove um questionário"""
    
    def get(self, request, questionario_id):
        questionario = Questionario.objects.get(id=questionario_id)
        context = {'pagina_questionarios': True, 'questionario': questionario}
        return render(self.request, 'administracao/remove_elemento.html', context)
        
    def post(self, request, questionario_id):
        questionario = Questionario.objects.get(id=questionario_id)
        questionario.delete()
        return HttpResponseRedirect(reverse('administracao:questionarios'))


class ExamesView(LoginRequired, View):
    """Página que lista os exames cadastrados no sistema"""
    
    def get(self, request):
        exames = Exame.objects.order_by('-id')
        context = {'pagina_exames': True, 'exames': exames}
        return render(self.request, 'administracao/exames.html', context)


class DetalhesExameView(LoginRequired, View):
    """Página com as informações sobre um exame"""
    
    def get(self, request, exame_id):
        exame = Exame.objects.get(id=exame_id)
        form = ExameForm(instance=exame)
        context = {'pagina_exames': True, 'exame': exame, 'form': form}
        return render(self.request, 'administracao/exame.html', context)


class CriaExameView(LoginRequired, View):
    """Cadastra as informações de um novo exame"""
    
    def get(self, request):
        form = ExameForm()
        context = {'pagina_exames': True, 'form': form}
        return render(self.request, 'administracao/novo_elemento.html', context)
    
    def post(self, request):
        form = ExameForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('administracao:exames'))
        context = {'pagina_exames': True, 'form': form}
        return render(self.request, 'administracao/novo_elemento.html', context)


class EditaExameView(LoginRequired, View):
    """Altera as informações de um exame"""
    
    def get(self, request, exame_id):
        exame = Exame.objects.get(id=exame_id)
        form = ExameForm(instance=exame)
        context = {'pagina_exames': True, 'exame': exame, 'form': form}
        return render(self.request, 'administracao/edita_elemento.html', context)
    
    def post(self, request, exame_id):
        exame = Exame.objects.get(id=exame_id)
        form = ExameForm(request.POST, request.FILES, instance=exame)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('administracao:exames'))
        context = {'pagina_exames': True, 'exame': exame, 'form': form}
        return render(self.request, 'administracao/edita_elemento.html', context)


class RemoveExameView(LoginRequired, View):
    """Remove um exame"""
    
    def get(self, request, exame_id):
        exame = Exame.objects.get(id=exame_id)
        context = {'pagina_exames': True, 'exame': exame}
        return render(self.request, 'administracao/remove_elemento.html', context)
        
    def post(self, request, exame_id):
        exame = Exame.objects.get(id=exame_id)
        exame.delete()
        return HttpResponseRedirect(reverse('administracao:exames'))


class DiretoresView(LoginRequired, View):
    """Página que lista as os questionários para os diretores cadastradas no sistema"""
    
    def get(self, request):
        diretores = Diretor.objects.order_by('-id')
        context = {'pagina_diretores': True, 'diretores': diretores}
        return render(self.request, 'administracao/diretores.html', context)


class DetalhesDiretorView(LoginRequired, View):
    """Página com as informações sobre um questionário para diretores"""
    
    def get(self, request, diretor_id):
        diretor = Diretor.objects.get(id=diretor_id)
        form = DiretorForm(instance=diretor)
        context = {'pagina_diretores': True, 'diretor': diretor, 'form': form}
        return render(self.request, 'administracao/diretor.html', context)


class CriaDiretorView(LoginRequired, View):
    """Cadastra as informações de um novo questionário para diretores"""
    
    def get(self, request):
        form = DiretorForm()
        context = {'pagina_diretores': True, 'form': form}
        return render(self.request, 'administracao/novo_elemento.html', context)
    
    def post(self, request):
        form = DiretorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('administracao:diretores'))
        context = {'pagina_diretores': True, 'form': form}
        return render(self.request, 'administracao/novo_elemento.html', context)


class EditaDiretorView(LoginRequired, View):
    """Altera as informações de um questionário para diretores"""
    
    def get(self, request, diretor_id):
        diretor = Diretor.objects.get(id=diretor_id)
        form = DiretorForm(instance=diretor)
        context = {'pagina_diretores': True, 'diretor': diretor, 'form': form}
        return render(self.request, 'administracao/edita_elemento.html', context)
    
    def post(self, request, diretor_id):
        diretor = Diretor.objects.get(id=diretor_id)
        form = DiretorForm(request.POST, request.FILES, instance=diretor)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('administracao:diretores'))
        context = {'pagina_diretores': True, 'diretor': diretor, 'form': form}
        return render(self.request, 'administracao/edita_elemento.html', context)


class RemoveDiretorView(LoginRequired, View):
    """Remove um questionário para diretores"""
    
    def get(self, request, diretor_id):
        diretor = Diretor.objects.get(id=diretor_id)
        context = {'pagina_diretores': True, 'diretor': diretor}
        return render(self.request, 'administracao/remove_elemento.html', context)
        
    def post(self, request, diretor_id):
        diretor = Diretor.objects.get(id=diretor_id)
        diretor.delete()
        return HttpResponseRedirect(reverse('administracao:diretores'))
