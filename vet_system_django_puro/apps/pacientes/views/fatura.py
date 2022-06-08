import io
from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect
from django.contrib import messages
from django.db.models import Q
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django_tables2 import RequestConfig
from django.template.response import TemplateResponse
from pacientes.models import FaturaProduto, Pacientes, HistoricoFatura
from administrativo.models import *
from pacientes.forms import FaturaForms
from pacientes.tables import FaturaProdutoTable
from django.db.models import FloatField, Sum
from django.db.models.functions import Cast
from service.Buscador import *
from service.Formata import *
from datetime import date
import xlsxwriter

def listar(request):
    """ CARREGA A TABELA PRINCIPAL COM OS DADOS """
    form = FaturaForms()
    url = Buscador.busca_url_base('/fatura')
    dados = {
        'title': url.nome, 
        'cor': url.cor, 
        'titulo': url.nome,
        'url_base': 'home',
        'img': url.img,
        'form': form
    }

    return render(request, 'fatura/index.html',dados)

def lista(request,id):
    """ CARREGA A TABELA PRINCIPAL COM OS DADOS """
    form = FaturaForms()
    url = Buscador.busca_url_base('/fatura')
    dados = {
        'title': url.nome, 
        'cor': url.cor, 
        'titulo': url.nome,
        'url_base': 'home',
        'id':id,
        'img': url.img,
        'form': form
    }

    return render(request, 'fatura/index.html',dados)

def cliente_paciente(request, id):
    """CARREGA OS DADOS DO SELECT DO PACIENTE"""
    paciente = Pacientes.objects.filter(pk=id)
    tableProduto = FaturaProdutoTable(FaturaProduto.objects.filter(faturado=0).filter(paciente__id=id).all().distinct())
    
    totalizadores_produto = FaturaProduto.objects.filter(faturado=0).filter(paciente__id=id).annotate(as_valor_produto=Cast('valor', FloatField())).aggregate(Sum('as_valor_produto'))
    produto_id = 0 
    data_cadastro = 0

    if totalizadores_produto['as_valor_produto__sum'] != None:
        total = totalizadores_produto['as_valor_produto__sum'];
    else:
        total = 0
     
    fatura_produto = FaturaProduto.objects.values('id', 'data_cadastro').filter(faturado=0).filter(paciente_id=id).order_by('-id')[:1]
    for linha in fatura_produto:
        produto_id = linha['id']
        data_cadastro = str(linha['data_cadastro'])
    
   
    dados = {
        'paciente':paciente,
        'tableProduto':tableProduto,
        'total':total,
        'produto_id':produto_id,
        'data_cadastro':data_cadastro
    }

    return render(request, 'fatura/cliente_paciente.html',dados)

def store(request):
    
    if request.method == 'POST': 
        produto = request.POST['produto']
        qtd_produto = request.POST['qtd_produto']
        tipo = request.POST['tipo']
        cliente = request.POST['cliente']

        if tipo == 'produto':
            produto_db = Produtos.objects.get(id=produto)
            cod = produto_db.id
            nome = produto_db.produto
            venda = produto_db.venda
        elif tipo == 'servico':
            servico_db = Servicos.objects.get(id=produto)
            cod = servico_db.id
            nome = servico_db.servico
            venda = servico_db.venda

        valor_produto = Formata.stringToFloat(qtd_produto) * Formata.stringToFloat(venda)
        paciente_db = Pacientes.objects.get(id=cliente)
        clientes_db = Clientes.objects.get(id=paciente_db.tutor.id)
        
        key = HistoricoFatura.objects.count()
        
        store = FaturaProduto.objects.create(
            paciente = paciente_db,
            tutor = clientes_db,
            cod = cod,
            key = key, 
            produto = nome,
            qtd = qtd_produto,
            valor = valor_produto
        )   
        store.save()
        return redirect('cliente_paciente', id=cliente)  

def delete(request, id):
    """DELETA NO BD"""
    if request.method == 'POST': 
        cliente = request.POST['cliente']
        fatura = get_object_or_404(FaturaProduto, pk=id)
        fatura.delete()
        return redirect('cliente_paciente', id=cliente)  

