from django.contrib import admin
from .models import *

class ListandoClientes(admin.ModelAdmin):
    list_display = ('id', 'nome', 'cpf')
    list_display_links = ('id', 'nome', 'cpf')
    search_fields = ('id', 'nome', 'cpf')
    list_per_page = 10

admin.site.register(Clientes, ListandoClientes)
