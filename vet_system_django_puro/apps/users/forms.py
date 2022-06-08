from django import forms
from .models import *
from service.Buscador import *
from service.Formata import *
from service.validation import *

class CadastroUsersForms (forms.Form, Buscador, Formata):
    
    nome = forms.CharField(required=False, label='NOME')
    sobrenome = forms.CharField(required=False, label='SOBRENOME')
    username = forms.CharField(required=False, label='USERNAME')
    email = forms.CharField(label='EMAIL', required=False, widget=forms.TextInput(attrs={'class': ''}))
    senha = forms.CharField(label='SENHA', required=False, widget=forms.TextInput(attrs={'class': '', "type": "password"}))                        
    confirma_senha = forms.CharField(required=False, label="CONFIRMA SENHA", widget=forms.TextInput(attrs={'class': '', "type": "password"}))
    

    def clean(self):
        cleaned_data = super(CadastroUsersForms, self).clean()
        nome = self.cleaned_data.get('nome')
        sobrenome = self.cleaned_data.get('sobrenome')
        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')
        senha = self.cleaned_data.get('senha')
        confirma_senha = self.cleaned_data.get('confirma_senha')
        lista_de_erros = {}
        
        min_len_3(nome,'nome', lista_de_erros)
        min_len_3(sobrenome,'sobrenome', lista_de_erros)
        min_len_3(username,'username', lista_de_erros)
        verifica_email(email,'email', lista_de_erros)
        min_len_6(senha,'senha', lista_de_erros)
        compara_senhas(confirma_senha, senha, 'confirma_senha', lista_de_erros)
    
        if lista_de_erros is not None:
            for erro in lista_de_erros:
                mensagem_erro = lista_de_erros[erro]
                self.add_error(erro, mensagem_erro) 
        return self.cleaned_data

class LoginUsersForms (forms.Form, Buscador, Formata):
    
    username = forms.CharField(required=False, label='USERNAME')
    senha = forms.CharField(label='SENHA', required=False, widget=forms.TextInput(attrs={'class': '', "type": "password"}))
    

    def clean(self):
        cleaned_data = super(LoginUsersForms, self).clean()
        username = self.cleaned_data.get('username')
        senha = self.cleaned_data.get('senha')
        lista_de_erros = {}
        
        min_len_3(username,'username', lista_de_erros)
        min_len_6(senha,'senha', lista_de_erros)
        
        if lista_de_erros is not None:
            for erro in lista_de_erros:
                mensagem_erro = lista_de_erros[erro]
                self.add_error(erro, mensagem_erro) 
        return self.cleaned_data
