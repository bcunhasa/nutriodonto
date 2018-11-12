from rest_framework import serializers

from administracao.models import *


class ExameSerializer(serializers.ModelSerializer):
    """Serializer do modelo Exame"""
    # edentulismo = EdentulismoSerializer(many=False)
    # fluorose = FluoroseSerializer(many=False)
    # traumatismo = TraumatismoSerializer(many=False)
    # carie = CarieSerializer(many=False)
    # periodontal = PeriodontalSerializer(many=False)
    
    class Meta:
        model = Exame
        fields = '__all__'


class QuestionarioSerializer(serializers.ModelSerializer):
    """Serializer do modelo Questionario"""
    
    class Meta:
        model = Questionario
        fields = '__all__'


class AlunoSerializer(serializers.ModelSerializer):
    """Serializer do modelo Aluno"""
    questionario = QuestionarioSerializer(many=False)
    exame = ExameSerializer(many=False)
    
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
