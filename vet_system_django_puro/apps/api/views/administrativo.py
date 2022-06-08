from rest_framework import viewsets, generics
from administrativo.models import *
from administrativo.serializer import *
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class FornecedoresViewSet(viewsets.ModelViewSet):
    """ API REST GET ALL """
    queryset = Fornecedores.objects.all()
    serializer_class = FornecedoresSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
        
class ProdutosViewSet(viewsets.ModelViewSet):
    """ API REST GET ALL """
    queryset = Produtos.objects.all()
    serializer_class = ProdutosSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
class ProdutosDoFornecedor(generics.ListAPIView):
    """Listando os produtos dos fornecedores"""
    def get_queryset(self):
        queryset = Produtos.objects.filter(fornecedor_id=self.kwargs['pk'])
        return queryset
    serializer_class = ProdutosSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class EstoqueViewSet(viewsets.ModelViewSet):
    """ API REST GET ALL """
    queryset = Estoque.objects.all()
    serializer_class = EstoqueSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
        
class ParceirosViewSet(viewsets.ModelViewSet):
    """ API REST GET ALL """
    queryset = Parceiros.objects.all()
    serializer_class = ParceirosSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
        
class ServicosViewSet(viewsets.ModelViewSet):
    """ API REST GET ALL """
    queryset = Servicos.objects.all()
    serializer_class = ServicosSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
        
class PagamentosViewSet(viewsets.ModelViewSet):
    """ API REST GET ALL """
    queryset = Pagamentos.objects.all()
    serializer_class = PagamentosSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
        
class CustosFixosViewSet(viewsets.ModelViewSet):
    """ API REST GET ALL """
    queryset = CustosFixos.objects.all()
    serializer_class = CustosFixosSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]