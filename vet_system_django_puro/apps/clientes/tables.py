import django_tables2 as tables
from django_tables2 import TemplateColumn
from .models import Clientes
from pacientes.models import Pacientes
from service.Formata import *

class ClientesTable(tables.Table):
    
    CENTER = { 'th': { 'class': 'center '}, 'td': {'class': 'center'}}
    LEFT = { 'th':{'class': 'text-left'}, 'td': {'class': 'text-left'}}
    

    id = tables.Column(attrs=CENTER, verbose_name='COD')
    nome = tables.TemplateColumn('<a href="{% url \'clientes.detalhes\' record.id  %}">{{ record.nome  }}</a>', 
                                    orderable=False,
                                    attrs=LEFT,
                                    verbose_name= 'NOME')
    cpf = tables.Column(attrs=LEFT, verbose_name= 'CPF')
    data_nascimento = tables.Column(attrs=CENTER, verbose_name= 'DATA NASCIMENTO')
    data_cadastro = tables.DateColumn(attrs=CENTER, verbose_name= 'DATA CADASTRO')
    
    PETS = tables.TemplateColumn('<a href="{% url \'pacientes.associados\' record.id  %}"><i class=\'fas fa-paw fa-2x teal-text\'></i></a>', 
                                    orderable=False,
                                    attrs=CENTER,
                                    verbose_name= '')

    CONTATOS = tables.TemplateColumn('<a  class="contato" data-id="{% url \'clientes.contatos\' record.id  %}"><i class=\'fas fa-phone a_href fa-2x teal-text\'></i></a>', 
                                    orderable=False,
                                    attrs=CENTER,
                                    verbose_name= '')
    
    ENDERECO = tables.TemplateColumn('<a  class="endereco" data-id="{% url \'clientes.endereco\' record.id  %}"><i class=\'fas a_href fa-map-marker-alt fa-2x teal-text\'></i></a>', 
                                    orderable=False,
                                    attrs=CENTER,
                                    verbose_name= '')
    
    
    EDITAR = tables.TemplateColumn('<a href="{% url \'clientes.editar\' record.id  %}"><i class=\'fas fa-user-edit fa-2x orange-text\'></i></a>', 
                                    orderable=False,
                                    attrs=CENTER,
                                    verbose_name= '')
    

    DELETAR = tables.TemplateColumn('<a onclick="return confirm(\'Tem certeza que deseja deletar?\')" href="{% url \'clientes.delete\' record.id  %}" ><i class=\'fas fa-trash fa-2x  red-text\'></i></a>', 
                                     orderable=False,
                                     attrs=CENTER,
                                     verbose_name= '')
    
    class Meta:
        attrs = {"class": "striped center uppercase table_top mt-1 size95"}
        model = Clientes
        fields = ['id', 'nome', 'cpf', 'data_nascimento','data_cadastro']
        actions = tables.Column(orderable=True)

class EnderecoTable(tables.Table):
    
    CENTER = { 'th': { 'class': 'center '}, 'td': {'class': 'center'}}
    LEFT = { 'th':{'class': 'text-left'}, 'td': {'class': 'text-left'}}
    
    id = tables.Column(attrs=CENTER, verbose_name='COD')
    cep = tables.Column(attrs=CENTER, verbose_name= 'CEP')
    estado = tables.Column(attrs=CENTER, verbose_name= 'ESTADO')
    cidade = tables.Column(attrs=LEFT, verbose_name= 'CIDADE')
    bairro = tables.Column(attrs=LEFT, verbose_name= 'BAIRRO')
    endereco = tables.Column(attrs=LEFT, verbose_name= 'ENDEREÇO')
    numero = tables.Column(attrs=CENTER, verbose_name= 'NÚMERO')
    complemento = tables.Column(attrs=LEFT, verbose_name= 'COMPLEMENTO')
        
    class Meta:
        attrs = {"class": "striped center uppercase table_top mt-1 size95"}
        model = Clientes
        fields = ['id', 'cep', 'estado', 'cidade', 'bairro', 'endereco', 'numero', 'complemento']
        actions = tables.Column(orderable=True)

class ContatosTable(tables.Table):
    
    CENTER = { 'th': { 'class': 'center '}, 'td': {'class': 'center'}}
    LEFT = { 'th':{'class': 'text-left'}, 'td': {'class': 'text-left'}}
    
    id = tables.Column(attrs=CENTER, verbose_name='COD')
    telefone_residencial = tables.Column(attrs=CENTER, verbose_name= 'TEL. RESIDENCIAL')
    telefone_comercial = tables.Column(attrs=CENTER, verbose_name= 'TEL. COMERCIAL')
    telefone_celular = tables.Column(attrs=CENTER, verbose_name= 'CELULAR')
    email = tables.Column(attrs=LEFT, verbose_name= 'EMAIL')
    
    
    class Meta:
        attrs = {"class": "striped center uppercase table_top mt-1 size95"}
        model = Clientes
        fields = ['id', 'telefone_residencial', 'telefone_comercial', 'telefone_celular', 'email']
        actions = tables.Column(orderable=True)



class AniversariosTutorTable(tables.Table):
    
    CENTER = { 'th': { 'class': 'center '}, 'td': {'class': 'center'}}
    LEFT = { 'th':{'class': 'text-left'}, 'td': {'class': 'text-left'}}
    
    id = tables.Column(attrs=CENTER, verbose_name='COD')
    
    nome = tables.TemplateColumn('<a href="{% url \'clientes.detalhes\' record.id  %}">{{ record.nome  }}</a>', 
                                    orderable=False,
                                    attrs=LEFT,
                                    verbose_name= 'NOME')
    
    CONTATOS = tables.TemplateColumn('<a  class="contato" data-id="{% url \'clientes.contatos\' record.id  %}"><i class=\'fas fa-phone a_href fa-2x teal-text\'></i></a>', 
                                    orderable=False,
                                    attrs=CENTER,
                                    verbose_name= '')
    
    ENDERECO = tables.TemplateColumn('<a  class="endereco" data-id="{% url \'clientes.endereco\' record.id  %}"><i class=\'fas a_href fa-map-marker-alt fa-2x teal-text\'></i></a>', 
                                    orderable=False,
                                    attrs=CENTER,
                                    verbose_name= '')
    
    
    class Meta:
        attrs = {"class": "striped center uppercase table_top mt-1 size95"}
        model = Clientes
        fields = ['id', 'nome']
        actions = tables.Column(orderable=True)

class AniversariosPetTable(tables.Table):
    
    CENTER = { 'th': { 'class': 'center '}, 'td': {'class': 'center'}}
    LEFT = { 'th':{'class': 'text-left'}, 'td': {'class': 'text-left'}}
    LEFT_BOLD = { 'th':{'class': 'text-left'}, 'td': {'class': 'text-left bold'}}
    
    id = tables.Column(attrs=CENTER, verbose_name='COD')
    nome = tables.Column(attrs=LEFT_BOLD, verbose_name='PACIENTE')  
    tutor = tables.TemplateColumn('<a href="{% url \'clientes.detalhes\' record.tutor.id  %}">{{ record.tutor }}</a>', 
                                    orderable=False,
                                    attrs=LEFT,
                                    verbose_name= 'TUTOR')

    CONTATOS = tables.TemplateColumn('<a  class="contato" data-id="{% url \'clientes.contatos\' record.tutor.id  %}"><i class=\'fas fa-phone a_href fa-2x teal-text\'></i></a>', 
                                    orderable=False,
                                    attrs=CENTER,
                                    verbose_name= '')
    
    ENDERECO = tables.TemplateColumn('<a  class="endereco" data-id="{% url \'clientes.endereco\' record.tutor.id  %}"><i class=\'fas a_href fa-map-marker-alt fa-2x teal-text\'></i></a>', 
                                    orderable=False,
                                    attrs=CENTER,
                                    verbose_name= '')
    
    
    class Meta:
        attrs = {"class": "striped center uppercase table_top mt-1 size95 size95"}
        model = Pacientes
        fields = ['id','nome', 'tutor']
        actions = tables.Column(orderable=True)