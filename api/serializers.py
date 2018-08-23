from rest_framework import serializers

from administracao.models import *


class CampanhaSerializer(serializers.ModelSerializer):
    """Serializer do modelo Campanha"""
    
    class Meta:
        model = Campanha
        fields = '__all__'
