import io
from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect
from django.contrib import messages
from django.db.models import Q
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django_tables2 import RequestConfig
from django.template.response import TemplateResponse
from pacientes.models import AssinaturaVeterinario
from pacientes.forms import VeterinarioForms
from pacientes.tables import VeterinarioTable
from django_tables2.export.export import TableExport
from service.Buscador import *
import xlsxwriter

def listar(request):
    """ CARREGA A TABELA PRINCIPAL COM OS DADOS """

    table = VeterinarioTable(AssinaturaVeterinario.objects.all())
   
    if 'sort' in request.GET:
        order = request.GET['sort']
    else:
        order = 'id'

    if 'buscar' in request.GET:
        buscar = request.GET['buscar']
    else:
        buscar = ''
    
    table = VeterinarioTable(AssinaturaVeterinario.objects.all().distinct().order_by(order).filter( Q(nome__icontains=buscar) | Q(crmv__icontains=buscar) | Q(uf__icontains=buscar)))

    table.paginate(page=request.GET.get("page", 1), per_page=8)
   
    url = Buscador.busca_url_base('/veterinario')
    dados = {
        'title': url.nome , 
        'buscar': buscar,
        'cor': url.cor, 
        'titulo': url.nome,
        'table': table,
        'url_export': 'veterinario.export',
        'url_base': 'administrativo',
        'img': url.img,
        'url_add': 'veterinario.adicionar'
    }

    return render(request, 'veterinario/index.html',dados)

def adicionar(request):
    """ PÁGINA DO ADICIONAR """
    
    form = VeterinarioForms()

    url = Buscador.busca_url_base('/veterinario')
    dados = {
        'title': url.nome + ' - ADICIONAR',
        'cor': url.cor, 
        'titulo': url.nome + ' - ADICIONAR',
        'form': form,
        'img': url.img,
        'url_base': 'veterinario',
        'url_action': 'veterinario.store'
    }
    
    return render(request, 'veterinario/adicionar.html',dados)
   
def editar(request, id):
    """ PÁGINA DO EDITAR """
    dado = get_object_or_404(AssinaturaVeterinario, pk=id)
    instance = get_object_or_404(AssinaturaVeterinario, pk=id)
    form = VeterinarioForms(instance=instance)
    url = Buscador.busca_url_base('/parceiros')
    dados = {
        'title': url.nome + ' - EDITAR',
        'cor': url.cor, 
        'titulo': 'Médico Veterinário ' + str(dado.nome) ,
        'id': id,
        'form': form,
        'img': url.img,
        'url_base': 'administrativo',
        'url_action': 'veterinario.put'
    }

    return render(request, 'veterinario/editar.html',dados)
  
def store(request):
    """SALVAR NO BD """

    if request.method == 'POST': 
        nome = request.POST['nome']
        crmv = request.POST['crmv']
        uf = request.POST['uf']
        form = VeterinarioForms(request.POST)
        
        if form.is_valid():
            check = AssinaturaVeterinario.objects.filter(crmv=crmv).count()
            if check == 0:
                store = AssinaturaVeterinario.objects.create(
                    nome = nome,
                    crmv = crmv,
                    uf = uf
                )   
                store.save()
                messages.success(request,'Veterinario salvo com sucesso!')
                return redirect('veterinario')  
            else:
                messages.error(request,'Médico Veterinário já cadastrado!')
                return redirect('veterinario')  
        else:
           
            url = Buscador.busca_url_base('/veterinario')
            dados = {
                'title': url.nome + ' - ADICIONAR',
                'cor': url.cor, 
                'titulo': url.nome + ' - ADICIONAR',
                'form': form,
                'img': url.img,
                'url_base': 'veterinario',
                'url_action': 'veterinario.store'
            }
            
            return render(request, 'veterinario/adicionar.html',dados)

def put(request, id):
    """EDITA NO BD"""    
        
    if request.method == 'POST': 
        nome = request.POST['nome']
        crmv = request.POST['crmv']
        uf = request.POST['uf']
        put = get_object_or_404(AssinaturaVeterinario, pk=id)

        form = VeterinarioForms(request.POST)

        if form.is_valid():
            put.nome = nome
            put.crmv = crmv
            put.uf = uf
            put.save()
    
            messages.success(request,'Médico Veterinário editado com sucesso!')
            return redirect('veterinario')  
        else:
            url = Buscador.busca_url_base('/veterinario')
            dado = get_object_or_404(AssinaturaVeterinario, pk=id)
            dados = {
                'title': url.nome + ' - EDITAR',
                'cor': url.cor, 
                'titulo': 'Médico Veterinário ' + str(dado.nome) ,
                'id': id,
                'form': form,
                'img': url.img,
                'url_base': 'veterinario',
                'url_action': 'veterinario.put'
            }

            return render(request, 'veterinario/editar.html',dados)
            
def delete(request, id):
    """DELETA NO BD"""
    veterinario = get_object_or_404(AssinaturaVeterinario, pk=id)
    veterinario.delete()
    messages.success(request,'Excluído com sucesso!')
    return redirect('veterinario')

def export(request): 
    """EXPORTA A TABELA PARA XLS"""
    output = io.BytesIO()
    workbook = xlsxwriter.Workbook(output)
    worksheet = workbook.add_worksheet()
    data = AssinaturaVeterinario.objects.all().values_list('nome', 'crmv', 'uf')
    header_data = ['NOME', 'CRMV', 'UF']
    header_format = workbook.add_format({'bold': True,'bg_color': '#00627C', 'color' : '#ffffff'})

    for row_num, columns in enumerate(data):
        for col_num, data in enumerate(header_data):
            worksheet.write(0, col_num, data, header_format)
        for col_num, cell_data in enumerate(columns):
            worksheet.write(row_num+1, col_num, cell_data)

    workbook.close()
    output.seek(0)
    filename = 'MédicosVeterinários.xlsx'
    response = HttpResponse(
        output,
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = 'attachment; filename=%s' % filename

    return response