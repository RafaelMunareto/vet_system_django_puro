import django_tables2 as tables
from django_tables2 import TemplateColumn
from .models import Parceiros, Fornecedores, Produtos, Estoque, Servicos, Pagamentos, CustosFixos
from service.Formata import *

class ParceirosTable(tables.Table):
    
    CENTER = { 'th': { 'class': 'center '}, 'td': {'class': 'center'}}
    LEFT = { 'th':{'class': 'text-left'}, 'td': {'class': 'text-left'}}
    LEFT_BOLD = { 'th':{'class': 'text-left'}, 'td': {'class': 'text-left bold'}}
    

    id = tables.Column(attrs=CENTER, verbose_name='COD')
    nome = tables.TemplateColumn('<a href="{% url \'parceiros.detalhes\' record.id  %}">{{ record.nome  }}</a>', 
                                    attrs=LEFT,
                                    verbose_name= 'NOME')
    cpf = tables.Column(attrs=LEFT, verbose_name= 'CPF')
    especialidade = tables.Column(attrs=LEFT_BOLD, verbose_name= 'ESPECIALIDADE')
    data_cadastro = tables.DateColumn(attrs=CENTER, verbose_name= 'DATA CADASTRO')


    CONTATOS = tables.TemplateColumn('<a  class="contato" data-id="{% url \'parceiros.contatos\' record.id  %}"><i class=\'fas fa-phone a_href fa-2x teal-text\'></i></a>', 
                                    orderable=False,
                                    attrs=CENTER,
                                    verbose_name= '')
    
    ENDERECO = tables.TemplateColumn('<a  class="endereco" data-id="{% url \'parceiros.endereco\' record.id  %}"><i class=\'fas fa-map-marker-alt fa-2x a_href teal-text\'></i></a>', 
                                    orderable=False,
                                    attrs=CENTER,
                                    verbose_name= '')
    
    
    EDITAR = tables.TemplateColumn('<a href="{% url \'parceiros.editar\' record.id  %}"><i class=\'fas fa-user-edit fa-2x orange-text\'></i></a>', 
                                    orderable=False,
                                    attrs=CENTER,
                                    verbose_name= '')
    

    DELETAR = tables.TemplateColumn('<a onclick="return confirm(\'Tem certeza que deseja deletar?\')" href="{% url \'parceiros.delete\' record.id  %}" ><i class=\'fas fa-trash fa-2x  red-text\'></i></a>', 
                                     orderable=False,
                                     attrs=CENTER,
                                     verbose_name= '')
    
    class Meta:
        attrs = {"class": "striped center uppercase table_top mt-1 size95"}
        model = Parceiros
        fields = ['id', 'nome', 'cpf', 'especialidade','data_cadastro']
        actions = tables.Column(orderable=True)

class ParceirosEnderecoTable(tables.Table):
    
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
        model = Parceiros
        fields = ['id', 'cep', 'estado', 'cidade', 'bairro', 'endereco', 'numero', 'complemento']
        actions = tables.Column(orderable=True)

class ParceirosContatosTable(tables.Table):
    
    CENTER = { 'th': { 'class': 'center '}, 'td': {'class': 'center'}}
    LEFT = { 'th':{'class': 'text-left'}, 'td': {'class': 'text-left'}}
    
    id = tables.Column(attrs=CENTER, verbose_name='COD')
    telefone_residencial = tables.Column(attrs=CENTER, verbose_name= 'TEL. RESIDENCIAL')
    telefone_comercial = tables.Column(attrs=CENTER, verbose_name= 'TEL. COMERCIAL')
    telefone_celular = tables.Column(attrs=CENTER, verbose_name= 'CELULAR')
    email = tables.Column(attrs=LEFT, verbose_name= 'EMAIL')
    
    class Meta:
        attrs = {"class": "striped center uppercase table_top mt-1 size95"}
        model = Parceiros
        fields = ['id', 'telefone_residencial', 'telefone_comercial', 'telefone_celular', 'email']
        actions = tables.Column(orderable=True)


class FornecedoresTable(tables.Table):
    
    CENTER = { 'th': { 'class': 'center '}, 'td': {'class': 'center'}}
    LEFT = { 'th':{'class': 'text-left'}, 'td': {'class': 'text-left'}}
    LEFT_BOLD = { 'th':{'class': 'text-left'}, 'td': {'class': 'text-left bold'}}
    

    id = tables.Column(attrs=CENTER, verbose_name='COD')
    nome = tables.TemplateColumn('<a href="{% url \'parceiros.detalhes\' record.id  %}">{{ record.nome  }}</a>', 

                                    attrs=LEFT,
                                    verbose_name= 'NOME')
    cnpj = tables.Column(attrs=LEFT, verbose_name= 'CNPJ')
    ramo = tables.Column(attrs=LEFT, verbose_name= 'RAMO')
    data_cadastro = tables.DateColumn(attrs=CENTER, verbose_name= 'DATA CADASTRO')

    PRODUTOS = tables.TemplateColumn('<a title="Produtos associados nesse fornecedor" \
                                     href="{% url \'produtos.associados\' record.id  %}"><i class=\'fas fa-shopping-cart fa-2x teal-text\'></i></a>', 
                                    orderable=False,
                                    attrs=CENTER,
                                    verbose_name= '')

    CONTATOS = tables.TemplateColumn('<a  class="contato" data-id="{% url \'fornecedores.contatos\' record.id  %}"><i class=\'fas fa-phone a_href fa-2x teal-text\'></i></a>', 
                                    orderable=False,
                                    attrs=CENTER,
                                    verbose_name= '')
    
    ENDERECO = tables.TemplateColumn('<a  class="endereco" data-id="{% url \'fornecedores.endereco\' record.id  %}"><i class=\'fas fa-map-marker-alt fa-2x a_href teal-text\'></i></a>', 
                                    orderable=False,
                                    attrs=CENTER,
                                    verbose_name= '')

    BANCÁRIO = tables.TemplateColumn('<a class="bancario" data-id="{% url \'fornecedores.bancario\' record.id  %}"><i class=\'fas fa-piggy-bank fa-2x a_href teal-text\'></i></a>', 
                                    orderable=False,
                                    attrs=CENTER,
                                    verbose_name= '')
    
    
    EDITAR = tables.TemplateColumn('<a href="{% url \'fornecedores.editar\' record.id  %}"><i class=\'fas fa-user-edit fa-2x orange-text\'></i></a>', 
                                    orderable=False,
                                    attrs=CENTER,
                                    verbose_name= '')
    

    DELETAR = tables.TemplateColumn('<a onclick="return confirm(\'Tem certeza que deseja deletar?\')" href="{% url \'fornecedores.delete\' record.id  %}" ><i class=\'fas fa-trash fa-2x  red-text\'></i></a>', 
                                     orderable=False,
                                     attrs=CENTER,
                                     verbose_name= '')
    
    class Meta:
        attrs = {"class": "striped center uppercase table_top mt-1 size95"}
        model = Fornecedores
        fields = ['id', 'nome', 'cnpj', 'ramo','data_cadastro']
        actions = tables.Column(orderable=True)

class FornecedoresEnderecoTable(tables.Table):
    
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
        model = Fornecedores
        fields = ['id', 'cep', 'estado', 'cidade', 'bairro', 'endereco', 'numero', 'complemento']
        actions = tables.Column(orderable=True)

class FornecedoresBancarioTable(tables.Table):
    
    CENTER = { 'th': { 'class': 'center '}, 'td': {'class': 'center'}}
    LEFT = { 'th':{'class': 'text-left'}, 'td': {'class': 'text-left'}}
    
    id = tables.Column(attrs=CENTER, verbose_name='COD')
    banco = tables.Column(attrs=CENTER, verbose_name= 'BANCO')
    agencia = tables.Column(attrs=CENTER, verbose_name= 'AGÊNCIA')
    conta = tables.Column(attrs=LEFT, verbose_name= 'CONTA')
    obs = tables.Column(attrs=LEFT, verbose_name= 'OBSERVAÇÃO')
    
    class Meta:
        attrs = {"class": "striped center uppercase table_top mt-1 size95"}
        model = Fornecedores
        fields = ['id', 'banco', 'agencia', 'conta', 'obs']
        actions = tables.Column(orderable=True)

class FornecedoresContatosTable(tables.Table):
    
    CENTER = { 'th': { 'class': 'center '}, 'td': {'class': 'center'}}
    LEFT = { 'th':{'class': 'text-left'}, 'td': {'class': 'text-left'}}
    
    id = tables.Column(attrs=CENTER, verbose_name='COD')
    telefone_residencial = tables.Column(attrs=CENTER, verbose_name= 'TEL. RESIDENCIAL')
    telefone_comercial = tables.Column(attrs=CENTER, verbose_name= 'TEL. COMERCIAL')
    telefone_celular = tables.Column(attrs=CENTER, verbose_name= 'CELULAR')
    email = tables.Column(attrs=LEFT, verbose_name= 'EMAIL')
    
    class Meta:
        attrs = {"class": "striped center uppercase table_top mt-1 size95"}
        model = Fornecedores
        fields = ['id', 'telefone_residencial', 'telefone_comercial', 'telefone_celular', 'email']
        actions = tables.Column(orderable=True)

class ProdutosTable(tables.Table):
    
    CENTER = { 'th': { 'class': 'center '}, 'td': {'class': 'center'}}
    LEFT = { 'th':{'class': 'text-left'}, 'td': {'class': 'text-left'}}
    LEFT_BOLD = { 'th':{'class': 'text-left'}, 'td': {'class': 'text-left bold'}}

    fornecedor = tables.TemplateColumn('<a href="{% url \'fornecedores.detalhes\' record.fornecedor.id  %}">{{ record.fornecedor  }}</a>', 
                                orderable=False,
                                attrs=LEFT,
                                verbose_name= 'FORNECEDOR')
    
    id = tables.Column(attrs=CENTER, verbose_name= 'COD')
    produto = tables.Column(attrs=LEFT, verbose_name= 'PRODUTO')
    un_medida = tables.Column(attrs=LEFT, verbose_name= 'UNID. MEDIDA')
    custo = tables.Column(attrs=LEFT, verbose_name= 'CUSTO UNITÁRIO')
    venda = tables.Column(attrs=LEFT, verbose_name= 'PREÇO DE VENDA')
    descricao = tables.Column(attrs=LEFT, verbose_name= 'DESCRIÇÃO')

    EDITAR = tables.TemplateColumn('<a href="{% url \'produtos.editar\' record.id  %}"><i class=\'fas fa-pen-square fa-2x orange-text\'></i></a>', 
                                    orderable=False,
                                    attrs=CENTER,
                                    verbose_name= '')
    

    DELETAR = tables.TemplateColumn('<a onclick="return confirm(\'Tem certeza que deseja deletar?\')" href="{% url \'produtos.delete\' record.id  %}" ><i class=\'fas fa-trash fa-2x  red-text\'></i></a>', 
                                     orderable=False,
                                     attrs=CENTER,
                                     verbose_name= '')
    
   
    class Meta:
        attrs = {"class": "striped center uppercase table_top mt-1 size95"}
        model = Produtos
        fields = ['id', 'fornecedor', 'un_medida','custo', 'venda', 'produto', 'descricao']
        actions = tables.Column(orderable=True)
        
class ProdutosAssociadosTable(tables.Table):
    
    CENTER = { 'th': { 'class': 'center '}, 'td': {'class': 'center'}}
    LEFT = { 'th':{'class': 'text-left'}, 'td': {'class': 'text-left'}}
    LEFT_BOLD = { 'th':{'class': 'text-left'}, 'td': {'class': 'text-left bold'}}


    produto = tables.Column(attrs=LEFT, verbose_name= 'PRODUTO')
    un_medida = tables.Column(attrs=LEFT, verbose_name= 'UNID. MEDIDA')
    custo = tables.Column(attrs=LEFT, verbose_name= 'CUSTO UNITÁRIO')
    descricao = tables.Column(attrs=LEFT, verbose_name= 'DESCRIÇÃO')

    
    EDITAR = tables.TemplateColumn('<a href="{% url \'produtos.editar\' record.id  %}"><i class=\'fas fa-pen-square fa-2x orange-text\'></i></a>', 
                                    orderable=False,
                                    attrs=CENTER,
                                    verbose_name= '')
    

    DELETAR = tables.TemplateColumn('<a onclick="return confirm(\'Tem certeza que deseja deletar?\')" href="{% url \'produtos.delete\' record.id  %}" ><i class=\'fas fa-trash fa-2x  red-text\'></i></a>', 
                                     orderable=False,
                                     attrs=CENTER,
                                     verbose_name= '')
    
    class Meta:
        attrs = {"class": "striped center uppercase table_top mt-1 size95"}
        model = Produtos
        fields = ['un_medida','custo', 'produto', 'descricao']
        actions = tables.Column(orderable=True)
      
class EstoqueTable(tables.Table):
    
    CENTER = { 'th': { 'class': 'center '}, 'td': {'class': 'center'}}
    LEFT = { 'th':{'class': 'text-left'}, 'td': {'class': 'text-left'}}
    LEFT_BOLD = { 'th':{'class': 'text-left'}, 'td': {'class': 'text-left bold'}}
    
    fornecedor = tables.TemplateColumn('<a href="{% url \'fornecedores.detalhes\' record.produto.fornecedor.id  %}">{{ record.produto.fornecedor  }}</a>', 
                                    orderable=False,
                                    attrs=LEFT,
                                    verbose_name= 'FORNECEDOR')
    
    cod = tables.TemplateColumn('<a href="{% url \'produtos.detalhes\' record.produto.id  %}">{{ record.produto.id  }}</a>', 
                                    orderable=False,
                                    attrs=CENTER,
                                    verbose_name= 'COD')

    produto = tables.TemplateColumn('{{ record.produto  }}', 
                                    attrs=LEFT,
                                    verbose_name= 'PRODUTO')
    
    qtd_total = tables.TemplateColumn('{{ record.qtd_total }} {{ record.produto.un_medida}}', 
                                    attrs=CENTER,
                                    verbose_name= 'QTD')
    
    valor_total = tables.Column(attrs=CENTER, verbose_name= 'CUSTO TOTAL')

    custo = tables.TemplateColumn('{{ record.produto.custo  }}', 
                                    orderable=False,
                                    attrs=LEFT,
                                    verbose_name= 'CUSTO UNITÁRIO')

    venda = tables.TemplateColumn('{{ record.produto.venda  }}', 
                                    orderable=False,
                                    attrs=LEFT,
                                    verbose_name= 'PREÇO DE VENDA')                             
    
    data_movimento = tables.DateColumn(attrs=CENTER, verbose_name= 'DATA')

    
    EDITAR = tables.TemplateColumn('<a href="{% url \'estoque.editar\' record.id  %}"><i class=\'fas fa-pen-square fa-2x orange-text\'></i></a>', 
                                    orderable=False,
                                    attrs=CENTER,
                                    verbose_name= '')
    

    DELETAR = tables.TemplateColumn('<a onclick="return confirm(\'Tem certeza que deseja deletar?\')" href="{% url \'estoque.delete\' record.id  %}" ><i class=\'fas fa-trash fa-2x  red-text\'></i></a>', 
                                     orderable=False,
                                     attrs=CENTER,
                                     verbose_name= '')
    
    class Meta:
        attrs = {"class": "striped center uppercase table_top mt-1 size95"}
        model = Estoque
        fields = ['fornecedor','cod', 'produto','custo', 'venda', 'qtd_total','valor_total', 'data_movimento']
        actions = tables.Column(orderable=True)


class ServicosTable(tables.Table):
    
    CENTER = { 'th': { 'class': 'center '}, 'td': {'class': 'center'}}
    LEFT = { 'th':{'class': 'text-left'}, 'td': {'class': 'text-left'}}
    LEFT_BOLD = { 'th':{'class': 'text-left'}, 'td': {'class': 'text-left bold'}}

    id = tables.Column(attrs=CENTER, verbose_name= 'COD')
    servico = tables.Column(attrs=LEFT, verbose_name= 'SERVIÇO')
    venda = tables.Column(attrs=LEFT, verbose_name= 'PREÇO DE VENDA')
    descricao = tables.Column(attrs=LEFT, verbose_name= 'DESCRIÇÃO')

    
    EDITAR = tables.TemplateColumn('<a href="{% url \'servicos.editar\' record.id  %}"><i class=\'fas fa-pen-square fa-2x orange-text\'></i></a>', 
                                    orderable=False,
                                    attrs=CENTER,
                                    verbose_name= '')
    

    DELETAR = tables.TemplateColumn('<a onclick="return confirm(\'Tem certeza que deseja deletar?\')" href="{% url \'servicos.delete\' record.id  %}" ><i class=\'fas fa-trash fa-2x  red-text\'></i></a>', 
                                     orderable=False,
                                     attrs=CENTER,
                                     verbose_name= '')
    
    class Meta:
        attrs = {"class": "striped center uppercase table_top mt-1 size95"}
        model = Servicos
        fields = ['id', 'servico', 'venda','descricao']
        actions = tables.Column(orderable=True)

class PagamentosTable(tables.Table):
    
    CENTER = { 'th': { 'class': 'center '}, 'td': {'class': 'center'}}
    LEFT = { 'th':{'class': 'text-left'}, 'td': {'class': 'text-left'}}
    LEFT_BOLD = { 'th':{'class': 'text-left'}, 'td': {'class': 'text-left bold'}}

    fornecedor = tables.TemplateColumn('{{ record.produto.fornecedor }}', 
                                    orderable=True,
                                    attrs=LEFT,
                                    verbose_name= 'FORNECEDOR')

    cod = tables.TemplateColumn('{{ record.produto.id }}', 
                                    orderable=True,
                                    attrs=LEFT,
                                    verbose_name= 'COD')

    produto = tables.TemplateColumn('{{ record.produto }}', 
                                    orderable=True,
                                    attrs=LEFT,
                                    verbose_name= 'PRODUTO')

    custo = tables.TemplateColumn('{{ record.produto.custo}}', 
                                    orderable=True,
                                    attrs=LEFT,
                                    verbose_name= 'CUSTO UNITÁRIO')
    
    qtd_total = tables.Column(attrs=LEFT, verbose_name= 'QTD TOTAL')
    
    valor_total = tables.Column(attrs=LEFT, verbose_name= 'VALOR À PAGAR')
       
    pagamento = tables.Column(attrs=CENTER, verbose_name= 'DATA PAGAMENTO')


    contatos = tables.TemplateColumn('<a  class="contato" data-id="{% url \'fornecedores.contatos\' record.produto.fornecedor.id  %}"><i class=\'fas fa-phone a_href fa-2x teal-text\'></i></a>', 
                                    orderable=False,
                                    attrs=CENTER,
                                    verbose_name= '')
    
    endereco = tables.TemplateColumn('<a  class="endereco" data-id="{% url \'fornecedores.endereco\' record.produto.fornecedor.id  %}"><i class=\'fas fa-map-marker-alt fa-2x a_href teal-text\'></i></a>', 
                                    orderable=False,
                                    attrs=CENTER,
                                    verbose_name= '')

    bancario = tables.TemplateColumn('<a class="bancario" data-id="{% url \'fornecedores.bancario\' record.produto.fornecedor.id  %}"><i class=\'fas fa-piggy-bank fa-2x a_href teal-text\'></i></a>', 
                                    orderable=False,
                                    attrs=CENTER,
                                    verbose_name= '')
    
    editar = tables.TemplateColumn('<a href="{% url \'pagamentos_fornecedor.editar\' record.id  %}"><i class=\'fas fa-pen-square fa-2x orange-text\'></i></a>', 
                                    orderable=False,
                                    attrs=CENTER,
                                    verbose_name= '')
        
    def render_pagamento(self, value):
        return Formata.stringToData(value)
    
    class Meta:
        attrs = {"class": "center uppercase table_top mt-1 size95"}

        model = Pagamentos
        fields = ['fornecedor', 'cod', 'produto', 'custo', 'qtd_total', 'valor_total', 'pagamento']
        actions = tables.Column(orderable=True)

class CustosFixosTable(tables.Table):
    
    CENTER = { 'th': { 'class': 'center '}, 'td': {'class': 'center'}}
    LEFT = { 'th':{'class': 'text-left'}, 'td': {'class': 'text-left'}}
    LEFT_BOLD = { 'th':{'class': 'text-left'}, 'td': {'class': 'text-left bold'}}

    id = tables.Column(attrs=CENTER, verbose_name= 'COD')
    nome = tables.Column(attrs=LEFT, verbose_name= 'NOME')
    custo = tables.Column(attrs=LEFT, verbose_name= 'CUSTO')
    descricao = tables.Column(attrs=LEFT, verbose_name= 'DESCRIÇÃO')
    pagamento = tables.Column(attrs=CENTER, verbose_name= 'DATA PAGAMENTO')
    recorrente = tables.Column(attrs=CENTER, verbose_name= 'RECORRENTE')
    
    EDITAR = tables.TemplateColumn('<a href="{% url \'custos_fixos.editar\' record.id  %}"><i class=\'fas fa-pen-square fa-2x orange-text\'></i></a>', 
                                    orderable=False,
                                    attrs=CENTER,
                                    verbose_name= '')
    

    DELETAR = tables.TemplateColumn('<a onclick="return confirm(\'Tem certeza que deseja deletar?\')" href="{% url \'custos_fixos.delete\' record.id  %}" ><i class=\'fas fa-trash fa-2x  red-text\'></i></a>', 
                                     orderable=False,
                                     attrs=CENTER,
                                     verbose_name= '')
    
    def render_pagamento(self, value):
        return Formata.stringToData(value)
    
    def render_custo(self, value):
        return Formata.dinheiro(value)
    
    def render_recorrente(self, value):
        return Formata.true_false(value) 
    
    class Meta:
        attrs = {"class": " center uppercase table_top mt-1 size95"}
        model = CustosFixos
        fields = ['id', 'nome', 'custo','descricao', 'pagamento']
        actions = tables.Column(orderable=True)