import io
from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect
from django.contrib import messages
from django.db.models import Q
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django_tables2 import RequestConfig
from django.template.response import TemplateResponse
from administrativo.models import Parceiros
from administrativo.forms import ParceirosForms
from administrativo.tables import ParceirosTable, ParceirosContatosTable, ParceirosEnderecoTable
from django_tables2.export.export import TableExport
from service.Buscador import *
import xlsxwriter

def listar(request):
    """ CARREGA A TABELA PRINCIPAL COM OS DADOS """
    user = Buscador.busca_user(request)
    table = ParceirosTable(Parceiros.objects.all())
   
    if 'sort' in request.GET:
        order = request.GET['sort']
    else:
        order = 'id'

    if 'buscar' in request.GET:
        buscar = request.GET['buscar']
    else:
        buscar = ''
    
    table = ParceirosTable(Parceiros.objects.all().distinct().order_by(order).filter( Q(nome__icontains=buscar) \
                        | Q(cpf__icontains=buscar) | Q(email__icontains=buscar) | Q(especialidade__icontains=buscar) ))

    table.paginate(page=request.GET.get("page", 1), per_page=8)
   
    url = Buscador.busca_url_base('/parceiros')
    dados = {
        'title': url.nome , 
        'buscar': buscar,
        'cor': url.cor, 
        'titulo': url.nome,
        'table': table,
        'url_export': 'parceiros.export',
        'url_base': 'administrativo',
        'img': url.img,
        'url_add': 'parceiros.adicionar'
    }

    return render(request, 'parceiros/index.html',dados)

def contatos(request, id):
    """ CARREGA A TABELA DE CONTATOS PELO ID """
    user = Buscador.busca_user(request)
    dado = get_object_or_404(Parceiros, pk=id)
    table = ParceirosContatosTable(Parceiros.objects.filter(id=id).all().distinct())
    url = Buscador.busca_url_base('/parceiros')
    dados = {
        'title': url.nome, 
        'cor': url.cor, 
        'titulo': 'Cadastro de ' + str(dado.nome) ,
        'table': table,
        'url_export': 'parceiros.export',
        'url_base': 'parceiros',
        'img': url.img
    }

    return render(request, 'parceiros/contatos.html',dados)

def detalhes(request, id):
    """ CARREGA A TABELA COMPLETA PELO ID """
    user = Buscador.busca_user(request)
    dado = get_object_or_404(Parceiros, pk=id)
    table = ParceirosTable(Parceiros.objects.filter(id=id).all().distinct())
    url = Buscador.busca_url_base('/parceiros')
    dados = {
        'title': url.nome, 
        'cor': url.cor, 
        'titulo': 'Cadastro de ' + str(dado.nome) ,
        'table': table,
        'url_export': 'parceiros.export',
        'url_base': 'parceiros',
        'img': url.img
    }

    return render(request, 'parceiros/detalhes.html',dados)

def endereco(request, id):
    """ CARREGA A TABELA DE ENDEREÇO PELO ID """
    user = Buscador.busca_user(request)
    dado = get_object_or_404(Parceiros, pk=id)
    table = ParceirosEnderecoTable(Parceiros.objects.filter(id=id).all().distinct())
    url = Buscador.busca_url_base('/parceiros')
    dados = {
        'title': url.nome, 
        'cor': url.cor, 
        'titulo': 'Cadastro de ' + str(dado.nome) ,
        'table': table,
        'url_export': 'parceiros.export',
        'url_base': 'parceiros',
        'img': url.img
    }

    return render(request, 'parceiros/endereco.html',dados)

def adicionar(request):
    """ PÁGINA DO ADICIONAR """
    user = Buscador.busca_user(request)
    form = ParceirosForms()

    url = Buscador.busca_url_base('/parceiros')
    dados = {
        'title': url.nome + ' - ADICIONAR',
        'cor': url.cor, 
        'titulo': url.nome + ' - ADICIONAR',
        'form': form,
        'img': url.img,
        'url_base': 'parceiros',
        'url_action': 'parceiros.store'
    }
    
    return render(request, 'parceiros/adicionar.html',dados)
   
def editar(request, id):
    """ PÁGINA DO EDITAR """
    dado = get_object_or_404(Parceiros, pk=id)
    instance = get_object_or_404(Parceiros, pk=id)
    form = ParceirosForms(instance=instance)
    url = Buscador.busca_url_base('/parceiros')
    dados = {
        'title': url.nome + ' - EDITAR',
        'cor': url.cor, 
        'titulo': 'Parceiro ' + str(dado.nome) ,
        'id': id,
        'form': form,
        'img': url.img,
        'url_base': 'parceiros',
        'url_action': 'parceiros.put'
    }

    return render(request, 'parceiros/editar.html',dados)
  
def store(request):
    """SALVAR NO BD """
    user = Buscador.busca_user(request)
    if request.method == 'POST': 
        nome = request.POST['nome']
        cpf = request.POST['cpf']
        especialidade = request.POST['especialidade']
        telefone_residencial = request.POST['telefone_residencial']
        telefone_celular = request.POST['telefone_celular']
        telefone_comercial = request.POST['telefone_celular']
        email = request.POST['email']
        cep = request.POST['cep']
        estado = request.POST['estado']
        cidade = request.POST['cidade']
        bairro = request.POST['bairro']
        endereco = request.POST['endereco']
        numero = request.POST['numero']
        complemento = request.POST['complemento']
        form = ParceirosForms(request.POST)
        
        if form.is_valid():
            check = Parceiros.objects.filter(cpf=cpf).count()
            if check == 0:
                store = Parceiros.objects.create(
                    nome = nome,
                    cpf = cpf,
                    especialidade = especialidade,
                    telefone_residencial = telefone_residencial,
                    telefone_celular = telefone_celular,
                    telefone_comercial = telefone_celular,
                    email = email,
                    cep = cep,
                    estado = estado,
                    cidade = cidade,
                    bairro = bairro,
                    endereco = endereco,
                    numero = numero,
                    complemento = complemento
                )   
                store.save()
                messages.success(request,'Parceiro salvo com sucesso!')
                return redirect('parceiros')  
            else:
                messages.error(request,'Parceiro já cadastrado!')
                return redirect('parceiros')  
        else:
           
            url = Buscador.busca_url_base('/parceiros')
            dados = {
                'title': url.nome + ' - ADICIONAR',
                'cor': url.cor, 
                'titulo': url.nome + ' - ADICIONAR',
                'form': form,
                'img': url.img,
                'url_base': 'parceiros',
                'url_action': 'parceiros.store'
            }
            
            return render(request, 'parceiros/adicionar.html',dados)

def put(request, id):
    """EDITA NO BD"""    
        
    if request.method == 'POST': 
        nome = request.POST['nome']
        cpf = request.POST['cpf']
        especialidade = request.POST['especialidade']
        telefone_residencial = request.POST['telefone_residencial']
        telefone_celular = request.POST['telefone_celular']
        telefone_comercial = request.POST['telefone_celular']
        email = request.POST['email']
        cep = request.POST['cep']
        estado = request.POST['estado']
        cidade = request.POST['cidade']
        bairro = request.POST['bairro']
        endereco = request.POST['endereco']
        numero = request.POST['numero']
        complemento = request.POST['complemento']
        put = get_object_or_404(Parceiros, pk=id)

        form = ParceirosForms(request.POST)

        if form.is_valid():
            put.nome = nome
            put.cpf = cpf
            put.especialidade = especialidade
            put.telefone_residencial = telefone_residencial
            put.telefone_celular = telefone_celular
            put.telefone_comercial = telefone_celular
            put.email = email
            put.cep = cep
            put.estado = estado
            put.cidade = cidade
            put.bairro = bairro
            put.endereco = endereco
            put.numero = numero
            put.complemento = complemento
            put.save()
    
            messages.success(request,'Parceiro editado com sucesso!')
            return redirect('parceiros')  
        else:
            url = Buscador.busca_url_base('/parceiros')
            dado = get_object_or_404(Parceiros, pk=id)
            dados = {
                'title': url.nome + ' - EDITAR',
                'cor': url.cor, 
                'titulo': 'Parceiro ' + str(dado.nome) ,
                'id': id,
                'form': form,
                'img': url.img,
                'url_base': 'parceiros',
                'url_action': 'parceiros.put'
            }

            return render(request, 'parceiros/editar.html',dados)
            
def delete(request, id):
    """DELETA NO BD"""
    user = Buscador.busca_user(request)
    parceiros = get_object_or_404(Parceiros, pk=id)
    parceiros.delete()
    messages.success(request,'Excluído com sucesso!')
    return redirect('parceiros')

def export(request): 
    """EXPORTA A TABELA PARA XLS"""
    user = Buscador.busca_user(request)
    output = io.BytesIO()
    workbook = xlsxwriter.Workbook(output)
    worksheet = workbook.add_worksheet()
    data = Parceiros.objects.all().values_list('nome', 'cpf', 'especialidade', 'telefone_residencial',\
                                              'telefone_celular', 'telefone_comercial', 'email', 'cep',\
                                               'estado', 'cidade', 'bairro', 'endereco', 'numero', 'complemento')
    header_data = ['NOME', 'CPF', 'ESPECIALIDADE', 'TEL RESIDENCIAL', 'TEL CELULAR', 'TEL COMERCIAL', \
                    'EMAIL', 'CEP', 'ESTADO', 'CIDADE', 'BAIRRO', 'ENDEREÇO', 'NÚMERO', 'COMPLEMENTO']
    header_format = workbook.add_format({'bold': True,'bg_color': '#00627C', 'color' : '#ffffff'})

    for row_num, columns in enumerate(data):
        for col_num, data in enumerate(header_data):
            worksheet.write(0, col_num, data, header_format)
        for col_num, cell_data in enumerate(columns):
            worksheet.write(row_num+1, col_num, cell_data)

    workbook.close()
    output.seek(0)
    filename = 'Parceiros.xlsx'
    response = HttpResponse(
        output,
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = 'attachment; filename=%s' % filename

    return response