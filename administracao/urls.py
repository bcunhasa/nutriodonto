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
    
    # Página que lista as campanhas cadastradas no sistema
    url(r'^administracao/campanhas/$', views.CampanhasView.as_view(), name='campanhas'),
    
    # Página que lista as ações cadastradas no sistema
    url(r'^administracao/acoes/$', views.AcoesView.as_view(), name='acoes'),
    
    # Página que lista as escolas cadastradas no sistema
    url(r'^administracao/escolas/$', views.EscolasView.as_view(), name='escolas'),
    
    # Página que lista os alunos cadastrados no sistema
    url(r'^administracao/alunos/$', views.AlunosView.as_view(), name='alunos'),
    
    # Página que lista os questionários cadastrados no sistema
    url(r'^administracao/questionarios/$', views.QuestionariosView.as_view(), name='questionarios'),
    
    # Página que lista os exames cadastrados no sistema
    url(r'^administracao/exames/$', views.ExamesView.as_view(), name='exames'),
]
