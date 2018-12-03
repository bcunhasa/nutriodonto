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
        
        context = {
            'pagina_graficos': True,
            'pagina_graficos_alunos': True,
            'alunos': alunos,
            'aluno_por_escola': aluno_por_escola,
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
        
        context = {
            'pagina_graficos': True,
            'pagina_graficos_diretores': True,
            'diretores': diretores,
        }
        
        return render(self.request, 'administracao/graficos_diretores.html', context)


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
