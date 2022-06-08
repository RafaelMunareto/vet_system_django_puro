from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect
from service.Buscador import *
from home.models import Urls
from django.db.models import Q
from administrativo.models import Pagamentos, CustosFixos
from django.db.models import FloatField, Sum
from django.db.models.functions import Cast
from service.Buscador import *
from service.Formata import *
from administrativo.models import Estoque

def listar(request):
    """ CARREGA A TABELA PRINCIPAL COM OS DADOS """
    user = Buscador.busca_user(request)
    url = Buscador.busca_url_request(request)
    urls_cards = Urls.objects.filter(grupo='administrativo').order_by('id')
    
    data = Buscador.busca_dia() 
    fornecedor = Pagamentos.objects.filter(pagamento__contains=data).filter(user=user).distinct().order_by('valor_total')
    total_valor2 = Pagamentos.objects.filter(pagamento__contains=data).filter(user=user).annotate(as_valor_total=Cast('valor_total', FloatField())).aggregate(Sum('as_valor_total'))

    data_recorrente = Buscador.busca_dia_recorrente()
    custos_fixos = CustosFixos.objects.filter(user=user).filter(Q(pagamento__contains=data) | Q(pagamento__contains=data_recorrente)).distinct().order_by('custo')
    total_valor = CustosFixos.objects.filter(user=user).filter(Q(pagamento__contains=data) | Q(pagamento__contains=data_recorrente)).annotate(as_custo=Cast('custo', FloatField())).aggregate(Sum('as_custo'))
   
    if total_valor['as_custo__sum'] != None:
        total_custos_fixos = total_valor['as_custo__sum'] 
    else:
        total_custos_fixos = 0

    if total_valor2['as_valor_total__sum'] != None:
        total_fornecedor = total_valor2['as_valor_total__sum']
    else:
        total_fornecedor = 0

    total_0 = total_fornecedor + total_custos_fixos 
    menor_estoque = Estoque.objects.filter(user=user).order_by('-qtd_total')[:5]  
    total = Formata.dinheiro(total_0)

    dados = {
        'title': url.nome, 
        'cor':url.cor,
        'titulo': url.nome,
        'img':url.img,
        'total':total,
        'total_custos_fixos':total_custos_fixos,
        'total_fornecedor':total_fornecedor,
        'custos_fixos':custos_fixos,
        'fornecedor': fornecedor,
        'menor_estoque':menor_estoque,
        'icone':url.icone,
        'url_base':url.rota,
        'urls_cards':urls_cards
    }

    return render(request, 'administrativo/index.html',dados)
