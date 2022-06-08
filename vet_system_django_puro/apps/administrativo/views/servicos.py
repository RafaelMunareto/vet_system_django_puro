import io
from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect
from django.contrib import messages
from django.db.models import Q
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django_tables2 import RequestConfig
from django.template.response import TemplateResponse
from administrativo.models import Servicos, Fornecedores
from administrativo.forms import ServicosForms
from administrativo.tables import ServicosTable
from django_tables2.export.export import TableExport
from service.Buscador import *
import xlsxwriter

def listar(request):
    """ CARREGA A TABELA PRINCIPAL COM OS DADOS """
    user = Buscador.busca_user(request)
    table = ServicosTable(Servicos.objects.all())
   
    if 'sort' in request.GET:
        order = request.GET['sort']
    else:
        order = 'id'

    if 'buscar' in request.GET:
        buscar = request.GET['buscar']
    else:
        buscar = ''
    
    table = ServicosTable(Servicos.objects.all().distinct().order_by(order).filter(Q(servico__icontains=buscar) | Q(descricao__icontains=buscar) ))

    table.paginate(page=request.GET.get("page", 1), per_page=8)
   
    url = Buscador.busca_url_base('/servicos')
    dados = {
        'title': url.nome , 
        'buscar': buscar,
        'cor': url.cor, 
        'titulo': url.nome,
        'table': table,
        'url_export': 'servicos.export',
        'url_base': 'administrativo',
        'img': url.img,
        'url_add': 'servicos.adicionar'
    }

    return render(request, 'servicos/index.html',dados)

def adicionar(request):
    """ PÁGINA DO ADICIONAR """
    
    form = ServicosForms()
    url = Buscador.busca_url_base('/servicos')
    dados = {
        'title': url.nome + ' ADICIONAR', 
        'cor': url.cor, 
        'titulo':'SERVIÇOS ADICIONAR',
        'form': form,
        'img': url.img,
        'url_base': 'servicos',
        'url_action': 'servicos.store'
    }
    
    return render(request, 'servicos/adicionar.html',dados)

def editar(request, id):
    """ PÁGINA DO EDITAR """
    dado = get_object_or_404(Servicos, pk=id)
    instance = get_object_or_404(Servicos, pk=id)
    form = ServicosForms(instance=instance)
    url = Buscador.busca_url_base('/servicos')
    dados = {
        'title': url.nome + ' - EDITAR',
        'cor': url.cor, 
        'titulo': 'Produto ' + str(dado.servico) ,
        'id': id,
        'form': form,
        'img': url.img,
        'url_base': 'servicos',
        'url_action': 'servicos.put'
    }

    return render(request, 'servicos/editar.html',dados)
  
def store(request):
    """SALVAR NO BD """
    user = Buscador.busca_user(request)
    
    if request.method == 'POST': 
        servico = request.POST['servico']
        descricao = request.POST['descricao']
        venda = request.POST['venda']
        form = ServicosForms(request.POST)
        
        if form.is_valid():
            store = Servicos.objects.create(
                servico = servico,
                descricao = descricao,
                venda = venda
            )   
            store.save()
            messages.success(request,'Serviço salvo com sucesso!')
            return redirect('servicos')  
        else:
            url = Buscador.busca_url_base('/servicos')
            dados = {
                'title': url.nome + ' ADICIONAR', 
                'cor': url.cor, 
                'titulo': url.nome + ' - ADICIONAR',
                'form': form,
                'img': url.img,
                'url_base': 'servicos',
                'url_action': 'servicos.store'
            }
            
            return render(request, 'servicos/adicionar.html',dados)

def put(request, id):
    """EDITA NO BD"""    
        
    if request.method == 'POST': 
        servico = request.POST['servico']
        descricao = request.POST['descricao']
        venda = request.POST['venda']
        put = get_object_or_404(Servicos, pk=id)
        form = ServicosForms(request.POST)         
        
    if form.is_valid():
        put.servico = servico
        put.descricao = descricao
        put.venda = venda
        put.save()

        messages.success(request,'Serviço editado com sucesso!')
        return redirect('servicos')  
    else:
        url = Buscador.busca_url_base('/servicos')
        dado = get_object_or_404(Servicos, pk=id)
        dados = {
            'title': url.nome + ' - EDITAR',
            'cor': url.cor, 
            'titulo': 'Serviço ' + str(dado.produto) ,
            'id': id,
            'form': form,
            'img': url.img,
            'url_base': 'servicos',
            'url_action': 'servicos.put'
        }

        return render(request, 'servicos/editar.html',dados)
            
def delete(request, id):
    """DELETA NO BD"""
    servicos = get_object_or_404(Servicos, pk=id)
    servicos.delete()
    messages.success(request,'Excluído com sucesso!')
    return redirect('servicos')

def export(request): 
    """EXPORTA A TABELA PARA XLS"""
    user = Buscador.busca_user(request)
    output = io.BytesIO()
    workbook = xlsxwriter.Workbook(output)
    worksheet = workbook.add_worksheet()
    data = Servicos.objects.all().values_list('servico', 'descricao','venda')
    header_data = ['SERVIÇO', 'DESCRIÇÃO', 'VENDA']
    header_format = workbook.add_format({'bold': True,'bg_color': '#00627C', 'color' : '#ffffff'})

    for row_num, columns in enumerate(data):
        for col_num, data in enumerate(header_data):
            worksheet.write(0, col_num, data, header_format)
        for col_num, cell_data in enumerate(columns):
            worksheet.write(row_num+1, col_num, cell_data)

    workbook.close()
    output.seek(0)
    filename = 'Servicos.xlsx'
    response = HttpResponse(
        output,
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = 'attachment; filename=%s' % filename

    return response