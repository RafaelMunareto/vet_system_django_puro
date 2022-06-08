from rest_framework import viewsets, generics
from clientes.models import *
from clientes.serializer import *
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class ClientesViewSet(viewsets.ModelViewSet):
    """ API REST GET ALL """
    queryset = Clientes.objects.all()
    serializer_class = ClientesSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
