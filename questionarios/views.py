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


class MargaridaGoncalvesView(View):
    """Questionário para o diretor da escola de T.I. Margarida Gonçalves"""
    
    def get(self, request):
        form = DiretorForm()
        context = {'pagina_margarida_goncalves': True, 'form': form}
        return render(self.request, 'questionarios/diretor.html', context)
    
    def post(self, request):
        form = DiretorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('questionarios:confirmacao'))
        context = {'pagina_margarida_goncalves': True, 'form': form}
        return render(self.request, 'questionarios/diretor.html', context)


class CarlosJobimView(View):
    """Questionário para o diretor da escola Antônio Carlos Jobim"""
    
    def get(self, request):
        form = DiretorForm()
        context = {'pagina_carlos_jobim': True, 'form': form}
        return render(self.request, 'questionarios/diretor.html', context)
    
    def post(self, request):
        form = DiretorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('questionarios:confirmacao'))
        context = {'pagina_carlos_jobim': True, 'form': form}
        return render(self.request, 'questionarios/diretor.html', context)


class HenriqueTaloneView(View):
    """Questionário para o diretor da escola Henrique Talone Pinheiro"""
    
    def get(self, request):
        form = DiretorForm()
        context = {'pagina_henrique_talone': True, 'form': form}
        return render(self.request, 'questionarios/diretor.html', context)
    
    def post(self, request):
        form = DiretorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('questionarios:confirmacao'))
        context = {'pagina_henrique_talone': True, 'form': form}
        return render(self.request, 'questionarios/diretor.html', context)


class AnneFrankView(View):
    """Questionário para o diretor da escola Anne Frank"""
    
    def get(self, request):
        form = DiretorForm()
        context = {'pagina_anne_frank': True, 'form': form}
        return render(self.request, 'questionarios/diretor.html', context)
    
    def post(self, request):
        form = DiretorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('questionarios:confirmacao'))
        context = {'pagina_anne_frank': True, 'form': form}
        return render(self.request, 'questionarios/diretor.html', context)


class PadreJosimoView(View):
    """Questionário para o diretor da escola de T.I. Padre Josimo M. Tavares"""
    
    def get(self, request):
        form = DiretorForm()
        context = {'pagina_padre_josimo': True, 'form': form}
        return render(self.request, 'questionarios/diretor.html', context)
    
    def post(self, request):
        form = DiretorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('questionarios:confirmacao'))
        context = {'pagina_padre_josimo': True, 'form': form}
        return render(self.request, 'questionarios/diretor.html', context)


class BeatrizRodriguesView(View):
    """Questionário para o diretor da escola Beatriz Rodrigues da Silva"""
    
    def get(self, request):
        form = DiretorForm()
        context = {'pagina_beatriz_rodrigues': True, 'form': form}
        return render(self.request, 'questionarios/diretor.html', context)
    
    def post(self, request):
        form = DiretorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('questionarios:confirmacao'))
        context = {'pagina_beatriz_rodrigues': True, 'form': form}
        return render(self.request, 'questionarios/diretor.html', context)


class MestrePacificoView(View):
    """Questionário para o diretor da escola Mestre Pacífico S. Campos"""
    
    def get(self, request):
        form = DiretorForm()
        context = {'pagina_mestre_pacifico': True, 'form': form}
        return render(self.request, 'questionarios/diretor.html', context)
    
    def post(self, request):
        form = DiretorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('questionarios:confirmacao'))
        context = {'pagina_mestre_pacifico': True, 'form': form}
        return render(self.request, 'questionarios/diretor.html', context)


class LuizGonzagaView(View):
    """Questionário para o diretor da escola Luiz Gonzaga"""
    
    def get(self, request):
        form = DiretorForm()
        context = {'pagina_luiz_gonzaga': True, 'form': form}
        return render(self.request, 'questionarios/diretor.html', context)
    
    def post(self, request):
        form = DiretorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('questionarios:confirmacao'))
        context = {'pagina_luiz_gonzaga': True, 'form': form}
        return render(self.request, 'questionarios/diretor.html', context)
