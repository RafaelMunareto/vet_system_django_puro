import io
from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect
from django.contrib import messages
from django.db.models import Q
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django_tables2 import RequestConfig
from django.template.response import TemplateResponse
from administrativo.models import CustosFixos, Pagamentos
from administrativo.tables import CustosFixosTable, PagamentosTable
from django_tables2.export.export import TableExport
from django.db.models import FloatField, Sum
from django.db.models.functions import Cast
from service.Buscador import *
import xlsxwriter
from datetime import datetime

def listar(request, periodo):
    """ CARREGA A TABELA PRINCIPAL COM OS DADOS """
    user = Buscador.busca_user(request)
    table = CustosFixosTable(CustosFixos.objects.all())
    
    if 'sort' in request.GET:
        order = request.GET['sort']
        order2 = request.GET['sort']
        try:
            CustosFixos.objects.all().order_by(order)
        except:
            order = 'pagamento'
        try:
            Pagamentos.objects.all().order_by(order)
        except:
            order2 = 'pagamento'
    else:
        order = 'pagamento'
        order2 = 'pagamento'
        
    if 'buscar' in request.GET:
        buscar = request.GET['buscar']
    else:
        buscar = ''
  
    if 'buscar2' in request.GET:
        buscar2 = request.GET['buscar2']
    else:
        buscar2 = ''
    
    if periodo == 1:
        data = Buscador.busca_dia() 
        data_recorrente = Buscador.busca_dia_recorrente()
        table = CustosFixosTable(CustosFixos.objects.filter(Q(pagamento__contains=data) | Q(pagamento__contains=data_recorrente)).distinct().order_by(order).filter(Q(nome__icontains=buscar) |  Q(descricao__icontains=buscar) ))
        total_valor = CustosFixos.objects.filter(Q(pagamento__contains=data) | Q(pagamento__contains=data_recorrente)).annotate(as_custo=Cast('custo', FloatField())).aggregate(Sum('as_custo'))
        table2 = PagamentosTable(Pagamentos.objects.filter(pagamento__contains=data).distinct().order_by(order2).filter( Q(produto__produto__icontains=buscar2) | Q(produto__fornecedor__nome__icontains=buscar2) ))
        total_valor2 = Pagamentos.objects.filter(pagamento__contains=data).annotate(as_valor_total=Cast('valor_total', FloatField())).aggregate(Sum('as_valor_total'))
    elif periodo == 2:
        data = Buscador.busca_semana() 
        table = CustosFixosTable(CustosFixos.objects.filter(pagamento__in=data).distinct().order_by(order, 'pagamento').filter(Q(nome__icontains=buscar) |  Q(descricao__icontains=buscar) ))
        total_valor = CustosFixos.objects.filter(pagamento__in=data).annotate(as_custo=Cast('custo', FloatField())).aggregate(Sum('as_custo'))
        table2 = PagamentosTable(Pagamentos.objects.filter(pagamento__in=data).distinct().order_by(order2).filter( Q(produto__produto__icontains=buscar2) | Q(produto__fornecedor__nome__icontains=buscar2) ))
        total_valor2 = Pagamentos.objects.filter(pagamento__in=data).annotate(as_valor_total=Cast('valor_total', FloatField())).aggregate(Sum('as_valor_total'))
    elif periodo == 3:
        data = Buscador.busca_mes()  
        table = CustosFixosTable(CustosFixos.objects.filter(Q(pagamento__contains=data) | Q(pagamento__contains=data_recorrente)).distinct().order_by(order).filter(Q(nome__icontains=buscar) |  Q(descricao__icontains=buscar) ))
        total_valor = CustosFixos.objects.filter(Q(pagamento__contains=data) | Q(pagamento__contains=data_recorrente)).annotate(as_custo=Cast('custo', FloatField())).aggregate(Sum('as_custo'))
        table2 = PagamentosTable(Pagamentos.objects.filter(pagamento__contains=data).distinct().order_by(order2).filter( Q(produto__produto__icontains=buscar2) | Q(produto__fornecedor__nome__icontains=buscar2) ))
        total_valor2 = Pagamentos.objects.filter(pagamento__contains=data).annotate(as_valor_total=Cast('valor_total', FloatField())).aggregate(Sum('as_valor_total'))
    elif periodo == 0:  
        data = ''
        table = CustosFixosTable(CustosFixos.objects.filter(Q(pagamento__contains='202') | Q(pagamento__contains='9999')).distinct().order_by(order).filter(Q(nome__icontains=buscar) | Q(descricao__icontains=buscar) ))
        total_valor = CustosFixos.objects.annotate(as_custo=Cast('custo', FloatField())).aggregate(Sum('as_custo'))
        table2 = PagamentosTable(Pagamentos.objects.filter(pagamento__contains='202').distinct().order_by(order2).filter( Q(produto__produto__icontains=buscar2) | Q(produto__fornecedor__nome__icontains=buscar2) ))
        total_valor2 = Pagamentos.objects.annotate(as_valor_total=Cast('valor_total', FloatField())).aggregate(Sum('as_valor_total'))

    if total_valor['as_custo__sum'] != None:
        total_valor = total_valor['as_custo__sum'] 
    else:
        total_valor = 0

    if total_valor2['as_valor_total__sum'] != None:
        total_valor2 = total_valor2['as_valor_total__sum']
    else:
        total_valor2 = 0

    total = total_valor + total_valor2 
    table.paginate(page=request.GET.get("page", 1), per_page=8)
    table2.paginate(page=request.GET.get("page", 1), per_page=8)

    periodo_formatado = Formata.formata_periodo(periodo)
    url = Buscador.busca_url_base('/pagamentos/0')
    dados = {
        'title': url.nome , 
        'buscar': buscar,
        'cor': url.cor, 
        'titulo': str(url.nome) + ' - ' + str(periodo_formatado),
        'table': table,
        'table2': table2,
        'total_valor2': total_valor2,
        'data':data,
        'id':id,
        'total':total,
        'total_valor':total_valor,
        'url_base': 'administrativo',
        'img': url.img,
    }

    return render(request, 'pagamentos/index.html',dados)
