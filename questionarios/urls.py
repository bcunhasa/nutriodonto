"""Define os padrões de URL para a aplicação"""

from django.conf.urls import url

from . import views

app_name="questionarios"

urlpatterns = [
    # Questionário para os diretores de escola
    url(r'^diretor/$', views.DiretorView.as_view(), name='diretor'),
    
    # Questionário para os alunos que fizeram ou farão o exame
    url(r'^aluno/$', views.AlunoView.as_view(), name='aluno'),
]
