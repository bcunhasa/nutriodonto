from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.views import View

import datetime

from administracao.models import *


class LoginRequired(LoginRequiredMixin):
    """Configurações para o login"""
    login_url = 'administracao/login/'
    redirect_field_name = 'next'


class EstudoView(LoginRequired, View):
    """Página que mostra os resultados do estudo"""
    
    def get(self, request):
        exames = Exame.objects.order_by('id')
        
        # Primeiras questões do arquivo 1
        idade_geral = [0, 0, 0, 0, 0, 0, 0, 0]
        idade_escolas = [
            [0, 0, 0, 0, 0, 0, 0, 0], # Escola Municipal Beatriz Rodrigues da Silva-2019
            [0, 0, 0, 0, 0, 0, 0, 0], # Escola Municipal de Tempo Integral Marcos Freire
            [0, 0, 0, 0, 0, 0, 0, 0], # Escola municipal de T.I. Anisio Spenola Teixeira
            [0, 0, 0, 0, 0, 0, 0, 0], # Escola municipal de T.I.Almirante Tamandare
            [0, 0, 0, 0, 0, 0, 0, 0], # Escola municipal de T.I. Caroline C. C. da Silva
            [0, 0, 0, 0, 0, 0, 0, 0], # Escola municipal Professor Sávia F. Jacome
            [0, 0, 0, 0, 0, 0, 0, 0], # Escola municipal de T.I. Vinícius de Moraes
            [0, 0, 0, 0, 0, 0, 0, 0], # Escola municipal de T.I. Euridice F. de Mello
            [0, 0, 0, 0, 0, 0, 0, 0], # Escola municipal Thiago Barbosa
            [0, 0, 0, 0, 0, 0, 0, 0], # Escola municipal de T.I. Sueli Pereira A. Reche
            [0, 0, 0, 0, 0, 0, 0, 0], # Escola municipal de T.I. Monsenhor Pedro P. Piagem
            [0, 0, 0, 0, 0, 0, 0, 0], # Escola municipal Maria Rosa de Castro Sales
            [0, 0, 0, 0, 0, 0, 0, 0], # Escola municipal Maria Júlia Amorim Rodrigues
            [0, 0, 0, 0, 0, 0, 0, 0], # Escola municipal de T.I. Luiz Nunes de Oliveira
            [0, 0, 0, 0, 0, 0, 0, 0], # Escola municipal de T.I. João Beltrão
            [0, 0, 0, 0, 0, 0, 0, 0], # Escola municipal Jorge Amado
            [0, 0, 0, 0, 0, 0, 0, 0], # Escola municipal Darcy Ribeiro
            [0, 0, 0, 0, 0, 0, 0, 0], # Escola municipal de T.I. Daniel Batista
            [0, 0, 0, 0, 0, 0, 0, 0], # Escola municipal Crispim Pereira de Alencar
            [0, 0, 0, 0, 0, 0, 0, 0], # Escola municipal de T.I. Aprigio T. de Matos
            [0, 0, 0, 0, 0, 0, 0, 0], # Escola municipal Aurélio Buarque de Holanda
            [0, 0, 0, 0, 0, 0, 0, 0], # Escola municipal Antônio G. de Carvalho Filho
            [0, 0, 0, 0, 0, 0, 0, 0], # Escola Silverio Ribeiro Matos
            [0, 0, 0, 0, 0, 0, 0, 0], # Escola municipal de T.I. Margarida Gonçalves
            [0, 0, 0, 0, 0, 0, 0, 0], # Escola municipal Antônio Carlos Jobim
            [0, 0, 0, 0, 0, 0, 0, 0], # Escola municipal Henrique Talone Pinheiro
            [0, 0, 0, 0, 0, 0, 0, 0], # Escola municipal Anne Frank
            [0, 0, 0, 0, 0, 0, 0, 0], # Escola municipal de T.I. Padre Josimo M. Tavares
            [0, 0, 0, 0, 0, 0, 0, 0], # Escola municipal Beatriz Rodrigues da Silva
            [0, 0, 0, 0, 0, 0, 0, 0], # Escola municipal Mestre Pacífico S. Campos
            [0, 0, 0, 0, 0, 0, 0, 0], # Escola municipal Luiz Gonzaga
        ]
        idade_territorios_saude = [
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
        ]
        idade_distritos_sanitarios = [
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
        ]
        
        raca_geral = [0, 0, 0, 0, 0]
        raca_escolas = [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
        ]
        raca_territorios_saude = [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
        ]
        raca_distritos_sanitarios = [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
        ]
        
        sexo_geral = [0, 0, 0, 0]
        sexo_escolas = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
        ]
        sexo_territorios_saude = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
        ]
        sexo_distritos_sanitarios = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
        ]
        
        for exame in exames:
            # Idade (12, 13, 14, 15, 16, 17, 18 e 19)
            idade = int((datetime.date.today() - exame.aluno.nascimento).days / 365.25)
            if idade <= 12:
                idade_geral[0] += idade_geral[0]
            elif idade == 13:
                idade_geral[1] += idade_geral[1]
            elif idade == 14:
                idade_geral[2] += idade_geral[2]
            elif idade == 15:
                idade_geral[3] += idade_geral[3]
            elif idade == 16:
                idade_geral[4] += idade_geral[4]
            elif idade == 17:
                idade_geral[5] += idade_geral[5]
            elif idade == 18:
                idade_geral[6] += idade_geral[6]
            elif idade >= 19:
                idade_geral[7] += idade_geral[7]
            
            # Raça (amarela, branca, indígena, parda, preta)
            raca = exame.aluno.raca
            if raca == 0:                # Amarela
                raca_geral[0] += raca_geral[0]
            elif raca == 1:              # Branca
                raca_geral[1] += raca_geral[1]
            elif raca == 2:              # Indígena
                raca_geral[2] += raca_geral[2]
            elif raca == 3:              # Parda
                raca_geral[3] += raca_geral[3]
            elif raca == 4:              # Preta
                raca_geral[4] += raca_geral[4]
            
            # Sexo (masculino, feminino, outro, sem resposta)
            sexo = exame.aluno.sexo
            if sexo == 0:               # Masculino
                sexo_geral[0] += sexo_geral[0]
            elif sexo == 1:             # Feminino
                sexo_geral[1] += sexo_geral[1]
            elif sexo == 2:             # Outro
                sexo_geral[2] += sexo_geral[2]
            elif sexo == 3:             # Prefiro não responder
                sexo_geral[3] += sexo_geral[3]
        
        context = {
            'pagina_estudo': True,
            'idade_geral': idade_geral,
            'idade_escolas': idade_escolas,
            'idade_territorios_saude': idade_territorios_saude,
            'idade_distritos_sanitarios': idade_distritos_sanitarios,
            'raca_geral': raca_geral,
            'raca_escolas': raca_escolas,
            'raca_territorios_saude': raca_territorios_saude,
            'raca_distritos_sanitarios': raca_distritos_sanitarios,
            'sexo_geral': sexo_geral,
            'sexo_escolas': sexo_escolas,
            'sexo_territorios_saude': sexo_territorios_saude,
            'sexo_distritos_sanitarios': sexo_distritos_sanitarios,
        }
        
        return render(self.request, 'estudo/estudo.html', context)
