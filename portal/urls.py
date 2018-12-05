"""Define os padrões de URL para a aplicação"""

from django.conf.urls import url

from . import views

app_name="portal"

urlpatterns = [
    # Página inicial
    url(r'^$', views.IndexView.as_view(), name='index'),
]
