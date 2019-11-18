from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import render
from django.views import View

import csv

from administracao.models import *
from administracao.const import *


class LoginRequired(LoginRequiredMixin):
    """Configurações para o login"""
    login_url = 'administracao/login/'
    redirect_field_name = 'next'


class ExportacaoView(LoginRequired, View):
    """Permite a exportacao de dados do banco"""
    
    def get(self, request):
        context = {
            'pagina_exportacao': True,
        }
        return render(self.request, 'exportacao/exportacao.html', context)


class DownloadCompletoView(LoginRequired, View):
    """Gera e envia o arquivo csv para a base completa"""
    
    def get(self, request):
        alunos = Aluno.objects.order_by('id')
        
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="base.csv"'

        writer = csv.writer(response, delimiter=';')
        writer.writerow(['campanha.nome', 'acao.nome', 'escola.id', 'escola.nome', 'escola.latitude', 'escola.longitude', 'aluno.numero_identificacao', 'aluno.periodo', 'aluno.turma', 'aluno.nascimento', 'aluno.sexo', 'aluno.raca', 'diretor.data', 'diretor.questao_1', 'diretor.questao_2', 'diretor.questao_3', 'diretor.questao_4', 'diretor.questao_5', 'diretor.questao_6', 'diretor.questao_7', 'diretor.questao_8', 'diretor.questao_9', 'diretor.questao_10', 'diretor.questao_11', 'diretor.questao_12', 'diretor.questao_13', 'diretor.questao_14', 'diretor.questao_15', 'diretor.questao_16', 'diretor.questao_17', 'diretor.questao_18', 'diretor.questao_19', 'diretor.questao_20', 'diretor.questao_21', 'diretor.questao_22', 'diretor.questao_23', 'diretor.questao_24', 'diretor.questao_25', 'diretor.questao_26', 'diretor.questao_27', 'diretor.questao_28', 'diretor.questao_29', 'diretor.questao_30', 'diretor.questao_31', 'diretor.questao_32', 'diretor.questao_33', 'diretor.questao_34', 'diretor.questao_35', 'diretor.questao_36', 'diretor.questao_37', 'diretor.questao_38', 'diretor.questao_39', 'diretor.questao_40', 'diretor.questao_41', 'diretor.questao_42', 'diretor.questao_43', 'diretor.questao_44', 'diretor.questao_45', 'diretor.questao_46', 'diretor.questao_47', 'diretor.questao_48', 'diretor.questao_49', 'diretor.questao_50', 'diretor.questao_51', 'diretor.questao_52', 'diretor.questao_53', 'diretor.questao_54', 'diretor.questao_55', 'diretor.questao_56', 'diretor.questao_57', 'diretor.questao_58', 'diretor.questao_59', 'diretor.questao_60', 'diretor.questao_61', 'diretor.questao_62', 'diretor.questao_63', 'diretor.questao_64', 'diretor.questao_65', 'diretor.questao_66', 'diretor.questao_67', 'diretor.questao_68', 'diretor.questao_69', 'diretor.questao_70', 'diretor.questao_71', 'diretor.questao_72', 'diretor.questao_73', 'diretor.questao_74', 'diretor.questao_75', 'diretor.questao_76', 'diretor.questao_77', 'diretor.questao_78', 'diretor.questao_79', 'diretor.questao_80', 'diretor.questao_81', 'diretor.questao_82', 'diretor.questao_83', 'diretor.questao_84', 'questionario.data', 'questionario.questao_1', 'questionario.questao_2', 'questionario.questao_3', 'questionario.questao_4', 'questionario.questao_5', 'questionario.questao_6', 'questionario.questao_7', 'questionario.questao_8', 'questionario.questao_9', 'questionario.questao_10', 'questionario.questao_11', 'questionario.questao_12', 'questionario.questao_13', 'questionario.questao_14', 'questionario.questao_15', 'questionario.questao_16', 'questionario.questao_17', 'questionario.questao_18', 'questionario.questao_19', 'questionario.questao_20', 'questionario.questao_21', 'questionario.questao_22', 'questionario.questao_23', 'questionario.questao_24', 'questionario.questao_25', 'questionario.questao_26', 'questionario.questao_27', 'questionario.questao_28', 'questionario.questao_29', 'questionario.questao_30', 'questionario.questao_31', 'questionario.questao_32', 'questionario.questao_33', 'questionario.questao_34', 'questionario.questao_35', 'questionario.questao_36', 'questionario.questao_37', 'questionario.questao_38', 'questionario.questao_39', 'questionario.questao_40', 'questionario.questao_41', 'questionario.questao_42', 'questionario.questao_43', 'questionario.questao_44', 'questionario.questao_45', 'questionario.questao_46', 'questionario.questao_47', 'questionario.questao_48', 'questionario.questao_49', 'questionario.questao_50', 'questionario.questao_51', 'questionario.questao_52', 'questionario.questao_53', 'questionario.questao_54', 'questionario.questao_55', 'questionario.questao_56', 'questionario.questao_57', 'questionario.questao_58', 'questionario.questao_59', 'questionario.questao_60', 'questionario.questao_61', 'questionario.questao_62', 'questionario.questao_63', 'questionario.questao_64', 'questionario.questao_65', 'questionario.questao_66', 'questionario.questao_67', 'questionario.questao_68', 'questionario.questao_69', 'questionario.questao_70', 'questionario.questao_71', 'questionario.questao_72', 'questionario.questao_73', 'questionario.questao_74', 'questionario.questao_75', 'questionario.questao_76', 'questionario.questao_77', 'questionario.questao_78', 'questionario.questao_79', 'questionario.questao_80', 'questionario.questao_81', 'questionario.questao_82', 'questionario.questao_83', 'questionario.questao_84', 'questionario.questao_85', 'questionario.questao_86', 'questionario.questao_87', 'questionario.questao_88', 'questionario.questao_89', 'questionario.questao_90', 'questionario.questao_91', 'questionario.questao_92', 'questionario.questao_93', 'questionario.questao_94', 'questionario.questao_95', 'questionario.questao_96', 'questionario.questao_97', 'questionario.questao_98', 'questionario.questao_99', 'questionario.questao_100', 'questionario.questao_101', 'questionario.questao_102', 'questionario.questao_103', 'questionario.questao_104', 'questionario.questao_105', 'questionario.questao_106', 'questionario.questao_107', 'questionario.questao_108', 'questionario.questao_109', 'questionario.questao_110', 'questionario.questao_111', 'questionario.questao_112', 'questionario.questao_113', 'questionario.questao_114', 'questionario.questao_115', 'questionario.questao_116', 'questionario.questao_117', 'questionario.questao_118', 'questionario.questao_119', 'questionario.questao_120', 'questionario.questao_121', 'questionario.questao_122', 'questionario.questao_123', 'questionario.questao_124', 'questionario.questao_125', 'questionario.questao_126', 'questionario.questao_127', 'questionario.questao_128', 'questionario.questao_129', 'questionario.questao_130', 'questionario.questao_131', 'questionario.questao_132', 'questionario.questao_133', 'questionario.questao_134', 'questionario.questao_135', 'questionario.questao_136', 'questionario.questao_137', 'questionario.questao_138', 'questionario.questao_139', 'questionario.questao_140', 'questionario.questao_141', 'questionario.questao_142', 'questionario.questao_143', 'questionario.questao_144', 'questionario.questao_145', 'questionario.questao_146', 'exame.data', 'exame.examinador', 'exame.anotador', 'exame.carie_coroa_18', 'exame.carie_tratamento_18', 'exame.carie_coroa_17', 'exame.carie_tratamento_17', 'exame.carie_coroa_16', 'exame.carie_tratamento_16', 'exame.carie_coroa_15', 'exame.carie_tratamento_15', 'exame.carie_coroa_14', 'exame.carie_tratamento_14', 'exame.carie_coroa_13', 'exame.carie_tratamento_13', 'exame.carie_coroa_12', 'exame.carie_tratamento_12', 'exame.carie_coroa_11', 'exame.carie_tratamento_11', 'exame.carie_coroa_21', 'exame.carie_tratamento_21', 'exame.carie_coroa_22', 'exame.carie_tratamento_22', 'exame.carie_coroa_23', 'exame.carie_tratamento_23', 'exame.carie_coroa_24', 'exame.carie_tratamento_24', 'exame.carie_coroa_25', 'exame.carie_tratamento_25', 'exame.carie_coroa_26', 'exame.carie_tratamento_26', 'exame.carie_coroa_27', 'exame.carie_tratamento_27', 'exame.carie_coroa_28', 'exame.carie_tratamento_28', 'exame.carie_coroa_38', 'exame.carie_tratamento_38', 'exame.carie_coroa_37', 'exame.carie_tratamento_37', 'exame.carie_coroa_36', 'exame.carie_tratamento_36', 'exame.carie_coroa_35', 'exame.carie_tratamento_35', 'exame.carie_coroa_34', 'exame.carie_tratamento_34', 'exame.carie_coroa_33', 'exame.carie_tratamento_33', 'exame.carie_coroa_32', 'exame.carie_tratamento_32', 'exame.carie_coroa_31', 'exame.carie_tratamento_31', 'exame.carie_coroa_41', 'exame.carie_tratamento_41', 'exame.carie_coroa_42', 'exame.carie_tratamento_42', 'exame.carie_coroa_43', 'exame.carie_tratamento_43', 'exame.carie_coroa_44', 'exame.carie_tratamento_44', 'exame.carie_coroa_45', 'exame.carie_tratamento_45', 'exame.carie_coroa_46', 'exame.carie_tratamento_46', 'exame.carie_coroa_47', 'exame.carie_tratamento_47', 'exame.carie_coroa_48', 'exame.carie_tratamento_48', 'exame.periodontal_sangramento_1716', 'exame.periodontal_calculo_1716', 'exame.periodontal_bolsa_1716', 'exame.periodontal_sangramento_11', 'exame.periodontal_calculo_11', 'exame.periodontal_bolsa_11', 'exame.periodontal_sangramento_2627', 'exame.periodontal_calculo_2627', 'exame.periodontal_bolsa_2627', 'exame.periodontal_sangramento_3736', 'exame.periodontal_calculo_3736', 'exame.periodontal_bolsa_3736', 'exame.periodontal_sangramento_31', 'exame.periodontal_calculo_31', 'exame.periodontal_bolsa_31', 'exame.periodontal_sangramento_4647', 'exame.periodontal_calculo_4647', 'exame.periodontal_bolsa_4647', 'cpod',])
        
        for aluno in alunos:
            diretor = Diretor.objects.get(escola_id=aluno.escola_id)
            
            resultados = {
                "cpod": 0,
            }
            
            try:
                exame = Exame.objects.get(aluno_id=aluno.id)
                
                # cálculo do cpo-d
                if exame.carie_coroa_18 == '1': resultados["cpod"] += 1
                if exame.carie_coroa_18 == '2': resultados["cpod"] += 1
                if exame.carie_coroa_18 == '3': resultados["cpod"] += 1
                if exame.carie_coroa_18 == '4': resultados["cpod"] += 1
                if exame.carie_coroa_18 == '5': resultados["cpod"] += 1
                if exame.carie_tratamento_18 == '6': resultados["cpod"] += 1
                if exame.carie_coroa_17 == '1': resultados["cpod"] += 1
                if exame.carie_coroa_17 == '2': resultados["cpod"] += 1
                if exame.carie_coroa_17 == '3': resultados["cpod"] += 1
                if exame.carie_coroa_17 == '4': resultados["cpod"] += 1
                if exame.carie_coroa_17 == '5': resultados["cpod"] += 1
                if exame.carie_tratamento_17 == '6': resultados["cpod"] += 1
                if exame.carie_coroa_16 == '1': resultados["cpod"] += 1
                if exame.carie_coroa_16 == '2': resultados["cpod"] += 1
                if exame.carie_coroa_16 == '3': resultados["cpod"] += 1
                if exame.carie_coroa_16 == '4': resultados["cpod"] += 1
                if exame.carie_coroa_16 == '5': resultados["cpod"] += 1
                if exame.carie_tratamento_16 == '6': resultados["cpod"] += 1
                if exame.carie_coroa_15 == '1': resultados["cpod"] += 1
                if exame.carie_coroa_15 == '2': resultados["cpod"] += 1
                if exame.carie_coroa_15 == '3': resultados["cpod"] += 1
                if exame.carie_coroa_15 == '4': resultados["cpod"] += 1
                if exame.carie_coroa_15 == '5': resultados["cpod"] += 1
                if exame.carie_tratamento_15 == '6': resultados["cpod"] += 1
                if exame.carie_coroa_14 == '1': resultados["cpod"] += 1
                if exame.carie_coroa_14 == '2': resultados["cpod"] += 1
                if exame.carie_coroa_14 == '3': resultados["cpod"] += 1
                if exame.carie_coroa_14 == '4': resultados["cpod"] += 1
                if exame.carie_coroa_14 == '5': resultados["cpod"] += 1
                if exame.carie_tratamento_14 == '6': resultados["cpod"] += 1
                if exame.carie_coroa_13 == '1': resultados["cpod"] += 1
                if exame.carie_coroa_13 == '2': resultados["cpod"] += 1
                if exame.carie_coroa_13 == '3': resultados["cpod"] += 1
                if exame.carie_coroa_13 == '4': resultados["cpod"] += 1
                if exame.carie_coroa_13 == '5': resultados["cpod"] += 1
                if exame.carie_tratamento_13 == '6': resultados["cpod"] += 1
                if exame.carie_coroa_12 == '1': resultados["cpod"] += 1
                if exame.carie_coroa_12 == '2': resultados["cpod"] += 1
                if exame.carie_coroa_12 == '3': resultados["cpod"] += 1
                if exame.carie_coroa_12 == '4': resultados["cpod"] += 1
                if exame.carie_coroa_12 == '5': resultados["cpod"] += 1
                if exame.carie_tratamento_12 == '6': resultados["cpod"] += 1
                if exame.carie_coroa_11 == '1': resultados["cpod"] += 1
                if exame.carie_coroa_11 == '2': resultados["cpod"] += 1
                if exame.carie_coroa_11 == '3': resultados["cpod"] += 1
                if exame.carie_coroa_11 == '4': resultados["cpod"] += 1
                if exame.carie_coroa_11 == '5': resultados["cpod"] += 1
                if exame.carie_tratamento_11 == '6': resultados["cpod"] += 1
                if exame.carie_coroa_21 == '1': resultados["cpod"] += 1
                if exame.carie_coroa_21 == '2': resultados["cpod"] += 1
                if exame.carie_coroa_21 == '3': resultados["cpod"] += 1
                if exame.carie_coroa_21 == '4': resultados["cpod"] += 1
                if exame.carie_coroa_21 == '5': resultados["cpod"] += 1
                if exame.carie_tratamento_21 == '6': resultados["cpod"] += 1
                if exame.carie_coroa_22 == '1': resultados["cpod"] += 1
                if exame.carie_coroa_22 == '2': resultados["cpod"] += 1
                if exame.carie_coroa_22 == '3': resultados["cpod"] += 1
                if exame.carie_coroa_22 == '4': resultados["cpod"] += 1
                if exame.carie_coroa_22 == '5': resultados["cpod"] += 1
                if exame.carie_tratamento_22 == '6': resultados["cpod"] += 1
                if exame.carie_coroa_23 == '1': resultados["cpod"] += 1
                if exame.carie_coroa_23 == '2': resultados["cpod"] += 1
                if exame.carie_coroa_23 == '3': resultados["cpod"] += 1
                if exame.carie_coroa_23 == '4': resultados["cpod"] += 1
                if exame.carie_coroa_23 == '5': resultados["cpod"] += 1
                if exame.carie_tratamento_23 == '6': resultados["cpod"] += 1
                if exame.carie_coroa_24 == '1': resultados["cpod"] += 1
                if exame.carie_coroa_24 == '2': resultados["cpod"] += 1
                if exame.carie_coroa_24 == '3': resultados["cpod"] += 1
                if exame.carie_coroa_24 == '4': resultados["cpod"] += 1
                if exame.carie_coroa_24 == '5': resultados["cpod"] += 1
                if exame.carie_tratamento_24 == '6': resultados["cpod"] += 1
                if exame.carie_coroa_25 == '1': resultados["cpod"] += 1
                if exame.carie_coroa_25 == '2': resultados["cpod"] += 1
                if exame.carie_coroa_25 == '3': resultados["cpod"] += 1
                if exame.carie_coroa_25 == '4': resultados["cpod"] += 1
                if exame.carie_coroa_25 == '5': resultados["cpod"] += 1
                if exame.carie_tratamento_25 == '6': resultados["cpod"] += 1
                if exame.carie_coroa_26 == '1': resultados["cpod"] += 1
                if exame.carie_coroa_26 == '2': resultados["cpod"] += 1
                if exame.carie_coroa_26 == '3': resultados["cpod"] += 1
                if exame.carie_coroa_26 == '4': resultados["cpod"] += 1
                if exame.carie_coroa_26 == '5': resultados["cpod"] += 1
                if exame.carie_tratamento_26 == '6': resultados["cpod"] += 1
                if exame.carie_coroa_27 == '1': resultados["cpod"] += 1
                if exame.carie_coroa_27 == '2': resultados["cpod"] += 1
                if exame.carie_coroa_27 == '3': resultados["cpod"] += 1
                if exame.carie_coroa_27 == '4': resultados["cpod"] += 1
                if exame.carie_coroa_27 == '5': resultados["cpod"] += 1
                if exame.carie_tratamento_27 == '6': resultados["cpod"] += 1
                if exame.carie_coroa_28 == '1': resultados["cpod"] += 1
                if exame.carie_coroa_28 == '2': resultados["cpod"] += 1
                if exame.carie_coroa_28 == '3': resultados["cpod"] += 1
                if exame.carie_coroa_28 == '4': resultados["cpod"] += 1
                if exame.carie_coroa_28 == '5': resultados["cpod"] += 1
                if exame.carie_tratamento_28 == '6': resultados["cpod"] += 1
                if exame.carie_coroa_38 == '1': resultados["cpod"] += 1
                if exame.carie_coroa_38 == '2': resultados["cpod"] += 1
                if exame.carie_coroa_38 == '3': resultados["cpod"] += 1
                if exame.carie_coroa_38 == '4': resultados["cpod"] += 1
                if exame.carie_coroa_38 == '5': resultados["cpod"] += 1
                if exame.carie_tratamento_38 == '6': resultados["cpod"] += 1
                if exame.carie_coroa_37 == '1': resultados["cpod"] += 1
                if exame.carie_coroa_37 == '2': resultados["cpod"] += 1
                if exame.carie_coroa_37 == '3': resultados["cpod"] += 1
                if exame.carie_coroa_37 == '4': resultados["cpod"] += 1
                if exame.carie_coroa_37 == '5': resultados["cpod"] += 1
                if exame.carie_tratamento_37 == '6': resultados["cpod"] += 1
                if exame.carie_coroa_36 == '1': resultados["cpod"] += 1
                if exame.carie_coroa_36 == '2': resultados["cpod"] += 1
                if exame.carie_coroa_36 == '3': resultados["cpod"] += 1
                if exame.carie_coroa_36 == '4': resultados["cpod"] += 1
                if exame.carie_coroa_36 == '5': resultados["cpod"] += 1
                if exame.carie_tratamento_36 == '6': resultados["cpod"] += 1
                if exame.carie_coroa_35 == '1': resultados["cpod"] += 1
                if exame.carie_coroa_35 == '2': resultados["cpod"] += 1
                if exame.carie_coroa_35 == '3': resultados["cpod"] += 1
                if exame.carie_coroa_35 == '4': resultados["cpod"] += 1
                if exame.carie_coroa_35 == '5': resultados["cpod"] += 1
                if exame.carie_tratamento_35 == '6': resultados["cpod"] += 1
                if exame.carie_coroa_34 == '1': resultados["cpod"] += 1
                if exame.carie_coroa_34 == '2': resultados["cpod"] += 1
                if exame.carie_coroa_34 == '3': resultados["cpod"] += 1
                if exame.carie_coroa_34 == '4': resultados["cpod"] += 1
                if exame.carie_coroa_34 == '5': resultados["cpod"] += 1
                if exame.carie_tratamento_34 == '6': resultados["cpod"] += 1
                if exame.carie_coroa_33 == '1': resultados["cpod"] += 1
                if exame.carie_coroa_33 == '2': resultados["cpod"] += 1
                if exame.carie_coroa_33 == '3': resultados["cpod"] += 1
                if exame.carie_coroa_33 == '4': resultados["cpod"] += 1
                if exame.carie_coroa_33 == '5': resultados["cpod"] += 1
                if exame.carie_tratamento_33 == '6': resultados["cpod"] += 1
                if exame.carie_coroa_32 == '1': resultados["cpod"] += 1
                if exame.carie_coroa_32 == '2': resultados["cpod"] += 1
                if exame.carie_coroa_32 == '3': resultados["cpod"] += 1
                if exame.carie_coroa_32 == '4': resultados["cpod"] += 1
                if exame.carie_coroa_32 == '5': resultados["cpod"] += 1
                if exame.carie_tratamento_32 == '6': resultados["cpod"] += 1
                if exame.carie_coroa_31 == '1': resultados["cpod"] += 1
                if exame.carie_coroa_31 == '2': resultados["cpod"] += 1
                if exame.carie_coroa_31 == '3': resultados["cpod"] += 1
                if exame.carie_coroa_31 == '4': resultados["cpod"] += 1
                if exame.carie_coroa_31 == '5': resultados["cpod"] += 1
                if exame.carie_tratamento_31 == '6': resultados["cpod"] += 1
                if exame.carie_coroa_41 == '1': resultados["cpod"] += 1
                if exame.carie_coroa_41 == '2': resultados["cpod"] += 1
                if exame.carie_coroa_41 == '3': resultados["cpod"] += 1
                if exame.carie_coroa_41 == '4': resultados["cpod"] += 1
                if exame.carie_coroa_41 == '5': resultados["cpod"] += 1
                if exame.carie_tratamento_41 == '6': resultados["cpod"] += 1
                if exame.carie_coroa_42 == '1': resultados["cpod"] += 1
                if exame.carie_coroa_42 == '2': resultados["cpod"] += 1
                if exame.carie_coroa_42 == '3': resultados["cpod"] += 1
                if exame.carie_coroa_42 == '4': resultados["cpod"] += 1
                if exame.carie_coroa_42 == '5': resultados["cpod"] += 1
                if exame.carie_tratamento_42 == '6': resultados["cpod"] += 1
                if exame.carie_coroa_43 == '1': resultados["cpod"] += 1
                if exame.carie_coroa_43 == '2': resultados["cpod"] += 1
                if exame.carie_coroa_43 == '3': resultados["cpod"] += 1
                if exame.carie_coroa_43 == '4': resultados["cpod"] += 1
                if exame.carie_coroa_43 == '5': resultados["cpod"] += 1
                if exame.carie_tratamento_43 == '6': resultados["cpod"] += 1
                if exame.carie_coroa_44 == '1': resultados["cpod"] += 1
                if exame.carie_coroa_44 == '2': resultados["cpod"] += 1
                if exame.carie_coroa_44 == '3': resultados["cpod"] += 1
                if exame.carie_coroa_44 == '4': resultados["cpod"] += 1
                if exame.carie_coroa_44 == '5': resultados["cpod"] += 1
                if exame.carie_tratamento_44 == '6': resultados["cpod"] += 1
                if exame.carie_coroa_45 == '1': resultados["cpod"] += 1
                if exame.carie_coroa_45 == '2': resultados["cpod"] += 1
                if exame.carie_coroa_45 == '3': resultados["cpod"] += 1
                if exame.carie_coroa_45 == '4': resultados["cpod"] += 1
                if exame.carie_coroa_45 == '5': resultados["cpod"] += 1
                if exame.carie_tratamento_45 == '6': resultados["cpod"] += 1
                if exame.carie_coroa_46 == '1': resultados["cpod"] += 1
                if exame.carie_coroa_46 == '2': resultados["cpod"] += 1
                if exame.carie_coroa_46 == '3': resultados["cpod"] += 1
                if exame.carie_coroa_46 == '4': resultados["cpod"] += 1
                if exame.carie_coroa_46 == '5': resultados["cpod"] += 1
                if exame.carie_tratamento_46 == '6': resultados["cpod"] += 1
                if exame.carie_coroa_47 == '1': resultados["cpod"] += 1
                if exame.carie_coroa_47 == '2': resultados["cpod"] += 1
                if exame.carie_coroa_47 == '3': resultados["cpod"] += 1
                if exame.carie_coroa_47 == '4': resultados["cpod"] += 1
                if exame.carie_coroa_47 == '5': resultados["cpod"] += 1
                if exame.carie_tratamento_47 == '6': resultados["cpod"] += 1
                if exame.carie_coroa_48 == '1': resultados["cpod"] += 1
                if exame.carie_coroa_48 == '2': resultados["cpod"] += 1
                if exame.carie_coroa_48 == '3': resultados["cpod"] += 1
                if exame.carie_coroa_48 == '4': resultados["cpod"] += 1
                if exame.carie_coroa_48 == '5': resultados["cpod"] += 1
                if exame.carie_tratamento_48 == '6': resultados["cpod"] += 1
            except:
                pass
            
            tem_questionario = True
            tem_exame = True
            
            try:
                questionario = Questionario.objects.get(aluno_id=aluno.id)
            except:
                tem_questionario = False
                
            try:
                exame = Exame.objects.get(aluno_id=aluno.id)
            except:
                tem_exame = False
            
                
            if not tem_questionario and tem_exame:
                writer.writerow([
                    aluno.escola.acao.campanha.nome,
                    
                    aluno.escola.acao.nome,
                    
                    aluno.escola.id,
                    aluno.escola.nome,
                    aluno.escola.latitude,
                    aluno.escola.longitude,
                    
                    aluno.numero_identificacao,
                    aluno.periodo, # get__display()
                    aluno.turma,
                    aluno.nascimento,
                    aluno.sexo, # get__display()
                    aluno.raca, # get__display()
                    
                    diretor.data,
                    diretor.questao_1,
                    diretor.questao_2, # get__display()
                    diretor.questao_3,
                    diretor.questao_4, # get__display()
                    diretor.questao_5, # get__display()
                    diretor.questao_6, # get__display()
                    diretor.questao_7, # get__display()
                    diretor.questao_8, # get__display()
                    diretor.questao_9, # get__display()
                    diretor.questao_10, # get__display()
                    diretor.questao_11, # get__display()
                    diretor.questao_12, # get__display()
                    diretor.questao_13, # get__display()
                    diretor.questao_14, # get__display()
                    diretor.questao_15, # get__display()
                    diretor.questao_16, # get__display()
                    diretor.questao_17, # get__display()
                    diretor.questao_18, # get__display()
                    diretor.questao_19, # get__display()
                    diretor.questao_20, # get__display()
                    diretor.questao_21, # get__display()
                    diretor.questao_22, # get__display()
                    diretor.questao_23, # get__display()
                    diretor.questao_24, # get__display()
                    diretor.questao_25, # get__display()
                    diretor.questao_26, # get__display()
                    diretor.questao_27, # get__display()
                    diretor.questao_28,
                    diretor.questao_29, # get__display()
                    diretor.questao_30, # get__display()
                    diretor.questao_31,
                    diretor.questao_32, # get__display()
                    diretor.questao_33,
                    diretor.questao_34, # get__display()
                    diretor.questao_35, # get__display()
                    diretor.questao_36, # get__display()
                    diretor.questao_37,
                    diretor.questao_38, # get__display()
                    diretor.questao_39,
                    diretor.questao_40, # get__display()
                    diretor.questao_41, # get__display()
                    diretor.questao_42, # get__display()
                    diretor.questao_43, # get__display()
                    diretor.questao_44, # get__display()
                    diretor.questao_45, # get__display()
                    diretor.questao_46, # get__display()
                    diretor.questao_47, # get__display()
                    diretor.questao_48, # get__display()
                    diretor.questao_49, # get__display()
                    diretor.questao_50, # get__display()
                    diretor.questao_51, # get__display()
                    diretor.questao_52, # get__display()
                    diretor.questao_53, # get__display()
                    diretor.questao_54, # get__display()
                    diretor.questao_55, # get__display()
                    diretor.questao_56, # get__display()
                    diretor.questao_57, # get__display()
                    diretor.questao_58, # get__display()
                    diretor.questao_59, # get__display()
                    diretor.questao_60, # get__display()
                    diretor.questao_61, # get__display()
                    diretor.questao_62, # get__display()
                    diretor.questao_63, # get__display()
                    diretor.questao_64, # get__display()
                    diretor.questao_65, # get__display()
                    diretor.questao_66, # get__display()
                    diretor.questao_67, # get__display()
                    diretor.questao_68, # get__display()
                    diretor.questao_69, # get__display()
                    diretor.questao_70, # get__display()
                    diretor.questao_71, # get__display()
                    diretor.questao_72, # get__display()
                    diretor.questao_73, # get__display()
                    diretor.questao_74, # get__display()
                    diretor.questao_75, # get__display()
                    diretor.questao_76, # get__display()
                    diretor.questao_77, # get__display()
                    diretor.questao_78, # get__display()
                    diretor.questao_79, # get__display()
                    diretor.questao_80, # get__display()
                    diretor.questao_81, # get__display()
                    diretor.questao_82, # get__display()
                    diretor.questao_83, # get__display()
                    diretor.questao_84, # get__display()
                    
                    None,
                    None, # get__display()
                    None, # get__display()
                    None, # get__display()
                    None, # get__display()
                    None, # get__display()
                    None, # get__display()
                    None, # get__display()
                    None, # get__display()
                    None, # get__display()
                    None, # get__display()
                    None, # get__display()
                    None, # get__display()
                    None, # get__display()
                    None, # get__display()
                    None, # get__display()
                    None, # get__display()
                    None, # get__display()
                    None, # get__display()
                    None, # get__display()
                    None, # get__display()
                    None, # get__display()
                    None, # get__display()
                    None, # get__display()
                    None, # get__display()
                    None, # get__display()
                    None, # get__display()
                    None, # get__display()
                    None, # get__display()
                    None, # get__display()
                    None, # get__display()
                    None, # get__display()
                    None, # get__display()
                    None, # get__display()
                    None, # get__display()
                    None, # get__display()
                    None, # get__display()
                    None, # get__display()
                    None, # get__display()
                    None, # get__display()
                    None, # get__display()
                    None, # get__display()
                    None, # get__display()
                    None, # get__display()
                    None, # get__display()
                    None, # get__display()
                    None, # get__display()
                    None, # get__display()
                    None, # get__display()
                    None, # get__display()
                    None, # get__display()
                    None, # get__display()
                    None, # get__display()
                    None, # get__display()
                    None, # get__display()
                    None, # get__display()
                    None, # get__display()
                    None, # get__display()
                    None, # get__display()
                    None, # get__display()
                    None,
                    None, # get__display()
                    None, # get__display()
                    None, # get__display()
                    None, # get__display()
                    None, # get__display()
                    None, # get__display()
                    None, # get__display()
                    None, # get__display()
                    None, # get__display()
                    None, # get__display()
                    None, # get__display()
                    None, # get__display()
                    None, # get__display()
                    None, # get__display()
                    None, # get__display()
                    None, # get__display()
                    None, # get__display()
                    None, # get__display()
                    None, # get__display()
                    None, # get__display()
                    None, # get__display()
                    None, # get__display()
                    None, # get__display()
                    None, # get__display()
                    None, # get__display()
                    None, # get__display()
                    None, # get__display()
                    None, # get__display()
                    None, # get__display()
                    None, # get__display()
                    None, # get__display()
                    None, # get__display()
                    None, # get__display()
                    None, # get__display()
                    None, # get__display()
                    None, # get__display()
                    None, # get__display()
                    None, # get__display()
                    None, # get__display()
                    None, # get__display()
                    None, # get__display()
                    None, # get__display()
                    None, # get__display()
                    None, # get__display()
                    None, # get__display()
                    None, # get__display()
                    None, # get__display()
                    None, # get__display()
                    None, # get__display()
                    None, # get__display()
                    None, # get__display()
                    None, # get__display()
                    None, # get__display()
                    None, # get__display()
                    None, # get__display()
                    None, # get__display()
                    None, # get__display()
                    None, # get__display()
                    None, # get__display()
                    None, # get__display()
                    None, # get__display()
                    None, # get__display()
                    None, # get__display()
                    None, # get__display()
                    None, # get__display()
                    None, # get__display()
                    None, # get__display()
                    None, # get__display()
                    None, # get__display()
                    None, # get__display()
                    None, # get__display()
                    None, # get__display()
                    None, # get__display()
                    None, # get__display()
                    None, # get__display()
                    None, # get__display()
                    None, # get__display()
                    None, # get__display()
                    None, # get__display()
                    None, # get__display()
                    None, # get__display()
                    None, # get__display()
                    None, # get__display()
                    None, # get__display()
                    None, # get__display()
                    None,
                    
                    exame.data,
                    exame.examinador,
                    exame.anotador,
                    exame.carie_coroa_18,
                    exame.carie_tratamento_18,
                    exame.carie_coroa_17,
                    exame.carie_tratamento_17,
                    exame.carie_coroa_16,
                    exame.carie_tratamento_16,
                    exame.carie_coroa_15,
                    exame.carie_tratamento_15,
                    exame.carie_coroa_14,
                    exame.carie_tratamento_14,
                    exame.carie_coroa_13,
                    exame.carie_tratamento_13,
                    exame.carie_coroa_12,
                    exame.carie_tratamento_12,
                    exame.carie_coroa_11,
                    exame.carie_tratamento_11,
                    exame.carie_coroa_21,
                    exame.carie_tratamento_21,
                    exame.carie_coroa_22,
                    exame.carie_tratamento_22,
                    exame.carie_coroa_23,
                    exame.carie_tratamento_23,
                    exame.carie_coroa_24,
                    exame.carie_tratamento_24,
                    exame.carie_coroa_25,
                    exame.carie_tratamento_25,
                    exame.carie_coroa_26,
                    exame.carie_tratamento_26,
                    exame.carie_coroa_27,
                    exame.carie_tratamento_27,
                    exame.carie_coroa_28,
                    exame.carie_tratamento_28,
                    exame.carie_coroa_38,
                    exame.carie_tratamento_38,
                    exame.carie_coroa_37,
                    exame.carie_tratamento_37,
                    exame.carie_coroa_36,
                    exame.carie_tratamento_36,
                    exame.carie_coroa_35,
                    exame.carie_tratamento_35,
                    exame.carie_coroa_34,
                    exame.carie_tratamento_34,
                    exame.carie_coroa_33,
                    exame.carie_tratamento_33,
                    exame.carie_coroa_32,
                    exame.carie_tratamento_32,
                    exame.carie_coroa_31,
                    exame.carie_tratamento_31,
                    exame.carie_coroa_41,
                    exame.carie_tratamento_41,
                    exame.carie_coroa_42,
                    exame.carie_tratamento_42,
                    exame.carie_coroa_43,
                    exame.carie_tratamento_43,
                    exame.carie_coroa_44,
                    exame.carie_tratamento_44,
                    exame.carie_coroa_45,
                    exame.carie_tratamento_45,
                    exame.carie_coroa_46,
                    exame.carie_tratamento_46,
                    exame.carie_coroa_47,
                    exame.carie_tratamento_47,
                    exame.carie_coroa_48,
                    exame.carie_tratamento_48,
                    exame.periodontal_sangramento_1716,
                    exame.periodontal_calculo_1716,
                    exame.periodontal_bolsa_1716,
                    exame.periodontal_sangramento_11,
                    exame.periodontal_calculo_11,
                    exame.periodontal_bolsa_11,
                    exame.periodontal_sangramento_2627,
                    exame.periodontal_calculo_2627,
                    exame.periodontal_bolsa_2627,
                    exame.periodontal_sangramento_3736,
                    exame.periodontal_calculo_3736,
                    exame.periodontal_bolsa_3736,
                    exame.periodontal_sangramento_31,
                    exame.periodontal_calculo_31,
                    exame.periodontal_bolsa_31,
                    exame.periodontal_sangramento_4647,
                    exame.periodontal_calculo_4647,
                    exame.periodontal_bolsa_4647,
                    resultados["cpod"],
                ])
                continue
            
            if tem_questionario and not tem_exame:
                writer.writerow([
                    aluno.escola.acao.campanha.nome,
                    
                    aluno.escola.acao.nome,
                    
                    aluno.escola.id,
                    aluno.escola.nome,
                    aluno.escola.latitude,
                    aluno.escola.longitude,
                    
                    aluno.numero_identificacao,
                    aluno.periodo, # get__display()
                    aluno.turma,
                    aluno.nascimento,
                    aluno.sexo, # get__display()
                    aluno.raca, # get__display()
                    
                    diretor.data,
                    diretor.questao_1,
                    diretor.questao_2, # get__display()
                    diretor.questao_3,
                    diretor.questao_4, # get__display()
                    diretor.questao_5, # get__display()
                    diretor.questao_6, # get__display()
                    diretor.questao_7, # get__display()
                    diretor.questao_8, # get__display()
                    diretor.questao_9, # get__display()
                    diretor.questao_10, # get__display()
                    diretor.questao_11, # get__display()
                    diretor.questao_12, # get__display()
                    diretor.questao_13, # get__display()
                    diretor.questao_14, # get__display()
                    diretor.questao_15, # get__display()
                    diretor.questao_16, # get__display()
                    diretor.questao_17, # get__display()
                    diretor.questao_18, # get__display()
                    diretor.questao_19, # get__display()
                    diretor.questao_20, # get__display()
                    diretor.questao_21, # get__display()
                    diretor.questao_22, # get__display()
                    diretor.questao_23, # get__display()
                    diretor.questao_24, # get__display()
                    diretor.questao_25, # get__display()
                    diretor.questao_26, # get__display()
                    diretor.questao_27, # get__display()
                    diretor.questao_28,
                    diretor.questao_29, # get__display()
                    diretor.questao_30, # get__display()
                    diretor.questao_31,
                    diretor.questao_32, # get__display()
                    diretor.questao_33,
                    diretor.questao_34, # get__display()
                    diretor.questao_35, # get__display()
                    diretor.questao_36, # get__display()
                    diretor.questao_37,
                    diretor.questao_38, # get__display()
                    diretor.questao_39,
                    diretor.questao_40, # get__display()
                    diretor.questao_41, # get__display()
                    diretor.questao_42, # get__display()
                    diretor.questao_43, # get__display()
                    diretor.questao_44, # get__display()
                    diretor.questao_45, # get__display()
                    diretor.questao_46, # get__display()
                    diretor.questao_47, # get__display()
                    diretor.questao_48, # get__display()
                    diretor.questao_49, # get__display()
                    diretor.questao_50, # get__display()
                    diretor.questao_51, # get__display()
                    diretor.questao_52, # get__display()
                    diretor.questao_53, # get__display()
                    diretor.questao_54, # get__display()
                    diretor.questao_55, # get__display()
                    diretor.questao_56, # get__display()
                    diretor.questao_57, # get__display()
                    diretor.questao_58, # get__display()
                    diretor.questao_59, # get__display()
                    diretor.questao_60, # get__display()
                    diretor.questao_61, # get__display()
                    diretor.questao_62, # get__display()
                    diretor.questao_63, # get__display()
                    diretor.questao_64, # get__display()
                    diretor.questao_65, # get__display()
                    diretor.questao_66, # get__display()
                    diretor.questao_67, # get__display()
                    diretor.questao_68, # get__display()
                    diretor.questao_69, # get__display()
                    diretor.questao_70, # get__display()
                    diretor.questao_71, # get__display()
                    diretor.questao_72, # get__display()
                    diretor.questao_73, # get__display()
                    diretor.questao_74, # get__display()
                    diretor.questao_75, # get__display()
                    diretor.questao_76, # get__display()
                    diretor.questao_77, # get__display()
                    diretor.questao_78, # get__display()
                    diretor.questao_79, # get__display()
                    diretor.questao_80, # get__display()
                    diretor.questao_81, # get__display()
                    diretor.questao_82, # get__display()
                    diretor.questao_83, # get__display()
                    diretor.questao_84, # get__display()
                    
                    questionario.data,
                    questionario.questao_1, # get__display()
                    questionario.questao_2, # get__display()
                    questionario.questao_3, # get__display()
                    questionario.questao_4, # get__display()
                    questionario.questao_5, # get__display()
                    questionario.questao_6, # get__display()
                    questionario.questao_7, # get__display()
                    questionario.questao_8, # get__display()
                    questionario.questao_9, # get__display()
                    questionario.questao_10, # get__display()
                    questionario.questao_11, # get__display()
                    questionario.questao_12, # get__display()
                    questionario.questao_13, # get__display()
                    questionario.questao_14, # get__display()
                    questionario.questao_15, # get__display()
                    questionario.questao_16, # get__display()
                    questionario.questao_17, # get__display()
                    questionario.questao_18, # get__display()
                    questionario.questao_19, # get__display()
                    questionario.questao_20, # get__display()
                    questionario.questao_21, # get__display()
                    questionario.questao_22, # get__display()
                    questionario.questao_23, # get__display()
                    questionario.questao_24, # get__display()
                    questionario.questao_25, # get__display()
                    questionario.questao_26, # get__display()
                    questionario.questao_27, # get__display()
                    questionario.questao_28, # get__display()
                    questionario.questao_29, # get__display()
                    questionario.questao_30, # get__display()
                    questionario.questao_31, # get__display()
                    questionario.questao_32, # get__display()
                    questionario.questao_33, # get__display()
                    questionario.questao_34, # get__display()
                    questionario.questao_35, # get__display()
                    questionario.questao_36, # get__display()
                    questionario.questao_37, # get__display()
                    questionario.questao_38, # get__display()
                    questionario.questao_39, # get__display()
                    questionario.questao_40, # get__display()
                    questionario.questao_41, # get__display()
                    questionario.questao_42, # get__display()
                    questionario.questao_43, # get__display()
                    questionario.questao_44, # get__display()
                    questionario.questao_45, # get__display()
                    questionario.questao_46, # get__display()
                    questionario.questao_47, # get__display()
                    questionario.questao_48, # get__display()
                    questionario.questao_49, # get__display()
                    questionario.questao_50, # get__display()
                    questionario.questao_51, # get__display()
                    questionario.questao_52, # get__display()
                    questionario.questao_53, # get__display()
                    questionario.questao_54, # get__display()
                    questionario.questao_55, # get__display()
                    questionario.questao_56, # get__display()
                    questionario.questao_57, # get__display()
                    questionario.questao_58, # get__display()
                    questionario.questao_59, # get__display()
                    questionario.questao_60,
                    questionario.questao_61, # get__display()
                    questionario.questao_62, # get__display()
                    questionario.questao_63, # get__display()
                    questionario.questao_64, # get__display()
                    questionario.questao_65, # get__display()
                    questionario.questao_66, # get__display()
                    questionario.questao_67, # get__display()
                    questionario.questao_68, # get__display()
                    questionario.questao_69, # get__display()
                    questionario.questao_70, # get__display()
                    questionario.questao_71, # get__display()
                    questionario.questao_72, # get__display()
                    questionario.questao_73, # get__display()
                    questionario.questao_74, # get__display()
                    questionario.questao_75, # get__display()
                    questionario.questao_76, # get__display()
                    questionario.questao_77, # get__display()
                    questionario.questao_78, # get__display()
                    questionario.questao_79, # get__display()
                    questionario.questao_80, # get__display()
                    questionario.questao_81, # get__display()
                    questionario.questao_82, # get__display()
                    questionario.questao_83, # get__display()
                    questionario.questao_84, # get__display()
                    questionario.questao_85, # get__display()
                    questionario.questao_86, # get__display()
                    questionario.questao_87, # get__display()
                    questionario.questao_88, # get__display()
                    questionario.questao_89, # get__display()
                    questionario.questao_90, # get__display()
                    questionario.questao_91, # get__display()
                    questionario.questao_92, # get__display()
                    questionario.questao_93, # get__display()
                    questionario.questao_94, # get__display()
                    questionario.questao_95, # get__display()
                    questionario.questao_96, # get__display()
                    questionario.questao_97, # get__display()
                    questionario.questao_98, # get__display()
                    questionario.questao_99, # get__display()
                    questionario.questao_100, # get__display()
                    questionario.questao_101, # get__display()
                    questionario.questao_102, # get__display()
                    questionario.questao_103, # get__display()
                    questionario.questao_104, # get__display()
                    questionario.questao_105, # get__display()
                    questionario.questao_106, # get__display()
                    questionario.questao_107, # get__display()
                    questionario.questao_108, # get__display()
                    questionario.questao_109, # get__display()
                    questionario.questao_110, # get__display()
                    questionario.questao_111, # get__display()
                    questionario.questao_112, # get__display()
                    questionario.questao_113, # get__display()
                    questionario.questao_114, # get__display()
                    questionario.questao_115, # get__display()
                    questionario.questao_116, # get__display()
                    questionario.questao_117, # get__display()
                    questionario.questao_118, # get__display()
                    questionario.questao_119, # get__display()
                    questionario.questao_120, # get__display()
                    questionario.questao_121, # get__display()
                    questionario.questao_122, # get__display()
                    questionario.questao_123, # get__display()
                    questionario.questao_124, # get__display()
                    questionario.questao_125, # get__display()
                    questionario.questao_126, # get__display()
                    questionario.questao_127, # get__display()
                    questionario.questao_128, # get__display()
                    questionario.questao_129, # get__display()
                    questionario.questao_130, # get__display()
                    questionario.questao_131, # get__display()
                    questionario.questao_132, # get__display()
                    questionario.questao_133, # get__display()
                    questionario.questao_134, # get__display()
                    questionario.questao_135, # get__display()
                    questionario.questao_136, # get__display()
                    questionario.questao_137, # get__display()
                    questionario.questao_138, # get__display()
                    questionario.questao_139, # get__display()
                    questionario.questao_140, # get__display()
                    questionario.questao_141, # get__display()
                    questionario.questao_142, # get__display()
                    questionario.questao_143, # get__display()
                    questionario.questao_144, # get__display()
                    questionario.questao_145, # get__display()
                    questionario.questao_146,
                    
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                ])
                continue
            
            # if questionario.questao_55 == '1':
            #     questionario.questao_55 = 'Não'
            if tem_questionario and tem_exame:
                writer.writerow([
                    aluno.escola.acao.campanha.nome,
                    
                    aluno.escola.acao.nome,
                    
                    aluno.escola.id,
                    aluno.escola.nome,
                    aluno.escola.latitude,
                    aluno.escola.longitude,
                    
                    aluno.numero_identificacao,
                    aluno.periodo, # get__display()
                    aluno.turma,
                    aluno.nascimento,
                    aluno.sexo, # get__display()
                    aluno.raca, # get__display()
                    
                    diretor.data,
                    diretor.questao_1,
                    diretor.questao_2, # get__display()
                    diretor.questao_3,
                    diretor.questao_4, # get__display()
                    diretor.questao_5, # get__display()
                    diretor.questao_6, # get__display()
                    diretor.questao_7, # get__display()
                    diretor.questao_8, # get__display()
                    diretor.questao_9, # get__display()
                    diretor.questao_10, # get__display()
                    diretor.questao_11, # get__display()
                    diretor.questao_12, # get__display()
                    diretor.questao_13, # get__display()
                    diretor.questao_14, # get__display()
                    diretor.questao_15, # get__display()
                    diretor.questao_16, # get__display()
                    diretor.questao_17, # get__display()
                    diretor.questao_18, # get__display()
                    diretor.questao_19, # get__display()
                    diretor.questao_20, # get__display()
                    diretor.questao_21, # get__display()
                    diretor.questao_22, # get__display()
                    diretor.questao_23, # get__display()
                    diretor.questao_24, # get__display()
                    diretor.questao_25, # get__display()
                    diretor.questao_26, # get__display()
                    diretor.questao_27, # get__display()
                    diretor.questao_28,
                    diretor.questao_29, # get__display()
                    diretor.questao_30, # get__display()
                    diretor.questao_31,
                    diretor.questao_32, # get__display()
                    diretor.questao_33,
                    diretor.questao_34, # get__display()
                    diretor.questao_35, # get__display()
                    diretor.questao_36, # get__display()
                    diretor.questao_37,
                    diretor.questao_38, # get__display()
                    diretor.questao_39,
                    diretor.questao_40, # get__display()
                    diretor.questao_41, # get__display()
                    diretor.questao_42, # get__display()
                    diretor.questao_43, # get__display()
                    diretor.questao_44, # get__display()
                    diretor.questao_45, # get__display()
                    diretor.questao_46, # get__display()
                    diretor.questao_47, # get__display()
                    diretor.questao_48, # get__display()
                    diretor.questao_49, # get__display()
                    diretor.questao_50, # get__display()
                    diretor.questao_51, # get__display()
                    diretor.questao_52, # get__display()
                    diretor.questao_53, # get__display()
                    diretor.questao_54, # get__display()
                    diretor.questao_55, # get__display()
                    diretor.questao_56, # get__display()
                    diretor.questao_57, # get__display()
                    diretor.questao_58, # get__display()
                    diretor.questao_59, # get__display()
                    diretor.questao_60, # get__display()
                    diretor.questao_61, # get__display()
                    diretor.questao_62, # get__display()
                    diretor.questao_63, # get__display()
                    diretor.questao_64, # get__display()
                    diretor.questao_65, # get__display()
                    diretor.questao_66, # get__display()
                    diretor.questao_67, # get__display()
                    diretor.questao_68, # get__display()
                    diretor.questao_69, # get__display()
                    diretor.questao_70, # get__display()
                    diretor.questao_71, # get__display()
                    diretor.questao_72, # get__display()
                    diretor.questao_73, # get__display()
                    diretor.questao_74, # get__display()
                    diretor.questao_75, # get__display()
                    diretor.questao_76, # get__display()
                    diretor.questao_77, # get__display()
                    diretor.questao_78, # get__display()
                    diretor.questao_79, # get__display()
                    diretor.questao_80, # get__display()
                    diretor.questao_81, # get__display()
                    diretor.questao_82, # get__display()
                    diretor.questao_83, # get__display()
                    diretor.questao_84, # get__display()
                    
                    questionario.data,
                    questionario.questao_1, # get__display()
                    questionario.questao_2, # get__display()
                    questionario.questao_3, # get__display()
                    questionario.questao_4, # get__display()
                    questionario.questao_5, # get__display()
                    questionario.questao_6, # get__display()
                    questionario.questao_7, # get__display()
                    questionario.questao_8, # get__display()
                    questionario.questao_9, # get__display()
                    questionario.questao_10, # get__display()
                    questionario.questao_11, # get__display()
                    questionario.questao_12, # get__display()
                    questionario.questao_13, # get__display()
                    questionario.questao_14, # get__display()
                    questionario.questao_15, # get__display()
                    questionario.questao_16, # get__display()
                    questionario.questao_17, # get__display()
                    questionario.questao_18, # get__display()
                    questionario.questao_19, # get__display()
                    questionario.questao_20, # get__display()
                    questionario.questao_21, # get__display()
                    questionario.questao_22, # get__display()
                    questionario.questao_23, # get__display()
                    questionario.questao_24, # get__display()
                    questionario.questao_25, # get__display()
                    questionario.questao_26, # get__display()
                    questionario.questao_27, # get__display()
                    questionario.questao_28, # get__display()
                    questionario.questao_29, # get__display()
                    questionario.questao_30, # get__display()
                    questionario.questao_31, # get__display()
                    questionario.questao_32, # get__display()
                    questionario.questao_33, # get__display()
                    questionario.questao_34, # get__display()
                    questionario.questao_35, # get__display()
                    questionario.questao_36, # get__display()
                    questionario.questao_37, # get__display()
                    questionario.questao_38, # get__display()
                    questionario.questao_39, # get__display()
                    questionario.questao_40, # get__display()
                    questionario.questao_41, # get__display()
                    questionario.questao_42, # get__display()
                    questionario.questao_43, # get__display()
                    questionario.questao_44, # get__display()
                    questionario.questao_45, # get__display()
                    questionario.questao_46, # get__display()
                    questionario.questao_47, # get__display()
                    questionario.questao_48, # get__display()
                    questionario.questao_49, # get__display()
                    questionario.questao_50, # get__display()
                    questionario.questao_51, # get__display()
                    questionario.questao_52, # get__display()
                    questionario.questao_53, # get__display()
                    questionario.questao_54, # get__display()
                    questionario.questao_55, # get__display()
                    questionario.questao_56, # get__display()
                    questionario.questao_57, # get__display()
                    questionario.questao_58, # get__display()
                    questionario.questao_59, # get__display()
                    questionario.questao_60,
                    questionario.questao_61, # get__display()
                    questionario.questao_62, # get__display()
                    questionario.questao_63, # get__display()
                    questionario.questao_64, # get__display()
                    questionario.questao_65, # get__display()
                    questionario.questao_66, # get__display()
                    questionario.questao_67, # get__display()
                    questionario.questao_68, # get__display()
                    questionario.questao_69, # get__display()
                    questionario.questao_70, # get__display()
                    questionario.questao_71, # get__display()
                    questionario.questao_72, # get__display()
                    questionario.questao_73, # get__display()
                    questionario.questao_74, # get__display()
                    questionario.questao_75, # get__display()
                    questionario.questao_76, # get__display()
                    questionario.questao_77, # get__display()
                    questionario.questao_78, # get__display()
                    questionario.questao_79, # get__display()
                    questionario.questao_80, # get__display()
                    questionario.questao_81, # get__display()
                    questionario.questao_82, # get__display()
                    questionario.questao_83, # get__display()
                    questionario.questao_84, # get__display()
                    questionario.questao_85, # get__display()
                    questionario.questao_86, # get__display()
                    questionario.questao_87, # get__display()
                    questionario.questao_88, # get__display()
                    questionario.questao_89, # get__display()
                    questionario.questao_90, # get__display()
                    questionario.questao_91, # get__display()
                    questionario.questao_92, # get__display()
                    questionario.questao_93, # get__display()
                    questionario.questao_94, # get__display()
                    questionario.questao_95, # get__display()
                    questionario.questao_96, # get__display()
                    questionario.questao_97, # get__display()
                    questionario.questao_98, # get__display()
                    questionario.questao_99, # get__display()
                    questionario.questao_100, # get__display()
                    questionario.questao_101, # get__display()
                    questionario.questao_102, # get__display()
                    questionario.questao_103, # get__display()
                    questionario.questao_104, # get__display()
                    questionario.questao_105, # get__display()
                    questionario.questao_106, # get__display()
                    questionario.questao_107, # get__display()
                    questionario.questao_108, # get__display()
                    questionario.questao_109, # get__display()
                    questionario.questao_110, # get__display()
                    questionario.questao_111, # get__display()
                    questionario.questao_112, # get__display()
                    questionario.questao_113, # get__display()
                    questionario.questao_114, # get__display()
                    questionario.questao_115, # get__display()
                    questionario.questao_116, # get__display()
                    questionario.questao_117, # get__display()
                    questionario.questao_118, # get__display()
                    questionario.questao_119, # get__display()
                    questionario.questao_120, # get__display()
                    questionario.questao_121, # get__display()
                    questionario.questao_122, # get__display()
                    questionario.questao_123, # get__display()
                    questionario.questao_124, # get__display()
                    questionario.questao_125, # get__display()
                    questionario.questao_126, # get__display()
                    questionario.questao_127, # get__display()
                    questionario.questao_128, # get__display()
                    questionario.questao_129, # get__display()
                    questionario.questao_130, # get__display()
                    questionario.questao_131, # get__display()
                    questionario.questao_132, # get__display()
                    questionario.questao_133, # get__display()
                    questionario.questao_134, # get__display()
                    questionario.questao_135, # get__display()
                    questionario.questao_136, # get__display()
                    questionario.questao_137, # get__display()
                    questionario.questao_138, # get__display()
                    questionario.questao_139, # get__display()
                    questionario.questao_140, # get__display()
                    questionario.questao_141, # get__display()
                    questionario.questao_142, # get__display()
                    questionario.questao_143, # get__display()
                    questionario.questao_144, # get__display()
                    questionario.questao_145, # get__display()
                    questionario.questao_146,
                    
                    exame.data,
                    exame.examinador,
                    exame.anotador,
                    exame.carie_coroa_18,
                    exame.carie_tratamento_18,
                    exame.carie_coroa_17,
                    exame.carie_tratamento_17,
                    exame.carie_coroa_16,
                    exame.carie_tratamento_16,
                    exame.carie_coroa_15,
                    exame.carie_tratamento_15,
                    exame.carie_coroa_14,
                    exame.carie_tratamento_14,
                    exame.carie_coroa_13,
                    exame.carie_tratamento_13,
                    exame.carie_coroa_12,
                    exame.carie_tratamento_12,
                    exame.carie_coroa_11,
                    exame.carie_tratamento_11,
                    exame.carie_coroa_21,
                    exame.carie_tratamento_21,
                    exame.carie_coroa_22,
                    exame.carie_tratamento_22,
                    exame.carie_coroa_23,
                    exame.carie_tratamento_23,
                    exame.carie_coroa_24,
                    exame.carie_tratamento_24,
                    exame.carie_coroa_25,
                    exame.carie_tratamento_25,
                    exame.carie_coroa_26,
                    exame.carie_tratamento_26,
                    exame.carie_coroa_27,
                    exame.carie_tratamento_27,
                    exame.carie_coroa_28,
                    exame.carie_tratamento_28,
                    exame.carie_coroa_38,
                    exame.carie_tratamento_38,
                    exame.carie_coroa_37,
                    exame.carie_tratamento_37,
                    exame.carie_coroa_36,
                    exame.carie_tratamento_36,
                    exame.carie_coroa_35,
                    exame.carie_tratamento_35,
                    exame.carie_coroa_34,
                    exame.carie_tratamento_34,
                    exame.carie_coroa_33,
                    exame.carie_tratamento_33,
                    exame.carie_coroa_32,
                    exame.carie_tratamento_32,
                    exame.carie_coroa_31,
                    exame.carie_tratamento_31,
                    exame.carie_coroa_41,
                    exame.carie_tratamento_41,
                    exame.carie_coroa_42,
                    exame.carie_tratamento_42,
                    exame.carie_coroa_43,
                    exame.carie_tratamento_43,
                    exame.carie_coroa_44,
                    exame.carie_tratamento_44,
                    exame.carie_coroa_45,
                    exame.carie_tratamento_45,
                    exame.carie_coroa_46,
                    exame.carie_tratamento_46,
                    exame.carie_coroa_47,
                    exame.carie_tratamento_47,
                    exame.carie_coroa_48,
                    exame.carie_tratamento_48,
                    exame.periodontal_sangramento_1716,
                    exame.periodontal_calculo_1716,
                    exame.periodontal_bolsa_1716,
                    exame.periodontal_sangramento_11,
                    exame.periodontal_calculo_11,
                    exame.periodontal_bolsa_11,
                    exame.periodontal_sangramento_2627,
                    exame.periodontal_calculo_2627,
                    exame.periodontal_bolsa_2627,
                    exame.periodontal_sangramento_3736,
                    exame.periodontal_calculo_3736,
                    exame.periodontal_bolsa_3736,
                    exame.periodontal_sangramento_31,
                    exame.periodontal_calculo_31,
                    exame.periodontal_bolsa_31,
                    exame.periodontal_sangramento_4647,
                    exame.periodontal_calculo_4647,
                    exame.periodontal_bolsa_4647,
                    resultados["cpod"],
                ])
            
            if not tem_questionario and not tem_exame:
                writer.writerow([
                    aluno.escola.acao.campanha.nome,
                    
                    aluno.escola.acao.nome,
                    
                    aluno.escola.id,
                    aluno.escola.nome,
                    aluno.escola.latitude,
                    aluno.escola.longitude,
                    
                    aluno.numero_identificacao,
                    aluno.periodo,
                    aluno.turma,
                    aluno.nascimento,
                    aluno.sexo,
                    aluno.raca,
                    
                    diretor.data,
                    diretor.questao_1,
                    diretor.questao_2,
                    diretor.questao_3,
                    diretor.questao_4,
                    diretor.questao_5,
                    diretor.questao_6,
                    diretor.questao_7,
                    diretor.questao_8,
                    diretor.questao_9,
                    diretor.questao_10,
                    diretor.questao_11,
                    diretor.questao_12,
                    diretor.questao_13,
                    diretor.questao_14,
                    diretor.questao_15,
                    diretor.questao_16,
                    diretor.questao_17,
                    diretor.questao_18,
                    diretor.questao_19,
                    diretor.questao_20,
                    diretor.questao_21,
                    diretor.questao_22,
                    diretor.questao_23,
                    diretor.questao_24,
                    diretor.questao_25,
                    diretor.questao_26,
                    diretor.questao_27,
                    diretor.questao_28,
                    diretor.questao_29,
                    diretor.questao_30,
                    diretor.questao_31,
                    diretor.questao_32,
                    diretor.questao_33,
                    diretor.questao_34,
                    diretor.questao_35,
                    diretor.questao_36,
                    diretor.questao_37,
                    diretor.questao_38,
                    diretor.questao_39,
                    diretor.questao_40,
                    diretor.questao_41,
                    diretor.questao_42,
                    diretor.questao_43,
                    diretor.questao_44,
                    diretor.questao_45,
                    diretor.questao_46,
                    diretor.questao_47,
                    diretor.questao_48,
                    diretor.questao_49,
                    diretor.questao_50,
                    diretor.questao_51,
                    diretor.questao_52,
                    diretor.questao_53,
                    diretor.questao_54,
                    diretor.questao_55,
                    diretor.questao_56,
                    diretor.questao_57,
                    diretor.questao_58,
                    diretor.questao_59,
                    diretor.questao_60,
                    diretor.questao_61,
                    diretor.questao_62,
                    diretor.questao_63,
                    diretor.questao_64,
                    diretor.questao_65,
                    diretor.questao_66,
                    diretor.questao_67,
                    diretor.questao_68,
                    diretor.questao_69,
                    diretor.questao_70,
                    diretor.questao_71,
                    diretor.questao_72,
                    diretor.questao_73,
                    diretor.questao_74,
                    diretor.questao_75,
                    diretor.questao_76,
                    diretor.questao_77,
                    diretor.questao_78,
                    diretor.questao_79,
                    diretor.questao_80,
                    diretor.questao_81,
                    diretor.questao_82,
                    diretor.questao_83,
                    diretor.questao_84,
                    
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                ])
        
        return response


class DownloadAlunoQuestionarioExameView(LoginRequired, View):
    """Gera e envia o arquivo csv para os alunos que fizeram o questionário e o exame"""
    
    def get(self, request):
        alunos = Aluno.objects.order_by('id')
        
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="aluno_questionario_exame.csv"'

        writer = csv.writer(response, delimiter=';')        
        writer.writerow(['escola.nome', 'aluno.numero_identificacao', 'aluno.periodo', 'aluno.turma', 'aluno.nascimento', 'aluno.sexo', 'aluno.raca', 'questionario.data', 'questionario.questao_1', 'questionario.questao_2', 'questionario.questao_3', 'questionario.questao_4', 'questionario.questao_5', 'questionario.questao_6', 'questionario.questao_7', 'questionario.questao_8', 'questionario.questao_9', 'questionario.questao_10', 'questionario.questao_11', 'questionario.questao_12', 'questionario.questao_13', 'questionario.questao_14', 'questionario.questao_15', 'questionario.questao_16', 'questionario.questao_17', 'questionario.questao_18', 'questionario.questao_19', 'questionario.questao_20', 'questionario.questao_21', 'questionario.questao_22', 'questionario.questao_23', 'questionario.questao_24', 'questionario.questao_25', 'questionario.questao_26', 'questionario.questao_27', 'questionario.questao_28', 'questionario.questao_29', 'questionario.questao_30', 'questionario.questao_31', 'questionario.questao_32', 'questionario.questao_33', 'questionario.questao_34', 'questionario.questao_35', 'questionario.questao_36', 'questionario.questao_37', 'questionario.questao_38', 'questionario.questao_39', 'questionario.questao_40', 'questionario.questao_41', 'questionario.questao_42', 'questionario.questao_43', 'questionario.questao_44', 'questionario.questao_45', 'questionario.questao_46', 'questionario.questao_47', 'questionario.questao_48', 'questionario.questao_49', 'questionario.questao_50', 'questionario.questao_51', 'questionario.questao_52', 'questionario.questao_53', 'questionario.questao_54', 'questionario.questao_55', 'questionario.questao_56', 'questionario.questao_57', 'questionario.questao_58', 'questionario.questao_59', 'questionario.questao_60', 'questionario.questao_61', 'questionario.questao_62', 'questionario.questao_63', 'questionario.questao_64', 'questionario.questao_65', 'questionario.questao_66', 'questionario.questao_67', 'questionario.questao_68', 'questionario.questao_69', 'questionario.questao_70', 'questionario.questao_71', 'questionario.questao_72', 'questionario.questao_73', 'questionario.questao_74', 'questionario.questao_75', 'questionario.questao_76', 'questionario.questao_77', 'questionario.questao_78', 'questionario.questao_79', 'questionario.questao_80', 'questionario.questao_81', 'questionario.questao_82', 'questionario.questao_83', 'questionario.questao_84', 'questionario.questao_85', 'questionario.questao_86', 'questionario.questao_87', 'questionario.questao_88', 'questionario.questao_89', 'questionario.questao_90', 'questionario.questao_91', 'questionario.questao_92', 'questionario.questao_93', 'questionario.questao_94', 'questionario.questao_95', 'questionario.questao_96', 'questionario.questao_97', 'questionario.questao_98', 'questionario.questao_99', 'questionario.questao_100', 'questionario.questao_101', 'questionario.questao_102', 'questionario.questao_103', 'questionario.questao_104', 'questionario.questao_105', 'questionario.questao_106', 'questionario.questao_107', 'questionario.questao_108', 'questionario.questao_109', 'questionario.questao_110', 'questionario.questao_111', 'questionario.questao_112', 'questionario.questao_113', 'questionario.questao_114', 'questionario.questao_115', 'questionario.questao_116', 'questionario.questao_117', 'questionario.questao_118', 'questionario.questao_119', 'questionario.questao_120', 'questionario.questao_121', 'questionario.questao_122', 'questionario.questao_123', 'questionario.questao_124', 'questionario.questao_125', 'questionario.questao_126', 'questionario.questao_127', 'questionario.questao_128', 'questionario.questao_129', 'questionario.questao_130', 'questionario.questao_131', 'questionario.questao_132', 'questionario.questao_133', 'questionario.questao_134', 'questionario.questao_135', 'questionario.questao_136', 'questionario.questao_137', 'questionario.questao_138', 'questionario.questao_139', 'questionario.questao_140', 'questionario.questao_141', 'questionario.questao_142', 'questionario.questao_143', 'questionario.questao_144', 'questionario.questao_145', 'questionario.questao_146', 'exame.data', 'exame.examinador', 'exame.anotador', 'exame.carie_coroa_18', 'exame.carie_tratamento_18', 'exame.carie_coroa_17', 'exame.carie_tratamento_17', 'exame.carie_coroa_16', 'exame.carie_tratamento_16', 'exame.carie_coroa_15', 'exame.carie_tratamento_15', 'exame.carie_coroa_14', 'exame.carie_tratamento_14', 'exame.carie_coroa_13', 'exame.carie_tratamento_13', 'exame.carie_coroa_12', 'exame.carie_tratamento_12', 'exame.carie_coroa_11', 'exame.carie_tratamento_11', 'exame.carie_coroa_21', 'exame.carie_tratamento_21', 'exame.carie_coroa_22', 'exame.carie_tratamento_22', 'exame.carie_coroa_23', 'exame.carie_tratamento_23', 'exame.carie_coroa_24', 'exame.carie_tratamento_24', 'exame.carie_coroa_25', 'exame.carie_tratamento_25', 'exame.carie_coroa_26', 'exame.carie_tratamento_26', 'exame.carie_coroa_27', 'exame.carie_tratamento_27', 'exame.carie_coroa_28', 'exame.carie_tratamento_28', 'exame.carie_coroa_38', 'exame.carie_tratamento_38', 'exame.carie_coroa_37', 'exame.carie_tratamento_37', 'exame.carie_coroa_36', 'exame.carie_tratamento_36', 'exame.carie_coroa_35', 'exame.carie_tratamento_35', 'exame.carie_coroa_34', 'exame.carie_tratamento_34', 'exame.carie_coroa_33', 'exame.carie_tratamento_33', 'exame.carie_coroa_32', 'exame.carie_tratamento_32', 'exame.carie_coroa_31', 'exame.carie_tratamento_31', 'exame.carie_coroa_41', 'exame.carie_tratamento_41', 'exame.carie_coroa_42', 'exame.carie_tratamento_42', 'exame.carie_coroa_43', 'exame.carie_tratamento_43', 'exame.carie_coroa_44', 'exame.carie_tratamento_44', 'exame.carie_coroa_45', 'exame.carie_tratamento_45', 'exame.carie_coroa_46', 'exame.carie_tratamento_46', 'exame.carie_coroa_47', 'exame.carie_tratamento_47', 'exame.carie_coroa_48', 'exame.carie_tratamento_48', 'exame.periodontal_sangramento_1716', 'exame.periodontal_calculo_1716', 'exame.periodontal_bolsa_1716', 'exame.periodontal_sangramento_11', 'exame.periodontal_calculo_11', 'exame.periodontal_bolsa_11', 'exame.periodontal_sangramento_2627', 'exame.periodontal_calculo_2627', 'exame.periodontal_bolsa_2627', 'exame.periodontal_sangramento_3736', 'exame.periodontal_calculo_3736', 'exame.periodontal_bolsa_3736', 'exame.periodontal_sangramento_31', 'exame.periodontal_calculo_31', 'exame.periodontal_bolsa_31', 'exame.periodontal_sangramento_4647', 'exame.periodontal_calculo_4647', 'exame.periodontal_bolsa_4647',])
        
        for aluno in alunos:
            try:
                questionario = Questionario.objects.get(aluno_id=aluno.id)
                exame = Exame.objects.get(aluno_id=aluno.id)
            except:
                continue
            
            writer.writerow([
                aluno.escola.nome,
                
                aluno.numero_identificacao,
                aluno.periodo, # get__display()
                aluno.turma,
                aluno.nascimento,
                aluno.sexo, # get__display()
                aluno.raca, # get__display()
                
                questionario.data,
                questionario.questao_1, # get__display()
                questionario.questao_2, # get__display()
                questionario.questao_3, # get__display()
                questionario.questao_4, # get__display()
                questionario.questao_5, # get__display()
                questionario.questao_6, # get__display()
                questionario.questao_7, # get__display()
                questionario.questao_8, # get__display()
                questionario.questao_9, # get__display()
                questionario.questao_10, # get__display()
                questionario.questao_11, # get__display()
                questionario.questao_12, # get__display()
                questionario.questao_13, # get__display()
                questionario.questao_14, # get__display()
                questionario.questao_15, # get__display()
                questionario.questao_16, # get__display()
                questionario.questao_17, # get__display()
                questionario.questao_18, # get__display()
                questionario.questao_19, # get__display()
                questionario.questao_20, # get__display()
                questionario.questao_21, # get__display()
                questionario.questao_22, # get__display()
                questionario.questao_23, # get__display()
                questionario.questao_24, # get__display()
                questionario.questao_25, # get__display()
                questionario.questao_26, # get__display()
                questionario.questao_27, # get__display()
                questionario.questao_28, # get__display()
                questionario.questao_29, # get__display()
                questionario.questao_30, # get__display()
                questionario.questao_31, # get__display()
                questionario.questao_32, # get__display()
                questionario.questao_33, # get__display()
                questionario.questao_34, # get__display()
                questionario.questao_35, # get__display()
                questionario.questao_36, # get__display()
                questionario.questao_37, # get__display()
                questionario.questao_38, # get__display()
                questionario.questao_39, # get__display()
                questionario.questao_40, # get__display()
                questionario.questao_41, # get__display()
                questionario.questao_42, # get__display()
                questionario.questao_43, # get__display()
                questionario.questao_44, # get__display()
                questionario.questao_45, # get__display()
                questionario.questao_46, # get__display()
                questionario.questao_47, # get__display()
                questionario.questao_48, # get__display()
                questionario.questao_49, # get__display()
                questionario.questao_50, # get__display()
                questionario.questao_51, # get__display()
                questionario.questao_52, # get__display()
                questionario.questao_53, # get__display()
                questionario.questao_54, # get__display()
                questionario.questao_55, # get__display()
                questionario.questao_56, # get__display()
                questionario.questao_57, # get__display()
                questionario.questao_58, # get__display()
                questionario.questao_59, # get__display()
                questionario.questao_60,
                questionario.questao_61, # get__display()
                questionario.questao_62, # get__display()
                questionario.questao_63, # get__display()
                questionario.questao_64, # get__display()
                questionario.questao_65, # get__display()
                questionario.questao_66, # get__display()
                questionario.questao_67, # get__display()
                questionario.questao_68, # get__display()
                questionario.questao_69, # get__display()
                questionario.questao_70, # get__display()
                questionario.questao_71, # get__display()
                questionario.questao_72, # get__display()
                questionario.questao_73, # get__display()
                questionario.questao_74, # get__display()
                questionario.questao_75, # get__display()
                questionario.questao_76, # get__display()
                questionario.questao_77, # get__display()
                questionario.questao_78, # get__display()
                questionario.questao_79, # get__display()
                questionario.questao_80, # get__display()
                questionario.questao_81, # get__display()
                questionario.questao_82, # get__display()
                questionario.questao_83, # get__display()
                questionario.questao_84, # get__display()
                questionario.questao_85, # get__display()
                questionario.questao_86, # get__display()
                questionario.questao_87, # get__display()
                questionario.questao_88, # get__display()
                questionario.questao_89, # get__display()
                questionario.questao_90, # get__display()
                questionario.questao_91, # get__display()
                questionario.questao_92, # get__display()
                questionario.questao_93, # get__display()
                questionario.questao_94, # get__display()
                questionario.questao_95, # get__display()
                questionario.questao_96, # get__display()
                questionario.questao_97, # get__display()
                questionario.questao_98, # get__display()
                questionario.questao_99, # get__display()
                questionario.questao_100, # get__display()
                questionario.questao_101, # get__display()
                questionario.questao_102, # get__display()
                questionario.questao_103, # get__display()
                questionario.questao_104, # get__display()
                questionario.questao_105, # get__display()
                questionario.questao_106, # get__display()
                questionario.questao_107, # get__display()
                questionario.questao_108, # get__display()
                questionario.questao_109, # get__display()
                questionario.questao_110, # get__display()
                questionario.questao_111, # get__display()
                questionario.questao_112, # get__display()
                questionario.questao_113, # get__display()
                questionario.questao_114, # get__display()
                questionario.questao_115, # get__display()
                questionario.questao_116, # get__display()
                questionario.questao_117, # get__display()
                questionario.questao_118, # get__display()
                questionario.questao_119, # get__display()
                questionario.questao_120, # get__display()
                questionario.questao_121, # get__display()
                questionario.questao_122, # get__display()
                questionario.questao_123, # get__display()
                questionario.questao_124, # get__display()
                questionario.questao_125, # get__display()
                questionario.questao_126, # get__display()
                questionario.questao_127, # get__display()
                questionario.questao_128, # get__display()
                questionario.questao_129, # get__display()
                questionario.questao_130, # get__display()
                questionario.questao_131, # get__display()
                questionario.questao_132, # get__display()
                questionario.questao_133, # get__display()
                questionario.questao_134, # get__display()
                questionario.questao_135, # get__display()
                questionario.questao_136, # get__display()
                questionario.questao_137, # get__display()
                questionario.questao_138, # get__display()
                questionario.questao_139, # get__display()
                questionario.questao_140, # get__display()
                questionario.questao_141, # get__display()
                questionario.questao_142, # get__display()
                questionario.questao_143, # get__display()
                questionario.questao_144, # get__display()
                questionario.questao_145, # get__display()
                questionario.questao_146,
                
                exame.data,
                exame.examinador,
                exame.anotador,
                exame.carie_coroa_18,
                exame.carie_tratamento_18,
                exame.carie_coroa_17,
                exame.carie_tratamento_17,
                exame.carie_coroa_16,
                exame.carie_tratamento_16,
                exame.carie_coroa_15,
                exame.carie_tratamento_15,
                exame.carie_coroa_14,
                exame.carie_tratamento_14,
                exame.carie_coroa_13,
                exame.carie_tratamento_13,
                exame.carie_coroa_12,
                exame.carie_tratamento_12,
                exame.carie_coroa_11,
                exame.carie_tratamento_11,
                exame.carie_coroa_21,
                exame.carie_tratamento_21,
                exame.carie_coroa_22,
                exame.carie_tratamento_22,
                exame.carie_coroa_23,
                exame.carie_tratamento_23,
                exame.carie_coroa_24,
                exame.carie_tratamento_24,
                exame.carie_coroa_25,
                exame.carie_tratamento_25,
                exame.carie_coroa_26,
                exame.carie_tratamento_26,
                exame.carie_coroa_27,
                exame.carie_tratamento_27,
                exame.carie_coroa_28,
                exame.carie_tratamento_28,
                exame.carie_coroa_38,
                exame.carie_tratamento_38,
                exame.carie_coroa_37,
                exame.carie_tratamento_37,
                exame.carie_coroa_36,
                exame.carie_tratamento_36,
                exame.carie_coroa_35,
                exame.carie_tratamento_35,
                exame.carie_coroa_34,
                exame.carie_tratamento_34,
                exame.carie_coroa_33,
                exame.carie_tratamento_33,
                exame.carie_coroa_32,
                exame.carie_tratamento_32,
                exame.carie_coroa_31,
                exame.carie_tratamento_31,
                exame.carie_coroa_41,
                exame.carie_tratamento_41,
                exame.carie_coroa_42,
                exame.carie_tratamento_42,
                exame.carie_coroa_43,
                exame.carie_tratamento_43,
                exame.carie_coroa_44,
                exame.carie_tratamento_44,
                exame.carie_coroa_45,
                exame.carie_tratamento_45,
                exame.carie_coroa_46,
                exame.carie_tratamento_46,
                exame.carie_coroa_47,
                exame.carie_tratamento_47,
                exame.carie_coroa_48,
                exame.carie_tratamento_48,
                exame.periodontal_sangramento_1716,
                exame.periodontal_calculo_1716,
                exame.periodontal_bolsa_1716,
                exame.periodontal_sangramento_11,
                exame.periodontal_calculo_11,
                exame.periodontal_bolsa_11,
                exame.periodontal_sangramento_2627,
                exame.periodontal_calculo_2627,
                exame.periodontal_bolsa_2627,
                exame.periodontal_sangramento_3736,
                exame.periodontal_calculo_3736,
                exame.periodontal_bolsa_3736,
                exame.periodontal_sangramento_31,
                exame.periodontal_calculo_31,
                exame.periodontal_bolsa_31,
                exame.periodontal_sangramento_4647,
                exame.periodontal_calculo_4647,
                exame.periodontal_bolsa_4647,
            ])
        
        return response


class DownloadListaCampanhasView(LoginRequired, View):
    """Gera e envia o arquivo csv da lista de campanhas"""
    
    def get(self, request):
        campanhas = Campanha.objects.order_by('id')
        
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="lista_campanhas.csv"'

        writer = csv.writer(response, delimiter=';')
        writer.writerow(['campanha.nome',])
        
        for campanha in campanhas:
            writer.writerow([
                campanha.nome,
            ])
        
        return response


class DownloadListaAcoesView(LoginRequired, View):
    """Gera e envia o arquivo csv da lista de ações"""
    
    def get(self, request):
        acoes = Acao.objects.order_by('id')
        
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="lista_acoes.csv"'

        writer = csv.writer(response, delimiter=';')
        writer.writerow(['acao.nome',])
        
        for acao in acoes:
            writer.writerow([
                acao.nome,
            ])
        
        return response


class DownloadListaEscolasView(LoginRequired, View):
    """Gera e envia o arquivo csv da lista de escolas"""
    
    def get(self, request):
        escolas = Escola.objects.order_by('id')
        
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="lista_escolas.csv"'

        writer = csv.writer(response, delimiter=';')
        writer.writerow(['escola.nome', 'escola.latitude', 'escola.longitude'])
        
        for escola in escolas:
            writer.writerow([
                escola.nome,
                escola.latitude,
                escola.longitude,
            ])
        
        return response


class DownloadListaAlunosView(LoginRequired, View):
    """Gera e envia o arquivo csv da lista de alunos"""
    
    def get(self, request):
        alunos = Aluno.objects.order_by('id')
        
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="lista_alunos.csv"'

        writer = csv.writer(response, delimiter=';')
        writer.writerow(['aluno.escola.nome', 'aluno.numero_identificacao', 'aluno.periodo', 'aluno.turma', 'aluno.nascimento', 'aluno.sexo', 'aluno.raca',])
        
        for aluno in alunos:
            writer.writerow([
                aluno.escola.nome,
                
                aluno.numero_identificacao,
                aluno.periodo, # get__display()
                aluno.turma,
                aluno.nascimento,
                aluno.sexo, # get__display()
                aluno.raca, # get__display()
            ])
        
        return response


class DownloadListaQuestionariosView(LoginRequired, View):
    """Gera e envia o arquivo csv da lista de questionários"""
    
    def get(self, request):
        questionarios = Questionario.objects.order_by('id')
        
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="lista_questionarios.csv"'

        writer = csv.writer(response, delimiter=';')
        writer.writerow(['aluno.numero_identificacao', 'questionario.data', 'questionario.questao_1', 'questionario.questao_2', 'questionario.questao_3', 'questionario.questao_4', 'questionario.questao_5', 'questionario.questao_6', 'questionario.questao_7', 'questionario.questao_8', 'questionario.questao_9', 'questionario.questao_10', 'questionario.questao_11', 'questionario.questao_12', 'questionario.questao_13', 'questionario.questao_14', 'questionario.questao_15', 'questionario.questao_16', 'questionario.questao_17', 'questionario.questao_18', 'questionario.questao_19', 'questionario.questao_20', 'questionario.questao_21', 'questionario.questao_22', 'questionario.questao_23', 'questionario.questao_24', 'questionario.questao_25', 'questionario.questao_26', 'questionario.questao_27', 'questionario.questao_28', 'questionario.questao_29', 'questionario.questao_30', 'questionario.questao_31', 'questionario.questao_32', 'questionario.questao_33', 'questionario.questao_34', 'questionario.questao_35', 'questionario.questao_36', 'questionario.questao_37', 'questionario.questao_38', 'questionario.questao_39', 'questionario.questao_40', 'questionario.questao_41', 'questionario.questao_42', 'questionario.questao_43', 'questionario.questao_44', 'questionario.questao_45', 'questionario.questao_46', 'questionario.questao_47', 'questionario.questao_48', 'questionario.questao_49', 'questionario.questao_50', 'questionario.questao_51', 'questionario.questao_52', 'questionario.questao_53', 'questionario.questao_54', 'questionario.questao_55', 'questionario.questao_56', 'questionario.questao_57', 'questionario.questao_58', 'questionario.questao_59', 'questionario.questao_60', 'questionario.questao_61', 'questionario.questao_62', 'questionario.questao_63', 'questionario.questao_64', 'questionario.questao_65', 'questionario.questao_66', 'questionario.questao_67', 'questionario.questao_68', 'questionario.questao_69', 'questionario.questao_70', 'questionario.questao_71', 'questionario.questao_72', 'questionario.questao_73', 'questionario.questao_74', 'questionario.questao_75', 'questionario.questao_76', 'questionario.questao_77', 'questionario.questao_78', 'questionario.questao_79', 'questionario.questao_80', 'questionario.questao_81', 'questionario.questao_82', 'questionario.questao_83', 'questionario.questao_84', 'questionario.questao_85', 'questionario.questao_86', 'questionario.questao_87', 'questionario.questao_88', 'questionario.questao_89', 'questionario.questao_90', 'questionario.questao_91', 'questionario.questao_92', 'questionario.questao_93', 'questionario.questao_94', 'questionario.questao_95', 'questionario.questao_96', 'questionario.questao_97', 'questionario.questao_98', 'questionario.questao_99', 'questionario.questao_100', 'questionario.questao_101', 'questionario.questao_102', 'questionario.questao_103', 'questionario.questao_104', 'questionario.questao_105', 'questionario.questao_106', 'questionario.questao_107', 'questionario.questao_108', 'questionario.questao_109', 'questionario.questao_110', 'questionario.questao_111', 'questionario.questao_112', 'questionario.questao_113', 'questionario.questao_114', 'questionario.questao_115', 'questionario.questao_116', 'questionario.questao_117', 'questionario.questao_118', 'questionario.questao_119', 'questionario.questao_120', 'questionario.questao_121', 'questionario.questao_122', 'questionario.questao_123', 'questionario.questao_124', 'questionario.questao_125', 'questionario.questao_126', 'questionario.questao_127', 'questionario.questao_128', 'questionario.questao_129', 'questionario.questao_130', 'questionario.questao_131', 'questionario.questao_132', 'questionario.questao_133', 'questionario.questao_134', 'questionario.questao_135', 'questionario.questao_136', 'questionario.questao_137', 'questionario.questao_138', 'questionario.questao_139', 'questionario.questao_140', 'questionario.questao_141', 'questionario.questao_142', 'questionario.questao_143', 'questionario.questao_144', 'questionario.questao_145', 'questionario.questao_146', ])
        
        for questionario in questionarios:
            writer.writerow([
                questionario.aluno.numero_identificacao,
                
                questionario.data,
                questionario.questao_1, # get__display()
                questionario.questao_2, # get__display()
                questionario.questao_3, # get__display()
                questionario.questao_4, # get__display()
                questionario.questao_5, # get__display()
                questionario.questao_6, # get__display()
                questionario.questao_7, # get__display()
                questionario.questao_8, # get__display()
                questionario.questao_9, # get__display()
                questionario.questao_10, # get__display()
                questionario.questao_11, # get__display()
                questionario.questao_12, # get__display()
                questionario.questao_13, # get__display()
                questionario.questao_14, # get__display()
                questionario.questao_15, # get__display()
                questionario.questao_16, # get__display()
                questionario.questao_17, # get__display()
                questionario.questao_18, # get__display()
                questionario.questao_19, # get__display()
                questionario.questao_20, # get__display()
                questionario.questao_21, # get__display()
                questionario.questao_22, # get__display()
                questionario.questao_23, # get__display()
                questionario.questao_24, # get__display()
                questionario.questao_25, # get__display()
                questionario.questao_26, # get__display()
                questionario.questao_27, # get__display()
                questionario.questao_28, # get__display()
                questionario.questao_29, # get__display()
                questionario.questao_30, # get__display()
                questionario.questao_31, # get__display()
                questionario.questao_32, # get__display()
                questionario.questao_33, # get__display()
                questionario.questao_34, # get__display()
                questionario.questao_35, # get__display()
                questionario.questao_36, # get__display()
                questionario.questao_37, # get__display()
                questionario.questao_38, # get__display()
                questionario.questao_39, # get__display()
                questionario.questao_40, # get__display()
                questionario.questao_41, # get__display()
                questionario.questao_42, # get__display()
                questionario.questao_43, # get__display()
                questionario.questao_44, # get__display()
                questionario.questao_45, # get__display()
                questionario.questao_46, # get__display()
                questionario.questao_47, # get__display()
                questionario.questao_48, # get__display()
                questionario.questao_49, # get__display()
                questionario.questao_50, # get__display()
                questionario.questao_51, # get__display()
                questionario.questao_52, # get__display()
                questionario.questao_53, # get__display()
                questionario.questao_54, # get__display()
                questionario.questao_55, # get__display()
                questionario.questao_56, # get__display()
                questionario.questao_57, # get__display()
                questionario.questao_58, # get__display()
                questionario.questao_59, # get__display()
                questionario.questao_60,
                questionario.questao_61, # get__display()
                questionario.questao_62, # get__display()
                questionario.questao_63, # get__display()
                questionario.questao_64, # get__display()
                questionario.questao_65, # get__display()
                questionario.questao_66, # get__display()
                questionario.questao_67, # get__display()
                questionario.questao_68, # get__display()
                questionario.questao_69, # get__display()
                questionario.questao_70, # get__display()
                questionario.questao_71, # get__display()
                questionario.questao_72, # get__display()
                questionario.questao_73, # get__display()
                questionario.questao_74, # get__display()
                questionario.questao_75, # get__display()
                questionario.questao_76, # get__display()
                questionario.questao_77, # get__display()
                questionario.questao_78, # get__display()
                questionario.questao_79, # get__display()
                questionario.questao_80, # get__display()
                questionario.questao_81, # get__display()
                questionario.questao_82, # get__display()
                questionario.questao_83, # get__display()
                questionario.questao_84, # get__display()
                questionario.questao_85, # get__display()
                questionario.questao_86, # get__display()
                questionario.questao_87, # get__display()
                questionario.questao_88, # get__display()
                questionario.questao_89, # get__display()
                questionario.questao_90, # get__display()
                questionario.questao_91, # get__display()
                questionario.questao_92, # get__display()
                questionario.questao_93, # get__display()
                questionario.questao_94, # get__display()
                questionario.questao_95, # get__display()
                questionario.questao_96, # get__display()
                questionario.questao_97, # get__display()
                questionario.questao_98, # get__display()
                questionario.questao_99, # get__display()
                questionario.questao_100, # get__display()
                questionario.questao_101, # get__display()
                questionario.questao_102, # get__display()
                questionario.questao_103, # get__display()
                questionario.questao_104, # get__display()
                questionario.questao_105, # get__display()
                questionario.questao_106, # get__display()
                questionario.questao_107, # get__display()
                questionario.questao_108, # get__display()
                questionario.questao_109, # get__display()
                questionario.questao_110, # get__display()
                questionario.questao_111, # get__display()
                questionario.questao_112, # get__display()
                questionario.questao_113, # get__display()
                questionario.questao_114, # get__display()
                questionario.questao_115, # get__display()
                questionario.questao_116, # get__display()
                questionario.questao_117, # get__display()
                questionario.questao_118, # get__display()
                questionario.questao_119, # get__display()
                questionario.questao_120, # get__display()
                questionario.questao_121, # get__display()
                questionario.questao_122, # get__display()
                questionario.questao_123, # get__display()
                questionario.questao_124, # get__display()
                questionario.questao_125, # get__display()
                questionario.questao_126, # get__display()
                questionario.questao_127, # get__display()
                questionario.questao_128, # get__display()
                questionario.questao_129, # get__display()
                questionario.questao_130, # get__display()
                questionario.questao_131, # get__display()
                questionario.questao_132, # get__display()
                questionario.questao_133, # get__display()
                questionario.questao_134, # get__display()
                questionario.questao_135, # get__display()
                questionario.questao_136, # get__display()
                questionario.questao_137, # get__display()
                questionario.questao_138, # get__display()
                questionario.questao_139, # get__display()
                questionario.questao_140, # get__display()
                questionario.questao_141, # get__display()
                questionario.questao_142, # get__display()
                questionario.questao_143, # get__display()
                questionario.questao_144, # get__display()
                questionario.questao_145, # get__display()
                questionario.questao_146,
            ])
        
        return response


class DownloadListaExamesView(LoginRequired, View):
    """Gera e envia o arquivo csv da lista de exames"""
    
    def get(self, request):
        exames = Exame.objects.order_by('id')
        
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="lista_exames.csv"'

        writer = csv.writer(response, delimiter=';')
        writer.writerow(['aluno.numero_identificacao', 'exame.data', 'exame.examinador', 'exame.anotador', 'exame.carie_coroa_18', 'exame.carie_tratamento_18', 'exame.carie_coroa_17', 'exame.carie_tratamento_17', 'exame.carie_coroa_16', 'exame.carie_tratamento_16', 'exame.carie_coroa_15', 'exame.carie_tratamento_15', 'exame.carie_coroa_14', 'exame.carie_tratamento_14', 'exame.carie_coroa_13', 'exame.carie_tratamento_13', 'exame.carie_coroa_12', 'exame.carie_tratamento_12', 'exame.carie_coroa_11', 'exame.carie_tratamento_11', 'exame.carie_coroa_21', 'exame.carie_tratamento_21', 'exame.carie_coroa_22', 'exame.carie_tratamento_22', 'exame.carie_coroa_23', 'exame.carie_tratamento_23', 'exame.carie_coroa_24', 'exame.carie_tratamento_24', 'exame.carie_coroa_25', 'exame.carie_tratamento_25', 'exame.carie_coroa_26', 'exame.carie_tratamento_26', 'exame.carie_coroa_27', 'exame.carie_tratamento_27', 'exame.carie_coroa_28', 'exame.carie_tratamento_28', 'exame.carie_coroa_38', 'exame.carie_tratamento_38', 'exame.carie_coroa_37', 'exame.carie_tratamento_37', 'exame.carie_coroa_36', 'exame.carie_tratamento_36', 'exame.carie_coroa_35', 'exame.carie_tratamento_35', 'exame.carie_coroa_34', 'exame.carie_tratamento_34', 'exame.carie_coroa_33', 'exame.carie_tratamento_33', 'exame.carie_coroa_32', 'exame.carie_tratamento_32', 'exame.carie_coroa_31', 'exame.carie_tratamento_31', 'exame.carie_coroa_41', 'exame.carie_tratamento_41', 'exame.carie_coroa_42', 'exame.carie_tratamento_42', 'exame.carie_coroa_43', 'exame.carie_tratamento_43', 'exame.carie_coroa_44', 'exame.carie_tratamento_44', 'exame.carie_coroa_45', 'exame.carie_tratamento_45', 'exame.carie_coroa_46', 'exame.carie_tratamento_46', 'exame.carie_coroa_47', 'exame.carie_tratamento_47', 'exame.carie_coroa_48', 'exame.carie_tratamento_48', 'exame.periodontal_sangramento_1716', 'exame.periodontal_calculo_1716', 'exame.periodontal_bolsa_1716', 'exame.periodontal_sangramento_11', 'exame.periodontal_calculo_11', 'exame.periodontal_bolsa_11', 'exame.periodontal_sangramento_2627', 'exame.periodontal_calculo_2627', 'exame.periodontal_bolsa_2627', 'exame.periodontal_sangramento_3736', 'exame.periodontal_calculo_3736', 'exame.periodontal_bolsa_3736', 'exame.periodontal_sangramento_31', 'exame.periodontal_calculo_31', 'exame.periodontal_bolsa_31', 'exame.periodontal_sangramento_4647', 'exame.periodontal_calculo_4647', 'exame.periodontal_bolsa_4647',])
        
        for exame in exames:
            writer.writerow([
                exame.aluno.numero_identificacao,
                
                exame.data,
                exame.examinador,
                exame.anotador,
                exame.carie_coroa_18,
                exame.carie_tratamento_18,
                exame.carie_coroa_17,
                exame.carie_tratamento_17,
                exame.carie_coroa_16,
                exame.carie_tratamento_16,
                exame.carie_coroa_15,
                exame.carie_tratamento_15,
                exame.carie_coroa_14,
                exame.carie_tratamento_14,
                exame.carie_coroa_13,
                exame.carie_tratamento_13,
                exame.carie_coroa_12,
                exame.carie_tratamento_12,
                exame.carie_coroa_11,
                exame.carie_tratamento_11,
                exame.carie_coroa_21,
                exame.carie_tratamento_21,
                exame.carie_coroa_22,
                exame.carie_tratamento_22,
                exame.carie_coroa_23,
                exame.carie_tratamento_23,
                exame.carie_coroa_24,
                exame.carie_tratamento_24,
                exame.carie_coroa_25,
                exame.carie_tratamento_25,
                exame.carie_coroa_26,
                exame.carie_tratamento_26,
                exame.carie_coroa_27,
                exame.carie_tratamento_27,
                exame.carie_coroa_28,
                exame.carie_tratamento_28,
                exame.carie_coroa_38,
                exame.carie_tratamento_38,
                exame.carie_coroa_37,
                exame.carie_tratamento_37,
                exame.carie_coroa_36,
                exame.carie_tratamento_36,
                exame.carie_coroa_35,
                exame.carie_tratamento_35,
                exame.carie_coroa_34,
                exame.carie_tratamento_34,
                exame.carie_coroa_33,
                exame.carie_tratamento_33,
                exame.carie_coroa_32,
                exame.carie_tratamento_32,
                exame.carie_coroa_31,
                exame.carie_tratamento_31,
                exame.carie_coroa_41,
                exame.carie_tratamento_41,
                exame.carie_coroa_42,
                exame.carie_tratamento_42,
                exame.carie_coroa_43,
                exame.carie_tratamento_43,
                exame.carie_coroa_44,
                exame.carie_tratamento_44,
                exame.carie_coroa_45,
                exame.carie_tratamento_45,
                exame.carie_coroa_46,
                exame.carie_tratamento_46,
                exame.carie_coroa_47,
                exame.carie_tratamento_47,
                exame.carie_coroa_48,
                exame.carie_tratamento_48,
                exame.periodontal_sangramento_1716,
                exame.periodontal_calculo_1716,
                exame.periodontal_bolsa_1716,
                exame.periodontal_sangramento_11,
                exame.periodontal_calculo_11,
                exame.periodontal_bolsa_11,
                exame.periodontal_sangramento_2627,
                exame.periodontal_calculo_2627,
                exame.periodontal_bolsa_2627,
                exame.periodontal_sangramento_3736,
                exame.periodontal_calculo_3736,
                exame.periodontal_bolsa_3736,
                exame.periodontal_sangramento_31,
                exame.periodontal_calculo_31,
                exame.periodontal_bolsa_31,
                exame.periodontal_sangramento_4647,
                exame.periodontal_calculo_4647,
                exame.periodontal_bolsa_4647,
            ])
        
        return response


class DownloadListaDiretoresView(LoginRequired, View):
    """Gera e envia o arquivo csv da lista de questionários de diretores"""
    
    def get(self, request):
        diretores = Diretor.objects.order_by('id')
        
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="lista_diretores.csv"'

        writer = csv.writer(response, delimiter=';')
        writer.writerow(['escola.nome', 'diretor.data', 'diretor.questao_1', 'diretor.questao_2', 'diretor.questao_3', 'diretor.questao_4', 'diretor.questao_5', 'diretor.questao_6', 'diretor.questao_7', 'diretor.questao_8', 'diretor.questao_9', 'diretor.questao_10', 'diretor.questao_11', 'diretor.questao_12', 'diretor.questao_13', 'diretor.questao_14', 'diretor.questao_15', 'diretor.questao_16', 'diretor.questao_17', 'diretor.questao_18', 'diretor.questao_19', 'diretor.questao_20', 'diretor.questao_21', 'diretor.questao_22', 'diretor.questao_23', 'diretor.questao_24', 'diretor.questao_25', 'diretor.questao_26', 'diretor.questao_27', 'diretor.questao_28', 'diretor.questao_29', 'diretor.questao_30', 'diretor.questao_31', 'diretor.questao_32', 'diretor.questao_33', 'diretor.questao_34', 'diretor.questao_35', 'diretor.questao_36', 'diretor.questao_37', 'diretor.questao_38', 'diretor.questao_39', 'diretor.questao_40', 'diretor.questao_41', 'diretor.questao_42', 'diretor.questao_43', 'diretor.questao_44', 'diretor.questao_45', 'diretor.questao_46', 'diretor.questao_47', 'diretor.questao_48', 'diretor.questao_49', 'diretor.questao_50', 'diretor.questao_51', 'diretor.questao_52', 'diretor.questao_53', 'diretor.questao_54', 'diretor.questao_55', 'diretor.questao_56', 'diretor.questao_57', 'diretor.questao_58', 'diretor.questao_59', 'diretor.questao_60', 'diretor.questao_61', 'diretor.questao_62', 'diretor.questao_63', 'diretor.questao_64', 'diretor.questao_65', 'diretor.questao_66', 'diretor.questao_67', 'diretor.questao_68', 'diretor.questao_69', 'diretor.questao_70', 'diretor.questao_71', 'diretor.questao_72', 'diretor.questao_73', 'diretor.questao_74', 'diretor.questao_75', 'diretor.questao_76', 'diretor.questao_77', 'diretor.questao_78', 'diretor.questao_79', 'diretor.questao_80', 'diretor.questao_81', 'diretor.questao_82', 'diretor.questao_83', 'diretor.questao_84',])
        
        for diretor in diretores:
            writer.writerow([
                diretor.escola.nome,
                diretor.data,
                diretor.questao_1,
                diretor.questao_2, # get__display()
                diretor.questao_3,
                diretor.questao_4, # get__display()
                diretor.questao_5, # get__display()
                diretor.questao_6, # get__display()
                diretor.questao_7, # get__display()
                diretor.questao_8, # get__display()
                diretor.questao_9, # get__display()
                diretor.questao_10, # get__display()
                diretor.questao_11, # get__display()
                diretor.questao_12, # get__display()
                diretor.questao_13, # get__display()
                diretor.questao_14, # get__display()
                diretor.questao_15, # get__display()
                diretor.questao_16, # get__display()
                diretor.questao_17, # get__display()
                diretor.questao_18, # get__display()
                diretor.questao_19, # get__display()
                diretor.questao_20, # get__display()
                diretor.questao_21, # get__display()
                diretor.questao_22, # get__display()
                diretor.questao_23, # get__display()
                diretor.questao_24, # get__display()
                diretor.questao_25, # get__display()
                diretor.questao_26, # get__display()
                diretor.questao_27, # get__display()
                diretor.questao_28,
                diretor.questao_29, # get__display()
                diretor.questao_30, # get__display()
                diretor.questao_31,
                diretor.questao_32, # get__display()
                diretor.questao_33,
                diretor.questao_34, # get__display()
                diretor.questao_35, # get__display()
                diretor.questao_36, # get__display()
                diretor.questao_37,
                diretor.questao_38, # get__display()
                diretor.questao_39,
                diretor.questao_40, # get__display()
                diretor.questao_41, # get__display()
                diretor.questao_42, # get__display()
                diretor.questao_43, # get__display()
                diretor.questao_44, # get__display()
                diretor.questao_45, # get__display()
                diretor.questao_46, # get__display()
                diretor.questao_47, # get__display()
                diretor.questao_48, # get__display()
                diretor.questao_49, # get__display()
                diretor.questao_50, # get__display()
                diretor.questao_51, # get__display()
                diretor.questao_52, # get__display()
                diretor.questao_53, # get__display()
                diretor.questao_54, # get__display()
                diretor.questao_55, # get__display()
                diretor.questao_56, # get__display()
                diretor.questao_57, # get__display()
                diretor.questao_58, # get__display()
                diretor.questao_59, # get__display()
                diretor.questao_60, # get__display()
                diretor.questao_61, # get__display()
                diretor.questao_62, # get__display()
                diretor.questao_63, # get__display()
                diretor.questao_64, # get__display()
                diretor.questao_65, # get__display()
                diretor.questao_66, # get__display()
                diretor.questao_67, # get__display()
                diretor.questao_68, # get__display()
                diretor.questao_69, # get__display()
                diretor.questao_70, # get__display()
                diretor.questao_71, # get__display()
                diretor.questao_72, # get__display()
                diretor.questao_73, # get__display()
                diretor.questao_74, # get__display()
                diretor.questao_75, # get__display()
                diretor.questao_76, # get__display()
                diretor.questao_77, # get__display()
                diretor.questao_78, # get__display()
                diretor.questao_79, # get__display()
                diretor.questao_80, # get__display()
                diretor.questao_81, # get__display()
                diretor.questao_82, # get__display()
                diretor.questao_83, # get__display()
                diretor.questao_84, # get__display()
            ])
        
        return response
