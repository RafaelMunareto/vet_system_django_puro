from django.contrib import admin
from .models import Agendamentos
from pacientes.models import Pacientes
from related_admin import RelatedFieldAdmin
from related_admin import getter_for_related_field

class ListandoAgendamentos(RelatedFieldAdmin):
    list_display = ('id', 'paciente__nome')
    list_display_links = ('id', 'paciente__nome')
    search_fields = ('id', 'paciente__nome')
    list_per_page = 10

admin.site.register(Agendamentos, ListandoAgendamentos)
