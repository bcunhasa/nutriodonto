"""Define os padrões de URL para a aplicação"""

from django.conf.urls import url

from . import views

app_name="administracao"

urlpatterns = [
    # Página de login
    url(r'^login/$', views.LoginView.as_view(), name='login'),
    
    # Página de logout
    url(r'^logout/$', views.LogoutView.as_view(), name='logout'),
    
    # Acompanhamento da coleta dos dados
    url(r'^visao_geral/$', views.VisaoGeralView.as_view(), name='visao_geral'),
    
    # Exibe dados gerados após o processo de inferência estatística
    url(r'^inferencia/$', views.InferenciaView.as_view(), name='inferencia'),
    
    # Exibe dados gerados após o processo de predição pelo naive bayes
    url(r'^predicao/$', views.PredicaoView.as_view(), name='predicao'),
    
    # Páginas que exibem gráficos baseados nos dados já coletados
    url(r'^graficos_alunos/$', views.GraficosAlunosView.as_view(), name='graficos_alunos'),
    url(r'^graficos_questionarios/$', views.GraficosQuestionariosView.as_view(), name='graficos_questionarios'),
    url(r'^graficos_exames/$', views.GraficosExamesView.as_view(), name='graficos_exames'),
    url(r'^graficos_diretores/$', views.GraficosDiretoresView.as_view(), name='graficos_diretores'),
    
    # Página que lista os usuários cadastrados no sistema
    url(r'^usuarios/$', views.UsuariosView.as_view(), name='usuarios'),
    
    # Páginas que lidam com as informações de campanha
    url(r'^campanhas/$', views.CampanhasView.as_view(), name='campanhas'),
    url(r'^campanha/(?P<campanha_id>\d+)/$', views.DetalhesCampanhaView.as_view(), name='campanha'),
    url(r'^cria_campanha/$', views.CriaCampanhaView.as_view(), name='cria_campanha'),
    url(r'^edita_campanha/(?P<campanha_id>\d+)/$', views.EditaCampanhaView.as_view(), name='edita_campanha'),
    url(r'^remove_campanha/(?P<campanha_id>\d+)/$', views.RemoveCampanhaView.as_view(), name='remove_campanha'),
    
    # Páginas que lidam com as informações de ação
    url(r'^acoes/$', views.AcoesView.as_view(), name='acoes'),
    url(r'^acao/(?P<acao_id>\d+)/$', views.DetalhesAcaoView.as_view(), name='acao'),
    url(r'^cria_acao/$', views.CriaAcaoView.as_view(), name='cria_acao'),
    url(r'^edita_acao/(?P<acao_id>\d+)/$', views.EditaAcaoView.as_view(), name='edita_acao'),
    url(r'^remove_acao/(?P<acao_id>\d+)/$', views.RemoveAcaoView.as_view(), name='remove_acao'),
    
    # Páginas que lidam com as informações de escola
    url(r'^escolas/$', views.EscolasView.as_view(), name='escolas'),
    url(r'^escola/(?P<escola_id>\d+)/$', views.DetalhesEscolaView.as_view(), name='escola'),
    url(r'^cria_escola/$', views.CriaEscolaView.as_view(), name='cria_escola'),
    url(r'^edita_escola/(?P<escola_id>\d+)/$', views.EditaEscolaView.as_view(), name='edita_escola'),
    url(r'^remove_escola/(?P<escola_id>\d+)/$', views.RemoveEscolaView.as_view(), name='remove_escola'),
    
    # Páginas que lidam com as informações de aluno
    url(r'^alunos/$', views.AlunosView.as_view(), name='alunos'),
    url(r'^aluno/(?P<aluno_id>\d+)/$', views.DetalhesAlunoView.as_view(), name='aluno'),
    url(r'^cria_aluno/$', views.CriaAlunoView.as_view(), name='cria_aluno'),
    url(r'^edita_aluno/(?P<aluno_id>\d+)/$', views.EditaAlunoView.as_view(), name='edita_aluno'),
    url(r'^remove_aluno/(?P<aluno_id>\d+)/$', views.RemoveAlunoView.as_view(), name='remove_aluno'),
    
    # Páginas que lidam com as informações de questionario
    url(r'^questionarios/$', views.QuestionariosView.as_view(), name='questionarios'),
    url(r'^questionario/(?P<questionario_id>\d+)/$', views.DetalhesQuestionarioView.as_view(), name='questionario'),
    url(r'^cria_questionario/$', views.CriaQuestionarioView.as_view(), name='cria_questionario'),
    url(r'^edita_questionario/(?P<questionario_id>\d+)/$', views.EditaQuestionarioView.as_view(), name='edita_questionario'),
    url(r'^remove_questionario/(?P<questionario_id>\d+)/$', views.RemoveQuestionarioView.as_view(), name='remove_questionario'),
    
    # Páginas que lidam com as informações de exame
    url(r'^exames/$', views.ExamesView.as_view(), name='exames'),
    url(r'^exame/(?P<exame_id>\d+)/$', views.DetalhesExameView.as_view(), name='exame'),
    url(r'^cria_exame/$', views.CriaExameView.as_view(), name='cria_exame'),
    url(r'^edita_exame/(?P<exame_id>\d+)/$', views.EditaExameView.as_view(), name='edita_exame'),
    url(r'^remove_exame/(?P<exame_id>\d+)/$', views.RemoveExameView.as_view(), name='remove_exame'),
    
    # Páginas que lidam com as informações dos questionários dos diretores
    url(r'^diretores/$', views.DiretoresView.as_view(), name='diretores'),
    url(r'^diretor/(?P<diretor_id>\d+)/$', views.DetalhesDiretorView.as_view(), name='diretor'),
    url(r'^cria_diretor/$', views.CriaDiretorView.as_view(), name='cria_diretor'),
    url(r'^edita_diretor/(?P<diretor_id>\d+)/$', views.EditaDiretorView.as_view(), name='edita_diretor'),
    url(r'^remove_diretor/(?P<diretor_id>\d+)/$', views.RemoveDiretorView.as_view(), name='remove_diretor'),
]
