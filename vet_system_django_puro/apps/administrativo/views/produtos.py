import io
from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect
from django.contrib import messages
from django.db.models import Q
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django_tables2 import RequestConfig
from django.template.response import TemplateResponse
from administrativo.models import Produtos, Fornecedores
from administrativo.forms import ProdutosForms, ProdutosEditarForms
from administrativo.tables import ProdutosTable, ProdutosAssociadosTable
from django_tables2.export.export import TableExport
from service.Buscador import *
import xlsxwriter

def listar(request):
    """ CARREGA A TABELA PRINCIPAL COM OS DADOS """
    user = Buscador.busca_user(request)
    table = ProdutosTable(Produtos.objects.all())
   
    if 'sort' in request.GET:
        order = request.GET['sort']
    else:
        order = 'id'

    if 'buscar' in request.GET:
        buscar = request.GET['buscar']
    else:
        buscar = ''
    
    table = ProdutosTable(Produtos.objects.all().distinct().order_by(order).filter( Q(fornecedor__nome__icontains=buscar) \
                        | Q(produto__icontains=buscar) | Q(descricao__icontains=buscar) ))

    table.paginate(page=request.GET.get("page", 1), per_page=8)
   
    url = Buscador.busca_url_base('/produtos')
    dados = {
        'title': url.nome , 
        'buscar': buscar,
        'cor': url.cor, 
        'titulo': url.nome,
        'table': table,
        'url_export': 'produtos.export',
        'url_base': 'administrativo',
        'img': url.img,
        'url_add': 'produtos.adicionar_novo'
    }

    return render(request, 'produtos/index.html',dados)

def detalhes(request, id):
    """ CARREGA A TABELA COMPLETA PELO ID """
    user = Buscador.busca_user(request)
    dado = get_object_or_404(Produtos, pk=id)
    table = ProdutosTable(Produtos.objects.filter(id=id).all().distinct())
    url = Buscador.busca_url_base('/produtos')
    dados = {
        'title': url.nome, 
        'cor': url.cor, 
        'titulo': 'Cadastro de ' + str(dado.produto) ,
        'table': table,
        'url_export': 'produtos.export',
        'url_base': 'produtos',
        'img': url.img
    }

    return render(request, 'produtos/detalhes.html',dados)

def adicionar(request, id):
    """ PÁGINA DO ADICIONAR """
    
    form = ProdutosForms(request)
    dado = get_object_or_404(Fornecedores, pk=id)
    url = Buscador.busca_url_base('/produtos')
    dados = {
        'title': url.nome + ' ADICIONAR', 
        'cor': url.cor, 
        'titulo':'Produto de ' +  str(dado.nome),
        'form': form,
        'img': url.img,
        'id':id,
        'url_base': 'produtos.associados',
        'url_action': 'produtos.store'
    }
    
    return render(request, 'produtos/adicionar.html',dados)

def adicionar_novo(request):
    """ PÁGINA DO ADICIONAR NOVO """
    
    form = ProdutosForms(request)
    url = Buscador.busca_url_base('/produtos')
    dados = {
        'title': url.nome + ' ADICIONAR', 
        'cor': url.cor, 
        'titulo':url.nome + ' - ADICIONAR',
        'form': form,
        'img': url.img,
        'url_base': 'produtos',
        'url_action': 'produtos.store'
    }
    
    return render(request, 'produtos/adicionar_novo.html',dados)

def associados(request, id):
    user = Buscador.busca_user(request)
    try: 
        dado = get_object_or_404(Fornecedores, pk=id)
        nome =  'Produtos de ' + dado.nome
    except:
        nome = 'Não possui produtos associados'
    
    table = ProdutosAssociadosTable(Produtos.objects.filter(fornecedor=id).all().distinct())
    url = Buscador.busca_url_base('/produtos')
    dados = {
        'title': url.nome, 
        'cor': url.cor, 
        'titulo':  str(nome),
        'table': table,
        'url_export': 'produtos.export',
        'url_base': 'fornecedores',
        'url_add': 'produtos.adicionar',
        'img': url.img,
        'id':id
    }

    return render(request, 'produtos/produtos_associados.html',dados)

def editar(request, id):
    """ PÁGINA DO EDITAR """
    user = Buscador.busca_user(request)
    dado = get_object_or_404(Produtos, pk=id)
    instance = get_object_or_404(Produtos, pk=id)
    form = ProdutosForms(request, instance=instance)
    url = Buscador.busca_url_base('/produtos')
    dados = {
        'title': url.nome + ' - EDITAR',
        'cor': url.cor, 
        'titulo': 'Produto ' + str(dado.fornecedor) ,
        'id': id,
        'form': form,
        'img': url.img,
        'url_base': 'produtos',
        'url_action': 'produtos.put'
    }

    return render(request, 'produtos/editar.html',dados)
  
def store(request):
    """SALVAR NO BD """
    user = Buscador.busca_user(request)
    if request.method == 'POST': 
        fornecedor_id = request.POST['fornecedor_id']
        produto = request.POST['produto']
        descricao = request.POST['descricao']
        un_medida = request.POST['un_medida']
        custo = request.POST['custo']
        venda = request.POST['venda']
        form = ProdutosForms(request.POST)
        
        if form.is_valid():
            fornecedor = Fornecedores.objects.get(id=fornecedor_id)
            store = Produtos.objects.create(
                fornecedor = fornecedor,
                produto = produto,
                descricao = descricao,
                un_medida = un_medida,
                custo = custo,
                venda = venda,
            )   
            store.save()
            messages.success(request,'Produto salvo com sucesso!')
            return redirect('produtos')  
        else:
            fornecedor_id = request.POST['fornecedor_id']
            url = Buscador.busca_url_base('/produtos')
            dados = {
                'title': url.nome + ' ADICIONAR', 
                'cor': url.cor, 
                'titulo': url.nome + ' - ADICIONAR',
                'form': form,
                'img': url.img,
                'id':fornecedor_id,
                'url_base': 'produtos',
                'url_action': 'produtos.store'
            }
            
            return render(request, 'produtos/adicionar_novo.html',dados)

def put(request, id):
    """EDITA NO BD"""    
    user = Buscador.busca_user(request)
    if request.method == 'POST': 
        fornecedor_id = request.POST['fornecedor_id']
        produto = request.POST['produto']
        descricao = request.POST['descricao']
        un_medida = request.POST['un_medida']
        custo = request.POST['custo']
        venda = request.POST['venda']
        put = get_object_or_404(Produtos, pk=id)
        form = ProdutosEditarForms(request.POST)
    
        id_fornecedor = Produtos.objects.get(id=fornecedor_id)
        fornecedor = Fornecedores.objects.get(pk=id_fornecedor.fornecedor.id)
         
    if form.is_valid():
   
        put.fornecedor = fornecedor
        put.produto = produto
        put.descricao = descricao
        put.un_medida = un_medida
        put.custo = custo
        put.venda = venda
        put.save()

        messages.success(request,'Produto editado com sucesso!')
        return redirect('produtos')  
    else:
        url = Buscador.busca_url_base('/produtos')
        dado = get_object_or_404(Produtos, pk=id)
        dados = {
            'title': url.nome + ' - EDITAR',
            'cor': url.cor, 
            'titulo': 'Produto ' + str(dado.produto) ,
            'id': id,
            'form': form,
            'img': url.img,
            'url_base': 'produtos',
            'url_action': 'produtos.put'
        }

        return render(request, 'produtos/editar.html',dados)
            
def delete(request, id):
    """DELETA NO BD"""
    produtos = get_object_or_404(Produtos, pk=id)
    produtos.delete()
    messages.success(request,'Excluído com sucesso!')
    return redirect('produtos')

def export(request): 
    """EXPORTA A TABELA PARA XLS"""
    user = Buscador.busca_user(request)
    output = io.BytesIO()
    workbook = xlsxwriter.Workbook(output)
    worksheet = workbook.add_worksheet()
    data = Produtos.objects.all().values_list('fornecedor', 'produto', 'descricao', 'un_medida','qtd', 'custo', 'venda', 'pagamento')
    header_data = ['FORNECEDOR', 'PRODUTO', 'DESCRIÇÃO', 'UN. MEDIDA', 'QTD', 'CUSTO', 'VENDA', 'PAGAMENTO']
    header_format = workbook.add_format({'bold': True,'bg_color': '#00627C', 'color' : '#ffffff'})

    for row_num, columns in enumerate(data):
        for col_num, data in enumerate(header_data):
            worksheet.write(0, col_num, data, header_format)
        for col_num, cell_data in enumerate(columns):
            worksheet.write(row_num+1, col_num, cell_data)

    workbook.close()
    output.seek(0)
    filename = 'produtos.xlsx'
    response = HttpResponse(
        output,
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = 'attachment; filename=%s' % filename

    return response