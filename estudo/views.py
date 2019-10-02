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
        idade_geral = ['Geral', 0, 0, 0, 0, 0, 0, 0, 0]
        idade_escolas = [
            ['Escola municipal de T.I. Padre Josimo M. Tavares',    0, 0, 0, 0, 0, 0, 0, 0],
            ['Escola Municipal Beatriz Rodrigues da Silva',         0, 0, 0, 0, 0, 0, 0, 0],
            ['Escola municipal Mestre Pacífico S. Campos',          0, 0, 0, 0, 0, 0, 0, 0],
            ['Escola municipal Luiz Gonzaga',                       0, 0, 0, 0, 0, 0, 0, 0],
            ['Escola municipal de T.I. Monsenhor Pedro P. Piagem',  0, 0, 0, 0, 0, 0, 0, 0],
            ['Escola municipal de T.I. Daniel Batista',             0, 0, 0, 0, 0, 0, 0, 0],
            ['Escola municipal Anne Frank',                         0, 0, 0, 0, 0, 0, 0, 0],
            ['Escola municipal Henrique Talone Pinheiro',           0, 0, 0, 0, 0, 0, 0, 0],
            ['Escola municipal de T.I. Aprigio T. de Matos',        0, 0, 0, 0, 0, 0, 0, 0],
            ['Escola municipal de T.I. Vinícius de Moraes',         0, 0, 0, 0, 0, 0, 0, 0],
            ['Escola municipal Darcy Ribeiro',                      0, 0, 0, 0, 0, 0, 0, 0],
            ['Escola municipal Antônio G. de Carvalho Filho',       0, 0, 0, 0, 0, 0, 0, 0],
            ['Escola municipal Antônio Carlos Jobim',               0, 0, 0, 0, 0, 0, 0, 0],
            ['Escola municipal de T.I.Almirante Tamandare',         0, 0, 0, 0, 0, 0, 0, 0],
            ['Escola municipal de T.I. Anisio Spenola Teixeira',    0, 0, 0, 0, 0, 0, 0, 0],
            ['Escola municipal Thiago Barbosa',                     0, 0, 0, 0, 0, 0, 0, 0],
            ['Escola municipal Aurélio Buarque de Holanda',         0, 0, 0, 0, 0, 0, 0, 0],
            ['Escola municipal de T.I. Margarida Gonçalves',        0, 0, 0, 0, 0, 0, 0, 0],
            ['Escola municipal Professor Sávia F. Jacome',          0, 0, 0, 0, 0, 0, 0, 0],
            ['Escola municipal Jorge Amado',                        0, 0, 0, 0, 0, 0, 0, 0],
            ['Escola municipal de T.I. Caroline C. C. da Silva',    0, 0, 0, 0, 0, 0, 0, 0],
            ['Escola municipal Maria Rosa de Castro Sales',         0, 0, 0, 0, 0, 0, 0, 0],
            ['Escola municipal de T.I. Euridice F. de Mello',       0, 0, 0, 0, 0, 0, 0, 0],
            ['Escola municipal Maria Júlia Amorim Rodrigues',       0, 0, 0, 0, 0, 0, 0, 0],
            ['Escola municipal Crispim Pereira de Alencar',         0, 0, 0, 0, 0, 0, 0, 0],
            ['Escola municipal de T.I. Sueli Pereira A. Reche',     0, 0, 0, 0, 0, 0, 0, 0],
            ['Escola municipal de T.I. Luiz Nunes de Oliveira',     0, 0, 0, 0, 0, 0, 0, 0],
            ['Escola Municipal de Tempo Integral Marcos Freire',    0, 0, 0, 0, 0, 0, 0, 0],
            ['Escola municipal de T.I. João Beltrão',               0, 0, 0, 0, 0, 0, 0, 0],
        ]
        idade_territorios_saude = [
            ['Kanela',     0, 0, 0, 0, 0, 0, 0, 0],
            ['Apinajé',    0, 0, 0, 0, 0, 0, 0, 0],
            ['Xambioá',    0, 0, 0, 0, 0, 0, 0, 0],
            ['Krahô',      0, 0, 0, 0, 0, 0, 0, 0],
            ['Karajá',     0, 0, 0, 0, 0, 0, 0, 0],
            ['Javaé',      0, 0, 0, 0, 0, 0, 0, 0],
            ['Xerente',    0, 0, 0, 0, 0, 0, 0, 0],
            ['Panikararu', 0, 0, 0, 0, 0, 0, 0, 0],
        ]
        idade_macrorregioes = [
            ['Norte',      0, 0, 0, 0, 0, 0, 0, 0],
            ['Centro sul', 0, 0, 0, 0, 0, 0, 0, 0],
            ['Sul',        0, 0, 0, 0, 0, 0, 0, 0],
            ['Zona rural', 0, 0, 0, 0, 0, 0, 0, 0],
        ]
        
        raca_geral = ['Geral', 0, 0, 0, 0, 0]
        raca_escolas = [
            ['Escola municipal de T.I. Padre Josimo M. Tavares',    0, 0, 0, 0, 0],
            ['Escola Municipal Beatriz Rodrigues da Silva',         0, 0, 0, 0, 0],
            ['Escola municipal Mestre Pacífico S. Campos',          0, 0, 0, 0, 0],
            ['Escola municipal Luiz Gonzaga',                       0, 0, 0, 0, 0],
            ['Escola municipal de T.I. Monsenhor Pedro P. Piagem',  0, 0, 0, 0, 0],
            ['Escola municipal de T.I. Daniel Batista',             0, 0, 0, 0, 0],
            ['Escola municipal Anne Frank',                         0, 0, 0, 0, 0],
            ['Escola municipal Henrique Talone Pinheiro',           0, 0, 0, 0, 0],
            ['Escola municipal de T.I. Aprigio T. de Matos',        0, 0, 0, 0, 0],
            ['Escola municipal de T.I. Vinícius de Moraes',         0, 0, 0, 0, 0],
            ['Escola municipal Darcy Ribeiro',                      0, 0, 0, 0, 0],
            ['Escola municipal Antônio G. de Carvalho Filho',       0, 0, 0, 0, 0],
            ['Escola municipal Antônio Carlos Jobim',               0, 0, 0, 0, 0],
            ['Escola municipal de T.I.Almirante Tamandare',         0, 0, 0, 0, 0],
            ['Escola municipal de T.I. Anisio Spenola Teixeira',    0, 0, 0, 0, 0],
            ['Escola municipal Thiago Barbosa',                     0, 0, 0, 0, 0],
            ['Escola municipal Aurélio Buarque de Holanda',         0, 0, 0, 0, 0],
            ['Escola municipal de T.I. Margarida Gonçalves',        0, 0, 0, 0, 0],
            ['Escola municipal Professor Sávia F. Jacome',          0, 0, 0, 0, 0],
            ['Escola municipal Jorge Amado',                        0, 0, 0, 0, 0],
            ['Escola municipal de T.I. Caroline C. C. da Silva',    0, 0, 0, 0, 0],
            ['Escola municipal Maria Rosa de Castro Sales',         0, 0, 0, 0, 0],
            ['Escola municipal de T.I. Euridice F. de Mello',       0, 0, 0, 0, 0],
            ['Escola municipal Maria Júlia Amorim Rodrigues',       0, 0, 0, 0, 0],
            ['Escola municipal Crispim Pereira de Alencar',         0, 0, 0, 0, 0],
            ['Escola municipal de T.I. Sueli Pereira A. Reche',     0, 0, 0, 0, 0],
            ['Escola municipal de T.I. Luiz Nunes de Oliveira',     0, 0, 0, 0, 0],
            ['Escola Municipal de Tempo Integral Marcos Freire',    0, 0, 0, 0, 0],
            ['Escola municipal de T.I. João Beltrão',               0, 0, 0, 0, 0],
        ]
        raca_territorios_saude = [
            ['Kanela',     0, 0, 0, 0, 0],
            ['Apinajé',    0, 0, 0, 0, 0],
            ['Xambioá',    0, 0, 0, 0, 0],
            ['Krahô',      0, 0, 0, 0, 0],
            ['Karajá',     0, 0, 0, 0, 0],
            ['Javaé',      0, 0, 0, 0, 0],
            ['Xerente',    0, 0, 0, 0, 0],
            ['Panikararu', 0, 0, 0, 0, 0],
        ]
        raca_macrorregioes = [
            ['Norte',      0, 0, 0, 0, 0],
            ['Centro sul', 0, 0, 0, 0, 0],
            ['Sul',        0, 0, 0, 0, 0],
            ['Zona rural', 0, 0, 0, 0, 0],
        ]
        
        sexo_geral = ['Geral', 0, 0, 0, 0]
        sexo_escolas = [
            ['Escola municipal de T.I. Padre Josimo M. Tavares',    0, 0, 0, 0],
            ['Escola Municipal Beatriz Rodrigues da Silva',         0, 0, 0, 0],
            ['Escola municipal Mestre Pacífico S. Campos',          0, 0, 0, 0],
            ['Escola municipal Luiz Gonzaga',                       0, 0, 0, 0],
            ['Escola municipal de T.I. Monsenhor Pedro P. Piagem',  0, 0, 0, 0],
            ['Escola municipal de T.I. Daniel Batista',             0, 0, 0, 0],
            ['Escola municipal Anne Frank',                         0, 0, 0, 0],
            ['Escola municipal Henrique Talone Pinheiro',           0, 0, 0, 0],
            ['Escola municipal de T.I. Aprigio T. de Matos',        0, 0, 0, 0],
            ['Escola municipal de T.I. Vinícius de Moraes',         0, 0, 0, 0],
            ['Escola municipal Darcy Ribeiro',                      0, 0, 0, 0],
            ['Escola municipal Antônio G. de Carvalho Filho',       0, 0, 0, 0],
            ['Escola municipal Antônio Carlos Jobim',               0, 0, 0, 0],
            ['Escola municipal de T.I.Almirante Tamandare',         0, 0, 0, 0],
            ['Escola municipal de T.I. Anisio Spenola Teixeira',    0, 0, 0, 0],
            ['Escola municipal Thiago Barbosa',                     0, 0, 0, 0],
            ['Escola municipal Aurélio Buarque de Holanda',         0, 0, 0, 0],
            ['Escola municipal de T.I. Margarida Gonçalves',        0, 0, 0, 0],
            ['Escola municipal Professor Sávia F. Jacome',          0, 0, 0, 0],
            ['Escola municipal Jorge Amado',                        0, 0, 0, 0],
            ['Escola municipal de T.I. Caroline C. C. da Silva',    0, 0, 0, 0],
            ['Escola municipal Maria Rosa de Castro Sales',         0, 0, 0, 0],
            ['Escola municipal de T.I. Euridice F. de Mello',       0, 0, 0, 0],
            ['Escola municipal Maria Júlia Amorim Rodrigues',       0, 0, 0, 0],
            ['Escola municipal Crispim Pereira de Alencar',         0, 0, 0, 0],
            ['Escola municipal de T.I. Sueli Pereira A. Reche',     0, 0, 0, 0],
            ['Escola municipal de T.I. Luiz Nunes de Oliveira',     0, 0, 0, 0],
            ['Escola Municipal de Tempo Integral Marcos Freire',    0, 0, 0, 0],
            ['Escola municipal de T.I. João Beltrão',               0, 0, 0, 0],
        ]
        sexo_territorios_saude = [
            ['Kanela',     0, 0, 0, 0],
            ['Apinajé',    0, 0, 0, 0],
            ['Xambioá',    0, 0, 0, 0],
            ['Krahô',      0, 0, 0, 0],
            ['Karajá',     0, 0, 0, 0],
            ['Javaé',      0, 0, 0, 0],
            ['Xerente',    0, 0, 0, 0],
            ['Panikararu', 0, 0, 0, 0],
        ]
        sexo_macrorregioes = [
            ['Norte',      0, 0, 0, 0],
            ['Centro sul', 0, 0, 0, 0],
            ['Sul',        0, 0, 0, 0],
            ['Zona rural', 0, 0, 0, 0],
        ]
        
        # Questões sobre CPO-D (nome, dentes considerados, total de indivíduos)
        cpod_geral = ['Geral', 0, 0]
        cpod_escolas = [
            ['Escola municipal de T.I. Padre Josimo M. Tavares',    0, 0],
            ['Escola Municipal Beatriz Rodrigues da Silva',         0, 0],
            ['Escola municipal Mestre Pacífico S. Campos',          0, 0],
            ['Escola municipal Luiz Gonzaga',                       0, 0],
            ['Escola municipal de T.I. Monsenhor Pedro P. Piagem',  0, 0],
            ['Escola municipal de T.I. Daniel Batista',             0, 0],
            ['Escola municipal Anne Frank',                         0, 0],
            ['Escola municipal Henrique Talone Pinheiro',           0, 0],
            ['Escola municipal de T.I. Aprigio T. de Matos',        0, 0],
            ['Escola municipal de T.I. Vinícius de Moraes',         0, 0],
            ['Escola municipal Darcy Ribeiro',                      0, 0],
            ['Escola municipal Antônio G. de Carvalho Filho',       0, 0],
            ['Escola municipal Antônio Carlos Jobim',               0, 0],
            ['Escola municipal de T.I.Almirante Tamandare',         0, 0],
            ['Escola municipal de T.I. Anisio Spenola Teixeira',    0, 0],
            ['Escola municipal Thiago Barbosa',                     0, 0],
            ['Escola municipal Aurélio Buarque de Holanda',         0, 0],
            ['Escola municipal de T.I. Margarida Gonçalves',        0, 0],
            ['Escola municipal Professor Sávia F. Jacome',          0, 0],
            ['Escola municipal Jorge Amado',                        0, 0],
            ['Escola municipal de T.I. Caroline C. C. da Silva',    0, 0],
            ['Escola municipal Maria Rosa de Castro Sales',         0, 0],
            ['Escola municipal de T.I. Euridice F. de Mello',       0, 0],
            ['Escola municipal Maria Júlia Amorim Rodrigues',       0, 0],
            ['Escola municipal Crispim Pereira de Alencar',         0, 0],
            ['Escola municipal de T.I. Sueli Pereira A. Reche',     0, 0],
            ['Escola municipal de T.I. Luiz Nunes de Oliveira',     0, 0],
            ['Escola Municipal de Tempo Integral Marcos Freire',    0, 0],
            ['Escola municipal de T.I. João Beltrão',               0, 0],
        ]
        cpod_territorios_saude = [
            ['Kanela',     0, 0],
            ['Apinajé',    0, 0],
            ['Xambioá',    0, 0],
            ['Krahô',      0, 0],
            ['Karajá',     0, 0],
            ['Javaé',      0, 0],
            ['Xerente',    0, 0],
            ['Panikararu', 0, 0],
        ]
        cpod_macrorregioes = [
            ['Norte',      0, 0],
            ['Centro sul', 0, 0],
            ['Sul',        0, 0],
            ['Zona rural', 0, 0],
        ]
        
        for exame in exames:
            # Idade (12, 13, 14, 15, 16, 17, 18 e 19)
            idade = int((datetime.date.today() - exame.aluno.nascimento).days / 365.25)
            coluna = 0
            if idade != None:
                if idade <= 12:
                    coluna = 1
                elif idade == 13:
                    coluna = 2
                elif idade == 14:
                    coluna = 3
                elif idade == 15:
                    coluna = 4
                elif idade == 16:
                    coluna = 5
                elif idade == 17:
                    coluna = 6
                elif idade == 18:
                    coluna = 7
                elif idade >= 19:
                    coluna = 8
            
                idade_geral[coluna] += 1
                if exame.aluno.escola.id == 4:    idade_escolas[0][coluna] += 1; idade_macrorregioes[0][coluna] += 1; idade_territorios_saude[0][coluna] += 1
                elif exame.aluno.escola.id == 65: idade_escolas[1][coluna] += 1; idade_macrorregioes[0][coluna] += 1; idade_territorios_saude[0][coluna] += 1
                elif exame.aluno.escola.id == 2:  idade_escolas[2][coluna] += 1; idade_macrorregioes[0][coluna] += 1; idade_territorios_saude[0][coluna] += 1
                elif exame.aluno.escola.id == 1:  idade_escolas[3][coluna] += 1; idade_macrorregioes[0][coluna] += 1; idade_territorios_saude[0][coluna] += 1
                elif exame.aluno.escola.id == 55: idade_escolas[4][coluna] += 1; idade_macrorregioes[0][coluna] += 1; idade_territorios_saude[1][coluna] += 1
                elif exame.aluno.escola.id == 48: idade_escolas[5][coluna] += 1; idade_macrorregioes[0][coluna] += 1; idade_territorios_saude[1][coluna] += 1
                elif exame.aluno.escola.id == 5:  idade_escolas[6][coluna] += 1; idade_macrorregioes[0][coluna] += 1; idade_territorios_saude[1][coluna] += 1
                elif exame.aluno.escola.id == 6:  idade_escolas[7][coluna] += 1; idade_macrorregioes[1][coluna] += 1; idade_territorios_saude[1][coluna] += 1
                elif exame.aluno.escola.id == 46: idade_escolas[8][coluna] += 1; idade_macrorregioes[0][coluna] += 1; idade_territorios_saude[1][coluna] += 1
                elif exame.aluno.escola.id == 59: idade_escolas[9][coluna] += 1; idade_macrorregioes[1][coluna] += 1; idade_territorios_saude[2][coluna] += 1
                elif exame.aluno.escola.id == 49: idade_escolas[10][coluna] += 1; idade_macrorregioes[1][coluna] += 1; idade_territorios_saude[2][coluna] += 1
                elif exame.aluno.escola.id == 44: idade_escolas[11][coluna] += 1; idade_macrorregioes[1][coluna] += 1; idade_territorios_saude[3][coluna] += 1
                elif exame.aluno.escola.id == 7:  idade_escolas[12][coluna] += 1; idade_macrorregioes[1][coluna] += 1; idade_territorios_saude[3][coluna] += 1
                elif exame.aluno.escola.id == 62: idade_escolas[13][coluna] += 1; idade_macrorregioes[1][coluna] += 1; idade_territorios_saude[3][coluna] += 1
                elif exame.aluno.escola.id == 63: idade_escolas[14][coluna] += 1; idade_macrorregioes[2][coluna] += 1; idade_territorios_saude[4][coluna] += 1
                elif exame.aluno.escola.id == 57: idade_escolas[15][coluna] += 1; idade_macrorregioes[2][coluna] += 1; idade_territorios_saude[4][coluna] += 1
                elif exame.aluno.escola.id == 45: idade_escolas[16][coluna] += 1; idade_macrorregioes[2][coluna] += 1; idade_territorios_saude[4][coluna] += 1
                elif exame.aluno.escola.id == 8:  idade_escolas[17][coluna] += 1; idade_macrorregioes[2][coluna] += 1; idade_territorios_saude[4][coluna] += 1
                elif exame.aluno.escola.id == 60: idade_escolas[18][coluna] += 1; idade_macrorregioes[2][coluna] += 1; idade_territorios_saude[5][coluna] += 1
                elif exame.aluno.escola.id == 50: idade_escolas[19][coluna] += 1; idade_macrorregioes[2][coluna] += 1; idade_territorios_saude[5][coluna] += 1
                elif exame.aluno.escola.id == 61: idade_escolas[20][coluna] += 1; idade_macrorregioes[2][coluna] += 1; idade_territorios_saude[5][coluna] += 1
                elif exame.aluno.escola.id == 54: idade_escolas[21][coluna] += 1; idade_macrorregioes[2][coluna] += 1; idade_territorios_saude[5][coluna] += 1
                elif exame.aluno.escola.id == 58: idade_escolas[22][coluna] += 1; idade_macrorregioes[2][coluna] += 1; idade_territorios_saude[6][coluna] += 1
                elif exame.aluno.escola.id == 53: idade_escolas[23][coluna] += 1; idade_macrorregioes[2][coluna] += 1; idade_territorios_saude[6][coluna] += 1
                elif exame.aluno.escola.id == 47: idade_escolas[24][coluna] += 1; idade_macrorregioes[3][coluna] += 1; idade_territorios_saude[7][coluna] += 1
                elif exame.aluno.escola.id == 56: idade_escolas[25][coluna] += 1; idade_macrorregioes[3][coluna] += 1; idade_territorios_saude[7][coluna] += 1
                elif exame.aluno.escola.id == 52: idade_escolas[26][coluna] += 1; idade_macrorregioes[3][coluna] += 1; idade_territorios_saude[7][coluna] += 1
                elif exame.aluno.escola.id == 64: idade_escolas[27][coluna] += 1; idade_macrorregioes[3][coluna] += 1; idade_territorios_saude[7][coluna] += 1
                elif exame.aluno.escola.id == 51: idade_escolas[28][coluna] += 1; idade_macrorregioes[3][coluna] += 1; idade_territorios_saude[7][coluna] += 1
            
            # Raça (amarela, branca, indígena, parda, preta)
            raca = exame.aluno.raca
            if raca != None:
                if raca == '0':                # Amarela
                    coluna = 1
                elif raca == '1':              # Branca
                    coluna = 2
                elif raca == '2':              # Indígena
                    coluna = 3
                elif raca == '3':              # Parda
                    coluna = 4
                elif raca == '4':              # Preta
                    coluna = 5
                
                raca_geral[coluna] += 1
                if exame.aluno.escola.id == 4:    raca_escolas[0][coluna] += 1; raca_macrorregioes[0][coluna] += 1; raca_territorios_saude[0][coluna] += 1
                elif exame.aluno.escola.id == 65: raca_escolas[1][coluna] += 1; raca_macrorregioes[0][coluna] += 1; raca_territorios_saude[0][coluna] += 1
                elif exame.aluno.escola.id == 2:  raca_escolas[2][coluna] += 1; raca_macrorregioes[0][coluna] += 1; raca_territorios_saude[0][coluna] += 1
                elif exame.aluno.escola.id == 1:  raca_escolas[3][coluna] += 1; raca_macrorregioes[0][coluna] += 1; raca_territorios_saude[0][coluna] += 1
                elif exame.aluno.escola.id == 55: raca_escolas[4][coluna] += 1; raca_macrorregioes[0][coluna] += 1; raca_territorios_saude[1][coluna] += 1
                elif exame.aluno.escola.id == 48: raca_escolas[5][coluna] += 1; raca_macrorregioes[0][coluna] += 1; raca_territorios_saude[1][coluna] += 1
                elif exame.aluno.escola.id == 5:  raca_escolas[6][coluna] += 1; raca_macrorregioes[0][coluna] += 1; raca_territorios_saude[1][coluna] += 1
                elif exame.aluno.escola.id == 6:  raca_escolas[7][coluna] += 1; raca_macrorregioes[1][coluna] += 1; raca_territorios_saude[1][coluna] += 1
                elif exame.aluno.escola.id == 46: raca_escolas[8][coluna] += 1; raca_macrorregioes[0][coluna] += 1; raca_territorios_saude[1][coluna] += 1
                elif exame.aluno.escola.id == 59: raca_escolas[9][coluna] += 1; raca_macrorregioes[1][coluna] += 1; raca_territorios_saude[2][coluna] += 1
                elif exame.aluno.escola.id == 49: raca_escolas[10][coluna] += 1; raca_macrorregioes[1][coluna] += 1; raca_territorios_saude[2][coluna] += 1
                elif exame.aluno.escola.id == 44: raca_escolas[11][coluna] += 1; raca_macrorregioes[1][coluna] += 1; raca_territorios_saude[3][coluna] += 1
                elif exame.aluno.escola.id == 7:  raca_escolas[12][coluna] += 1; raca_macrorregioes[1][coluna] += 1; raca_territorios_saude[3][coluna] += 1
                elif exame.aluno.escola.id == 62: raca_escolas[13][coluna] += 1; raca_macrorregioes[1][coluna] += 1; raca_territorios_saude[3][coluna] += 1
                elif exame.aluno.escola.id == 63: raca_escolas[14][coluna] += 1; raca_macrorregioes[2][coluna] += 1; raca_territorios_saude[4][coluna] += 1
                elif exame.aluno.escola.id == 57: raca_escolas[15][coluna] += 1; raca_macrorregioes[2][coluna] += 1; raca_territorios_saude[4][coluna] += 1
                elif exame.aluno.escola.id == 45: raca_escolas[16][coluna] += 1; raca_macrorregioes[2][coluna] += 1; raca_territorios_saude[4][coluna] += 1
                elif exame.aluno.escola.id == 8:  raca_escolas[17][coluna] += 1; raca_macrorregioes[2][coluna] += 1; raca_territorios_saude[4][coluna] += 1
                elif exame.aluno.escola.id == 60: raca_escolas[18][coluna] += 1; raca_macrorregioes[2][coluna] += 1; raca_territorios_saude[5][coluna] += 1
                elif exame.aluno.escola.id == 50: raca_escolas[19][coluna] += 1; raca_macrorregioes[2][coluna] += 1; raca_territorios_saude[5][coluna] += 1
                elif exame.aluno.escola.id == 61: raca_escolas[20][coluna] += 1; raca_macrorregioes[2][coluna] += 1; raca_territorios_saude[5][coluna] += 1
                elif exame.aluno.escola.id == 54: raca_escolas[21][coluna] += 1; raca_macrorregioes[2][coluna] += 1; raca_territorios_saude[5][coluna] += 1
                elif exame.aluno.escola.id == 58: raca_escolas[22][coluna] += 1; raca_macrorregioes[2][coluna] += 1; raca_territorios_saude[6][coluna] += 1
                elif exame.aluno.escola.id == 53: raca_escolas[23][coluna] += 1; raca_macrorregioes[2][coluna] += 1; raca_territorios_saude[6][coluna] += 1
                elif exame.aluno.escola.id == 47: raca_escolas[24][coluna] += 1; raca_macrorregioes[3][coluna] += 1; raca_territorios_saude[7][coluna] += 1
                elif exame.aluno.escola.id == 56: raca_escolas[25][coluna] += 1; raca_macrorregioes[3][coluna] += 1; raca_territorios_saude[7][coluna] += 1
                elif exame.aluno.escola.id == 52: raca_escolas[26][coluna] += 1; raca_macrorregioes[3][coluna] += 1; raca_territorios_saude[7][coluna] += 1
                elif exame.aluno.escola.id == 64: raca_escolas[27][coluna] += 1; raca_macrorregioes[3][coluna] += 1; raca_territorios_saude[7][coluna] += 1
                elif exame.aluno.escola.id == 51: raca_escolas[28][coluna] += 1; raca_macrorregioes[3][coluna] += 1; raca_territorios_saude[7][coluna] += 1
            
            # Sexo (masculino, feminino, outro, sem resposta)
            sexo = exame.aluno.sexo
            if sexo != None:
                if sexo == '0':               # Masculino
                    coluna = 1
                elif sexo == '1':             # Feminino
                    coluna = 2
                elif sexo == '2':             # Outro
                    coluna = 3
                elif sexo == '3':             # Prefiro não responder
                    coluna = 4
            
                sexo_geral[coluna] += 1
                if exame.aluno.escola.id == 4:    sexo_escolas[0][coluna] += 1; sexo_macrorregioes[0][coluna] += 1; sexo_territorios_saude[0][coluna] += 1
                elif exame.aluno.escola.id == 65: sexo_escolas[1][coluna] += 1; sexo_macrorregioes[0][coluna] += 1; sexo_territorios_saude[0][coluna] += 1
                elif exame.aluno.escola.id == 2:  sexo_escolas[2][coluna] += 1; sexo_macrorregioes[0][coluna] += 1; sexo_territorios_saude[0][coluna] += 1
                elif exame.aluno.escola.id == 1:  sexo_escolas[3][coluna] += 1; sexo_macrorregioes[0][coluna] += 1; sexo_territorios_saude[0][coluna] += 1
                elif exame.aluno.escola.id == 55: sexo_escolas[4][coluna] += 1; sexo_macrorregioes[0][coluna] += 1; sexo_territorios_saude[1][coluna] += 1
                elif exame.aluno.escola.id == 48: sexo_escolas[5][coluna] += 1; sexo_macrorregioes[0][coluna] += 1; sexo_territorios_saude[1][coluna] += 1
                elif exame.aluno.escola.id == 5:  sexo_escolas[6][coluna] += 1; sexo_macrorregioes[0][coluna] += 1; sexo_territorios_saude[1][coluna] += 1
                elif exame.aluno.escola.id == 6:  sexo_escolas[7][coluna] += 1; sexo_macrorregioes[1][coluna] += 1; sexo_territorios_saude[1][coluna] += 1
                elif exame.aluno.escola.id == 46: sexo_escolas[8][coluna] += 1; sexo_macrorregioes[0][coluna] += 1; sexo_territorios_saude[1][coluna] += 1
                elif exame.aluno.escola.id == 59: sexo_escolas[9][coluna] += 1; sexo_macrorregioes[1][coluna] += 1; sexo_territorios_saude[2][coluna] += 1
                elif exame.aluno.escola.id == 49: sexo_escolas[10][coluna] += 1; sexo_macrorregioes[1][coluna] += 1; sexo_territorios_saude[2][coluna] += 1
                elif exame.aluno.escola.id == 44: sexo_escolas[11][coluna] += 1; sexo_macrorregioes[1][coluna] += 1; sexo_territorios_saude[3][coluna] += 1
                elif exame.aluno.escola.id == 7:  sexo_escolas[12][coluna] += 1; sexo_macrorregioes[1][coluna] += 1; sexo_territorios_saude[3][coluna] += 1
                elif exame.aluno.escola.id == 62: sexo_escolas[13][coluna] += 1; sexo_macrorregioes[1][coluna] += 1; sexo_territorios_saude[3][coluna] += 1
                elif exame.aluno.escola.id == 63: sexo_escolas[14][coluna] += 1; sexo_macrorregioes[2][coluna] += 1; sexo_territorios_saude[4][coluna] += 1
                elif exame.aluno.escola.id == 57: sexo_escolas[15][coluna] += 1; sexo_macrorregioes[2][coluna] += 1; sexo_territorios_saude[4][coluna] += 1
                elif exame.aluno.escola.id == 45: sexo_escolas[16][coluna] += 1; sexo_macrorregioes[2][coluna] += 1; sexo_territorios_saude[4][coluna] += 1
                elif exame.aluno.escola.id == 8:  sexo_escolas[17][coluna] += 1; sexo_macrorregioes[2][coluna] += 1; sexo_territorios_saude[4][coluna] += 1
                elif exame.aluno.escola.id == 60: sexo_escolas[18][coluna] += 1; sexo_macrorregioes[2][coluna] += 1; sexo_territorios_saude[5][coluna] += 1
                elif exame.aluno.escola.id == 50: sexo_escolas[19][coluna] += 1; sexo_macrorregioes[2][coluna] += 1; sexo_territorios_saude[5][coluna] += 1
                elif exame.aluno.escola.id == 61: sexo_escolas[20][coluna] += 1; sexo_macrorregioes[2][coluna] += 1; sexo_territorios_saude[5][coluna] += 1
                elif exame.aluno.escola.id == 54: sexo_escolas[21][coluna] += 1; sexo_macrorregioes[2][coluna] += 1; sexo_territorios_saude[5][coluna] += 1
                elif exame.aluno.escola.id == 58: sexo_escolas[22][coluna] += 1; sexo_macrorregioes[2][coluna] += 1; sexo_territorios_saude[6][coluna] += 1
                elif exame.aluno.escola.id == 53: sexo_escolas[23][coluna] += 1; sexo_macrorregioes[2][coluna] += 1; sexo_territorios_saude[6][coluna] += 1
                elif exame.aluno.escola.id == 47: sexo_escolas[24][coluna] += 1; sexo_macrorregioes[3][coluna] += 1; sexo_territorios_saude[7][coluna] += 1
                elif exame.aluno.escola.id == 56: sexo_escolas[25][coluna] += 1; sexo_macrorregioes[3][coluna] += 1; sexo_territorios_saude[7][coluna] += 1
                elif exame.aluno.escola.id == 52: sexo_escolas[26][coluna] += 1; sexo_macrorregioes[3][coluna] += 1; sexo_territorios_saude[7][coluna] += 1
                elif exame.aluno.escola.id == 64: sexo_escolas[27][coluna] += 1; sexo_macrorregioes[3][coluna] += 1; sexo_territorios_saude[7][coluna] += 1
                elif exame.aluno.escola.id == 51: sexo_escolas[28][coluna] += 1; sexo_macrorregioes[3][coluna] += 1; sexo_territorios_saude[7][coluna] += 1
            
            # '1 - Cariado'; '4 - Perdido devido à cárie'; '5 - Perdido por outras razões'; '2 - Restaurado mas com cárie'; '3 - Restaurado e sem cárie'.
            # '6 - Extração'.
            escola = 0
            macrorregiao = 0
            territorio_saude = 0
            
            if exame.aluno.escola.id == 4: escola = 0; macrorregiao = 0; territorio_saude = 0
            elif exame.aluno.escola.id == 65: escola = 1; macrorregiao = 0; territorio_saude = 0
            elif exame.aluno.escola.id == 2: escola = 2; macrorregiao = 0; territorio_saude = 0
            elif exame.aluno.escola.id == 1: escola = 3; macrorregiao = 0; territorio_saude = 0
            elif exame.aluno.escola.id == 55: escola = 4; macrorregiao = 0; territorio_saude = 1
            elif exame.aluno.escola.id == 48: escola = 5; macrorregiao = 0; territorio_saude = 1
            elif exame.aluno.escola.id == 5: escola = 6; macrorregiao = 0; territorio_saude = 1
            elif exame.aluno.escola.id == 6: escola = 7; macrorregiao = 1; territorio_saude = 1
            elif exame.aluno.escola.id == 46: escola = 8; macrorregiao = 0; territorio_saude = 1
            elif exame.aluno.escola.id == 59: escola = 9; macrorregiao = 1; territorio_saude = 2
            elif exame.aluno.escola.id == 49: escola = 10; macrorregiao = 1; territorio_saude = 2
            elif exame.aluno.escola.id == 44: escola = 11; macrorregiao = 1; territorio_saude = 3
            elif exame.aluno.escola.id == 7: escola = 12; macrorregiao = 1; territorio_saude = 3
            elif exame.aluno.escola.id == 62: escola = 13; macrorregiao = 1; territorio_saude = 3
            elif exame.aluno.escola.id == 63: escola = 14; macrorregiao = 2; territorio_saude = 4
            elif exame.aluno.escola.id == 57: escola = 15; macrorregiao = 2; territorio_saude = 4
            elif exame.aluno.escola.id == 45: escola = 16; macrorregiao = 2; territorio_saude = 4
            elif exame.aluno.escola.id == 8: escola = 17; macrorregiao = 2; territorio_saude = 4
            elif exame.aluno.escola.id == 60: escola = 18; macrorregiao = 2; territorio_saude = 5
            elif exame.aluno.escola.id == 50: escola = 19; macrorregiao = 2; territorio_saude = 5
            elif exame.aluno.escola.id == 61: escola = 20; macrorregiao = 2; territorio_saude = 5
            elif exame.aluno.escola.id == 54: escola = 21; macrorregiao = 2; territorio_saude = 5
            elif exame.aluno.escola.id == 58: escola = 22; macrorregiao = 2; territorio_saude = 6
            elif exame.aluno.escola.id == 53: escola = 23; macrorregiao = 2; territorio_saude = 6
            elif exame.aluno.escola.id == 47: escola = 24; macrorregiao = 3; territorio_saude = 7
            elif exame.aluno.escola.id == 56: escola = 25; macrorregiao = 3; territorio_saude = 7
            elif exame.aluno.escola.id == 52: escola = 26; macrorregiao = 3; territorio_saude = 7
            elif exame.aluno.escola.id == 64: escola = 27; macrorregiao = 3; territorio_saude = 7
            elif exame.aluno.escola.id == 51: escola = 28; macrorregiao = 3; territorio_saude = 7
            
            if exame.carie_coroa_18 == '1': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_coroa_17 == '1': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_coroa_16 == '1': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_coroa_15 == '1': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_coroa_14 == '1': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_coroa_13 == '1': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_coroa_12 == '1': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_coroa_11 == '1': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_coroa_21 == '1': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_coroa_22 == '1': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_coroa_23 == '1': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_coroa_24 == '1': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_coroa_25 == '1': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_coroa_26 == '1': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_coroa_27 == '1': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_coroa_28 == '1': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_coroa_38 == '1': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_coroa_37 == '1': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_coroa_36 == '1': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_coroa_35 == '1': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_coroa_34 == '1': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_coroa_33 == '1': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_coroa_32 == '1': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_coroa_31 == '1': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_coroa_41 == '1': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_coroa_42 == '1': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_coroa_43 == '1': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_coroa_44 == '1': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_coroa_45 == '1': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_coroa_46 == '1': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_coroa_47 == '1': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_coroa_48 == '1': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            
            if exame.carie_coroa_18 == '2': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_coroa_17 == '2': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_coroa_16 == '2': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_coroa_15 == '2': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_coroa_14 == '2': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_coroa_13 == '2': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_coroa_12 == '2': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_coroa_11 == '2': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_coroa_21 == '2': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_coroa_22 == '2': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_coroa_23 == '2': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_coroa_24 == '2': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_coroa_25 == '2': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_coroa_26 == '2': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_coroa_27 == '2': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_coroa_28 == '2': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_coroa_38 == '2': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_coroa_37 == '2': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_coroa_36 == '2': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_coroa_35 == '2': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_coroa_34 == '2': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_coroa_33 == '2': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_coroa_32 == '2': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_coroa_31 == '2': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_coroa_41 == '2': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_coroa_42 == '2': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_coroa_43 == '2': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_coroa_44 == '2': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_coroa_45 == '2': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_coroa_46 == '2': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_coroa_47 == '2': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_coroa_48 == '2': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            
            if exame.carie_coroa_18 == '3': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_coroa_17 == '3': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_coroa_16 == '3': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_coroa_15 == '3': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_coroa_14 == '3': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_coroa_13 == '3': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_coroa_12 == '3': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_coroa_11 == '3': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_coroa_21 == '3': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_coroa_22 == '3': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_coroa_23 == '3': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_coroa_24 == '3': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_coroa_25 == '3': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_coroa_26 == '3': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_coroa_27 == '3': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_coroa_28 == '3': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_coroa_38 == '3': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_coroa_37 == '3': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_coroa_36 == '3': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_coroa_35 == '3': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_coroa_34 == '3': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_coroa_33 == '3': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_coroa_32 == '3': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_coroa_31 == '3': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_coroa_41 == '3': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_coroa_42 == '3': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_coroa_43 == '3': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_coroa_44 == '3': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_coroa_45 == '3': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_coroa_46 == '3': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_coroa_47 == '3': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_coroa_48 == '3': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            
            if exame.carie_coroa_18 == '4': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_coroa_17 == '4': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_coroa_16 == '4': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_coroa_15 == '4': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_coroa_14 == '4': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_coroa_13 == '4': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_coroa_12 == '4': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_coroa_11 == '4': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_coroa_21 == '4': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_coroa_22 == '4': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_coroa_23 == '4': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_coroa_24 == '4': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_coroa_25 == '4': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_coroa_26 == '4': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_coroa_27 == '4': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_coroa_28 == '4': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_coroa_38 == '4': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_coroa_37 == '4': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_coroa_36 == '4': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_coroa_35 == '4': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_coroa_34 == '4': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_coroa_33 == '4': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_coroa_32 == '4': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_coroa_31 == '4': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_coroa_41 == '4': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_coroa_42 == '4': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_coroa_43 == '4': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_coroa_44 == '4': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_coroa_45 == '4': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_coroa_46 == '4': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_coroa_47 == '4': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_coroa_48 == '4': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            
            if exame.carie_coroa_18 == '5': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_coroa_17 == '5': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_coroa_16 == '5': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_coroa_15 == '5': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_coroa_14 == '5': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_coroa_13 == '5': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_coroa_12 == '5': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_coroa_11 == '5': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_coroa_21 == '5': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_coroa_22 == '5': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_coroa_23 == '5': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_coroa_24 == '5': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_coroa_25 == '5': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_coroa_26 == '5': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_coroa_27 == '5': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_coroa_28 == '5': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_coroa_38 == '5': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_coroa_37 == '5': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_coroa_36 == '5': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_coroa_35 == '5': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_coroa_34 == '5': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_coroa_33 == '5': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_coroa_32 == '5': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_coroa_31 == '5': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_coroa_41 == '5': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_coroa_42 == '5': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_coroa_43 == '5': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_coroa_44 == '5': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_coroa_45 == '5': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_coroa_46 == '5': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_coroa_47 == '5': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_coroa_48 == '5': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            
            if exame.carie_tratamento_18 == '6': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_tratamento_17 == '6': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_tratamento_16 == '6': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_tratamento_15 == '6': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_tratamento_14 == '6': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_tratamento_13 == '6': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_tratamento_12 == '6': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_tratamento_11 == '6': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_tratamento_21 == '6': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_tratamento_22 == '6': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_tratamento_23 == '6': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_tratamento_24 == '6': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_tratamento_25 == '6': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_tratamento_26 == '6': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_tratamento_27 == '6': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_tratamento_28 == '6': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_tratamento_38 == '6': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_tratamento_37 == '6': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_tratamento_36 == '6': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_tratamento_35 == '6': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_tratamento_34 == '6': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_tratamento_33 == '6': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_tratamento_32 == '6': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_tratamento_31 == '6': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_tratamento_41 == '6': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_tratamento_42 == '6': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_tratamento_43 == '6': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_tratamento_44 == '6': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_tratamento_45 == '6': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_tratamento_46 == '6': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_tratamento_47 == '6': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            if exame.carie_tratamento_48 == '6': cpod_geral[1] += 1; cpod_escolas[escola][1] += 1; cpod_macrorregioes[macrorregiao][1] += 1; cpod_territorios_saude[territorio_saude][1] += 1
            
            cpod_geral[2] += 1
            cpod_escolas[escola][2] += 1
            cpod_macrorregioes[macrorregiao][2] += 1
            cpod_territorios_saude[territorio_saude][2] += 1
        
        if cpod_geral[2] != 0:
            cpod_geral[1] /= cpod_geral[2]
        
        for escola in cpod_escolas:
            if escola[2] != 0:
                escola[1] /= escola[2]
        
        for macrorregiao in cpod_macrorregioes:
            if macrorregiao[2] != 0:
                macrorregiao[1] /= macrorregiao[2]
        
        for territorio_saude in cpod_territorios_saude:
            if territorio_saude[2] != 0:
                territorio_saude[1] /= territorio_saude[2]
        
        context = {
            'pagina_estudo': True,
            
            'idade_geral': idade_geral,
            'idade_escolas': idade_escolas,
            'idade_territorios_saude': idade_territorios_saude,
            'idade_macrorregioes': idade_macrorregioes,
            
            'raca_geral': raca_geral,
            'raca_escolas': raca_escolas,
            'raca_territorios_saude': raca_territorios_saude,
            'raca_macrorregioes': raca_macrorregioes,
            
            'sexo_geral': sexo_geral,
            'sexo_escolas': sexo_escolas,
            'sexo_territorios_saude': sexo_territorios_saude,
            'sexo_macrorregioes': sexo_macrorregioes,
            
            'cpod_geral': cpod_geral,
            'cpod_escolas': cpod_escolas,
            'cpod_territorios_saude': cpod_territorios_saude,
            'cpod_macrorregioes': cpod_macrorregioes,
        }
        
        return render(self.request, 'estudo/estudo.html', context)
