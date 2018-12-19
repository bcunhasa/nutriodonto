from django.db import models

from .const import *


class Noticia(models.Model):
    """Modelo que representa uma notícia do portal"""
    titulo = models.CharField(max_length=TAMANHO_TITULO, verbose_name='Título')

    def __str__(self):
        """Devolve a representação do modelo em string"""
        return self.nome


class Documento(models.Model):
    """Modelo que representa um documento público"""
    titulo = models.CharField(max_length=TAMANHO_TITULO, verbose_name='Título')

    def __str__(self):
        """Devolve a representação do modelo em string"""
        return self.nome


class Foto(models.Model):
    """Modelo que representa uma foto da página de mídia"""
    titulo = models.CharField(max_length=TAMANHO_TITULO, verbose_name='Título')

    def __str__(self):
        """Devolve a representação do modelo em string"""
        return self.nome


class Vídeo(models.Model):
    """Modelo que representa um vídeo da página de mídia"""
    titulo = models.CharField(max_length=TAMANHO_TITULO, verbose_name='Título')

    def __str__(self):
        """Devolve a representação do modelo em string"""
        return self.nome
