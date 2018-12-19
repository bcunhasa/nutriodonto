from django import forms

from .models import *


class NoticiaForm(forms.ModelForm):
    
    class Meta:
        model = Noticia
        fields = '__all__'


class DocumentoForm(forms.ModelForm):
    
    class Meta:
        model = Documento
        fields = '__all__'


class FotoForm(forms.ModelForm):
    
    class Meta:
        model = Foto
        fields = '__all__'


class VídeoForm(forms.ModelForm):
    
    class Meta:
        model = Vídeo
        fields = '__all__'
