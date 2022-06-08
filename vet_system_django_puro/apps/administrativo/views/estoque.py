import io
from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect
from django.contrib import messages
from django.db.models import Q
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django_tables2 import RequestConfig
from django.template.response import TemplateResponse
from administrativo.models import Estoque, Produtos, Pagamentos
from administrativo.forms import EstoqueForms, EstoqueEditarForms
from administrativo.tables import EstoqueTable
from django_tables2.export.export import TableExport
from django.db.models import FloatField, Sum
from django.db.models.functions import Cast
from service.Buscador import *
from service.Formata import *
import xlsxwriter

def listar(request):
    """ CARREGA A TABELA PRINCIPAL COM OS DADOS """
    user = Buscador.busca_user(request)
    table = EstoqueTable(Estoque.objects.all())
    form = EstoqueForms()

    if 'sort' in request.GET:
        order = request.GET['sort']
    else:
        order = 'id'

    if 'buscar' in request.GET:
        buscar = request.GET['buscar']
    else:
        buscar = ''
    
    table = EstoqueTable(Estoque.objects.all().distinct().order_by(order).filter(Q(produto__produto__icontains=buscar)))

    table.paginate(page=request.GET.get("page", 1), per_page=8)
   
    totalizadores = Estoque.objects.all().annotate(
                as_qtd_total=Cast('qtd_total', FloatField()),
                as_valor_total=Cast('valor_total', FloatField())) \
                .aggregate(Sum('as_qtd_total'), Sum('as_valor_total'))
    
    estoque = Estoque.objects.distinct().all()
    menor_estoque = Estoque.objects.all().order_by('-qtd_total')[:5]     
    maior_estoque = Estoque.objects.all().order_by('qtd_total')[:5]

    url = Buscador.busca_url_base('/estoque')
    dados = {
        'title': url.nome , 
        'buscar': buscar,
        'cor': url.cor, 
        'titulo': url.nome,
        'table': table,
        'form':form,
        'url_export': 'estoque.export',
        'url_base': 'administrativo',
        'img': url.img,
        'url_action':'estoque.store',
        'estoque':estoque,
        'totalizadores':totalizadores,
        'menor_estoque':menor_estoque,
        'maior_estoque':maior_estoque
    }

    return render(request, 'estoque/index.html',dados)

def editar(request, id):
    """ PÁGINA DO EDITAR """
    instance = get_object_or_404(Estoque, pk=id)
    form = EstoqueEditarForms(instance=instance)
    url = Buscador.busca_url_base('/estoque')
    dados = {
        'title': url.nome + ' - EDITAR',
        'cor': url.cor, 
        'titulo': 'Produto ' + str(instance.produto) ,
        'id': id,
        'form': form,
        'img': url.img,
        'url_base': 'estoque',
        'url_action': 'estoque.put'
    }

    return render(request, 'estoque/editar.html',dados)
  
def store(request):
    """SALVAR NO BD """
    user = Buscador.busca_user(request)
    if request.method == 'POST': 
        produto_id = request.POST['produto_id']
        pagamento = request.POST['pagamento']
     
        form = EstoqueForms(request.POST)
        if form.is_valid():   
            produto = Produtos.objects.get(id=produto_id)
            check = Estoque.objects.filter(produto_id=produto.id).count()
            qtd = Formata.stringToFloat(request.POST['qtd'])
            custo = Formata.stringToFloat(produto.custo)
            valor = qtd * custo

            store_pagamentos = Pagamentos.objects.create(
                produto = produto,
                qtd_total = qtd,
                valor_total = valor,
                pagamento = pagamento)   
                
            store_pagamentos.save()

            if check == 0:
                store = Estoque.objects.create(
                    produto = produto,
                    qtd_total = qtd,
                    valor_total = valor,
                )   
                store.save()
                messages.success(request,'Estoque salvo com sucesso!')
                return redirect('estoque')  
            else:
                produto = Produtos.objects.get(id=produto.id)
                custo = Formata.stringToFloat(produto.custo)
                put = get_object_or_404(Estoque, produto_id=produto.id)

                qtd_total = (int(qtd) + float(put.qtd_total))
                valor = qtd_total * custo
             
                put.produto = produto
                put.qtd_total = qtd_total
                put.valor_total = valor
                put.save()
                messages.success(request,'Estoque salvo com sucesso!')
                return redirect('estoque')  
        else:
            
            form = EstoqueForms(request.POST)
            table = EstoqueTable(Estoque.objects.all())
         
            if 'sort' in request.GET:
                order = request.GET['sort']
            else:
                order = 'id'
            if 'buscar' in request.GET:
                buscar = request.GET['buscar']
            else:
                buscar = ''
        
            table = EstoqueTable(Estoque.objects.all().distinct().order_by(order).filter(Q(produto__produto__icontains=buscar)))
            table.paginate(page=request.GET.get("page", 1), per_page=8)
            url = Buscador.busca_url_base('/estoque')

            dados = {
                'title': url.nome , 
                'buscar': buscar,
                'cor': url.cor, 
                'titulo': url.nome,
                'table': table,
                'form':form,
                'url_export': 'estoque.export',
                'url_base': 'administrativo',
                'img': url.img,
                'url_action':'estoque.store'
            }

            return render(request, 'estoque/index.html',dados)

def put(request, id):
    """EDITA NO BD"""    
        
    if request.method == 'POST': 
        put = get_object_or_404(Estoque, pk=id)
        qtd_total = request.POST['qtd_total']
        valor_total = request.POST['valor_total']
        pagamento = request.POST['pagamento']
        form = EstoqueEditarForms(request.POST)
         
    if form.is_valid():        
        put.qtd_total = qtd_total
        put.valor_total = valor_total
        put.save()

        messages.success(request,'Estoque editado com sucesso!')
        return redirect('estoque')  
    else:
        url = Buscador.busca_url_base('/estoque')
        dado = get_object_or_404(Estoque, pk=id)
        dados = {
            'title': url.nome + ' - EDITAR',
            'cor': url.cor, 
            'titulo': 'Produto ' + str(dado.produto) ,
            'id': id,
            'form': form,
            'img': url.img,
            'url_base': 'estoque',
            'url_action': 'estoque.put'
        }

        return render(request, 'estoque/editar.html',dados)
            
def delete(request, id):
    """DELETA NO BD"""
    estoque = get_object_or_404(Estoque, pk=id)
    estoque.delete()
    messages.success(request,'Excluído com sucesso!')
    return redirect('estoque')

def export(request): 
    """EXPORTA A TABELA PARA XLS"""
    user = Buscador.busca_user(request)
    output = io.BytesIO()
    workbook = xlsxwriter.Workbook(output)
    worksheet = workbook.add_worksheet()
    data = Estoque.objects.all().values_list('produto', 'produto__produto', 'qtd_total', 'valor_total')
    header_data = ['COD PRODUTO', 'PRODUTO', 'QTD', 'CUSTO']
    header_format = workbook.add_format({'bold': True,'bg_color': '#00627C', 'color' : '#ffffff'})

    for row_num, columns in enumerate(data):
        for col_num, data in enumerate(header_data):
            worksheet.write(0, col_num, data, header_format)
        for col_num, cell_data in enumerate(columns):
            worksheet.write(row_num+1, col_num, cell_data)

    workbook.close()
    output.seek(0)
    filename = 'estoque.xlsx'
    response = HttpResponse(
        output,
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = 'attachment; filename=%s' % filename

    return response