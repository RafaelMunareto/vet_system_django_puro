from django.contrib import admin
from .models import *
from related_admin import RelatedFieldAdmin
from related_admin import getter_for_related_field

class ListandoPacientes(RelatedFieldAdmin):
    list_display = ('id', 'nome', 'tutor__nome')
    list_display_links = ('id', 'nome', 'tutor__nome')
    search_fields = ('id', 'nome', 'tutor__nome')
    list_per_page = 10

admin.site.register(Pacientes, ListandoPacientes)

class ListandoFaturaProduto(RelatedFieldAdmin):
    list_display = ('id', 'paciente__nome', 'paciente__tutor', 'data_cadastro')
    list_display_links = ('id', 'paciente__nome')
    search_fields = ('id', 'paciente__nome', 'paciente__tutor', 'data_cadastro')
    list_per_page = 10

admin.site.register(FaturaProduto, ListandoFaturaProduto)  

class ListandoHistoricoFaturas(RelatedFieldAdmin):
    list_display = ('id', 'paciente__nome', 'paciente__tutor', 'data_cadastro')
    list_display_links = ('id', 'paciente__nome')
    search_fields = ('id', 'paciente__nome', 'paciente__tutor', 'data_cadastro')
    list_per_page = 10

admin.site.register(HistoricoFatura, ListandoHistoricoFaturas) 

class ListandoPrescricao(RelatedFieldAdmin):
    list_display = ('id', 'paciente__nome', 'paciente__tutor', 'vet__nome')
    list_display_links = ('id', 'paciente__nome')
    search_fields = ('id', 'paciente__nome', 'paciente__tutor', 'vet__nome')
    list_per_page = 10

admin.site.register(Prescricao, ListandoPrescricao) 

class ListandoAssinaturaVeterinario(RelatedFieldAdmin):
    list_display = ('id', 'nome', 'crmv')
    list_display_links = ('id', 'nome')
    search_fields = ('id', 'nome', 'crmv')
    list_per_page = 10

admin.site.register(AssinaturaVeterinario, ListandoAssinaturaVeterinario) 

