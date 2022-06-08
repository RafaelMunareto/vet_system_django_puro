from rest_framework import viewsets, generics
from pacientes.models import *
from pacientes.serializer import *
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
       
class PacientesViewSet(viewsets.ModelViewSet):
    """ API REST GET ALL """
    queryset = Pacientes.objects.all()
    serializer_class = PacientesSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
class PacientesDosClientes(generics.ListAPIView):
    """Listando as matrículas de um aluno ou aluna"""
    def get_queryset(self):
        queryset = Pacientes.objects.filter(cliente_id=self.kwargs['pk'])
        return queryset
    serializer_class = PacientesSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
class FaturaProdutoViewSet(viewsets.ModelViewSet):
    """ API REST GET ALL """
    queryset = FaturaProduto.objects.all()
    serializer_class = FaturaProdutoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class HistoricoFaturaViewSet(viewsets.ModelViewSet):
    """ API REST GET ALL """
    queryset = HistoricoFatura.objects.all()
    serializer_class = HistoricoFaturaSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
class HistoricoFaturasDosPacientes(generics.ListAPIView):
    """Listando as matrículas de um aluno ou aluna"""
    def get_queryset(self):
        queryset = HistoricoFatura.objects.filter(paciente_id=self.kwargs['pk'])
        return queryset
    serializer_class = HistoricoFaturaSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
class PacientesDosClientes(generics.ListAPIView):
    """Listando os pacientes dos clientes"""
    def get_queryset(self):
        queryset = Pacientes.objects.filter(tutor_id=self.kwargs['pk'])
        return queryset
    serializer_class = PacientesSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
class AssinaturaVeterinarioViewSet(viewsets.ModelViewSet):
    """ API REST GET ALL """
    queryset = AssinaturaVeterinario.objects.all()
    serializer_class = AssinaturaVeterinarioSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class PrecricaoViewSet(viewsets.ModelViewSet):
    """ API REST GET ALL """
    queryset = Prescricao.objects.all()
    serializer_class = PrescricaoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
class PrescricaoDosPacientes(generics.ListAPIView):
    """Listando os pacientes dos clientes"""
    def get_queryset(self):
        queryset = Prescricao.objects.filter(paciente_id=self.kwargs['pk'])
        return queryset
    serializer_class = PrescricaoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

