"""Define os padrões de URL para a aplicação"""

from django.conf.urls import url

from . import views

app_name="mapas"

urlpatterns = [
    # Apresentação de mapas
    url(r'^mapa_escolas/$', views.EscolasView.as_view(), name='escolas'),
]
