"""Define os padrões de URL para a aplicação"""

from django.conf.urls import url

from . import views

app_name="questionarios"

urlpatterns = [
    # Mostra a confirmação do envio do formulário
    url(r'^confirmacao/$', views.ConfirmacaoView.as_view(), name='confirmacao'),

    # Questionário para o diretor de escola
    url(r'^diretor/$', views.QuestionarioDiretorView.as_view(), name='diretor'),
]
