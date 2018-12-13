"""Define os padrões de URL para a aplicação"""

from django.conf.urls import url

from . import views

app_name="portal"

urlpatterns = [
    # Página inicial
    url(r'^$', views.IndexView.as_view(), name='index'),
    
    # Informações sobre o projeto
    url(r'^projeto/$', views.ProjetoView.as_view(), name='projeto'),
    
    # Compatilhamento de documentos públicos
    url(r'^documentos/$', views.DocumentosView.as_view(), name='documentos'),
    
    # Exibição de mídias
    url(r'^midia/$', views.MidiaView.as_view(), name='midia'),
    
    # Informações de contato
    url(r'^contatos/$', views.ContatosView.as_view(), name='contatos'),
]
