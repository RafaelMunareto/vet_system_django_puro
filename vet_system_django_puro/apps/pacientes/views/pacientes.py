import io
from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect
from django.contrib import messages
from django.db.models import Q
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django_tables2 import RequestConfig
from django.template.response import TemplateResponse
from clientes.models import Clientes
from pacientes.models import Pacientes
from pacientes.forms import PacientesForms, PacientesEditarForms
from pacientes.tables import PacientesTable, PacientesAssociadosTable
from django_tables2.export.export import TableExport
from service.Buscador import *
from service.Formata import *
import xlsxwriter

def listar(request):
    """ CARREGA A TABELA PRINCIPAL COM OS DADOS """

    table = PacientesTable(Pacientes.objects.all())
    
    if 'sort' in request.GET:
        order = request.GET['sort']
    else:
        order = 'id'

    if 'buscar' in request.GET:
        buscar = request.GET['buscar']
    else:
        buscar = ''
    
    table = PacientesTable(Pacientes.objects.all().distinct().order_by(order).filter( Q(nome__icontains=buscar) | Q(raca__icontains=buscar) ))

    table.paginate(page=request.GET.get("page", 1), per_page=8)
   
    url = Buscador.busca_url_base('/pacientes')
    dados = {
        'title': url.nome, 
        'buscar': buscar,
        'cor': url.cor, 
        'titulo': url.nome,
        'table': table,
        'url_export': 'pacientes.export',
        'url_base': 'home',
        'url_add': 'pacientes.adicionar_novo',
        'img': url.img
    }

    return render(request, 'pacientes/index.html',dados)

def detalhes(request, id):
    """ CARREGA A TABELA COMPLETA PELO ID """

    dado = get_object_or_404(Pacientes, pk=id)
    table = PacientesTable(Pacientes.objects.filter(id=id).all().distinct())
    url = Buscador.busca_url_base('/pacientes')
    dados = {
        'title': url.nome, 
        'cor': url.cor, 
        'titulo': 'Cadastro de ' + str(dado.nome) ,
        'table': table,
        'url_export': 'pacientes.export',
        'url_base': 'pacientes',
        'img': url.img
    }

    return render(request, 'pacientes/detalhes.html',dados)

def adicionar(request, id):
    """ PÁGINA DO ADICIONAR """
    
    form = PacientesForms()
    dado = get_object_or_404(Clientes, pk=id)
    url = Buscador.busca_url_base('/pacientes')
    dados = {
        'title': url.nome + ' ADICIONAR', 
        'cor': url.cor, 
        'titulo':'Pets de ' +  dado.nome,
        'form': form,
        'img': url.img,
        'id':id,
        'url_base': 'pacientes.associados',
        'url_action': 'pacientes.store'
    }
    
    return render(request, 'pacientes/adicionar.html',dados)

def adicionar_novo(request):
    """ PÁGINA DO ADICIONAR NOVO """
    
    form = PacientesForms()
    url = Buscador.busca_url_base('/pacientes')
    dados = {
        'title': url.nome + ' ADICIONAR', 
        'cor': url.cor, 
        'titulo':url.nome + ' - ADICIONAR',
        'form': form,
        'img': url.img,
        'url_base': 'pacientes',
        'url_action': 'pacientes.store'
    }
    
    return render(request, 'pacientes/adicionar_novo.html',dados)
  
def associados(request, id):

    try:
        dado = get_object_or_404(Clientes, pk=id)
        nome =  'PETs de ' + dado.nome
    except:
        nome = 'Não possui pets associados'
        
    table = PacientesAssociadosTable(Pacientes.objects.filter(tutor=id).all().distinct())
    url = Buscador.busca_url_base('/pacientes')
    dados = {
        'title': url.nome, 
        'cor': url.cor, 
        'titulo':   str(nome) ,
        'table': table,
        'url_export': 'pacientes.export',
        'url_base': 'clientes',
        'url_add': 'pacientes.adicionar',
        'img': url.img,
        'id':id,
    }

    return render(request, 'pacientes/pacientes_associados.html',dados)
 
def editar(request, id):
    """ PÁGINA DO EDITAR """
    dado = get_object_or_404(Pacientes, pk=id)
    instance = get_object_or_404(Pacientes, pk=id)
    id_cliente = dado.tutor.id
    form = PacientesForms(instance=instance)
    url = Buscador.busca_url_base('/pacientes')
    dados = {
        'title': url.nome + ' EDITAR', 
        'cor': url.cor, 
        'titulo': dado.nome,
        'id': id,
        'id_cliente':id_cliente,
        'form': form,
        'img': url.img,
        'url_base': 'pacientes.associados',
        'url_action': 'pacientes.put'
    }

    return render(request, 'pacientes/editar.html',dados)
  
def store(request):
    """SALVAR NO BD """

    if request.method == 'POST': 
        cliente_id = request.POST['cliente_id']
        nome = request.POST['nome']
        raca = request.POST['raca']
        especie = request.POST['especie']
        sexo = request.POST['sexo']
        peso = request.POST['peso']
        data_nascimento = request.POST['data_nascimento']
        form = PacientesForms(request.POST)
        
        if form.is_valid():
            tutor = Clientes.objects.get(id=cliente_id)
            idade = Formata.data_menos_hoje(request.POST['data_nascimento'])
            store = Pacientes.objects.create(
                tutor = tutor,
                nome = nome,
                raca = raca,
                especie = especie,
                sexo = sexo,
                idade = idade,
                peso = peso,
                data_nascimento = data_nascimento
            )   
            store.save()
            messages.success(request,'Paciente salvo com sucesso!')
            return redirect('pacientes.associados', id=cliente_id)  
        else:
            cliente_id = request.POST['cliente_id']
            url = Buscador.busca_url_base('/pacientes')
            dados = {
                'title': url.nome + ' ADICIONAR', 
                'cor': url.cor, 
                'titulo': url.nome + ' - ADICIONAR',
                'form': form,
                'img': url.img,
                'id':cliente_id,
                'url_base': 'pacientes.associados',
                'url_action': 'pacientes.store'
            }
            
            return render(request, 'pacientes/adicionar.html',dados)

def put(request, id):
    """EDITAR NO BD"""    
        
    if request.method == 'POST': 
        cliente_id = request.POST['cliente_id']
        id_tutor = Pacientes.objects.get(id=cliente_id)
        tutor = Clientes.objects.get(id=id_tutor.tutor.id)
        nome = request.POST['nome']
        raca = request.POST['raca']
        especie = request.POST['especie']
        sexo = request.POST['sexo']
        peso = request.POST['peso']
        data_nascimento = request.POST['data_nascimento']
        put = get_object_or_404(Pacientes, pk=id)
        form = PacientesEditarForms(request.POST)

        if form.is_valid():
            idade = Formata.data_menos_hoje(request.POST['data_nascimento'])
            put.tutor = tutor
            put.nome = nome
            put.raca = raca
            put.especie = especie
            put.sexo = sexo
            put.idade = idade
            put.peso = peso
            put.data_nascimento = data_nascimento
            put.save()
    
            messages.success(request,'Paciente editado com sucesso!')
            return redirect('pacientes.associados', id=id_tutor.tutor.id)
        else:
            cliente_id = request.POST['cliente_id']
            url = Buscador.busca_url_base('/pacientes')
            dados = {
                'title':str(url.nome) + ' EDITAR', 
                'cor': url.cor, 
                'titulo': str(url.nome) + ' - EDITAR',
                'form': form,
                'img': url.img,
                'id':cliente_id,
                'url_base': 'pacientes.associados',
                'url_action': 'pacientes.put'
            }
            
            return render(request, 'pacientes/editar.html',dados)
            
def delete(request, id):
    """PARA EXCLUIR"""
    pacientes = get_object_or_404(Pacientes, pk=id)
    pacientes.delete()
    messages.success(request,'Excluído com sucesso!')
    return redirect('pacientes.associados', id=pacientes.tutor.id)

def export(request): 
    """EXPORTA A TABELA PARA XLS"""
    output = io.BytesIO()
    workbook = xlsxwriter.Workbook(output)
    worksheet = workbook.add_worksheet()
    data = Pacientes.objects.all().values_list('tutor', 'nome', 'raca', 'sexo', 'anos', 'meses', 'peso', 'data_nascimento')
    header_data = ['TUTOR', 'NOME', 'RAÇA', 'SEXO', 'ANOS', 'MESES', 'PESO', 'DATA DE NASCIMENTO']
    header_format = workbook.add_format({'bold': True,'bg_color': '#00627C', 'color' : '#ffffff'})
    
    for row_num, columns in enumerate(data):
        for col_num, data in enumerate(header_data):
            worksheet.write(0, col_num, data, header_format)
        for col_num, cell_data in enumerate(columns):
            worksheet.write(row_num+1, col_num, cell_data)

    workbook.close()
    output.seek(0)
    filename = 'Pacientes.xlsx'
    response = HttpResponse(
        output,
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = 'attachment; filename=%s' % filename

    return response