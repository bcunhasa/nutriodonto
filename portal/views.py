from django.shortcuts import render
from django.views import View


class IndexView(View):
    """Página inicial do site"""
    
    def get(self, request):
        return render(self.request, 'portal/index.html')
