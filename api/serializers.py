from rest_framework import serializers

from administracao.models import *


class AcaoSerializer(serializers.ModelSerializer):
    """Serializer do modelo Acao"""
    
    class Meta:
        model = Acao
        fields = '__all__'


class CampanhaSerializer(serializers.ModelSerializer):
    """Serializer do modelo Campanha"""
    acoes = AcaoSerializer(many=True)
    
    class Meta:
        model = Campanha
        fields = ('id', 'nome', 'acoes')





class AlunoSerializer(serializers.ModelSerializer):
    """Serializer do modelo Aluno"""
    
    class Meta:
        model = Aluno
        fields = '__all__'
