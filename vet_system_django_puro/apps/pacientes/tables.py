import django_tables2 as tables
from django_tables2 import TemplateColumn
from .models import Pacientes, FaturaProduto, HistoricoFatura, AssinaturaVeterinario, Prescricao
from service.Formata import *

class PacientesTable(tables.Table):
    
    CENTER = { 'th': { 'class': 'center '}, 'td': {'class': 'center'}}
    LEFT = { 'th':{'class': 'text-left'}, 'td': {'class': 'text-left'}}
    LEFT_BOLD = { 'th':{'class': 'text-left bold'}, 'td': {'class': 'text-left bold'}}
    
    id = tables.Column(attrs=CENTER, verbose_name='COD')
    nome = tables.Column(attrs=LEFT_BOLD, verbose_name='PACIENTE')  
    tutor = tables.TemplateColumn('<a href="{% url \'clientes.detalhes\' record.tutor.id  %}">{{ record.tutor }}</a>', 
                                    orderable=False,
                                    attrs=LEFT,
                                    verbose_name= 'TUTOR')
    raca = tables.Column(attrs=LEFT, verbose_name= 'RAÇA')
    especie = tables.Column(attrs=LEFT, verbose_name= 'ESPÉCIE')
    sexo = tables.Column(attrs=LEFT, verbose_name= 'SEXO')
    idade = tables.Column(attrs=LEFT, verbose_name= 'IDADE')
    peso = tables.Column(attrs=CENTER, verbose_name= 'PESO')
    data_nascimento = tables.Column(attrs=CENTER, verbose_name= 'DATA NASCIMENTO')
    
    AGENDAR = tables.TemplateColumn('<a href="{% url \'agendamentos.adicionar_novo\' record.id  %}"><i class=\'fas fa-calendar-alt fa-2x teal-text\'></i></a>', 
                                    orderable=False,
                                    attrs=CENTER,
                                    verbose_name= '')

    FATURA = tables.TemplateColumn('<a href="{% url \'fatura.detalhes\' record.id  %}"><i class=\'fas fa-receipt fa-2x teal-text\'></i></a>', 
                                    orderable=False,
                                    attrs=CENTER,
                                    verbose_name= '')
     
    EDITAR = tables.TemplateColumn('<a href="{% url \'pacientes.editar\' record.id  %}"><i class=\'fas fa-user-edit fa-2x orange-text\'></i></a>', 
                                    orderable=False,
                                    attrs=CENTER,
                                    verbose_name= '')
    
    DELETAR = tables.TemplateColumn('<a onclick="return confirm(\'Tem certeza que deseja deletar?\')" href="{% url \'pacientes.delete\' record.id  %}" ><i class=\'fas fa-trash fa-2x  red-text\'></i></a>', 
                                     orderable=False,
                                     attrs=CENTER,
                                     verbose_name= '')
    
    class Meta:
        attrs = {"class": "striped center uppercase table_top mt-1 size95 size95"}
        model = Pacientes
        fields = ['id','nome', 'tutor', 'raca', 'especie', 'sexo', 'idade', 'peso', 'data_nascimento']
        actions = tables.Column(orderable=True)

class PacientesAssociadosTable(tables.Table):
    
    CENTER = { 'th': { 'class': 'center '}, 'td': {'class': 'center'}}
    LEFT = { 'th':{'class': 'text-left'}, 'td': {'class': 'text-left'}}
    LEFT_BOLD = { 'th':{'class': 'text-left bold'}, 'td': {'class': 'text-left bold'}}
    
    id = tables.Column(attrs=CENTER, verbose_name='COD')
    nome = tables.Column(attrs=LEFT_BOLD, verbose_name='PACIENTE')  
    raca = tables.Column(attrs=LEFT, verbose_name= 'RAÇA')
    especie = tables.Column(attrs=LEFT, verbose_name= 'ESPÉCIE')
    sexo = tables.Column(attrs=LEFT, verbose_name= 'SEXO')
    idade = tables.Column(attrs=LEFT, verbose_name= 'IDADE')
    peso = tables.Column(attrs=CENTER, verbose_name= 'PESO')
    data_nascimento = tables.Column(attrs=CENTER, verbose_name= 'DATA NASCIMENTO')
    
    AGENDAR = tables.TemplateColumn('<a href="{% url \'agendamentos.adicionar_novo\' record.id  %}"><i class=\'fas fa-calendar-alt fa-2x teal-text\'></i></a>', 
                                    orderable=False,
                                    attrs=CENTER,
                                    verbose_name= '')

    EDITAR = tables.TemplateColumn('<a href="{% url \'pacientes.editar\' record.id  %}"><i class=\'fas fa-user-edit fa-2x orange-text\'></i></a>', 
                                    orderable=False,
                                    attrs=CENTER,
                                    verbose_name= '')
    
    DELETAR = tables.TemplateColumn('<a onclick="return confirm(\'Tem certeza que deseja deletar?\')" href="{% url \'pacientes.delete\' record.id  %}" ><i class=\'fas fa-trash fa-2x  red-text\'></i></a>', 
                                     orderable=False,
                                     attrs=CENTER,
                                     verbose_name= '')
    
    class Meta:
        attrs = {"class": "striped center uppercase table_top mt-1 size95 size95"}
        model = Pacientes
        fields = ['id','nome', 'raca', 'especie', 'sexo', 'idade', 'peso', 'data_nascimento']
        actions = tables.Column(orderable=True)

class FaturaProdutoTable(tables.Table):
            
    CENTER = { 'th': { 'class': 'center teal-text darken-2'}, 'td': {'class': 'center'}}
    LEFT = { 'th':{'class': 'text-left teal-text darken-2'}, 'td': {'class': 'text-left'}}
    LEFT_DATA = { 'th':{'class': 'text-left teal-text darken-2'}, 'td': {'class': 'text-left', 'id':'data_cadastro'}}
    LEFT_BOLD = { 'th':{'class': 'text-left bold teal-text darken-2'}, 'td': {'class': 'text-left bold'}}
    
    cod = tables.TemplateColumn('{{ record.cod }}', 
                                    orderable=False,
                                    attrs=CENTER,
                                    verbose_name= 'COD')
   
    produto = tables.TemplateColumn('{{ record.produto }}', 
                                    orderable=False,
                                    attrs=LEFT,
                                    verbose_name= 'PRODUTOS')

    qtd = tables.TemplateColumn('{{ record.qtd }} {{ record.produto.un_medida }}', 
                                    orderable=False,
                                    attrs=CENTER,
                                    verbose_name= 'QTD')
    
    valor = tables.TemplateColumn('{{ record.valor }}', 
                                    orderable=False,
                                    attrs=LEFT,
                                    verbose_name= 'R$')
    
    data_cadastro = tables.DateColumn(attrs=LEFT_DATA, verbose_name='DATA',  orderable=False)  


    DELETAR = tables.TemplateColumn('<a class="pointer btn_delete" data-id="{% url \'fatura.delete\' record.id  %}" ><i class=\'fas fa-trash fa-2x  red-text\'></i></a>', 
                                     orderable=False,
                                     attrs=CENTER,
                                     verbose_name= '')
    
    class Meta:
        attrs = {"class": " center uppercase table_top mt-1 size95 size95"}
        model = FaturaProduto
        fields = ['cod','produto', 'qtd', 'valor', 'data_cadastro']
        actions = tables.Column(orderable=True)

class HistoricoFaturaTable(tables.Table):
            
    CENTER = { 'th': { 'class': 'center teal-text darken-2'}, 'td': {'class': 'center'}}
    LEFT = { 'th':{'class': 'text-left teal-text darken-2'}, 'td': {'class': 'text-left'}}
    LEFT_BOLD = { 'th':{'class': 'text-left bold teal-text darken-2'}, 'td': {'class': 'text-left bold'}}
    
    paciente = tables.TemplateColumn('{{ record.paciente }}', 
                                    orderable=False,
                                    attrs=LEFT,
                                    verbose_name= 'PACIENTE')

    tutor = tables.TemplateColumn('{{ record.tutor }}', 
                                    orderable=False,
                                    attrs=LEFT,
                                    verbose_name= 'TUTOR')

    total = tables.TemplateColumn('{{ record.total }}', 
                                    orderable=False,
                                    attrs=CENTER,
                                    verbose_name= 'TOTAL')
    
    data_cadastro = tables.DateColumn(attrs=CENTER, verbose_name='DATA',  orderable=False)  

    
    FATURA = tables.TemplateColumn('<a href="{% url \'historico_fatura.export\' record.id  %}" ><i class=\'fas fa-file-pdf fa-2x  red-text\'></i></a>', 
                                     orderable=False,
                                     attrs=CENTER,
                                     verbose_name= '')
    
    DELETAR = tables.TemplateColumn('<a onclick="return confirm(\'Tem certeza que deseja deletar?\')" href="{% url \'historico_fatura.delete\' record.id  %}" ><i class=\'fas fa-trash fa-2x  red-text\'></i></a>', 
                                     orderable=False,
                                     attrs=CENTER,
                                     verbose_name= '')
    
    class Meta:
        attrs = {"class": " center uppercase table_top mt-1 size95 size95"}
        model = HistoricoFatura
        fields = ['paciente', 'tutor', 'total', 'data_cadastro']
        actions = tables.Column(orderable=True)
        
class VeterinarioTable(tables.Table):
    
    CENTER = { 'th': { 'class': 'center '}, 'td': {'class': 'center'}}
    LEFT = { 'th':{'class': 'text-left'}, 'td': {'class': 'text-left'}}
    LEFT_BOLD = { 'th':{'class': 'text-left'}, 'td': {'class': 'text-left bold'}}
    

    id = tables.Column(attrs=CENTER, verbose_name='COD')
    nome = tables.Column(attrs=LEFT, verbose_name= 'NOME')
    crmv = tables.Column(attrs=LEFT, verbose_name= 'CRMV')
    uf = tables.Column(attrs=LEFT, verbose_name= 'UF')

    EDITAR = tables.TemplateColumn('<a href="{% url \'veterinario.editar\' record.id  %}"><i class=\'fas fa-user-edit fa-2x orange-text\'></i></a>', 
                                    orderable=False,
                                    attrs=CENTER,
                                    verbose_name= '')
    

    DELETAR = tables.TemplateColumn('<a onclick="return confirm(\'Tem certeza que deseja deletar?\')" href="{% url \'veterinario.delete\' record.id  %}" ><i class=\'fas fa-trash fa-2x  red-text\'></i></a>', 
                                     orderable=False,
                                     attrs=CENTER,
                                     verbose_name= '')
    
    class Meta:
        attrs = {"class": "striped center uppercase table_top mt-1 size95"}
        model = AssinaturaVeterinario
        fields = ['id', 'nome', 'crmv', 'uf']
        actions = tables.Column(orderable=True)

class HistoricoPrescricaoTable(tables.Table):
            
    CENTER = { 'th': { 'class': 'center teal-text darken-2'}, 'td': {'class': 'center'}}
    LEFT = { 'th':{'class': 'text-left teal-text darken-2'}, 'td': {'class': 'text-left'}}
    LEFT_BOLD = { 'th':{'class': 'text-left bold teal-text darken-2'}, 'td': {'class': 'text-left bold'}}
    
    paciente = tables.TemplateColumn('{{ record.paciente }}', 
                                    orderable=False,
                                    attrs=LEFT,
                                    verbose_name= 'PACIENTE')

    tutor = tables.TemplateColumn('{{ record.tutor }}', 
                                    orderable=False,
                                    attrs=LEFT,
                                    verbose_name= 'TUTOR')

    data_cadastro = tables.DateTimeColumn(attrs=CENTER, verbose_name='DATA',  orderable=False)  

    
    PRESCRICAO = tables.TemplateColumn('<a href="{% url \'historico_prescricao.export\' record.id  %}" ><i class=\'fas fa-file-pdf fa-2x  red-text\'></i></a>', 
                                     orderable=False,
                                     attrs=CENTER,
                                     verbose_name= 'PRESCRIÇÃO')
    
    DELETAR = tables.TemplateColumn('<a onclick="return confirm(\'Tem certeza que deseja deletar?\')" href="{% url \'prescricao.delete\' record.id  %}" ><i class=\'fas fa-trash fa-2x  red-text\'></i></a>', 
                                     orderable=False,
                                     attrs=CENTER,
                                     verbose_name= '')
    
    class Meta:
        attrs = {"class": " center uppercase table_top mt-1 size95 size95"}
        model = Prescricao
        fields = ['paciente', 'tutor', 'data_cadastro']
        actions = tables.Column(orderable=True)
        