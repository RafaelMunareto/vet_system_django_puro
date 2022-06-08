from django.urls import path
from .views import *

urlpatterns = [
    
    path('', home.listar, name='home'),
    path('busca', home.busca, name='busca'),
    path('busca_paciente', home.busca_paciente, name='busca_paciente'),
]
