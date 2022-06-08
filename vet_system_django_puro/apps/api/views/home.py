from rest_framework import viewsets, generics
from home.models import *
from home.serializer import *
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class UrlsViewSet(viewsets.ModelViewSet):
    """ API REST GET ALL """
    queryset = Urls.objects.all()
    serializer_class = UrlsSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
