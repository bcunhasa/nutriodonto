from django.shortcuts import render
from django.views import View


class IndexView(View):
    """Página inicial do site"""
    
    def get(self, request):
        return render(self.request, 'portal/index.html')


class ProjetoView(View):
    """Informações sobre o projeto"""
    
    def get(self, request):
        return render(self.request, 'portal/projeto.html')


class DocumentosView(View):
    """Compatilhamento de documentos públicos"""
    
    def get(self, request):
        return render(self.request, 'portal/documentos.html')


class MidiaView(View):
    """Exibição de mídias"""
    
    def get(self, request):
        return render(self.request, 'portal/midia.html')


class ContatosView(View):
    """Informações de contato"""
    
    def get(self, request):
        return render(self.request, 'portal/contatos.html')
