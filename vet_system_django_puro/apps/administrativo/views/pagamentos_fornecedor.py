import io
from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect
from django.contrib import messages
from django.db.models import Q
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django_tables2 import RequestConfig
from django.template.response import TemplateResponse
from administrativo.models import Pagamentos
from administrativo.forms import PagamentosForms, PagamentosEditarForms
from administrativo.tables import PagamentosTable
from django_tables2.export.export import TableExport
from django.db.models import FloatField, Sum 
from django.db.models.functions import Cast
from service.Buscador import *
import xlsxwriter
from datetime import datetime

def listar(request, id, data):
    """ CARREGA A TABELA PRINCIPAL COM OS DADOS """
    user = Buscador.busca_user(request)
    table = PagamentosTable(Pagamentos.objects.all())
    form = PagamentosForms()
    
    if 'sort' in request.GET:
        order = request.GET['sort']
    else:
        order = 'pagamento'

    if 'buscar' in request.GET:
        buscar = request.GET['buscar']
    else:
        buscar = ''
    
    if id == 0 and data != '0':
        table = PagamentosTable(Pagamentos.objects.all().distinct().order_by(order).filter(pagamento=data).filter( Q(produto__produto__icontains=buscar) | Q(produto__fornecedor__nome__icontains=buscar) ))
        total_valor = Pagamentos.objects.filter(pagamento=data).annotate(as_valor_total=Cast('valor_total', FloatField())).aggregate(Sum('as_valor_total'))
    elif id != 0 and data == '0':
        table = PagamentosTable(Pagamentos.objects.all().distinct().order_by(order).filter(produto__fornecedor__id=id).filter( Q(produto__produto__icontains=buscar) | Q(produto__fornecedor__nome__icontains=buscar) ))
        total_valor = Pagamentos.objects.filter(produto__fornecedor__id=id).annotate(as_valor_total=Cast('valor_total', FloatField())).aggregate(Sum('as_valor_total'))
    elif id != 0 and data != '0':
        table = PagamentosTable(Pagamentos.objects.all().distinct().order_by(order).filter(pagamento=data).filter(produto__fornecedor__id=id).filter( Q(produto__produto__icontains=buscar) | Q(produto__fornecedor__nome__icontains=buscar) ))
        total_valor = Pagamentos.objects.filter(pagamento=data).filter(produto__fornecedor__id=id).annotate(as_valor_total=Cast('valor_total', FloatField())).aggregate(Sum('as_valor_total'))
    else:
        table = PagamentosTable(Pagamentos.objects.all().distinct().order_by(order).filter( Q(produto__produto__icontains=buscar) | Q(produto__fornecedor__nome__icontains=buscar) ))
        total_valor = Pagamentos.objects.annotate(as_valor_total=Cast('valor_total', FloatField())).aggregate(Sum('as_valor_total'))


    table.paginate(page=request.GET.get("page", 1), per_page=8)


    url = Buscador.busca_url_base('/pagamentos_fornecedor/0/0')
    dados = {
        'title': url.nome , 
        'buscar': buscar,
        'cor': url.cor, 
        'titulo': url.nome,
        'table': table,
        'data':data,
        'id':0,
        'url_export': 'pagamentos_fornecedor.export',
        'url_base': 'pagamentos',
        'img': url.img,
        'form':form,
        'total_valor':total_valor
    }

    return render(request, 'pagamentos/pagamentos_fornecedor/index.html',dados)

def editar(request, id):
    """ PÁGINA DO EDITAR """
    dado = get_object_or_404(Pagamentos, pk=id)
    instance = get_object_or_404(Pagamentos, pk=id)
    form = PagamentosEditarForms(instance=instance)
    url = Buscador.busca_url_base('/pagamentos_fornecedor/0/0')
    dados = {
        'title': url.nome + ' - EDITAR',
        'cor': url.cor, 
        'titulo': 'Pagamentos  para ' + str(dado.produto.fornecedor) ,
        'id': id,
        'form': form,
        'img': url.img,
        'url_base': 'pagamentos',
        'url_action': 'pagamentos_fornecedor.put'
    }

    return render(request, 'pagamentos/pagamentos_fornecedor/editar.html',dados)

def put(request, id):
    """EDITA NO BD"""    
        
    if request.method == 'POST': 
        pagamento = request.POST['pagamento']
        put = get_object_or_404(Pagamentos, pk=id)
        form = PagamentosEditarForms(request.POST)
             
    if form.is_valid():
        put.pagamento = pagamento
        put.save()

        messages.success(request,'Pagamento editado com sucesso!')
        return redirect('pagamentos', id=0, data=0)  
    else:
        url = Buscador.busca_url_base('/pagamentos_fornecedor/0/0')
        dado = get_object_or_404(Pagamentos, pk=id)
        dados = {
            'title': url.nome + ' - EDITAR',
            'cor': url.cor, 
            'titulo': 'Pagamento para ' + str(dado.produto.fornecedor) ,
            'id': id,
            'form': form,
            'img': url.img,
            'url_action': 'pagamentos_fornecedor.put'
        }

        return render(request, 'pagamentos/pagamentos_fornecedor/editar.html',dados)

def export(request): 
    """EXPORTA A TABELA PARA XLS"""
    user = Buscador.busca_user(request)
    output = io.BytesIO()
    workbook = xlsxwriter.Workbook(output)
    worksheet = workbook.add_worksheet()
    data = Pagamentos.objects.all().values_list('produto', 'qtd_total', 'valor_total', 'pagamento')
    header_data = ['PRODUTO', 'QTD', 'VALOR', 'DATA PAGAMENTO']
    header_format = workbook.add_format({'bold': True,'bg_color': '#00627C', 'color' : '#ffffff'})

    for row_num, columns in enumerate(data):
        for col_num, data in enumerate(header_data):
            worksheet.write(0, col_num, data, header_format)
        for col_num, cell_data in enumerate(columns):
            worksheet.write(row_num+1, col_num, cell_data)

    workbook.close()
    output.seek(0)
    filename = 'pagamentos_fornecedor.xlsx'
    response = HttpResponse(
        output,
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = 'attachment; filename=%s' % filename

    return response