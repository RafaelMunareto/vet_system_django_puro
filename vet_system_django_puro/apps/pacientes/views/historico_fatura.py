import io
import os 
from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect
from django.contrib import messages
from django.db.models import Q
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django_tables2 import RequestConfig
from django.template.response import TemplateResponse
from pacientes.models import HistoricoFatura, FaturaProduto, Pacientes
from pacientes.forms import FaturaForms
from pacientes.tables import HistoricoFaturaTable
from django_tables2.export.export import TableExport
from service.Buscador import *
from service.Formata import *
from django.db.models import Subquery
from django.db.models import FloatField, Sum
from django.db.models.functions import Cast
from easy_pdf.views import PDFTemplateView
from datetime import datetime

def listar(request,id):
    """ CARREGA A TABELA PRINCIPAL COM OS DADOS """
    form = FaturaForms()
    table = HistoricoFaturaTable(HistoricoFatura.objects.all())
    
    if 'sort' in request.GET:
        order = request.GET['sort']
    else:
        order = 'id'

    if 'buscar' in request.GET:
        buscar = request.GET['buscar']
    else:
        buscar = ''
    
    if id != 0:
        table = HistoricoFaturaTable(HistoricoFatura.objects.all().distinct().order_by(order).filter(paciente_id=id).filter( Q(paciente__nome__icontains=buscar) | Q(tutor__nome__icontains=buscar) ))
        dado = get_object_or_404(Pacientes, pk=id)
        tutor = ' de ' + str(dado.tutor)
    else:
        table = HistoricoFaturaTable(HistoricoFatura.objects.all().distinct().order_by(order).filter( Q(paciente__nome__icontains=buscar) | Q(tutor__nome__icontains=buscar) ))
        tutor = ''
        
    table.paginate(page=request.GET.get("page", 1), per_page=8)
    url = Buscador.busca_url_base('/historico_fatura/0')
    dados = {
        'title': url.nome, 
        'buscar': buscar,
        'cor': url.cor, 
        'titulo': str(url.nome) + str(tutor),
        'table': table,
        'form':form,
        'id':id,
        'url_export': 'historico_fatura.export',
        'url_base': 'fatura',
        'img': url.img,
    }

    return render(request, 'fatura/historico_faturas/index.html',dados)

def store(request):
    """SALVAR NO BD """

    if request.method == 'POST': 
        cliente_id = request.POST['cliente_id']
        data_cadastro = request.POST['data_cadastro']
        total = Formata.stringToFloat(request.POST['total'])
        key = HistoricoFatura.objects.count()
        fatura_produto = FaturaProduto.objects.filter(paciente__id=cliente_id).filter(key=key).filter(data_cadastro=data_cadastro).distinct()
        for linha in fatura_produto:
            paciente = linha.paciente
            tutor = linha.tutor
            data_cadastro = linha.data_cadastro
                
        store = HistoricoFatura.objects.create(
            paciente = paciente,
            tutor = tutor,
            total = total, 
            key = key,
            data_cadastro = data_cadastro)   

        store.save()  
        
        for linha in fatura_produto:
            linha.faturado = 1
            linha.save() 
      
        messages.success(request,'Fatura salvo com sucesso!')
        return redirect('historico_fatura', id=cliente_id)  
       
def delete(request, id):
    """DELETA NO BD"""
    historico_fatura = get_object_or_404(HistoricoFatura, pk=id)
    historico_fatura.delete()
    messages.success(request,'Excluído com sucesso!')
    return redirect('historico_fatura', id=0)

class HelloPDFView(PDFTemplateView):
    template_name = "fatura/historico_faturas/fatura_pdf.html"

    def get_context_data(self, **kwargs):
        fatura = get_object_or_404(HistoricoFatura, pk=self.kwargs.get('id'))
        faturas = FaturaProduto.objects.filter(key=fatura.key)

        return super(HelloPDFView, self).get_context_data( pagesize="A4",fatura=fatura, faturas=faturas,**kwargs)
