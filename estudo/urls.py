"""Define os padrões de URL para a aplicação"""

from django.conf.urls import url

from . import views

app_name="estudo"

urlpatterns = [
    # Acompanhamento dos resultados do estudo
    url(r'^estudo/$', views.EstudoView.as_view(), name='estudo'),
]
