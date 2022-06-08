import io
from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect
from django.contrib import messages
from django.db.models import Q
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django_tables2 import RequestConfig
from django.template.response import TemplateResponse
from clientes.models import Clientes
from clientes.forms import AniversariosForm
from pacientes.models import Pacientes
from clientes.tables import AniversariosTutorTable, AniversariosPetTable
from service.Buscador import *
from service.Formata import *
import xlsxwriter

def listar(request):
    """ CARREGA A TABELA PRINCIPAL COM OS DADOS """

    form = AniversariosForm()
    data = Buscador.busca_dia_aniversario()
    url = Buscador.busca_url_base('/aniversarios')
    dados = {
        'title': url.nome,
        'cor': url.cor, 
        'form':form,
        'data':data,
        'titulo': url.nome,
        'url_base': 'home',
        'img': url.img,
    }

    return render(request, 'aniversarios/index.html',dados)

def aniversarios_tutor(request, data):
    
    data = data.replace('-','/')
    table = AniversariosTutorTable(Clientes.objects.filter(data_nascimento__contains=data).order_by('data_nascimento'))
    dados = {'table': table,
             'data': data
    
    }
   
    return render(request, 'aniversarios/table_tutor.html',dados)


def aniversarios_pet(request, data):

    data = data.replace('-','/')
    table = AniversariosPetTable(Pacientes.objects.filter(data_nascimento__contains=data).order_by('data_nascimento'))
    dados = {'table': table,
             'data': data
    
    }
   
    return render(request, 'aniversarios/table_pet.html',dados)