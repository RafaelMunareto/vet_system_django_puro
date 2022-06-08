import django_tables2 as tables
from django_tables2 import TemplateColumn
from .models import Agendamentos
from service.Formata import *

class AgendamentosTable(tables.Table):
    
    CENTER = { 'th': { 'class': 'center '}, 'td': {'class': 'center'}}
    LEFT = { 'th':{'class': 'text-left'}, 'td': {'class': 'text-left'}}
    CENTER_BOLD = { 'th':{'class': 'center bold'}, 'td': {'class': 'center bold'}}
    TIPO = { 'th':{'class': 'left bold'}, 'td': {'class': 'left bold tipo'}}
    
    data = tables.Column(attrs=CENTER, verbose_name='DATA')
    time = tables.Column(attrs=CENTER, verbose_name='HORÁRIO')
    
    paciente = tables.TemplateColumn('<a class="a_href bold" href="{% url \'pacientes.detalhes\' record.paciente.id  %}">{{ record.paciente }}</a>', 
                                    orderable=False,
                                    attrs=LEFT,
                                    verbose_name= 'PACIENTE')
    
    tipo = tables.Column(attrs=LEFT, verbose_name='TIPO')
    obs = tables.Column(attrs=LEFT, verbose_name= 'OBSERVAÇÃO')

    EDITAR = tables.TemplateColumn('<a href="{% url \'agendamentos.editar\' record.id  %}"><i class=\'fas fa-history fa-2x orange-text\'></i></a>', 
                                    orderable=False,
                                    attrs=CENTER,
                                    verbose_name= '')
    
    DELETAR = tables.TemplateColumn('<a onclick="return confirm(\'Tem certeza que deseja deletar?\')" href="{% url \'agendamentos.delete\' record.id  %}" ><i class=\'fas fa-trash fa-2x  red-text\'></i></a>', 
                                     orderable=False,
                                     attrs=CENTER,
                                     verbose_name= '')
    
    def render_data(self, value):
        return Formata.stringToData(value)
    
    def render_tipo(self, value):
        return Formata.formata_tipo(value)
    
    class Meta:
        attrs = {"class": "striped center uppercase table_top size95 size95", 'id': 'table_agendamento'}
        model = Agendamentos
        fields = [ 'paciente', 'data', 'time', 'tipo', 'obs']
        actions = tables.Column(orderable=True)
