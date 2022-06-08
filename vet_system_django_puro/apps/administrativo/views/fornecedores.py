import io
from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect
from django.contrib import messages
from django.db.models import Q
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django_tables2 import RequestConfig
from django.template.response import TemplateResponse
from administrativo.models import Fornecedores
from administrativo.forms import FornecedoresForms
from administrativo.tables import FornecedoresTable, FornecedoresContatosTable, FornecedoresEnderecoTable, FornecedoresBancarioTable
from django_tables2.export.export import TableExport
from service.Buscador import *
import xlsxwriter

def listar(request):
    """ CARREGA A TABELA PRINCIPAL COM OS DADOS """
    user = Buscador.busca_user(request)
    table = FornecedoresTable(Fornecedores.objects.all())
   
    if 'sort' in request.GET:
        order = request.GET['sort']
    else:
        order = 'id'

    if 'buscar' in request.GET:
        buscar = request.GET['buscar']
    else:
        buscar = ''
    
    table = FornecedoresTable(Fornecedores.objects.all().distinct().order_by(order).filter( Q(nome__icontains=buscar) \
                        | Q(cnpj__icontains=buscar) | Q(email__icontains=buscar) | Q(ramo__icontains=buscar) ))

    table.paginate(page=request.GET.get("page", 1), per_page=8)
   
    url = Buscador.busca_url_base('/fornecedores')
    dados = {
        'title': url.nome , 
        'buscar': buscar,
        'cor': url.cor, 
        'titulo': url.nome,
        'table': table,
        'url_export': 'fornecedores.export',
        'url_base': 'administrativo',
        'img': url.img,
        'url_add': 'fornecedores.adicionar'
    }

    return render(request, 'fornecedores/index.html',dados)

def contatos(request, id):
    """ CARREGA A TABELA DE CONTATOS PELO ID """
    user = Buscador.busca_user(request)
    dado = get_object_or_404(Fornecedores, pk=id)
    table = FornecedoresContatosTable(Fornecedores.objects.filter(id=id).all().distinct())
    url = Buscador.busca_url_base('/fornecedores')
    dados = {
        'title': url.nome, 
        'cor': url.cor, 
        'titulo': 'Cadastro de ' + str(dado.nome) ,
        'table': table,
        'url_export': 'fornecedores.export',
        'url_base': 'fornecedores',
        'img': url.img
    }

    return render(request, 'fornecedores/contatos.html',dados)

def detalhes(request, id):
    """ CARREGA A TABELA COMPLETA PELO ID """
    user = Buscador.busca_user(request) 
    dado = get_object_or_404(Fornecedores, pk=id)
    table = FornecedoresTable(Fornecedores.objects.filter(id=id).all().distinct())
    url = Buscador.busca_url_base('/fornecedores')
    dados = {
        'title': url.nome, 
        'cor': url.cor, 
        'titulo': 'Cadastro de ' + str(dado.nome) ,
        'table': table,
        'url_export': 'fornecedores.export',
        'url_base': 'fornecedores',
        'img': url.img
    }

    return render(request, 'fornecedores/detalhes.html',dados)

def endereco(request, id):
    """ CARREGA A TABELA DE ENDEREÇO PELO ID """
    user = Buscador.busca_user(request)  
    dado = get_object_or_404(Fornecedores, pk=id)
    table = FornecedoresEnderecoTable(Fornecedores.objects.filter(id=id).all().distinct())
    url = Buscador.busca_url_base('/fornecedores')
    dados = {
        'title': url.nome, 
        'cor': url.cor, 
        'titulo': 'Cadastro de ' + str(dado.nome) ,
        'table': table,
        'url_export': 'fornecedores.export',
        'url_base': 'fornecedores',
        'img': url.img
    }

    return render(request, 'fornecedores/endereco.html',dados)

def bancario(request, id):
    """ CARREGA A TABELA DE DADOS BANCÁRIOS PELO ID """
    user = Buscador.busca_user(request)
    dado = get_object_or_404(Fornecedores, pk=id)
    table = FornecedoresBancarioTable(Fornecedores.objects.filter(id=id).all().distinct())
    url = Buscador.busca_url_base('/fornecedores')
    dados = {
        'title': url.nome, 
        'cor': url.cor, 
        'titulo': 'Cadastro de ' + str(dado.nome) ,
        'table': table,
        'url_export': 'fornecedores.export',
        'url_base': 'fornecedores',
        'img': url.img
    }

    return render(request, 'fornecedores/bancario.html',dados)

def adicionar(request):
    """ PÁGINA DO ADICIONAR """
    
    form = FornecedoresForms()

    url = Buscador.busca_url_base('/fornecedores')
    dados = {
        'title': url.nome + ' - ADICIONAR',
        'cor': url.cor, 
        'titulo': url.nome + ' - ADICIONAR',
        'form': form,
        'img': url.img,
        'url_base': 'fornecedores',
        'url_action': 'fornecedores.store'
    }
    
    return render(request, 'fornecedores/adicionar.html',dados)
   
def editar(request, id):
    """ PÁGINA DO EDITAR """
    dado = get_object_or_404(Fornecedores, pk=id)
    instance = get_object_or_404(Fornecedores, pk=id)
    form = FornecedoresForms(instance=instance)
    url = Buscador.busca_url_base('/fornecedores')
    dados = {
        'title': url.nome + ' - EDITAR',
        'cor': url.cor, 
        'titulo': 'Fornecedor ' + str(dado.nome) ,
        'id': id,
        'form': form,
        'img': url.img,
        'url_base': 'fornecedores',
        'url_action': 'fornecedores.put'
    }

    return render(request, 'fornecedores/editar.html',dados)
  
def store(request):
    """SALVAR NO BD """
    user = Buscador.busca_user(request)
    if request.method == 'POST': 
        nome = request.POST['nome']
        cnpj = request.POST['cnpj']
        ramo = request.POST['ramo']
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
        obs = request.POST['obs']
        banco = request.POST['banco']
        agencia = request.POST['agencia']
        conta = request.POST['conta']
               
        form = FornecedoresForms(request.POST)
        
        if form.is_valid():
            check = Fornecedores.objects.filter(cnpj=cnpj).count()
            if check == 0:
                store = Fornecedores.objects.create(
                    nome = nome,
                    cnpj = cnpj,
                    ramo = ramo,
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
                    complemento = complemento,
                    obs = obs,
                    banco = banco,
                    agencia = agencia,
                    conta = conta
                )   
                store.save()
                messages.success(request,'Fornecedor salvo com sucesso!')
                return redirect('fornecedores')  
            else:
                messages.error(request,'Fornecedor já cadastrado!')
                return redirect('fornecedores')  
        else:
           
            url = Buscador.busca_url_base('/fornecedores')
            dados = {
                'title': url.nome + ' - ADICIONAR',
                'cor': url.cor, 
                'titulo': url.nome + ' - ADICIONAR',
                'form': form,
                'img': url.img,
                'url_base': 'fornecedores',
                'url_action': 'fornecedores.store'
            }
            
            return render(request, 'fornecedores/adicionar.html',dados)

def put(request, id):
    """EDITA NO BD"""    
        
    if request.method == 'POST': 
        nome = request.POST['nome']
        cnpj = request.POST['cnpj']
        ramo = request.POST['ramo']
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
        obs = request.POST['obs']
        banco = request.POST['banco']
        agencia = request.POST['agencia']
        conta = request.POST['conta']
        put = get_object_or_404(Fornecedores, pk=id)

        form = FornecedoresForms(request.POST)

        if form.is_valid():
            put.nome = nome
            put.cnpj = cnpj
            put.ramo = ramo
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
            put.obs = obs
            put.banco = banco
            put.agencia = agencia
            put.conta = conta
            put.save()

            messages.success(request,'Fornecedor editado com sucesso!')
            return redirect('fornecedores')  
        else:
            url = Buscador.busca_url_base('/fornecedores')
            dado = get_object_or_404(Fornecedores, pk=id)
            dados = {
                'title': url.nome + ' - EDITAR',
                'cor': url.cor, 
                'titulo': 'Fornecedor ' + str(dado.nome) ,
                'id': id,
                'form': form,
                'img': url.img,
                'url_base': 'fornecedores',
                'url_action': 'fornecedores.put'
            }

            return render(request, 'fornecedores/editar.html',dados)
                
def delete(request, id):
    """DELETA NO BD"""
    fornecedores = get_object_or_404(Fornecedores, pk=id)
    fornecedores.delete()
    messages.success(request,'Excluído com sucesso!')
    return redirect('fornecedores')

def export(request): 
    """EXPORTA A TABELA PARA XLS"""
    user = Buscador.busca_user(request)
    output = io.BytesIO()
    workbook = xlsxwriter.Workbook(output)
    worksheet = workbook.add_worksheet()
    data = Fornecedores.objects.all().values_list('nome', 'cnpj', 'ramo', 'telefone_residencial',\
                                              'telefone_celular', 'telefone_comercial', 'email', 'cep',\
                                               'estado', 'cidade', 'bairro', 'endereco', 'numero', 'complemento')
    header_data = ['NOME', 'CNPJ', 'RAMO', 'TEL RESIDENCIAL', 'TEL CELULAR', 'TEL COMERCIAL', \
                    'EMAIL', 'CEP', 'ESTADO', 'CIDADE', 'BAIRRO', 'ENDEREÇO', 'NÚMERO', 'COMPLEMENTO']
    header_format = workbook.add_format({'bold': True,'bg_color': '#00627C', 'color' : '#ffffff'})

    for row_num, columns in enumerate(data):
        for col_num, data in enumerate(header_data):
            worksheet.write(0, col_num, data, header_format)
        for col_num, cell_data in enumerate(columns):
            worksheet.write(row_num+1, col_num, cell_data)

    workbook.close()
    output.seek(0)
    filename = 'Fornecedores.xlsx'
    response = HttpResponse(
        output,
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = 'attachment; filename=%s' % filename

    return response