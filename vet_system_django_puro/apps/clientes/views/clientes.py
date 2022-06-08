import io
from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect
from django.contrib import messages
from django.db.models import Q
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django_tables2 import RequestConfig
from django.template.response import TemplateResponse
from clientes.models import Clientes
from clientes.forms import ClientesForms
from clientes.tables import ClientesTable, ContatosTable, EnderecoTable
from django_tables2.export.export import TableExport
from service.Buscador import *
import xlsxwriter

def listar(request):
    """ CARREGA A TABELA PRINCIPAL COM OS DADOS """

    table = ClientesTable(Clientes.objects.all())
   
    if 'sort' in request.GET:
        order = request.GET['sort']
    else:
        order = 'id'

    if 'buscar' in request.GET:
        buscar = request.GET['buscar']
    else:
        buscar = ''
    
    table = ClientesTable(Clientes.objects.all().distinct().order_by(order).filter( Q(nome__icontains=buscar) \
                        | Q(cpf__icontains=buscar) | Q(email__icontains=buscar) ))

    table.paginate(page=request.GET.get("page", 1), per_page=8)
   
    url = Buscador.busca_url_base('/clientes')
    dados = {
        'title': url.nome , 
        'buscar': buscar,
        'cor': url.cor, 
        'titulo': url.nome,
        'table': table,
        'url_export': 'clientes.export',
        'url_base': 'home',
        'img': url.img,
        'url_add': 'clientes.adicionar'
    }

    return render(request, 'clientes/index.html',dados)

def contatos(request, id):
    """ CARREGA A TABELA DE CONTATOS PELO ID """
    dado = get_object_or_404(Clientes, pk=id)
    table = ContatosTable(Clientes.objects.filter(id=id).all().distinct())
    url = Buscador.busca_url_base('/clientes')
    dados = {
        'title': url.nome, 
        'cor': url.cor, 
        'titulo': 'Cadastro de ' + str(dado.nome) ,
        'table': table,
        'url_export': 'clientes.export',
        'url_base': 'clientes',
        'img': url.img
    }

    return render(request, 'clientes/contatos.html',dados)

def detalhes(request, id):
    """ CARREGA A TABELA COMPLETA PELO ID """

    dado = get_object_or_404(Clientes, pk=id)
    table = ClientesTable(Clientes.objects.filter(id=id).all().distinct())
    url = Buscador.busca_url_base('/clientes')
    dados = {
        'title': url.nome, 
        'cor': url.cor, 
        'titulo': 'Cadastro de ' + str(dado.nome) ,
        'table': table,
        'url_export': 'clientes.export',
        'url_base': 'clientes',
        'img': url.img
    }

    return render(request, 'clientes/detalhes.html',dados)

def endereco(request, id):
    """ CARREGA A TABELA DE ENDEREÇO PELO ID """
        
    dado = get_object_or_404(Clientes, pk=id)
    table = EnderecoTable(Clientes.objects.filter(id=id).all().distinct())
    url = Buscador.busca_url_base('/clientes')
    dados = {
        'title': url.nome, 
        'cor': url.cor, 
        'titulo': 'Cadastro de ' + str(dado.nome) ,
        'table': table,
        'url_export': 'clientes.export',
        'url_base': 'clientes',
        'img': url.img
    }

    return render(request, 'clientes/endereco.html',dados)

def adicionar(request):
    """ PÁGINA DO ADICIONAR """
    
    form = ClientesForms()

    url = Buscador.busca_url_base('/clientes')
    dados = {
        'title': url.nome + ' - ADICIONAR',
        'cor': url.cor, 
        'titulo': url.nome + ' - ADICIONAR',
        'form': form,
        'img': url.img,
        'url_base': 'clientes',
        'url_action': 'clientes.store'
    }
    
    return render(request, 'clientes/adicionar.html',dados)
   
def editar(request, id):
    """ PÁGINA DO EDITAR """
    dado = get_object_or_404(Clientes, pk=id)
    instance = get_object_or_404(Clientes, pk=id)
    form = ClientesForms(instance=instance)
    url = Buscador.busca_url_base('/clientes')
    dados = {
        'title': url.nome + ' - EDITAR', 
        'cor': url.cor, 
        'titulo': 'Cliente ' + str(dado.nome) ,
        'id': id,
        'form': form,
        'img': url.img,
        'url_base': 'clientes',
        'url_action': 'clientes.put'
    }

    return render(request, 'clientes/editar.html',dados)
  
def store(request):
    """SALVAR NO BD """

    if request.method == 'POST': 
        nome = request.POST['nome']
        cpf = request.POST['cpf']
        data_nascimento = request.POST['data_nascimento']
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
        form = ClientesForms(request.POST)
        
        if form.is_valid():
            check = Clientes.objects.filter(cpf=cpf).count()
            if check == 0:
                store = Clientes.objects.create(
                    nome = nome,
                    cpf = cpf,
                    data_nascimento = data_nascimento,
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
                id_salvo = Clientes.objects.latest('id').id
                messages.success(request,'Cliente salvo com sucesso!')
                return redirect('pacientes.adicionar', id=id_salvo)  
            else:
                messages.error(request,'Cliente já cadastrado!')
                return redirect('clientes')  
        else:
           
            url = Buscador.busca_url_base('/clientes')
            dados = {
                'title': url.nome + ' - ADICIONAR',
                'cor': url.cor, 
                'titulo': url.nome + ' - ADICIONAR',
                'form': form,
                'img': url.img,
                'url_base': 'clientes',
                'url_action': 'clientes.store'
            }
            
            return render(request, 'clientes/adicionar.html',dados)

def put(request, id):
    """EDITA NO BD"""    
        
    if request.method == 'POST': 
        nome = request.POST['nome']
        cpf = request.POST['cpf']
        data_nascimento = request.POST['data_nascimento']
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
        put = get_object_or_404(Clientes, pk=id)

        form = ClientesForms(request.POST)

        if form.is_valid():
            put.nome = nome
            put.cpf = cpf
            put.data_nascimento = data_nascimento
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
    
            messages.success(request,'Cliente editado com sucesso!')
            return redirect('clientes')  
        else:
            url = Buscador.busca_url_base('/clientes')
            dado = get_object_or_404(Clientes, pk=id)
            dados = {
                'title': url.nome + ' - EDITAR',
                'cor': url.cor, 
                'titulo': 'Cliente ' + str(dado.nome) ,
                'id': id,
                'form': form,
                'img': url.img,
                'url_base': 'clientes',
                'url_action': 'clientes.put'
            }

            return render(request, 'clientes/editar.html',dados)
            
def delete(request, id):
    """DELETA NO BD"""
    clientes = get_object_or_404(Clientes, pk=id)
    clientes.delete()
    messages.success(request,'Excluído com sucesso!')
    return redirect('clientes')

def export(request): 
    """EXPORTA A TABELA PARA XLS"""
    output = io.BytesIO()
    workbook = xlsxwriter.Workbook(output)
    worksheet = workbook.add_worksheet()
    data = Clientes.objects.all().values_list('nome', 'cpf', 'data_nascimento', 'telefone_residencial',\
                                              'telefone_celular', 'telefone_comercial', 'email', 'cep',\
                                               'estado', 'cidade', 'bairro', 'endereco', 'numero', 'complemento')
    header_data = ['NOME', 'CPF', 'DATA NASCIMENTO', 'TEL RESIDENCIAL', 'TEL CELULAR', 'TEL COMERCIAL', \
                    'EMAIL', 'CEP', 'ESTADO', 'CIDADE', 'BAIRRO', 'ENDEREÇO', 'NÚMERO', 'COMPLEMENTO']
    header_format = workbook.add_format({'bold': True,'bg_color': '#00627C', 'color' : '#ffffff'})

    for row_num, columns in enumerate(data):
        for col_num, data in enumerate(header_data):
            worksheet.write(0, col_num, data, header_format)
        for col_num, cell_data in enumerate(columns):
            worksheet.write(row_num+1, col_num, cell_data)

    workbook.close()
    output.seek(0)
    filename = 'Clientes.xlsx'
    response = HttpResponse(
        output,
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = 'attachment; filename=%s' % filename

    return response