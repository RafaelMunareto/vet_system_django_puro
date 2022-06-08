from django import forms
from .models import Clientes
from service.Buscador import *
from service.Formata import *
from service.validation import *

class ClientesForms (forms.ModelForm, Buscador, Formata):
    
    nome = forms.CharField(required=False, label='NOME')
    cpf = forms.CharField(label='CPF', required=False, widget=forms.TextInput(attrs={'class': 'cpf'}))
    data_nascimento = forms.CharField(label='DATA NASCIMENTO', required=False, widget=forms.TextInput(attrs={'class': 'date'}))                        
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
        model = Clientes
        exclude = ['id', 'data_cadastro']
        
    
    
    def clean(self):
        cleaned_data = super(ClientesForms, self).clean()
        nome = self.cleaned_data.get('nome')
        cpf = self.cleaned_data.get('cpf')
        data_nascimento = self.cleaned_data.get('data_nascimento')
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
        tamanho_data(data_nascimento,'data_nascimento', lista_de_erros)
        tamanho_celular(telefone_celular,'telefone_celular', lista_de_erros)
        verifica_email(email,'email', lista_de_erros)
        tamanho_cep(cep,'cep', lista_de_erros)
        escolha_valida(estado,'estado', lista_de_erros)
        min_len_3(cidade,'cidade', lista_de_erros)
        min_len_3(bairro,'bairro', lista_de_erros)
        min_len_3(endereco,'endereco', lista_de_erros)
        campo_nao_preechido(estado,'estado', lista_de_erros)
        
        
        if lista_de_erros is not None:
            for erro in lista_de_erros:
                mensagem_erro = lista_de_erros[erro]
                self.add_error(erro, mensagem_erro) 
        return self.cleaned_data

class AniversariosForm(forms.Form, Buscador, Formata):
    
    aniversarios_tutor = forms.ChoiceField(label='', required=False, choices=([(0, 'ESCOLHA A DATA')] + [(Formata.data_aniversario(linha['data_nascimento']), Formata.data_aniversario(linha['data_nascimento'])) 
                        for linha in Buscador.busca_data_nascimento_clientes()]), widget=forms.Select(attrs={"id": "aniversarios_tutor","class": "e1 !important"}))
    
    aniversarios_pet = forms.ChoiceField(label='', required=False, choices=([(0, 'ESCOLHA A DATA')] + [(Formata.data_aniversario(linha['data_nascimento']), Formata.data_aniversario(linha['data_nascimento'])) 
                        for linha in Buscador.busca_data_nascimento_pacientes()]), widget=forms.Select(attrs={"id": "aniversarios_pet", "class": "e2 !important"}))