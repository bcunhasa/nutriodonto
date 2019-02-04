"""Define os padrões de URL para a api rest"""

from django.conf.urls import url

from . import views

app_name="api"

urlpatterns = [
    # Retorna o token do usuário para que seja possível realizar as operações
    url(r'^token/$', views.ClienteAutenticacaoAPIView.as_view(), name='token'),
    
    # Carga inicial para o aplicativo
    url(r'^dados/$', views.CargaInicialAPIView.as_view(), name='dados'),
    
    # Atualiza os dados do aluno pré-cadastrado com as informações de exame e questionário
    url(r'^aluno/(?P<pk>[0-9]+)/$', views.AtualizaAlunoAPIView.as_view(), name='aluno'),
    
    
    # URLs para o exemplo dado no curso de Ionic
    url(r'^noticias/$', views.NoticiasAPIView.as_view(), name='noticias'),
    url(r'^cria_noticia/$', views.CriaNoticiaAPIView.as_view(), name='cria_noticia'),
    url(r'^atualiza_noticia(?P<pk>[0-9]+)/$', views.AtualizaNoticiaAPIView.as_view(), name='atualiza_noticia'),
]
