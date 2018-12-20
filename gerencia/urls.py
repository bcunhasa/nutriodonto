"""Define os padrões de URL para a aplicação"""

from django.conf.urls import url

from . import views

app_name="gerencia"

urlpatterns = [
    # Páginas que lidam com as informações de notícia
    url(r'^noticias/$', views.NoticiasView.as_view(), name='noticias'),
    url(r'^noticia/(?P<noticia_id>\d+)/$', views.DetalhesNoticiaView.as_view(), name='noticia'),
    url(r'^cria_noticia/$', views.CriaNoticiaView.as_view(), name='cria_noticia'),
    url(r'^edita_noticia/(?P<noticia_id>\d+)/$', views.EditaNoticiaView.as_view(), name='edita_noticia'),
    url(r'^remove_noticia/(?P<noticia_id>\d+)/$', views.RemoveNoticiaView.as_view(), name='remove_noticia'),
    
    # Páginas que lidam com as informações de documento
    url(r'^documentos/$', views.DocumentosView.as_view(), name='documentos'),
    url(r'^documento/(?P<documento_id>\d+)/$', views.DetalhesDocumentoView.as_view(), name='documento'),
    url(r'^cria_documento/$', views.CriaDocumentoView.as_view(), name='cria_documento'),
    url(r'^edita_documento/(?P<documento_id>\d+)/$', views.EditaDocumentoView.as_view(), name='edita_documento'),
    url(r'^remove_documento/(?P<documento_id>\d+)/$', views.RemoveDocumentoView.as_view(), name='remove_documento'),
    
    # Páginas que lidam com as informações de foto
    url(r'^fotos/$', views.FotosView.as_view(), name='fotos'),
    url(r'^foto/(?P<foto_id>\d+)/$', views.DetalhesFotoView.as_view(), name='foto'),
    url(r'^cria_foto/$', views.CriaFotoView.as_view(), name='cria_foto'),
    url(r'^edita_foto/(?P<foto_id>\d+)/$', views.EditaFotoView.as_view(), name='edita_foto'),
    url(r'^remove_foto/(?P<foto_id>\d+)/$', views.RemoveFotoView.as_view(), name='remove_foto'),
    
    # Páginas que lidam com as informações de video
    url(r'^videos/$', views.VideosView.as_view(), name='videos'),
    url(r'^video/(?P<video_id>\d+)/$', views.DetalhesVideoView.as_view(), name='video'),
    url(r'^cria_video/$', views.CriaVideoView.as_view(), name='cria_video'),
    url(r'^edita_video/(?P<video_id>\d+)/$', views.EditaVideoView.as_view(), name='edita_video'),
    url(r'^remove_video/(?P<video_id>\d+)/$', views.RemoveVideoView.as_view(), name='remove_video'),
]
