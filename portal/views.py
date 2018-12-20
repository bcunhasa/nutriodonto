from django.shortcuts import render
from django.views import View

from gerencia.models import Noticia, Documento, Foto, Video


class IndexView(View):
    """Página inicial do site"""
    
    def get(self, request):
        noticias = Noticia.objects.order_by('-id')
        context = {'noticias': noticias}
        return render(self.request, 'portal/index.html', context)


class ProjetoView(View):
    """Informações sobre o projeto"""
    
    def get(self, request):
        return render(self.request, 'portal/projeto.html')


class DocumentosView(View):
    """Compatilhamento de documentos públicos"""
    
    def get(self, request):
        documentos = Documento.objects.order_by('-id')
        context = {'documentos': documentos}
        return render(self.request, 'portal/documentos.html', context)


class MidiaView(View):
    """Exibição de mídias"""
    
    def get(self, request):
        fotos = Foto.objects.order_by('-id')
        videos = Video.objects.order_by('-id')
        context = {'fotos': fotos, 'videos': videos}
        return render(self.request, 'portal/midia.html', context)


class ContatosView(View):
    """Informações de contato"""
    
    def get(self, request):
        return render(self.request, 'portal/contatos.html')
