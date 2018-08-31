from rest_framework import serializers

from administracao.models import *


class AlunoSerializer(serializers.ModelSerializer):
    """Serializer do modelo Aluno"""
    
    class Meta:
        model = Aluno
        fields = '__all__'


class EscolaSerializer(serializers.ModelSerializer):
    """Serializer do modelo Escola"""
    alunos = AlunoSerializer(many=True)
    
    class Meta:
        model = Escola
        fields = ('id', 'nome', 'alunos')


class AcaoSerializer(serializers.ModelSerializer):
    """Serializer do modelo Ação"""
    escolas = EscolaSerializer(many=True)
    
    class Meta:
        model = Acao
        fields = ('id', 'nome', 'escolas')


class CampanhaSerializer(serializers.ModelSerializer):
    """Serializer do modelo Campanha"""
    acoes = AcaoSerializer(many=True)
    
    class Meta:
        model = Campanha
        fields = ('id', 'nome', 'acoes')
