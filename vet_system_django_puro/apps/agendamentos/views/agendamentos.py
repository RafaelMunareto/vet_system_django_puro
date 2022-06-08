import io
import re
from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect
from django.contrib import messages
from django.db.models import Q
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django_tables2 import RequestConfig
from django.template.response import TemplateResponse
from agendamentos.models import Agendamentos
from pacientes.models import Pacientes
from agendamentos.forms import AgendamentosForms
from agendamentos.tables import AgendamentosTable
from django_tables2.export.export import TableExport
from service.Buscador import *
from service.Formata import *
import xlsxwriter

def listar(request, tipo, periodo):
    """ CARREGA A TABELA PRINCIPAL COM OS DADOS """

    table = AgendamentosTable(Agendamentos.objects.all())
    dados = Agendamentos.objects.all().distinct('tipo').order_by("tipo")
    
    if 'sort' in request.GET:
        order = request.GET['sort']
    else:
        order='data'

    if 'buscar' in request.GET:
        buscar = request.GET['buscar']
    else:
        buscar = ''
    
    if tipo == 0:
        tipo_r = (1,5)
    elif tipo == 1:
        tipo_r = (0,1)
    elif tipo == 2:
        tipo_r = (2,2)
    elif tipo == 3:
        tipo_r = (3,3)
    elif tipo == 4:
        tipo_r = (4,4)

    if periodo == 1:
        data = Buscador.busca_dia() 
        table = AgendamentosTable(Agendamentos.objects.filter(tipo__range=tipo_r).filter(data__contains=data).distinct().order_by(order, 'time').filter(Q(paciente__nome__icontains=buscar) | Q(tipo__icontains=buscar) | Q(obs__icontains=buscar) ))
    elif periodo == 2:
        data = Buscador.busca_semana() 
        table = AgendamentosTable(Agendamentos.objects.filter(tipo__range=tipo_r).filter(data__in=data).distinct().order_by(order, 'time').filter(Q(paciente__nome__icontains=buscar) | Q(tipo__icontains=buscar) | Q(obs__icontains=buscar) ))
    elif periodo == 3:
        data = Buscador.busca_mes()   
        table = AgendamentosTable(Agendamentos.objects.filter(tipo__range=tipo_r).filter(data__contains=data).distinct().order_by(order, 'time').filter(Q(paciente__nome__icontains=buscar) | Q(tipo__icontains=buscar) | Q(obs__icontains=buscar) ))
    elif periodo == 0:  
        table = AgendamentosTable(Agendamentos.objects.filter(tipo__range=tipo_r).filter(data__contains='202').distinct().order_by(order, 'time').filter(Q(paciente__nome__icontains=buscar) | Q(tipo__icontains=buscar) | Q(obs__icontains=buscar) ))
             
    table.paginate(page=request.GET.get("page", 1), per_page=8)
    periodo_formatado = Formata.formata_periodo(periodo)
    url = Buscador.busca_url_base('/agendamentos/0/0')
    
    dados = {
        'title': url.nome, 
        'buscar': buscar,
        'cor': url.cor, 
        'titulo': str(url.nome) + ' - ' + str(periodo_formatado),
        'table': table,
        'tipo':tipo,
        'periodo':periodo,
        'dados':dados,
        'url_export': 'agendamentos.export',
        'url_base': 'home',
        'url_add': 'agendamentos.adicionar',
        'img': url.img
    }

    return render(request, 'agendamentos/index.html',dados)

def adicionar(request):
    """ PÁGINA DO ADICIONAR """
    
    form = AgendamentosForms()
    url = Buscador.busca_url_base('/agendamentos/0/0')
    dados = {
        'title': url.nome + ' ADICIONAR', 
        'cor': url.cor, 
        'titulo': url.nome + ' ADICIONAR',
        'form': form,
        'img': url.img,
        'url_base': 'agendamentos',
        'id':0,
        'url_action': 'agendamentos.store'
    }
    
    return render(request, 'agendamentos/adicionar.html',dados)

def adicionar_novo(request, id):
    """ PÁGINA DO ADICIONAR """
    
    form = AgendamentosForms()
    url = Buscador.busca_url_base('/agendamentos/0/0')
    dado = get_object_or_404(Pacientes, pk=id)
    dados = {
        'title': url.nome + ' - ADICIONAR', 
        'cor': url.cor, 
        'titulo': str(dado.nome) + ' - ADICIONAR',
        'form': form,
        'img': url.img,
        'id_paciente':id,
        'url_base': 'agendamentos',
        'id':0,
        'url_action': 'agendamentos.store'
    }
    
    return render(request, 'agendamentos/adicionar.html',dados)

def editar(request, id):
    """ PÁGINA DO EDITAR """
    dado = get_object_or_404(Agendamentos, pk=id)
    instance = get_object_or_404(Agendamentos, pk=id)
    id_paciente = dado.paciente.id
    form = AgendamentosForms(instance=instance)
    url = Buscador.busca_url_base('/agendamentos/0/0')
    dados = {
        'title': url.nome + ' EDITAR', 
        'cor': url.cor, 
        'titulo': 'AGENDAMENTO DE ' + str(dado.paciente),
        'id': id,
        'id_paciente':id_paciente,
        'form': form,
        'img': url.img,
        'url_base': 'agendamentos',
        'url_action': 'agendamentos.put'
    }

    return render(request, 'agendamentos/editar.html',dados)
  
def store(request):
    """SALVAR NO BD """

    if request.method == 'POST': 
        paciente_id = int(request.POST['paciente_id'])
        time = request.POST['time']
        data = request.POST['data']
        tipo = request.POST['tipo']
        obs = request.POST['obs']
        form = AgendamentosForms(request.POST)
        
        if form.is_valid():
            paciente = Pacientes.objects.get(id=paciente_id)
            store = Agendamentos.objects.create(
                paciente = paciente,
                data = data,
                time = time,
                tipo = tipo,
                obs = obs
            )   
            store.save()
            messages.success(request,'Compromisso salvo com sucesso!')
            return redirect('agendamentos', tipo=0, periodo=0)  
        else:
            url = Buscador.busca_url_base('/agendamentos/0/0')
            dados = {
                'title': url.nome + ' ADICIONAR', 
                'cor': url.cor, 
                'titulo': url.nome + ' - ADICIONAR',
                'form': form,
                'img': url.img,
                'id':0,
                'url_base': 'agendamentos',
                'url_action': 'agendamentos.store'
            }
            
            return render(request, 'agendamentos/adicionar.html',dados)

def put(request, id):
    """EDITAR NO BD"""    
        
    if request.method == 'POST':
        paciente_id = int(request.POST['paciente_id'])
        data = request.POST['data']
        time = request.POST['time']
        tipo = request.POST['tipo']
        obs = request.POST['obs']
        paciente = Pacientes.objects.get(id=paciente_id)
        put = get_object_or_404(Agendamentos, pk=id)
        form = AgendamentosForms(request.POST)

        if form.is_valid():
            put.paciente = paciente
            put.data = data
            put.time = time
            put.tipo = tipo
            put.obs = obs
            put.save()
    
            messages.success(request,'Compromisso editado com sucesso!')
            return redirect('agendamentos', tipo=0, periodo=0)  
        else:
            id_paciente = request.POST['paciente_id']
            url = Buscador.busca_url_base('/agendamentos/0/0')
            dados = {
                'title': str(url.nome) + ' EDITAR', 
                'cor': url.cor, 
                'titulo': str(url.nome) + ' - EDITAR',
                'form': form,
                'img': url.img,
                'id':0,
                'id_paciente':id_paciente,
                'url_base': 'agendamentos',
                'url_action': 'agendamentos.put'
            }
            
            return render(request, 'agendamentos/editar.html',dados)
            
def delete(request, id):
    """PARA EXCLUIR"""
    agendamentos = get_object_or_404(Agendamentos, pk=id)
    agendamentos.delete()
    messages.success(request,'Excluído com sucesso!')
    return redirect('agendamentos', tipo=0, periodo=0)

def export(request): 
    """EXPORTA A TABELA PARA XLS"""
    output = io.BytesIO()
    workbook = xlsxwriter.Workbook(output)
    worksheet = workbook.add_worksheet()
    data = Agendamentos.objects.all().values_list('paciente', 'data', 'time', 'tipo', 'obs')
    header_data = ['PACIENTE', 'DATA', 'HORÁRIO', 'TIPO', 'OBS']
    header_format = workbook.add_format({'bold': True,'bg_color': '#00627C', 'color' : '#ffffff'})
    
    for row_num, columns in enumerate(data):
        for col_num, data in enumerate(header_data):
            worksheet.write(0, col_num, data, header_format)
        for col_num, cell_data in enumerate(columns):
            worksheet.write(row_num+1, col_num, cell_data)

    workbook.close()
    output.seek(0)
    filename = 'agendamentos.xlsx'
    response = HttpResponse(
        output,
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = 'attachment; filename=%s' % filename

    return response