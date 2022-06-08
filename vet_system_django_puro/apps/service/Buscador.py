import io 
from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect
from home.models import Urls
from clientes.models import Clientes
from django.contrib import auth, messages
from pacientes.models import Pacientes, FaturaProduto, AssinaturaVeterinario
from administrativo.models import Fornecedores, Produtos, Servicos, Pagamentos
from datetime import date
from service.Formata import *
from datetime import timedelta
from django.contrib.auth.models import User

class Buscador:
    
    def busca_user(request):
        try:
            id = request.user.id
            return get_object_or_404(User, pk=id)
        except:
            pass
        
    def busca_url_request(request):
        """Busca as Páginas de acordo com o acesso"""
        return Urls.objects.filter(urls=request.META['PATH_INFO']).first()
    
    def busca_url_base(dado):
        """Busca as Páginas de acordo com o acesso"""
        return Urls.objects.filter(urls=dado).first()
    
    def busca_tutores():
        """Busca todos os tutores"""
        return Clientes.objects.values('id', 'nome')

    def busca_data_pagamentos():
        """Busca as datas dos pagamentos"""
        return Pagamentos.objects.values('pagamento').order_by('pagamento')
    
    def busca_fornecedor_pagamentos():
        """Busca os fornecedores dos pagamentos"""
        return Pagamentos.objects.values('produto__fornecedor__id', 'produto__fornecedor__nome').distinct()

    def busca_fornecedores():
        """Busca todos os fornecedores"""
        return Fornecedores.objects.values('id', 'nome')
    
    def busca_produtos():
        """Busca todos os produtos"""
        return Produtos.objects.all()
    
    def busca_produtos_values():
        """Busca todos os produtos values"""
        return Produtos.objects.values('id', 'produto')
    
    def busca_servicos():
        """Busca todos os servicos"""
        return Servicos.objects.values('id', 'servico')
    
    def busca_pacientes():
        """Busca todos os pacientes"""
        return Pacientes.objects.values('id', 'nome')
    
    def busca_pacientes_all():
        """Busca todos os pacientes all"""
        return Pacientes.objects.all()
        
    def busca_faturas_all():
        """Busca todos os faturas all"""
        return FaturaProduto.objects.all()
    
    def busca_dia():
        """Busca data do dia"""
        data_atual = date.today()
        dia = data_atual.strftime('%Y-%m-%d')
        return str(dia)

    def busca_dia_aniversario():
        """Busca dia aniversário"""
        data_atual = date.today()
        dia = data_atual.strftime('%d-%m')
        return str(dia)

    def busca_dia_recorrente():
        """Busca data do dia com 99-9999"""
        data_atual = date.today()
        dia = data_atual.strftime('9999-99-%d')
        return str(dia)
    
    def busca_mes():
        """Busca data do mes"""
        data_atual = date.today()
        mes = data_atual.strftime('%Y-%m')
        return str(mes)
      
    def busca_semana():
        """Busca data do ano"""
        dia1 = date.today() + timedelta(days=0)
        dia1_f = dia1.strftime('%Y-%m-%d')
        dia1_r = dia1.strftime('9999-99-%d')
        dia2 = date.today() + timedelta(days=1)
        dia2_f = dia2.strftime('%Y-%m-%d')
        dia2_r = dia1.strftime('9999-99-%d')
        dia3 = date.today() + timedelta(days=2)
        dia3_f = dia3.strftime('%Y-%m-%d')
        dia3_r = dia1.strftime('9999-99-%d')
    
        return [dia1_f, dia1_r, dia2_f, dia2_r ,dia3_f, dia3_r]
    
    def busca_veterinario():
        """Busca veterinario"""
        return AssinaturaVeterinario.objects.values('id', 'crmv', 'nome')

    def busca_data_nascimento_pacientes():
        """ Busca da data de nascimento do Paciente"""
        return Pacientes.objects.order_by().values('data_nascimento').distinct('data_nascimento')
    
    def busca_data_nascimento_clientes():
        """ Busca da data de nascimento do Cliente"""
        return Clientes.objects.order_by().values('data_nascimento').distinct('data_nascimento')