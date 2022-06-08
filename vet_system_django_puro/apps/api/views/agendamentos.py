from rest_framework import viewsets, generics
from agendamentos.models import *
from agendamentos.serializer import *
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class AgendamentosViewSet(viewsets.ModelViewSet):
    """ API REST GET ALL """
    queryset = Agendamentos.objects.all()
    serializer_class = AgendamentosSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
