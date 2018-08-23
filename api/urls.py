"""Define os padrões de URL para a api rest"""

from django.conf.urls import url

from . import views

app_name="api"

urlpatterns = [
    # Retorna o token do usuário para que seja possível realizar as operações
    url(r'^token/$', views.ClienteAutenticacaoAPIView.as_view(), name='token'),
    
    # Carga inicial do cliente
    url(r'^dados/$', views.CargaInicialAPIView.as_view(), name='dados'),
]
