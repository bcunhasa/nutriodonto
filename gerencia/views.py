from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.views import View

from administracao.views import LoginRequired
from .models import *
from .forms import *
from .const import *


class NoticiasView(LoginRequired, View):
    """Página que lista as notícias cadastradas no sistema"""
    
    def get(self, request):
        noticias = Noticia.objects.order_by('-id')
        context = {'pagina_noticias': True, 'noticias': noticias}
        return render(self.request, 'gerencia/noticias.html', context)


class DetalhesNoticiaView(LoginRequired, View):
    """Página com as informações sobre uma notícia"""
    
    def get(self, request, noticia_id):
        noticia = Noticia.objects.get(id=noticia_id)
        form = NoticiaForm(instance=noticia)
        context = {'pagina_noticias': True, 'noticia': noticia, 'form': form}
        return render(self.request, 'gerencia/noticia.html', context)


class CriaNoticiaView(LoginRequired, View):
    """Cadastra as informações de uma nova notícia"""
    
    def get(self, request):
        form = NoticiaForm()
        context = {'pagina_noticias': True, 'form': form}
        return render(self.request, 'gerencia/novo_elemento.html', context)
    
    def post(self, request):
        form = NoticiaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('gerencia:noticias'))
        context = {'pagina_noticias': True, 'form': form}
        return render(self.request, 'gerencia/novo_elemento.html', context)


class EditaNoticiaView(LoginRequired, View):
    """Altera as informações de uma notícia"""
    
    def get(self, request, noticia_id):
        noticia = Noticia.objects.get(id=noticia_id)
        form = NoticiaForm(instance=noticia)
        context = {'pagina_noticias': True, 'noticia': noticia, 'form': form}
        return render(self.request, 'gerencia/edita_elemento.html', context)
    
    def post(self, request, noticia_id):
        noticia = Noticia.objects.get(id=noticia_id)
        form = NoticiaForm(request.POST, request.FILES, instance=noticia)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('gerencia:noticias'))
        context = {'pagina_noticias': True, 'noticia': noticia, 'form': form}
        return render(self.request, 'gerencia/edita_elemento.html', context)


class RemoveNoticiaView(LoginRequired, View):
    """Remove uma notícia"""
    
    def get(self, request, noticia_id):
        noticia = Noticia.objects.get(id=noticia_id)
        context = {'pagina_noticias': True, 'noticia': noticia}
        return render(self.request, 'gerencia/remove_elemento.html', context)
        
    def post(self, request, noticia_id):
        noticia = Noticia.objects.get(id=noticia_id)
        noticia.delete()
        return HttpResponseRedirect(reverse('gerencia:noticias'))


class DocumentosView(LoginRequired, View):
    """Página que lista os documentos cadastrados no sistema"""
    
    def get(self, request):
        documentos = Documento.objects.order_by('-id')
        context = {'pagina_documentos': True, 'documentos': documentos}
        return render(self.request, 'gerencia/documentos.html', context)


class DetalhesDocumentoView(LoginRequired, View):
    """Página com as informações sobre um documento"""
    
    def get(self, request, documento_id):
        documento = Documento.objects.get(id=documento_id)
        form = DocumentoForm(instance=documento)
        context = {'pagina_documentos': True, 'documento': documento, 'form': form}
        return render(self.request, 'gerencia/documento.html', context)


class CriaDocumentoView(LoginRequired, View):
    """Cadastra as informações de um novo documento"""
    
    def get(self, request):
        form = DocumentoForm()
        context = {'pagina_documentos': True, 'form': form}
        return render(self.request, 'gerencia/novo_elemento.html', context)
    
    def post(self, request):
        form = DocumentoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('gerencia:documentos'))
        context = {'pagina_documentos': True, 'form': form}
        return render(self.request, 'gerencia/novo_elemento.html', context)


class EditaDocumentoView(LoginRequired, View):
    """Altera as informações de um documento"""
    
    def get(self, request, documento_id):
        documento = Documento.objects.get(id=documento_id)
        form = DocumentoForm(instance=documento)
        context = {'pagina_documentos': True, 'documento': documento, 'form': form}
        return render(self.request, 'gerencia/edita_elemento.html', context)
    
    def post(self, request, documento_id):
        documento = Documento.objects.get(id=documento_id)
        form = DocumentoForm(request.POST, request.FILES, instance=documento)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('gerencia:documentos'))
        context = {'pagina_documentos': True, 'documento': documento, 'form': form}
        return render(self.request, 'gerencia/edita_elemento.html', context)


class RemoveDocumentoView(LoginRequired, View):
    """Remove um documento"""
    
    def get(self, request, documento_id):
        documento = Documento.objects.get(id=documento_id)
        context = {'pagina_documentos': True, 'documento': documento}
        return render(self.request, 'gerencia/remove_elemento.html', context)
        
    def post(self, request, documento_id):
        documento = Documento.objects.get(id=documento_id)
        documento.delete()
        return HttpResponseRedirect(reverse('gerencia:documentos'))


class FotosView(LoginRequired, View):
    """Página que lista as fotos cadastradas no sistema"""
    
    def get(self, request):
        fotos = Foto.objects.order_by('-id')
        context = {'pagina_fotos': True, 'fotos': fotos}
        return render(self.request, 'gerencia/fotos.html', context)


class DetalhesFotoView(LoginRequired, View):
    """Página com as informações sobre uma foto"""
    
    def get(self, request, foto_id):
        foto = Foto.objects.get(id=foto_id)
        form = FotoForm(instance=foto)
        context = {'pagina_fotos': True, 'foto': foto, 'form': form}
        return render(self.request, 'gerencia/foto.html', context)


class CriaFotoView(LoginRequired, View):
    """Cadastra as informações de uma nova foto"""
    
    def get(self, request):
        form = FotoForm()
        context = {'pagina_fotos': True, 'form': form}
        return render(self.request, 'gerencia/novo_elemento.html', context)
    
    def post(self, request):
        form = FotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('gerencia:fotos'))
        context = {'pagina_fotos': True, 'form': form}
        return render(self.request, 'gerencia/novo_elemento.html', context)


class EditaFotoView(LoginRequired, View):
    """Altera as informações de uma foto"""
    
    def get(self, request, foto_id):
        foto = Foto.objects.get(id=foto_id)
        form = FotoForm(instance=foto)
        context = {'pagina_fotos': True, 'foto': foto, 'form': form}
        return render(self.request, 'gerencia/edita_elemento.html', context)
    
    def post(self, request, foto_id):
        foto = Foto.objects.get(id=foto_id)
        form = FotoForm(request.POST, request.FILES, instance=foto)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('gerencia:fotos'))
        context = {'pagina_fotos': True, 'foto': foto, 'form': form}
        return render(self.request, 'gerencia/edita_elemento.html', context)


class RemoveFotoView(LoginRequired, View):
    """Remove uma foto"""
    
    def get(self, request, foto_id):
        foto = Foto.objects.get(id=foto_id)
        context = {'pagina_fotos': True, 'foto': foto}
        return render(self.request, 'gerencia/remove_elemento.html', context)
        
    def post(self, request, foto_id):
        foto = Foto.objects.get(id=foto_id)
        foto.delete()
        return HttpResponseRedirect(reverse('gerencia:fotos'))


class VideosView(LoginRequired, View):
    """Página que lista os vídeos cadastradas no sistema"""
    
    def get(self, request):
        videos = Video.objects.order_by('-id')
        context = {'pagina_videos': True, 'videos': videos}
        return render(self.request, 'gerencia/videos.html', context)


class DetalhesVideoView(LoginRequired, View):
    """Página com as informações sobre um vídeo"""
    
    def get(self, request, video_id):
        video = Video.objects.get(id=video_id)
        form = VideoForm(instance=video)
        context = {'pagina_videos': True, 'video': video, 'form': form}
        return render(self.request, 'gerencia/video.html', context)


class CriaVideoView(LoginRequired, View):
    """Cadastra as informações de um novo vídeo"""
    
    def get(self, request):
        form = VideoForm()
        context = {'pagina_videos': True, 'form': form}
        return render(self.request, 'gerencia/novo_elemento.html', context)
    
    def post(self, request):
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('gerencia:videos'))
        context = {'pagina_videos': True, 'form': form}
        return render(self.request, 'gerencia/novo_elemento.html', context)


class EditaVideoView(LoginRequired, View):
    """Altera as informações de um vídeo"""
    
    def get(self, request, video_id):
        video = Video.objects.get(id=video_id)
        form = VideoForm(instance=video)
        context = {'pagina_videos': True, 'video': video, 'form': form}
        return render(self.request, 'gerencia/edita_elemento.html', context)
    
    def post(self, request, video_id):
        video = Video.objects.get(id=video_id)
        form = VideoForm(request.POST, request.FILES, instance=video)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('gerencia:videos'))
        context = {'pagina_videos': True, 'video': video, 'form': form}
        return render(self.request, 'gerencia/edita_elemento.html', context)


class RemoveVideoView(LoginRequired, View):
    """Remove um vídeo"""
    
    def get(self, request, video_id):
        video = Video.objects.get(id=video_id)
        context = {'pagina_videos': True, 'video': video}
        return render(self.request, 'gerencia/remove_elemento.html', context)
        
    def post(self, request, video_id):
        video = Video.objects.get(id=video_id)
        video.delete()
        return HttpResponseRedirect(reverse('gerencia:videos'))
