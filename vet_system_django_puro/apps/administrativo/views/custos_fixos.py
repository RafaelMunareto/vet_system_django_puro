import io
from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect
from django.contrib import messages
from django.db.models import Q
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django_tables2 import RequestConfig
from django.template.response import TemplateResponse
from administrativo.models import CustosFixos, Pagamentos
from administrativo.forms import CustosFixosForms
from administrativo.tables import CustosFixosTable
from django_tables2.export.export import TableExport
from service.Buscador import *
from service.Formata import *
import xlsxwriter

def listar(request):
    """ CARREGA A TABELA PRINCIPAL COM OS DADOS """
    user = Buscador.busca_user(request)
    table = CustosFixosTable(CustosFixos.objects.filter(user=user))    
   
    if 'sort' in request.GET:
        order = request.GET['sort']
    else:
        order = 'id'

    if 'buscar' in request.GET:
        buscar = request.GET['buscar']
    else:
        buscar = ''
    
    table = CustosFixosTable(CustosFixos.objects.filter(user=user).distinct().order_by(order).filter(Q(nome__icontains=buscar) | Q(descricao__icontains=buscar) ))

    table.paginate(page=request.GET.get("page", 1), per_page=8)
   
    url = Buscador.busca_url_base('/custos_fixos')
    dados = {
        'title': url.nome , 
        'buscar': buscar,
        'cor': url.cor, 
        'titulo': url.nome,
        'table': table,
        'url_export': 'custos_fixos.export',
        'url_base': 'administrativo',
        'img': url.img,
        'url_add': 'custos_fixos.adicionar'
    }

    return render(request, 'custos_fixos/index.html',dados)

def adicionar(request):
    """ PÁGINA DO ADICIONAR """
    
    form = CustosFixosForms()
    url = Buscador.busca_url_base('/custos_fixos')
    dados = {
        'title': url.nome + ' ADICIONAR', 
        'cor': url.cor, 
        'titulo':'Custo FixoS ADICIONAR',
        'form': form,
        'img': url.img, 
        'url_base': 'custos_fixos',
        'url_action': 'custos_fixos.store'
    }
    
    return render(request, 'custos_fixos/adicionar.html',dados)

def editar(request, id):
    """ PÁGINA DO EDITAR """
    user = Buscador.busca_user(request)
    dado = get_object_or_404(CustosFixos, user=user, pk=id)
    instance = get_object_or_404(CustosFixos, user=user, pk=id)
    form = CustosFixosForms(instance=instance)
    url = Buscador.busca_url_base('/custos_fixos')
    dados = {
        'title': url.nome + ' - EDITAR',
        'cor': url.cor, 
        'titulo': 'Custo Fixo ' + str(dado.nome) ,
        'id': id,
        'form': form,
        'img': url.img,
        'url_base': 'custos_fixos',
        'url_action': 'custos_fixos.put'
    }

    return render(request, 'custos_fixos/editar.html',dados)
  
def store(request):
    """SALVAR NO BD """
    user = Buscador.busca_user(request)
    if request.method == 'POST': 
        nome = request.POST['nome']
        custo = request.POST['custo']
        recorrente = request.POST.get('recorrente', False)
        pagamento = request.POST['pagamento']
        descricao = request.POST['descricao']
        form = CustosFixosForms(request.POST)

      
        if form.is_valid():
            
            if recorrente == 'on':
                recorrente = True
                pagamento = '9999-99-' + pagamento[8:10][:2]
            else:
                recorrente = False

            store = CustosFixos.objects.create(
                user = user,
                nome = nome,
                custo = Formata.stringToFloat(custo),
                pagamento = pagamento,
                descricao = descricao,
                recorrente = recorrente
            )   
            store.save()
            
            messages.success(request,'Custo Fixo salvo com sucesso!')
            return redirect('custos_fixos')  
        else:
            url = Buscador.busca_url_base('/custos_fixos')
            dados = {
                'title': url.nome + ' ADICIONAR', 
                'cor': url.cor, 
                'titulo': url.nome + ' - ADICIONAR',
                'form': form,
                'img': url.img,
                'url_base': 'custos_fixos',
                'url_action': 'custos_fixos.store'
            }
            
            return render(request, 'custos_fixos/adicionar.html',dados)

def put(request, id):
    """EDITA NO BD"""    
    user = Buscador.busca_user(request)
    
    if request.method == 'POST': 
        nome = request.POST['nome']
        custo = request.POST['custo']
        pagamento = request.POST['pagamento']
        recorrente = request.POST['recorrente']
        descricao = request.POST['descricao']
        put = get_object_or_404(CustosFixos, user=user, pk=id)
        form = CustosFixosForms(request.POST)         
        
    if form.is_valid():

        if recorrente == 'on':
            recorrente = True
            pagamento = '9999-99-' + pagamento[8:10][:2]
        else:
            recorrente = False

        put.nome = nome
        put.custo = Formata.stringToFloat(custo)
        put.pagamento = pagamento
        put.recorrente = recorrente
        put.descricao = descricao
        put.save()

        messages.success(request,'Custo Fixo editado com sucesso!')
        return redirect('custos_fixos')  
    else:
        url = Buscador.busca_url_base('/custos_fixos')
        dado = get_object_or_404(CustosFixos, user=user, pk=id)
        dados = {
            'title': url.nome + ' - EDITAR',
            'cor': url.cor, 
            'titulo': 'Custo Fixo ' + str(dado.nome) ,
            'id': id,
            'form': form,
            'img': url.img,
            'url_base': 'custos_fixos',
            'url_action': 'custos_fixos.put'
        }

        return render(request, 'custos_fixos/editar.html',dados)
            
def delete(request, id):
    """DELETA NO BD"""
    user = Buscador.busca_user(request)
    custo_fixo = get_object_or_404(CustosFixos, user=user, pk=id)
    custo_fixo.delete()
    messages.success(request,'Excluído com sucesso!')
    return redirect('custos_fixos')

def export(request): 
    """EXPORTA A TABELA PARA XLS"""
    user = Buscador.busca_user(request)
    output = io.BytesIO()
    workbook = xlsxwriter.Workbook(output)
    worksheet = workbook.add_worksheet()
    data = CustosFixos.objects.filter(user=user).all().values_list('nome', 'custo','pagamento', 'descricao')
    header_data = ['NOME', 'CUSTO', 'DATA PAGAMENTO', 'DESCRIÇÃO']
    header_format = workbook.add_format({'bold': True,'bg_color': '#00627C', 'color' : '#ffffff'})

    for row_num, columns in enumerate(data):
        for col_num, data in enumerate(header_data):
            worksheet.write(0, col_num, data, header_format)
        for col_num, cell_data in enumerate(columns):
            worksheet.write(row_num+1, col_num, cell_data)

    workbook.close()
    output.seek(0)
    filename = 'custos_fixos.xlsx'
    response = HttpResponse(
        output,
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = 'attachment; filename=%s' % filename

    return response