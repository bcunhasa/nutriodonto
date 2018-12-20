from django.db import models

from .const import *


class Noticia(models.Model):
    """Modelo que representa uma notícia do portal"""
    titulo = models.CharField(max_length=TAMANHO_TITULO, verbose_name='Título')
    data = models.CharField(max_length=TAMANHO_TITULO, verbose_name='Data de criação')
    texto = models.TextField(verbose_name='Texto')
    imagem = models.CharField(max_length=TAMANHO_TITULO, verbose_name='URL da imagem')

    def __str__(self):
        """Devolve a representação do modelo em string"""
        return self.titulo


class Documento(models.Model):
    """Modelo que representa um documento público"""
    titulo = models.CharField(max_length=TAMANHO_TITULO, verbose_name='Título')
    data = models.DateTimeField(auto_now_add=True, verbose_name='Data de criação')
    url = models.CharField(max_length=TAMANHO_TITULO, verbose_name='URL do documento')

    def __str__(self):
        """Devolve a representação do modelo em string"""
        return self.titulo


class Foto(models.Model):
    """Modelo que representa uma foto da página de mídia"""
    titulo = models.CharField(max_length=TAMANHO_TITULO, verbose_name='Título')
    data = models.DateTimeField(auto_now_add=True, verbose_name='Data de criação')
    url = models.CharField(max_length=TAMANHO_TITULO, verbose_name='URL da foto')

    def __str__(self):
        """Devolve a representação do modelo em string"""
        return self.titulo


class Video(models.Model):
    """Modelo que representa um vídeo da página de mídia"""
    titulo = models.CharField(max_length=TAMANHO_TITULO, verbose_name='Título')
    data = models.DateTimeField(auto_now_add=True, verbose_name='Data de criação')
    url = models.CharField(max_length=TAMANHO_TITULO, verbose_name='URL do vídeo')

    def __str__(self):
        """Devolve a representação do modelo em string"""
        return self.titulo
