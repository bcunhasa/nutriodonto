from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import View

from administracao.models import *
from .forms import *


class ConfirmacaoView(View):
    """Mostra a confirmação do envio do formulário"""
    
    def get(self, request):
        return render(self.request, 'questionarios/confirmacao.html')


class QuestionarioDiretorView(View):
    """Questionário para o diretor de escola"""
    
    def get(self, request):
        form = DiretorForm()
        context = {'form': form}
        return render(self.request, 'questionarios/diretor.html', context)
    
    def post(self, request):
        form = DiretorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('questionarios:confirmacao'))
        context = {'form': form}
        return render(self.request, 'questionarios/diretor.html', context)
