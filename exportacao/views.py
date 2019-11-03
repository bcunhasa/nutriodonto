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
        writer.writerow(['campanha.nome', 'acao.nome', 'escola.nome', 'escola.latitude', 'escola.longitude', 'aluno.numero_identificacao', 'aluno.periodo', 'aluno.turma', 'aluno.nascimento', 'aluno.sexo', 'aluno.raca', 'questionario.data', 'questionario.questao_1', 'questionario.questao_2', 'questionario.questao_3', 'questionario.questao_4', 'questionario.questao_5', 'questionario.questao_6', 'questionario.questao_7', 'questionario.questao_8', 'questionario.questao_9', 'questionario.questao_10', 'questionario.questao_11', 'questionario.questao_12', 'questionario.questao_13', 'questionario.questao_14', 'questionario.questao_15', 'questionario.questao_16', 'questionario.questao_17', 'questionario.questao_18', 'questionario.questao_19', 'questionario.questao_20', 'questionario.questao_21', 'questionario.questao_22', 'questionario.questao_23', 'questionario.questao_24', 'questionario.questao_25', 'questionario.questao_26', 'questionario.questao_27', 'questionario.questao_28', 'questionario.questao_29', 'questionario.questao_30', 'questionario.questao_31', 'questionario.questao_32', 'questionario.questao_33', 'questionario.questao_34', 'questionario.questao_35', 'questionario.questao_36', 'questionario.questao_37', 'questionario.questao_38', 'questionario.questao_39', 'questionario.questao_40', 'questionario.questao_41', 'questionario.questao_42', 'questionario.questao_43', 'questionario.questao_44', 'questionario.questao_45', 'questionario.questao_46', 'questionario.questao_47', 'questionario.questao_48', 'questionario.questao_49', 'questionario.questao_50', 'questionario.questao_51', 'questionario.questao_52', 'questionario.questao_53', 'questionario.questao_54', 'questionario.questao_55', 'questionario.questao_56', 'questionario.questao_57', 'questionario.questao_58', 'questionario.questao_59', 'questionario.questao_60', 'questionario.questao_61', 'questionario.questao_62', 'questionario.questao_63', 'questionario.questao_64', 'questionario.questao_65', 'questionario.questao_66', 'questionario.questao_67', 'questionario.questao_68', 'questionario.questao_69', 'questionario.questao_70', 'questionario.questao_71', 'questionario.questao_72', 'questionario.questao_73', 'questionario.questao_74', 'questionario.questao_75', 'questionario.questao_76', 'questionario.questao_77', 'questionario.questao_78', 'questionario.questao_79', 'questionario.questao_80', 'questionario.questao_81', 'questionario.questao_82', 'questionario.questao_83', 'questionario.questao_84', 'questionario.questao_85', 'questionario.questao_86', 'questionario.questao_87', 'questionario.questao_88', 'questionario.questao_89', 'questionario.questao_90', 'questionario.questao_91', 'questionario.questao_92', 'questionario.questao_93', 'questionario.questao_94', 'questionario.questao_95', 'questionario.questao_96', 'questionario.questao_97', 'questionario.questao_98', 'questionario.questao_99', 'questionario.questao_100', 'questionario.questao_101', 'questionario.questao_102', 'questionario.questao_103', 'questionario.questao_104', 'questionario.questao_105', 'questionario.questao_106', 'questionario.questao_107', 'questionario.questao_108', 'questionario.questao_109', 'questionario.questao_110', 'questionario.questao_111', 'questionario.questao_112', 'questionario.questao_113', 'questionario.questao_114', 'questionario.questao_115', 'questionario.questao_116', 'questionario.questao_117', 'questionario.questao_118', 'questionario.questao_119', 'questionario.questao_120', 'questionario.questao_121', 'questionario.questao_122', 'questionario.questao_123', 'questionario.questao_124', 'questionario.questao_125', 'questionario.questao_126', 'questionario.questao_127', 'questionario.questao_128', 'questionario.questao_129', 'questionario.questao_130', 'questionario.questao_131', 'questionario.questao_132', 'questionario.questao_133', 'questionario.questao_134', 'questionario.questao_135', 'questionario.questao_136', 'questionario.questao_137', 'questionario.questao_138', 'questionario.questao_139', 'questionario.questao_140', 'questionario.questao_141', 'questionario.questao_142', 'questionario.questao_143', 'questionario.questao_144', 'questionario.questao_145', 'questionario.questao_146', 'exame.data', 'exame.examinador', 'exame.anotador', 'exame.carie_coroa_18', 'exame.carie_tratamento_18', 'exame.carie_coroa_17', 'exame.carie_tratamento_17', 'exame.carie_coroa_16', 'exame.carie_tratamento_16', 'exame.carie_coroa_15', 'exame.carie_tratamento_15', 'exame.carie_coroa_14', 'exame.carie_tratamento_14', 'exame.carie_coroa_13', 'exame.carie_tratamento_13', 'exame.carie_coroa_12', 'exame.carie_tratamento_12', 'exame.carie_coroa_11', 'exame.carie_tratamento_11', 'exame.carie_coroa_21', 'exame.carie_tratamento_21', 'exame.carie_coroa_22', 'exame.carie_tratamento_22', 'exame.carie_coroa_23', 'exame.carie_tratamento_23', 'exame.carie_coroa_24', 'exame.carie_tratamento_24', 'exame.carie_coroa_25', 'exame.carie_tratamento_25', 'exame.carie_coroa_26', 'exame.carie_tratamento_26', 'exame.carie_coroa_27', 'exame.carie_tratamento_27', 'exame.carie_coroa_28', 'exame.carie_tratamento_28', 'exame.carie_coroa_38', 'exame.carie_tratamento_38', 'exame.carie_coroa_37', 'exame.carie_tratamento_37', 'exame.carie_coroa_36', 'exame.carie_tratamento_36', 'exame.carie_coroa_35', 'exame.carie_tratamento_35', 'exame.carie_coroa_34', 'exame.carie_tratamento_34', 'exame.carie_coroa_33', 'exame.carie_tratamento_33', 'exame.carie_coroa_32', 'exame.carie_tratamento_32', 'exame.carie_coroa_31', 'exame.carie_tratamento_31', 'exame.carie_coroa_41', 'exame.carie_tratamento_41', 'exame.carie_coroa_42', 'exame.carie_tratamento_42', 'exame.carie_coroa_43', 'exame.carie_tratamento_43', 'exame.carie_coroa_44', 'exame.carie_tratamento_44', 'exame.carie_coroa_45', 'exame.carie_tratamento_45', 'exame.carie_coroa_46', 'exame.carie_tratamento_46', 'exame.carie_coroa_47', 'exame.carie_tratamento_47', 'exame.carie_coroa_48', 'exame.carie_tratamento_48', 'exame.periodontal_sangramento_1716', 'exame.periodontal_calculo_1716', 'exame.periodontal_bolsa_1716', 'exame.periodontal_sangramento_11', 'exame.periodontal_calculo_11', 'exame.periodontal_bolsa_11', 'exame.periodontal_sangramento_2627', 'exame.periodontal_calculo_2627', 'exame.periodontal_bolsa_2627', 'exame.periodontal_sangramento_3736', 'exame.periodontal_calculo_3736', 'exame.periodontal_bolsa_3736', 'exame.periodontal_sangramento_31', 'exame.periodontal_calculo_31', 'exame.periodontal_bolsa_31', 'exame.periodontal_sangramento_4647', 'exame.periodontal_calculo_4647', 'exame.periodontal_bolsa_4647',])
        
        for aluno in alunos:
            try:
                questionario = Questionario.objects.get(aluno_id=aluno.id)
                exame = Exame.objects.get(aluno_id=aluno.id)
            except:
                continue
            
            if questionario.questao_55 == '1':
                questionario.questao_55 = 'Não'
            
            writer.writerow([
                aluno.escola.acao.campanha.nome,
                
                aluno.escola.acao.nome,
                
                aluno.escola.nome,
                aluno.escola.latitude,
                aluno.escola.longitude,
                
                aluno.numero_identificacao,
                aluno.get_periodo_display(),
                aluno.turma,
                aluno.nascimento,
                aluno.get_sexo_display(),
                aluno.get_raca_display(),
                
                questionario.data,
                questionario.get_questao_1_display(),
                questionario.get_questao_2_display(),
                questionario.get_questao_3_display(),
                questionario.get_questao_4_display(),
                questionario.get_questao_5_display(),
                questionario.get_questao_6_display(),
                questionario.get_questao_7_display(),
                questionario.get_questao_8_display(),
                questionario.get_questao_9_display(),
                questionario.get_questao_10_display(),
                questionario.get_questao_11_display(),
                questionario.get_questao_12_display(),
                questionario.get_questao_13_display(),
                questionario.get_questao_14_display(),
                questionario.get_questao_15_display(),
                questionario.get_questao_16_display(),
                questionario.get_questao_17_display(),
                questionario.get_questao_18_display(),
                questionario.get_questao_19_display(),
                questionario.get_questao_20_display(),
                questionario.get_questao_21_display(),
                questionario.get_questao_22_display(),
                questionario.get_questao_23_display(),
                questionario.get_questao_24_display(),
                questionario.get_questao_25_display(),
                questionario.get_questao_26_display(),
                questionario.get_questao_27_display(),
                questionario.get_questao_28_display(),
                questionario.get_questao_29_display(),
                questionario.get_questao_30_display(),
                questionario.get_questao_31_display(),
                questionario.get_questao_32_display(),
                questionario.get_questao_33_display(),
                questionario.get_questao_34_display(),
                questionario.get_questao_35_display(),
                questionario.get_questao_36_display(),
                questionario.get_questao_37_display(),
                questionario.get_questao_38_display(),
                questionario.get_questao_39_display(),
                questionario.get_questao_40_display(),
                questionario.get_questao_41_display(),
                questionario.get_questao_42_display(),
                questionario.get_questao_43_display(),
                questionario.get_questao_44_display(),
                questionario.get_questao_45_display(),
                questionario.get_questao_46_display(),
                questionario.get_questao_47_display(),
                questionario.get_questao_48_display(),
                questionario.get_questao_49_display(),
                questionario.get_questao_50_display(),
                questionario.get_questao_51_display(),
                questionario.get_questao_52_display(),
                questionario.get_questao_53_display(),
                questionario.get_questao_54_display(),
                questionario.get_questao_55_display(),
                questionario.get_questao_56_display(),
                questionario.get_questao_57_display(),
                questionario.get_questao_58_display(),
                questionario.get_questao_59_display(),
                questionario.questao_60,
                questionario.get_questao_61_display(),
                questionario.get_questao_62_display(),
                questionario.get_questao_63_display(),
                questionario.get_questao_64_display(),
                questionario.get_questao_65_display(),
                questionario.get_questao_66_display(),
                questionario.get_questao_67_display(),
                questionario.get_questao_68_display(),
                questionario.get_questao_69_display(),
                questionario.get_questao_70_display(),
                questionario.get_questao_71_display(),
                questionario.get_questao_72_display(),
                questionario.get_questao_73_display(),
                questionario.get_questao_74_display(),
                questionario.get_questao_75_display(),
                questionario.get_questao_76_display(),
                questionario.get_questao_77_display(),
                questionario.get_questao_78_display(),
                questionario.get_questao_79_display(),
                questionario.get_questao_80_display(),
                questionario.get_questao_81_display(),
                questionario.get_questao_82_display(),
                questionario.get_questao_83_display(),
                questionario.get_questao_84_display(),
                questionario.get_questao_85_display(),
                questionario.get_questao_86_display(),
                questionario.get_questao_87_display(),
                questionario.get_questao_88_display(),
                questionario.get_questao_89_display(),
                questionario.get_questao_90_display(),
                questionario.get_questao_91_display(),
                questionario.get_questao_92_display(),
                questionario.get_questao_93_display(),
                questionario.get_questao_94_display(),
                questionario.get_questao_95_display(),
                questionario.get_questao_96_display(),
                questionario.get_questao_97_display(),
                questionario.get_questao_98_display(),
                questionario.get_questao_99_display(),
                questionario.get_questao_100_display(),
                questionario.get_questao_101_display(),
                questionario.get_questao_102_display(),
                questionario.get_questao_103_display(),
                questionario.get_questao_104_display(),
                questionario.get_questao_105_display(),
                questionario.get_questao_106_display(),
                questionario.get_questao_107_display(),
                questionario.get_questao_108_display(),
                questionario.get_questao_109_display(),
                questionario.get_questao_110_display(),
                questionario.get_questao_111_display(),
                questionario.get_questao_112_display(),
                questionario.get_questao_113_display(),
                questionario.get_questao_114_display(),
                questionario.get_questao_115_display(),
                questionario.get_questao_116_display(),
                questionario.get_questao_117_display(),
                questionario.get_questao_118_display(),
                questionario.get_questao_119_display(),
                questionario.get_questao_120_display(),
                questionario.get_questao_121_display(),
                questionario.get_questao_122_display(),
                questionario.get_questao_123_display(),
                questionario.get_questao_124_display(),
                questionario.get_questao_125_display(),
                questionario.get_questao_126_display(),
                questionario.get_questao_127_display(),
                questionario.get_questao_128_display(),
                questionario.get_questao_129_display(),
                questionario.get_questao_130_display(),
                questionario.get_questao_131_display(),
                questionario.get_questao_132_display(),
                questionario.get_questao_133_display(),
                questionario.get_questao_134_display(),
                questionario.get_questao_135_display(),
                questionario.get_questao_136_display(),
                questionario.get_questao_137_display(),
                questionario.get_questao_138_display(),
                questionario.get_questao_139_display(),
                questionario.get_questao_140_display(),
                questionario.get_questao_141_display(),
                questionario.get_questao_142_display(),
                questionario.get_questao_143_display(),
                questionario.get_questao_144_display(),
                questionario.get_questao_145_display(),
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
                aluno.get_periodo_display(),
                aluno.turma,
                aluno.nascimento,
                aluno.get_sexo_display(),
                aluno.get_raca_display(),
                
                questionario.data,
                questionario.get_questao_1_display(),
                questionario.get_questao_2_display(),
                questionario.get_questao_3_display(),
                questionario.get_questao_4_display(),
                questionario.get_questao_5_display(),
                questionario.get_questao_6_display(),
                questionario.get_questao_7_display(),
                questionario.get_questao_8_display(),
                questionario.get_questao_9_display(),
                questionario.get_questao_10_display(),
                questionario.get_questao_11_display(),
                questionario.get_questao_12_display(),
                questionario.get_questao_13_display(),
                questionario.get_questao_14_display(),
                questionario.get_questao_15_display(),
                questionario.get_questao_16_display(),
                questionario.get_questao_17_display(),
                questionario.get_questao_18_display(),
                questionario.get_questao_19_display(),
                questionario.get_questao_20_display(),
                questionario.get_questao_21_display(),
                questionario.get_questao_22_display(),
                questionario.get_questao_23_display(),
                questionario.get_questao_24_display(),
                questionario.get_questao_25_display(),
                questionario.get_questao_26_display(),
                questionario.get_questao_27_display(),
                questionario.get_questao_28_display(),
                questionario.get_questao_29_display(),
                questionario.get_questao_30_display(),
                questionario.get_questao_31_display(),
                questionario.get_questao_32_display(),
                questionario.get_questao_33_display(),
                questionario.get_questao_34_display(),
                questionario.get_questao_35_display(),
                questionario.get_questao_36_display(),
                questionario.get_questao_37_display(),
                questionario.get_questao_38_display(),
                questionario.get_questao_39_display(),
                questionario.get_questao_40_display(),
                questionario.get_questao_41_display(),
                questionario.get_questao_42_display(),
                questionario.get_questao_43_display(),
                questionario.get_questao_44_display(),
                questionario.get_questao_45_display(),
                questionario.get_questao_46_display(),
                questionario.get_questao_47_display(),
                questionario.get_questao_48_display(),
                questionario.get_questao_49_display(),
                questionario.get_questao_50_display(),
                questionario.get_questao_51_display(),
                questionario.get_questao_52_display(),
                questionario.get_questao_53_display(),
                questionario.get_questao_54_display(),
                questionario.get_questao_55_display(),
                questionario.get_questao_56_display(),
                questionario.get_questao_57_display(),
                questionario.get_questao_58_display(),
                questionario.get_questao_59_display(),
                questionario.questao_60,
                questionario.get_questao_61_display(),
                questionario.get_questao_62_display(),
                questionario.get_questao_63_display(),
                questionario.get_questao_64_display(),
                questionario.get_questao_65_display(),
                questionario.get_questao_66_display(),
                questionario.get_questao_67_display(),
                questionario.get_questao_68_display(),
                questionario.get_questao_69_display(),
                questionario.get_questao_70_display(),
                questionario.get_questao_71_display(),
                questionario.get_questao_72_display(),
                questionario.get_questao_73_display(),
                questionario.get_questao_74_display(),
                questionario.get_questao_75_display(),
                questionario.get_questao_76_display(),
                questionario.get_questao_77_display(),
                questionario.get_questao_78_display(),
                questionario.get_questao_79_display(),
                questionario.get_questao_80_display(),
                questionario.get_questao_81_display(),
                questionario.get_questao_82_display(),
                questionario.get_questao_83_display(),
                questionario.get_questao_84_display(),
                questionario.get_questao_85_display(),
                questionario.get_questao_86_display(),
                questionario.get_questao_87_display(),
                questionario.get_questao_88_display(),
                questionario.get_questao_89_display(),
                questionario.get_questao_90_display(),
                questionario.get_questao_91_display(),
                questionario.get_questao_92_display(),
                questionario.get_questao_93_display(),
                questionario.get_questao_94_display(),
                questionario.get_questao_95_display(),
                questionario.get_questao_96_display(),
                questionario.get_questao_97_display(),
                questionario.get_questao_98_display(),
                questionario.get_questao_99_display(),
                questionario.get_questao_100_display(),
                questionario.get_questao_101_display(),
                questionario.get_questao_102_display(),
                questionario.get_questao_103_display(),
                questionario.get_questao_104_display(),
                questionario.get_questao_105_display(),
                questionario.get_questao_106_display(),
                questionario.get_questao_107_display(),
                questionario.get_questao_108_display(),
                questionario.get_questao_109_display(),
                questionario.get_questao_110_display(),
                questionario.get_questao_111_display(),
                questionario.get_questao_112_display(),
                questionario.get_questao_113_display(),
                questionario.get_questao_114_display(),
                questionario.get_questao_115_display(),
                questionario.get_questao_116_display(),
                questionario.get_questao_117_display(),
                questionario.get_questao_118_display(),
                questionario.get_questao_119_display(),
                questionario.get_questao_120_display(),
                questionario.get_questao_121_display(),
                questionario.get_questao_122_display(),
                questionario.get_questao_123_display(),
                questionario.get_questao_124_display(),
                questionario.get_questao_125_display(),
                questionario.get_questao_126_display(),
                questionario.get_questao_127_display(),
                questionario.get_questao_128_display(),
                questionario.get_questao_129_display(),
                questionario.get_questao_130_display(),
                questionario.get_questao_131_display(),
                questionario.get_questao_132_display(),
                questionario.get_questao_133_display(),
                questionario.get_questao_134_display(),
                questionario.get_questao_135_display(),
                questionario.get_questao_136_display(),
                questionario.get_questao_137_display(),
                questionario.get_questao_138_display(),
                questionario.get_questao_139_display(),
                questionario.get_questao_140_display(),
                questionario.get_questao_141_display(),
                questionario.get_questao_142_display(),
                questionario.get_questao_143_display(),
                questionario.get_questao_144_display(),
                questionario.get_questao_145_display(),
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
                aluno.get_periodo_display(),
                aluno.turma,
                aluno.nascimento,
                aluno.get_sexo_display(),
                aluno.get_raca_display(),
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
                questionario.get_questao_1_display(),
                questionario.get_questao_2_display(),
                questionario.get_questao_3_display(),
                questionario.get_questao_4_display(),
                questionario.get_questao_5_display(),
                questionario.get_questao_6_display(),
                questionario.get_questao_7_display(),
                questionario.get_questao_8_display(),
                questionario.get_questao_9_display(),
                questionario.get_questao_10_display(),
                questionario.get_questao_11_display(),
                questionario.get_questao_12_display(),
                questionario.get_questao_13_display(),
                questionario.get_questao_14_display(),
                questionario.get_questao_15_display(),
                questionario.get_questao_16_display(),
                questionario.get_questao_17_display(),
                questionario.get_questao_18_display(),
                questionario.get_questao_19_display(),
                questionario.get_questao_20_display(),
                questionario.get_questao_21_display(),
                questionario.get_questao_22_display(),
                questionario.get_questao_23_display(),
                questionario.get_questao_24_display(),
                questionario.get_questao_25_display(),
                questionario.get_questao_26_display(),
                questionario.get_questao_27_display(),
                questionario.get_questao_28_display(),
                questionario.get_questao_29_display(),
                questionario.get_questao_30_display(),
                questionario.get_questao_31_display(),
                questionario.get_questao_32_display(),
                questionario.get_questao_33_display(),
                questionario.get_questao_34_display(),
                questionario.get_questao_35_display(),
                questionario.get_questao_36_display(),
                questionario.get_questao_37_display(),
                questionario.get_questao_38_display(),
                questionario.get_questao_39_display(),
                questionario.get_questao_40_display(),
                questionario.get_questao_41_display(),
                questionario.get_questao_42_display(),
                questionario.get_questao_43_display(),
                questionario.get_questao_44_display(),
                questionario.get_questao_45_display(),
                questionario.get_questao_46_display(),
                questionario.get_questao_47_display(),
                questionario.get_questao_48_display(),
                questionario.get_questao_49_display(),
                questionario.get_questao_50_display(),
                questionario.get_questao_51_display(),
                questionario.get_questao_52_display(),
                questionario.get_questao_53_display(),
                questionario.get_questao_54_display(),
                questionario.get_questao_55_display(),
                questionario.get_questao_56_display(),
                questionario.get_questao_57_display(),
                questionario.get_questao_58_display(),
                questionario.get_questao_59_display(),
                questionario.questao_60,
                questionario.get_questao_61_display(),
                questionario.get_questao_62_display(),
                questionario.get_questao_63_display(),
                questionario.get_questao_64_display(),
                questionario.get_questao_65_display(),
                questionario.get_questao_66_display(),
                questionario.get_questao_67_display(),
                questionario.get_questao_68_display(),
                questionario.get_questao_69_display(),
                questionario.get_questao_70_display(),
                questionario.get_questao_71_display(),
                questionario.get_questao_72_display(),
                questionario.get_questao_73_display(),
                questionario.get_questao_74_display(),
                questionario.get_questao_75_display(),
                questionario.get_questao_76_display(),
                questionario.get_questao_77_display(),
                questionario.get_questao_78_display(),
                questionario.get_questao_79_display(),
                questionario.get_questao_80_display(),
                questionario.get_questao_81_display(),
                questionario.get_questao_82_display(),
                questionario.get_questao_83_display(),
                questionario.get_questao_84_display(),
                questionario.get_questao_85_display(),
                questionario.get_questao_86_display(),
                questionario.get_questao_87_display(),
                questionario.get_questao_88_display(),
                questionario.get_questao_89_display(),
                questionario.get_questao_90_display(),
                questionario.get_questao_91_display(),
                questionario.get_questao_92_display(),
                questionario.get_questao_93_display(),
                questionario.get_questao_94_display(),
                questionario.get_questao_95_display(),
                questionario.get_questao_96_display(),
                questionario.get_questao_97_display(),
                questionario.get_questao_98_display(),
                questionario.get_questao_99_display(),
                questionario.get_questao_100_display(),
                questionario.get_questao_101_display(),
                questionario.get_questao_102_display(),
                questionario.get_questao_103_display(),
                questionario.get_questao_104_display(),
                questionario.get_questao_105_display(),
                questionario.get_questao_106_display(),
                questionario.get_questao_107_display(),
                questionario.get_questao_108_display(),
                questionario.get_questao_109_display(),
                questionario.get_questao_110_display(),
                questionario.get_questao_111_display(),
                questionario.get_questao_112_display(),
                questionario.get_questao_113_display(),
                questionario.get_questao_114_display(),
                questionario.get_questao_115_display(),
                questionario.get_questao_116_display(),
                questionario.get_questao_117_display(),
                questionario.get_questao_118_display(),
                questionario.get_questao_119_display(),
                questionario.get_questao_120_display(),
                questionario.get_questao_121_display(),
                questionario.get_questao_122_display(),
                questionario.get_questao_123_display(),
                questionario.get_questao_124_display(),
                questionario.get_questao_125_display(),
                questionario.get_questao_126_display(),
                questionario.get_questao_127_display(),
                questionario.get_questao_128_display(),
                questionario.get_questao_129_display(),
                questionario.get_questao_130_display(),
                questionario.get_questao_131_display(),
                questionario.get_questao_132_display(),
                questionario.get_questao_133_display(),
                questionario.get_questao_134_display(),
                questionario.get_questao_135_display(),
                questionario.get_questao_136_display(),
                questionario.get_questao_137_display(),
                questionario.get_questao_138_display(),
                questionario.get_questao_139_display(),
                questionario.get_questao_140_display(),
                questionario.get_questao_141_display(),
                questionario.get_questao_142_display(),
                questionario.get_questao_143_display(),
                questionario.get_questao_144_display(),
                questionario.get_questao_145_display(),
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
        writer.writerow([])
        
        for diretor in diretores:
            writer.writerow([
                diretor.escola.nome,
                diretor.data,
                diretor.questao_1,
                diretor.get_questao_2_display(),
                diretor.questao_3,
                diretor.get_questao_4_display(),
                diretor.get_questao_5_display(),
                diretor.get_questao_6_display(),
                diretor.get_questao_7_display(),
                diretor.get_questao_8_display(),
                diretor.get_questao_9_display(),
                diretor.get_questao_10_display(),
                diretor.get_questao_11_display(),
                diretor.get_questao_12_display(),
                diretor.get_questao_13_display(),
                diretor.get_questao_14_display(),
                diretor.get_questao_15_display(),
                diretor.get_questao_16_display(),
                diretor.get_questao_17_display(),
                diretor.get_questao_18_display(),
                diretor.get_questao_19_display(),
                diretor.get_questao_20_display(),
                diretor.get_questao_21_display(),
                diretor.get_questao_22_display(),
                diretor.get_questao_23_display(),
                diretor.get_questao_24_display(),
                diretor.get_questao_25_display(),
                diretor.get_questao_26_display(),
                diretor.get_questao_27_display(),
                diretor.questao_28,
                diretor.get_questao_29_display(),
                diretor.get_questao_30_display(),
                diretor.questao_31,
                diretor.get_questao_32_display(),
                diretor.questao_33,
                diretor.get_questao_34_display(),
                diretor.get_questao_35_display(),
                diretor.get_questao_36_display(),
                diretor.questao_37,
                diretor.get_questao_38_display(),
                diretor.questao_39,
                diretor.get_questao_40_display(),
                diretor.get_questao_41_display(),
                diretor.get_questao_42_display(),
                diretor.get_questao_43_display(),
                diretor.get_questao_44_display(),
                diretor.get_questao_45_display(),
                diretor.get_questao_46_display(),
                diretor.get_questao_47_display(),
                diretor.get_questao_48_display(),
                diretor.get_questao_49_display(),
                diretor.get_questao_50_display(),
                diretor.get_questao_51_display(),
                diretor.get_questao_52_display(),
                diretor.get_questao_53_display(),
                diretor.get_questao_54_display(),
                diretor.get_questao_55_display(),
                diretor.get_questao_56_display(),
                diretor.get_questao_57_display(),
                diretor.get_questao_58_display(),
                diretor.get_questao_59_display(),
                diretor.get_questao_60_display(),
                diretor.get_questao_61_display(),
                diretor.get_questao_62_display(),
                diretor.get_questao_63_display(),
                diretor.get_questao_64_display(),
                diretor.get_questao_65_display(),
                diretor.get_questao_66_display(),
                diretor.get_questao_67_display(),
                diretor.get_questao_68_display(),
                diretor.get_questao_69_display(),
                diretor.get_questao_70_display(),
                diretor.get_questao_71_display(),
                diretor.get_questao_72_display(),
                diretor.get_questao_73_display(),
                diretor.get_questao_74_display(),
                diretor.get_questao_75_display(),
                diretor.get_questao_76_display(),
                diretor.get_questao_77_display(),
                diretor.get_questao_78_display(),
                diretor.get_questao_79_display(),
                diretor.get_questao_80_display(),
                diretor.get_questao_81_display(),
                diretor.get_questao_82_display(),
                diretor.get_questao_83_display(),
                diretor.get_questao_84_display(),
            ])
        
        return response
