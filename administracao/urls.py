"""Define os padrões de URL para o site"""

from django.conf.urls import url

from . import views

app_name="administracao"

urlpatterns = [
    # Página inicial
    url(r'^$', views.IndexView.as_view(), name='index'),
    
    # Página de login
    url(r'^login/$', views.LoginView.as_view(), name='login'),
    
    # Página de logout
    url(r'^logout/$', views.LogoutView.as_view(), name='logout'),
    
    # Visão geral
    url(r'^administracao$', views.VisaoGeralView.as_view(), name='visao_geral'),
    
    # Página que exibe gráficos baseados nos dados já coletados
    url(r'^administracao/graficos/$', views.GraficosView.as_view(), name='graficos'),
    
    # Página que lista os usuários cadastrados no sistema
    url(r'^administracao/usuarios/$', views.UsuariosView.as_view(), name='usuarios'),
    
    # Páginas que lidam com as informações de campanha
    url(r'^administracao/campanhas/$', views.CampanhasView.as_view(), name='campanhas'),
    url(r'^administracao/campanha/(?P<campanha_id>\d+)/$', views.DetalhesCampanhaView.as_view(), name='campanha'),
    url(r'^administracao/cria_campanha/$', views.CriaCampanhaView.as_view(), name='cria_campanha'),
    url(r'^administracao/edita_campanha/(?P<campanha_id>\d+)/$', views.EditaCampanhaView.as_view(), name='edita_campanha'),
    url(r'^administracao/remove_campanha/(?P<campanha_id>\d+)/$', views.RemoveCampanhaView.as_view(), name='remove_campanha'),
    
    # Páginas que lidam com as informações de ação
    url(r'^administracao/acoes/$', views.AcoesView.as_view(), name='acoes'),
    url(r'^administracao/acao/(?P<acao_id>\d+)/$', views.DetalhesAcaoView.as_view(), name='acao'),
    url(r'^administracao/cria_acao/$', views.CriaAcaoView.as_view(), name='cria_acao'),
    url(r'^administracao/edita_acao/(?P<acao_id>\d+)/$', views.EditaAcaoView.as_view(), name='edita_acao'),
    url(r'^administracao/remove_acao/(?P<acao_id>\d+)/$', views.RemoveAcaoView.as_view(), name='remove_acao'),
    
    # Páginas que lidam com as informações de escola
    url(r'^administracao/escolas/$', views.EscolasView.as_view(), name='escolas'),
    url(r'^administracao/escola/(?P<escola_id>\d+)/$', views.DetalhesEscolaView.as_view(), name='escola'),
    url(r'^administracao/cria_escola/$', views.CriaEscolaView.as_view(), name='cria_escola'),
    url(r'^administracao/edita_escola/(?P<escola_id>\d+)/$', views.EditaEscolaView.as_view(), name='edita_escola'),
    url(r'^administracao/remove_escola/(?P<escola_id>\d+)/$', views.RemoveEscolaView.as_view(), name='remove_escola'),
    
    # Páginas que lidam com as informações de aluno
    url(r'^administracao/alunos/$', views.AlunosView.as_view(), name='alunos'),
    url(r'^administracao/aluno/(?P<aluno_id>\d+)/$', views.DetalhesAlunoView.as_view(), name='aluno'),
    url(r'^administracao/cria_aluno/$', views.CriaAlunoView.as_view(), name='cria_aluno'),
    url(r'^administracao/edita_aluno/(?P<aluno_id>\d+)/$', views.EditaAlunoView.as_view(), name='edita_aluno'),
    url(r'^administracao/remove_aluno/(?P<aluno_id>\d+)/$', views.RemoveAlunoView.as_view(), name='remove_aluno'),
    
    # Páginas que lidam com as informações de questionario
    url(r'^administracao/questionarios/$', views.QuestionariosView.as_view(), name='questionarios'),
    url(r'^administracao/questionario/(?P<questionario_id>\d+)/$', views.DetalhesQuestionarioView.as_view(), name='questionario'),
    url(r'^administracao/cria_questionario/$', views.CriaQuestionarioView.as_view(), name='cria_questionario'),
    url(r'^administracao/edita_questionario/(?P<questionario_id>\d+)/$', views.EditaQuestionarioView.as_view(), name='edita_questionario'),
    url(r'^administracao/remove_questionario/(?P<questionario_id>\d+)/$', views.RemoveQuestionarioView.as_view(), name='remove_questionario'),
    
    # Páginas que lidam com as informações de exame
    url(r'^administracao/exames/$', views.ExamesView.as_view(), name='exames'),
    url(r'^administracao/exame/(?P<exame_id>\d+)/$', views.DetalhesExameView.as_view(), name='exame'),
    url(r'^administracao/cria_exame/$', views.CriaExameView.as_view(), name='cria_exame'),
    url(r'^administracao/edita_exame/(?P<exame_id>\d+)/$', views.EditaExameView.as_view(), name='edita_exame'),
    url(r'^administracao/remove_exame/(?P<exame_id>\d+)/$', views.RemoveExameView.as_view(), name='remove_exame'),
]
