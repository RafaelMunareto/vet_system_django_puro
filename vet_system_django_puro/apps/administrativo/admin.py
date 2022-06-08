from django.contrib import admin
from .models import *

class ListandoParceiros(admin.ModelAdmin):
    list_display = ('id', 'nome', 'cpf')
    list_display_links = ('id', 'nome', 'cpf')
    search_fields = ('id', 'nome', 'cpf')
    list_per_page = 10

admin.site.register(Parceiros, ListandoParceiros)

class ListandoFornecedores(admin.ModelAdmin):
    list_display = ('id', 'nome', 'cnpj', 'ramo')
    list_display_links = ('id', 'nome', 'cnpj')
    search_fields = ('id', 'nome', 'cnpj', 'ramo')
    list_per_page = 10

admin.site.register(Fornecedores, ListandoFornecedores)

class ListandoProdutos(admin.ModelAdmin):
    list_display = ('id', 'fornecedor', 'produto', 'descricao')
    list_display_links = ('id', 'fornecedor', 'produto', 'descricao')
    search_fields = ('id', 'fornecedor', 'produto', 'descricao')
    list_per_page = 10

admin.site.register(Produtos, ListandoProdutos)

class ListandoEstoques(admin.ModelAdmin):
    list_display = ('id', 'produto')
    list_display_links = ('id', 'produto')
    search_fields = ('id', 'produto')
    list_per_page = 10

admin.site.register(Estoque, ListandoEstoques)

class ListandoPagamentos(admin.ModelAdmin):
    list_display = ('id', 'produto')
    list_display_links = ('id', 'produto')
    search_fields = ('id', 'produto')
    list_per_page = 10

admin.site.register(Pagamentos, ListandoPagamentos)

class ListandoServicos(admin.ModelAdmin):
    list_display = ('id', 'servico')
    list_display_links = ('id', 'servico')
    search_fields = ('id', 'servico')
    list_per_page = 10

admin.site.register(Servicos, ListandoServicos)

class ListandoCustosFixos(admin.ModelAdmin):
    list_display = ('id', 'nome', 'descricao')
    list_display_links = ('id', 'nome')
    search_fields = ('id', 'nome')
    list_per_page = 10

admin.site.register(CustosFixos, ListandoCustosFixos)





