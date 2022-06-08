from rest_framework import serializers
from .models import *

class PacientesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pacientes
        fields = '__all__'
        
class FaturaProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FaturaProduto
        fields = '__all__'

class HistoricoFaturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoricoFatura
        fields = '__all__'

class AssinaturaVeterinarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssinaturaVeterinario
        fields = '__all__'

class PrescricaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prescricao
        fields = '__all__'
        