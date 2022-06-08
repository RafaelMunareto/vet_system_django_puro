import io
import os 
from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect
from django.contrib import messages
from django.db.models import Q
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django_tables2 import RequestConfig
from django.template.response import TemplateResponse
from pacientes.models import AssinaturaVeterinario, Prescricao, Pacientes
from clientes.models import Clientes
from pacientes.forms import PrescricaoForms, FaturaForms, HistoricoForms
from pacientes.tables import HistoricoFaturaTable, HistoricoPrescricaoTable
from django_tables2.export.export import TableExport
from service.Buscador import *
from service.Formata import *
from django.db.models import Subquery
from django.db.models import FloatField, Sum
from django.db.models.functions import Cast
from easy_pdf.views import PDFTemplateView
from datetime import datetime

def listar(request):
    """ CARREGA A TABELA PRINCIPAL COM OS DADOS """
    form = PrescricaoForms()
    url = Buscador.busca_url_base('/prescricao')
    dados = {
        'title': url.nome, 
        'cor': url.cor, 
        'titulo': url.nome,
        'form':form,
        'url_base': 'home',
        'img': url.img,
    }

    return render(request, 'prescricao/index.html',dados)

def store(request):
    """SALVAR NO BD """

    if request.method == 'POST': 
        paciente_id = request.POST['paciente']
        veterinario_id = request.POST['veterinario']
        prescricao = request.POST['prescricao']
        form = PrescricaoForms(request.POST)
          
        if form.is_valid():
            paciente = get_object_or_404(Pacientes, pk=paciente_id)
            tutor = get_object_or_404(Clientes, pk=paciente.tutor.id)
            vet = get_object_or_404(AssinaturaVeterinario, pk=veterinario_id)
            
            store = Prescricao.objects.create(
                paciente = paciente,
                tutor = tutor,
                prescricao = prescricao,
                vet = vet
            )   
            store.save()
            messages.success(request,'Prescrição salva com sucesso!')
            return redirect('prescricao.historico_prescricao', id=paciente_id)  
        else:
            url = Buscador.busca_url_base('/prescricao')
            dados = {
                'title': url.nome + ' ADICIONAR', 
                'cor': url.cor, 
                'titulo': url.nome + ' - ADICIONAR',
                'form': form,
                'img': url.img,
                'url_base': 'prescricao',
                'url_action': 'prescricao'
            }
            
            return render(request, 'prescricao/index.html',dados)
 
def historico_prescricao(request, id):
    """ CARREGA A TABELA DO HISTÓRICO DE PRESRIÇÃO """
    if id == 0:
        table = HistoricoPrescricaoTable(Prescricao.objects.all())
    else:
        table = HistoricoPrescricaoTable(Prescricao.objects.filter(paciente_id=id).all().distinct())
    
    url = Buscador.busca_url_base('/prescricao')

    if id == 0:
        nome = 'HISTÓRICO PRESCRIÇÃO - TODOS'
    else:      
        try:
            dado = get_object_or_404(Prescricao, pk=id)
            nome = 'Prescrição de ' + str(dado.paciente.nome)
        except:
            nome = 'NÃO POSSUI HISTÓRICO'
        
    form = HistoricoForms()
    dados = {
        'title': 'HISTÓRICO PRESCRIÇÃO', 
        'cor': url.cor, 
        'titulo': nome,
        'table':table,
        'form':form,
        'id_paciente':id,
        'url_base': 'prescricao',
        'url_add':'prescricao',
        'img': url.img,
    }

    return render(request, 'prescricao/historico_prescricao.html',dados)

def delete(request, id):
    """DELETA NO BD"""
    historico_prescricao = get_object_or_404(Prescricao, pk=id)
    historico_prescricao.delete()
    messages.success(request,'Excluído com sucesso!')
    return redirect('prescricao.historico_prescricao', id=0)

class HelloPDFView(PDFTemplateView):
    template_name = "prescricao/prescricao_pdf.html"

    def get_context_data(self, **kwargs):
        prescricao = get_object_or_404(Prescricao, pk=self.kwargs.get('id'))
        prescricoes = Prescricao.objects.filter(id=prescricao.id)

        return super(HelloPDFView, self).get_context_data( pagesize="A4",prescricao=prescricao, prescricoes=prescricoes,**kwargs)
