"""Define os padrões de URL para a aplicação"""

from django.conf.urls import url

from . import views

app_name="questionarios"

urlpatterns = [
    # Mostra a confirmação do envio do formulário
    url(r'^confirmacao/$', views.ConfirmacaoView.as_view(), name='confirmacao'),

    # Questionário para o diretor da escola de T.I. Margarida Gonçalves
    url(r'^margarida_goncalves/$', views.MargaridaGoncalvesView.as_view(), name='margarida_goncalves'),
    
    # Questionário para o diretor da escola Antônio Carlos Jobim
    url(r'^carlos_jobim/$', views.CarlosJobimView.as_view(), name='carlos_jobim'),
    
    # Questionário para o diretor da escola Henrique Talone Pinheiro
    url(r'^henrique_talone/$', views.HenriqueTaloneView.as_view(), name='henrique_talone'),
    
    # Questionário para o diretor da escola Anne Frank
    url(r'^anne_frank/$', views.AnneFrankView.as_view(), name='anne_frank'),
    
    # Questionário para o diretor da escola de T.I. Padre Josimo M. Tavares
    url(r'^padre_josimo/$', views.PadreJosimoView.as_view(), name='padre_josimo'),
    
    # Questionário para o diretor da escola Beatriz Rodrigues da Silva
    url(r'^beatriz_rodrigues/$', views.BeatrizRodriguesView.as_view(), name='beatriz_rodrigues'),
    
    # Questionário para o diretor da escola Mestre Pacífico S. Campos
    url(r'^mestre_pacifico/$', views.MestrePacificoView.as_view(), name='mestre_pacifico'),
    
    # Questionário para o diretor da escola Luiz Gonzaga
    url(r'^luiz_gonzaga/$', views.LuizGonzagaView.as_view(), name='luiz_gonzaga'),
]
