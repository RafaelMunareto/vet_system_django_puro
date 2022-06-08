from django import forms
from .models import Parceiros, Fornecedores, Produtos, Estoque, Servicos, Pagamentos, CustosFixos
from service.Buscador import *
from service.Formata import *
from service.validation import *
from datetime import date, datetime
import easy_date
import date_converter

UN_MEDIDA = [
    (0, 'UNIDADE DE MEDIDA'),
    ('kg', 'KILOGRAMA'),
    ('g', 'GRAMA'),
    ('mg', 'MILEGRAMA'),
    ('mcg', 'MICROGRAMA'),
    ('l', 'LITRO'),
    ('ml', 'MILELITRO'),
    ('unidade', 'UNITÁRIO'),
    ('comprimido', 'COMPRIMIDO'),
    ('ampola', 'AMPOLO'),
    ('caixa', 'CAIXA')
]

class ParceirosForms (forms.ModelForm, Buscador, Formata):
    
    nome = forms.CharField(required=False, label='NOME')
    cpf = forms.CharField(label='CPF', required=False, widget=forms.TextInput(attrs={'class': 'cpf'}))
    especialidade = forms.CharField(label='ESPECIALIDADE', required=False)                        
    telefone_residencial = forms.CharField(required=False, label="TEL RESIDENCIAL", widget=forms.TextInput(attrs={'class': 'telefone'}))
    telefone_comercial = forms.CharField(required=False, label="TEL COMERCIAL", widget=forms.TextInput(attrs={'class': 'telefone'}))
    telefone_celular = forms.CharField(required=False, label="TEL CELULAR", widget=forms.TextInput(attrs={'class': 'celular'}))
    email = forms.CharField(required=False, label="EMAIL", widget=forms.TextInput(attrs={'class': 'email'}))
    cep = forms.CharField(required=False, label="CEP", widget=forms.TextInput(attrs={'class': 'cep'}))
    estado = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'placeholder': 'ESTADO'}))
    cidade = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'placeholder': 'CIDADE'}))
    bairro = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'placeholder': 'BAIRRO'}))
    endereco = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'placeholder': 'ENDEREÇO'}))
    numero = forms.IntegerField(required=False, label="NÚMERO", widget=forms.NumberInput(attrs={}))
    complemento = forms.CharField(required=False, label="COMPLEMENTO", widget=forms.TextInput(attrs={}))
    
    class Meta:
        model = Parceiros
        exclude = ['id', 'data_cadastro', 'user']
        
    
    
    def clean(self):
        cleaned_data = super(ParceirosForms, self).clean()
        nome = self.cleaned_data.get('nome')
        cpf = self.cleaned_data.get('cpf')
        especialidade = self.cleaned_data.get('especialidade')
        telefone_celular = self.cleaned_data.get('telefone_celular')
        email = self.cleaned_data.get('email')
        cep = self.cleaned_data.get('cep')
        estado = self.cleaned_data.get('estado')
        cidade = self.cleaned_data.get('cidade')
        bairro = self.cleaned_data.get('bairro')
        endereco = self.cleaned_data.get('endereco')
        numero = self.cleaned_data.get('numero')
        lista_de_erros = {}
        
        min_len_3(nome,'nome', lista_de_erros)
        tamanho_cpf(cpf,'cpf', lista_de_erros)
        tamanho_celular(telefone_celular,'telefone_celular', lista_de_erros)
        verifica_email(email,'email', lista_de_erros)
        tamanho_cep(cep,'cep', lista_de_erros)
        escolha_valida(estado,'estado', lista_de_erros)
        min_len_3(cidade,'cidade', lista_de_erros)
        min_len_3(bairro,'bairro', lista_de_erros)
        min_len_3(especialidade,'especialidade', lista_de_erros)
        min_len_3(endereco,'endereco', lista_de_erros)
        campo_nao_preechido(estado,'estado', lista_de_erros)
        
        
        if lista_de_erros is not None:
            for erro in lista_de_erros:
                mensagem_erro = lista_de_erros[erro]
                self.add_error(erro, mensagem_erro) 
        return self.cleaned_data

class FornecedoresForms (forms.ModelForm, Buscador, Formata):
    
    nome = forms.CharField(required=False, label='NOME')
    cnpj = forms.CharField(label='CNPJ', required=False, widget=forms.TextInput(attrs={'class': 'cnpj'}))
    ramo = forms.CharField(label='RAMO', required=False)                        
    telefone_residencial = forms.CharField(required=False, label="TEL RESIDENCIAL", widget=forms.TextInput(attrs={'class': 'telefone'}))
    telefone_comercial = forms.CharField(required=False, label="TEL COMERCIAL", widget=forms.TextInput(attrs={'class': 'telefone'}))
    telefone_celular = forms.CharField(required=False, label="TEL CELULAR", widget=forms.TextInput(attrs={'class': 'celular'}))
    email = forms.CharField(required=False, label="EMAIL", widget=forms.TextInput(attrs={'class': 'email'}))
    cep = forms.CharField(required=False, label="CEP", widget=forms.TextInput(attrs={'class': 'cep'}))
    estado = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'placeholder': 'ESTADO'}))
    cidade = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'placeholder': 'CIDADE'}))
    bairro = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'placeholder': 'BAIRRO'}))
    endereco = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'placeholder': 'ENDEREÇO'}))
    numero = forms.IntegerField(required=False, label="NÚMERO", widget=forms.NumberInput(attrs={}))
    complemento = forms.CharField(required=False, label="COMPLEMENTO", widget=forms.TextInput(attrs={}))
    obs = forms.CharField(required=False, label="OBS", widget=forms.TextInput(attrs={}))
    banco = forms.CharField(required=False, label="BANCO", widget=forms.TextInput(attrs={}))
    agencia = forms.CharField(required=False, label="AGÊNCIA", widget=forms.TextInput(attrs={}))
    conta = forms.CharField(required=False, label="CONTA", widget=forms.TextInput(attrs={}))

    class Meta:
        model = Fornecedores
        exclude = ['id', 'data_cadastro', 'user']
        
    def clean(self):
        cleaned_data = super(FornecedoresForms, self).clean()
        nome = self.cleaned_data.get('nome')
        cnpj = self.cleaned_data.get('cnpj')
        ramo = self.cleaned_data.get('ramo')
        telefone_celular = self.cleaned_data.get('telefone_celular')
        email = self.cleaned_data.get('email')
        cep = self.cleaned_data.get('cep')
        estado = self.cleaned_data.get('estado')
        cidade = self.cleaned_data.get('cidade')
        bairro = self.cleaned_data.get('bairro')
        endereco = self.cleaned_data.get('endereco')
        numero = self.cleaned_data.get('numero')
        lista_de_erros = {}
        
        min_len_3(nome,'nome', lista_de_erros)
        tamanho_cpf(cnpj,'cnpj', lista_de_erros)
        tamanho_celular(telefone_celular,'telefone_celular', lista_de_erros)
        verifica_email(email,'email', lista_de_erros)
        tamanho_cep(cep,'cep', lista_de_erros)
        escolha_valida(estado,'estado', lista_de_erros)
        min_len_3(cidade,'cidade', lista_de_erros)
        min_len_3(bairro,'bairro', lista_de_erros)
        min_len_3(ramo,'ramo', lista_de_erros)
        min_len_3(endereco,'endereco', lista_de_erros)
        campo_nao_preechido(estado,'estado', lista_de_erros)
        
        
        if lista_de_erros is not None:
            for erro in lista_de_erros:
                mensagem_erro = lista_de_erros[erro]
                self.add_error(erro, mensagem_erro) 
        return self.cleaned_data

class ProdutosForms (forms.ModelForm, Buscador, Formata):
    
    fornecedor_id = forms.ChoiceField(label='', required=True, choices=([(0, 'ESCOLHA O FORNECEDOR')] + [(int(linha['id']),  str(linha['id']) + ' - ' + str(linha['nome'].upper())) 
                    for linha in Buscador.busca_fornecedores()]), widget=forms.Select(attrs={"name": "fornecedor_id","class": "e1 !important"}))
    produto = forms.CharField(label='PRODUTO', required=False)
    un_medida = forms.ChoiceField(label='', required=True, choices=UN_MEDIDA, widget=forms.Select(attrs={"name": "un_medida","class": "comite_select !important"}))
    descricao = forms.CharField(label='DESCRIÇÃO', required=False)                        
    custo = forms.CharField(required=False, label="CUSTO UNITÁRIO", widget=forms.TextInput(attrs={'class': 'money'}))
    venda = forms.CharField(required=False, label="PREÇO VENDA", widget=forms.TextInput(attrs={'class': 'money'}))
    
    class Meta:
        model = Produtos
        exclude = ['id', 'data_cadastro', 'fornecedor', 'user']
        
    def clean(self):
        cleaned_data = super(ProdutosForms, self).clean()
        fornecedor_id = self.cleaned_data.get('fornecedor_id')
        produto = self.cleaned_data.get('produto')
        un_medida = self.cleaned_data.get('un_medida')
        custo = self.cleaned_data.get('custo')
        venda = self.cleaned_data.get('venda')
        lista_de_erros = {}
        
        escolha_valida(fornecedor_id,'fornecedor_id', lista_de_erros)
        min_len_3(produto,'produto', lista_de_erros)
        escolha_valida(un_medida,'un_medida', lista_de_erros)
        campo_nao_preenchido(custo,'custo', lista_de_erros)
        campo_nao_preenchido(venda,'venda', lista_de_erros)
       
                
        if lista_de_erros is not None:
            for erro in lista_de_erros:
                mensagem_erro = lista_de_erros[erro]
                self.add_error(erro, mensagem_erro) 
        return self.cleaned_data


class ServicosForms (forms.ModelForm, Buscador, Formata):
    
    servico = forms.CharField(label='SERVIÇOS', required=False)
    descricao = forms.CharField(label='DESCRIÇÃO', required=False)                        
    venda = forms.CharField(required=False, label="PREÇO VENDA", widget=forms.TextInput(attrs={'class': 'money'}))
    
    class Meta:
        model = Servicos
        exclude = ['id', 'data_cadastro', 'user']
        
    def clean(self):
        cleaned_data = super(ServicosForms, self).clean()
        servico = self.cleaned_data.get('servico')
        custo = self.cleaned_data.get('custo')
        venda = self.cleaned_data.get('venda')
        
        lista_de_erros = {}
        
        min_len_3(servico,'servico', lista_de_erros)
        campo_nao_preenchido(custo,'custo', lista_de_erros)
        campo_nao_preenchido(venda,'venda', lista_de_erros)
                
        if lista_de_erros is not None:
            for erro in lista_de_erros:
                mensagem_erro = lista_de_erros[erro]
                self.add_error(erro, mensagem_erro) 
        return self.cleaned_data


class ProdutosEditarForms (forms.ModelForm, Buscador, Formata):
    
    produto = forms.CharField(label='PRODUTO', required=False)
    un_medida = forms.ChoiceField(label='', required=True, choices=UN_MEDIDA, widget=forms.Select(attrs={"name": "un_medida","class": "comite_select !important"}))
    descricao = forms.CharField(label='DESCRIÇÃO', required=False)                        
    custo = forms.CharField(required=False, label="CUSTO UNITÁRIO", widget=forms.TextInput(attrs={'class': 'money'}))
    venda = forms.CharField(required=False, label="VENDA", widget=forms.TextInput(attrs={'class': 'money'}))
    pagamento = forms.DateField(label='DATA PAGAMENTO', required=True, widget=forms.DateInput(attrs={'class': 'datepicker', 'placeholder':'DATA PAGAMENTO'}))        

    class Meta:
        model = Produtos
        exclude = ['id', 'data_cadastro', 'fornecedor', 'user']
        
    def clean(self):
        cleaned_data = super(ProdutosEditarForms, self).clean()
        produto = self.cleaned_data.get('produto')
        un_medida = self.cleaned_data.get('un_medida')
        custo = self.cleaned_data.get('custo')
        venda = self.cleaned_data.get('venda')
        pagamento = self.cleaned_data.get('pagamento')
        lista_de_erros = {}
        
        min_len_3(produto,'produto', lista_de_erros)
        escolha_valida(un_medida,'un_medida', lista_de_erros)
        campo_nao_preenchido(custo,'custo', lista_de_erros)
        campo_nao_preenchido(venda,'venda', lista_de_erros)
        campo_nao_preenchido(pagamento,'pagamento', lista_de_erros)
                
        if lista_de_erros is not None:
            for erro in lista_de_erros:
                mensagem_erro = lista_de_erros[erro]
                self.add_error(erro, mensagem_erro) 
        return self.cleaned_data

class EstoqueForms (forms.Form, Buscador, Formata):
    
    produto_id = forms.ChoiceField(label='', required=True, choices=([(0, 'ESCOLHA O PRODUTO')] + [(int(linha.id),  str(linha.fornecedor).upper() + ' - ' + ' COD ' + str(linha.id) + ' - ' + str(linha.produto.upper())) 
                    for linha in Buscador.busca_produtos()]), widget=forms.Select(attrs={"name": "produto_id","class": "e1 !important"}))
    qtd = forms.CharField(label='QTD', required=False)
    pagamento = forms.DateField(label='DATA PAGAMENTO', required=True, widget=forms.DateInput(attrs={'class': 'datepicker', 'placeholder':'DATA PAGAMENTO'}))        

    class Meta:
        model = Estoque
        exclude = ['id', 'data_movimento', 'produto', 'valor_total', 'qtd_total', 'user']
        
    def clean(self):
        cleaned_data = super(EstoqueForms, self).clean()
        qtd = self.cleaned_data.get('qtd')
        produto_id = self.cleaned_data.get('produto_id')
        pagamento = self.cleaned_data.get('pagamento')
        lista_de_erros = {}
        
        campo_nao_preenchido(qtd,'qtd', lista_de_erros)
        escolha_valida(produto_id,'produto_id', lista_de_erros)
        campo_nao_preenchido(pagamento,'pagamento', lista_de_erros)
        
                
        if lista_de_erros is not None:
            for erro in lista_de_erros:
                mensagem_erro = lista_de_erros[erro]
                self.add_error(erro, mensagem_erro) 
        return self.cleaned_data

class EstoqueEditarForms (forms.ModelForm, Buscador, Formata):
    
    qtd_total = forms.CharField(label='QTD TOTAL', required=False)
    valor_total = forms.CharField(label='VALOR TOTAL', required=False)
    pagamento = forms.DateField(label='DATA PAGAMENTO', required=True, widget=forms.DateInput(attrs={'class': 'datepicker', 'placeholder':'DATA PAGAMENTO'}))        

    class Meta:
        model = Estoque
        fields = ['valor_total', 'qtd_total', 'pagamento']
        
    def clean(self):
        cleaned_data = super(EstoqueEditarForms, self).clean()
        qtd_total = self.cleaned_data.get('qtd_total')
        valor_total = self.cleaned_data.get('valor_total')
        pagamento = self.cleaned_data.get('pagamento')
        lista_de_erros = {}
        
        campo_nao_preenchido(qtd_total,'qtd_total', lista_de_erros)
        campo_nao_preenchido(valor_total,'valor_total', lista_de_erros)
        campo_nao_preenchido(pagamento,'pagamento', lista_de_erros)
               
        if lista_de_erros is not None:
            for erro in lista_de_erros:
                mensagem_erro = lista_de_erros[erro]
                self.add_error(erro, mensagem_erro) 
        return self.cleaned_data


class PagamentosForms(forms.Form, Buscador, Formata):
    
    fornecedor_id = forms.ChoiceField(label='', required=True, choices=([(0, 'ESCOLHA O FORNECEDOR')] + [(int(linha['id']),  str(linha['id']) + ' - ' + str(linha['nome']).upper()) 
                    for linha in Buscador.busca_fornecedores()]), widget=forms.Select(attrs={"name": "fornecedor_id","class": "e1 !important", 'id':'fornecedor_id'}))
    
    pagamento_id = forms.ChoiceField(label='', required=True, choices=([(0, 'TODAS AS DATAS')] + [(linha['pagamento'],  (Formata.stringToData(linha['pagamento'])))
                    for linha in Buscador.busca_data_pagamentos()]), widget=forms.Select(attrs={"name": "pagamento_id","class": "e1 !important", 'id':'pagamento_id'}))

class PagamentosEditarForms (forms.ModelForm, Buscador, Formata):
    
    pagamento = forms.DateField(label='DATA PAGAMENTO', required=True, widget=forms.DateInput(attrs={'class': 'datepicker', 'placeholder':'DATA PAGAMENTO'}))        

    class Meta:
        model = Pagamentos
        fields = ['pagamento']
        
    def clean(self):
        cleaned_data = super(PagamentosEditarForms, self).clean()
        pagamento = self.cleaned_data.get('pagamento')
        lista_de_erros = {}
        
        campo_nao_preenchido(pagamento,'pagamento', lista_de_erros)
               
        if lista_de_erros is not None:
            for erro in lista_de_erros:
                mensagem_erro = lista_de_erros[erro]
                self.add_error(erro, mensagem_erro) 
        return self.cleaned_data

class CustosFixosForms (forms.ModelForm, Buscador, Formata):
    
    nome = forms.CharField(label='NOME', required=False)
    custo = forms.CharField(label='CUSTO', required=False, widget=forms.TextInput(attrs={'class': 'money'}))
    descricao = forms.CharField(label='DESCRIÇÃO', required=False)                        
    pagamento = forms.DateField(label='DATA PAGAMENTO', required=True, widget=forms.DateInput(attrs={'class': 'datepicker', 'placeholder':'DATA PAGAMENTO'}))        

    class Meta:
        model = CustosFixos
        exclude = ['id', 'data_cadastro', 'custo', 'user']
        
    def clean(self):
        cleaned_data = super(CustosFixosForms, self).clean()
        nome = self.cleaned_data.get('nome')
        custo = self.cleaned_data.get('custo')
        pagamento = self.cleaned_data.get('pagamento')
        
        lista_de_erros = {}
        
        min_len_3(nome,'nome', lista_de_erros)
        campo_nao_preenchido(custo,'custo', lista_de_erros)
        campo_nao_preenchido(pagamento, 'pagamento', lista_de_erros)      
        
        if lista_de_erros is not None:
            for erro in lista_de_erros:
                mensagem_erro = lista_de_erros[erro]
                self.add_error(erro, mensagem_erro) 
        return self.cleaned_data
