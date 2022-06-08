from rest_framework import serializers
from .models import *

class FornecedoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fornecedores
        fields = '__all__'
        
class ProdutosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produtos
        fields = '__all__'

class EstoqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estoque
        fields = '__all__'
        
class ParceirosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parceiros
        fields = '__all__'
        
class ServicosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servicos
        fields = '__all__'
        
class PagamentosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pagamentos
        fields = '__all__'
        
class CustosFixosSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustosFixos
        fields = '__all__'