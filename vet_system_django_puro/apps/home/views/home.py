from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect
from django.db.models import Q
from service.Buscador import *
from home.models import Urls
from agendamentos.models import Agendamentos
from pacientes.models import Pacientes

def listar(request):
    """ CARREGA A TABELA PRINCIPAL COM OS DADOS """
    urls_cards = Urls.objects.filter(grupo='principal').all().order_by('id')
    url = Buscador.busca_url_base('')
    data = Buscador.busca_dia() 
    compromissos = Agendamentos.objects.filter(data__contains=data).order_by('data', 'time')[:5]
    dados = {
        'title': 'HOME' , 
        'cor':url.cor,
        'urls_cards':urls_cards,
        'compromissos':compromissos
    }
    
    return render(request, 'home/index.html',dados)

def busca(request):
    
    dados={
        'title': 'VET SYSTEM - BUSCA'
    }
    
    return render(request, 'home/busca.html', dados)

def busca_paciente(request):
  
    if 'search_paciente' in request.GET:
        search_paciente = request.GET['search_paciente']
    else:
        search_paciente = ''
        
    if search_paciente == '':
        pacientes = Pacientes.objects.all().distinct()
    else:
        pacientes = Pacientes.objects.all().distinct().order_by('nome').filter( Q(nome__icontains=search_paciente) | Q(especie__icontains=search_paciente) | \
                                                                                Q(raca__icontains=search_paciente))
    
        
    dados = {
        'search_paciente':search_paciente,
        'pacientes':pacientes
    }
    
    return render(request, 'home/busca_paciente.html', dados)