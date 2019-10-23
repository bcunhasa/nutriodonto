"""Define os padrões de URL para a aplicação"""

from django.conf.urls import url

from . import views

app_name="exportacao"

urlpatterns = [
    # Permite a exportação da base por meio de arquivos csv
    url(r'^exportacao/$', views.ExportacaoView.as_view(), name='exportacao'),
    url(r'^download_completo/$', views.DownloadCompletoView.as_view(), name='download_completo'),
    url(r'^download_aluno_questionario_exame/$', views.DownloadAlunoQuestionarioExameView.as_view(), name='download_aluno_questionario_exame'),
    url(r'^lista_campanhas/$', views.DownloadListaCampanhasView.as_view(), name='lista_campanhas'),
    url(r'^lista_acoes/$', views.DownloadListaAcoesView.as_view(), name='lista_acoes'),
    url(r'^lista_escolas/$', views.DownloadListaEscolasView.as_view(), name='lista_escolas'),
    url(r'^lista_alunos/$', views.DownloadListaAlunosView.as_view(), name='lista_alunos'),
    url(r'^lista_questionarios/$', views.DownloadListaQuestionariosView.as_view(), name='lista_questionarios'),
    url(r'^lista_exames/$', views.DownloadListaExamesView.as_view(), name='lista_exames'),
    url(r'^lista_diretores/$', views.DownloadListaDiretoresView.as_view(), name='lista_diretores'),
]
