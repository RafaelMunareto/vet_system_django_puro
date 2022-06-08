from django import forms
from .models import *
from service.Buscador import *
from service.Formata import *
from service.validation import *

SEXO = [
    (0, 'SEXO'),
    ('MACHO', 'MACHO'),
    ('FÊMEA', 'FÊMEA')]

ESPECIE = [
    (0, 'ESPÉCIE'),
    ('CANINO', 'CANINO'),
    ('FELINO', 'FELINO'),
    ('EXÓTICO', 'EXÓTICO')
]

UF = [
    (0, 'UF'),
    ('AC', 'AC'),
    ('AL', 'AL'),
    ('AP', 'AP'),
    ('AM', 'AM'),
    ('BA', 'BA'),
    ('CE', 'CE'),
    ('ES', 'ES'),
    ('GO', 'GO'),
    ('MA', 'MA'),
    ('MT', 'MT'),
    ('MS', 'MS'),
    ('MG', 'MG'),
    ('PA', 'PA'),
    ('PB', 'PB'),
    ('PR', 'PR'),
    ('PE', 'PE'),
    ('PI', 'PI'),
    ('RJ', 'RJ'),
    ('RN', 'RN'),
    ('RS', 'RS'),
    ('RO', 'RO'),
    ('RR', 'RR'),
    ('SC', 'SC'),
    ('SP', 'SP'),
    ('SE', 'SE'),
    ('TO', 'TO'),
    ('DF', 'DF'),
]

class PacientesForms (forms.ModelForm, Buscador, Formata):
    
    cliente_id = forms.ChoiceField(label='', required=True, choices=([(0, 'ESCOLHA O TUTOR')] + [(int(linha['id']),  str(linha['id']) + ' - ' + str(linha['nome'].upper())) 
                    for linha in Buscador.busca_tutores()]), widget=forms.Select(attrs={"name": "cliente_id","class": "e1 !important"}))
    nome = forms.CharField(required=False, label='NOME')
    raca = forms.CharField(required=False, label='RAÇA')
    especie = forms.ChoiceField(label='', required=False, choices=ESPECIE , widget=forms.Select(attrs={'class': 'comite_select'}))   
    sexo = forms.ChoiceField( label='', required=False, choices=SEXO , widget=forms.Select(attrs={'class': 'comite_select'}))   
    peso = forms.CharField(required=False, label='PESO',  widget=forms.TextInput(attrs={'class': 'money'}))
    data_nascimento = forms.CharField(label='DATA NASCIMENTO', required=False, widget=forms.TextInput(attrs={'class': 'date'}))                        
    
    class Meta:
        model = Pacientes
        fields = ['nome','raca','especie','sexo','peso','data_nascimento']

    
    def clean(self):
        cleaned_data = super(PacientesForms, self).clean()
        cliente_id = self.cleaned_data.get('cliente_id')
        nome = self.cleaned_data.get('nome')
        raca = self.cleaned_data.get('raca')
        especie = self.cleaned_data.get('especie')
        sexo = self.cleaned_data.get('sexo')
        peso = self.cleaned_data.get('peso')
        data_nascimento = self.cleaned_data.get('data_nascimento')
        lista_de_erros = {}
        
        min_len_3(nome,'nome', lista_de_erros)
        min_len_3(raca,'raca', lista_de_erros)
        campo_nao_preechido(data_nascimento,'data_nascimento', lista_de_erros)   
        campo_nao_preechido(peso,'peso', lista_de_erros)
        escolha_valida(cliente_id,'cliente_id', lista_de_erros)
        escolha_valida(sexo,'sexo', lista_de_erros)
        escolha_valida(especie,'especie', lista_de_erros)
        
        if lista_de_erros is not None:
            for erro in lista_de_erros:
                mensagem_erro = lista_de_erros[erro]
                self.add_error(erro, mensagem_erro) 
        return self.cleaned_data  
    
class PacientesEditarForms (forms.ModelForm, Buscador, Formata):

    nome = forms.CharField(required=False, label='NOME')
    raca = forms.CharField(required=False, label='RAÇA')
    especie = forms.ChoiceField(label='', required=False, choices=ESPECIE , widget=forms.Select(attrs={'class': 'comite_select'}))   
    sexo = forms.ChoiceField( label='', required=False, choices=SEXO , widget=forms.Select(attrs={'class': 'comite_select'}))   
    peso = forms.CharField(required=False, label='PESO',  widget=forms.TextInput(attrs={'class': 'money'}))
    data_nascimento = forms.CharField(label='DATA NASCIMENTO', required=False, widget=forms.TextInput(attrs={'class': 'date'}))                        
    
    class Meta:
        model = Pacientes
        fields = ['nome','raca','especie','sexo','peso','data_nascimento']

    
    def clean(self):
        cleaned_data = super(PacientesEditarForms, self).clean()
        nome = self.cleaned_data.get('nome')
        raca = self.cleaned_data.get('raca')
        especie = self.cleaned_data.get('especie')
        sexo = self.cleaned_data.get('sexo')
        peso = self.cleaned_data.get('peso')
        data_nascimento = self.cleaned_data.get('data_nascimento')
        lista_de_erros = {}
        
        min_len_3(nome,'nome', lista_de_erros)
        min_len_3(raca,'raca', lista_de_erros)
        campo_nao_preechido(data_nascimento,'data_nascimento', lista_de_erros)   
        campo_nao_preechido(peso,'peso', lista_de_erros)
        escolha_valida(sexo,'sexo', lista_de_erros)
        escolha_valida(especie,'especie', lista_de_erros)
        
        if lista_de_erros is not None:
            for erro in lista_de_erros:
                mensagem_erro = lista_de_erros[erro]
                self.add_error(erro, mensagem_erro) 
        return self.cleaned_data
    
class FaturaForms(forms.Form, Buscador):        
    
    paciente = forms.ChoiceField(label='', required=True, choices=([(0, 'ESCOLHA O PACIENTE')] + [(int(linha.id), str(linha.tutor).upper() +  ' - COD ' + str(linha.id) + ' - ' + str(linha.nome).upper()) 
                for linha in Buscador.busca_pacientes_all()]), widget=forms.Select(attrs={"class": "e1 !important", 'id': 'cliente'}))

    produto = forms.ChoiceField(label='', required=True, choices=([(0, 'ESCOLHA O PRODUTO')] + [(int(linha['id']),  str(linha['id']) + ' - ' + str(linha['produto'].upper())) 
            for linha in Buscador.busca_produtos_values()]), widget=forms.Select(attrs={"id": "produto","class": "e2 !important", 'style': 'min-width:20rem'}))

    servico = forms.ChoiceField(label='', required=True, choices=([(0, 'ESCOLHA O SERVIÇO')] + [(int(linha['id']),  str(linha['id']) + ' - ' + str(linha['servico'].upper())) 
            for linha in Buscador.busca_servicos()]), widget=forms.Select(attrs={"id": "servico","class": "e3 !important", 'style': 'min-width:20rem'}))

    data_cadastro = forms.ChoiceField(label='', required=True, choices=([(0, 'NOVA FATURA')] + [(int(linha.id), str(linha.data_cadastro)) 
                for linha in Buscador.busca_faturas_all()]), widget=forms.Select(attrs={"class": "e4 !important", 'id': 'cliente'}))
    
    qtd_servico = forms.FloatField(label='QTD', required=True,  widget=forms.NumberInput(attrs={"name": "qtd_servico", 'id': 'qtd_servico'}))
    qtd_produto = forms.FloatField(label='QTD', required=True,  widget=forms.NumberInput(attrs={"name": "qtd_produto", 'id': 'qtd_produto'}))

class PrescricaoForms(forms.ModelForm, Buscador):        
    
    paciente = forms.ChoiceField(label='', required=True, choices=([(0, 'ESCOLHA O PACIENTE')] + [(int(linha.id), str(linha.tutor).upper() +  ' - COD ' + str(linha.id) + ' - ' + str(linha.nome).upper()) 
                for linha in Buscador.busca_pacientes_all()]), widget=forms.Select(attrs={"class": "e1 !important", 'id': 'paciente_id'}))

    veterinario = forms.ChoiceField(label='', required=True, choices=([(0, 'ESCOLHA O VETERINÁRIO')] + [(int(linha['id']),  str(linha['crmv']) + ' - ' + str(linha['nome'].upper())) 
            for linha in Buscador.busca_veterinario()]), widget=forms.Select(attrs={"id": "servico","class": "e3 !important", 'style': 'min-width:20rem'}))


    prescricao = forms.CharField(label='PRESCRIÇÃO:', required=True, widget=forms.Textarea(attrs={"rows":5, "cols":20, 'id': 'prescricao'}))
    
    class Meta:
        model = Prescricao
        fields = ['prescricao']

    
    def clean(self):
        cleaned_data = super(PrescricaoForms, self).clean()
        paciente = self.cleaned_data.get('paciente')
        veterinario = self.cleaned_data.get('veterinario')
        prescricao = self.cleaned_data.get('prescricao')
        lista_de_erros = {}
        
        campo_nao_preechido(prescricao,'prescricao', lista_de_erros)
        escolha_valida(paciente,'paciente', lista_de_erros)
        escolha_valida(veterinario,'veterinario', lista_de_erros)
        
        if lista_de_erros is not None:
            for erro in lista_de_erros:
                mensagem_erro = lista_de_erros[erro]
                self.add_error(erro, mensagem_erro) 
        return self.cleaned_data
    
class VeterinarioForms (forms.ModelForm, Buscador, Formata):

    nome = forms.CharField(required=False, label='NOME')
    crmv = forms.CharField(required=False, label='CRMV')
    uf = forms.ChoiceField(label='', required=False, choices=UF , widget=forms.Select(attrs={'id': 'e1'}))   
    
    class Meta:
        model = AssinaturaVeterinario
        fields = ['nome','crmv','uf']

    
    def clean(self):
        cleaned_data = super(VeterinarioForms, self).clean()
        nome = self.cleaned_data.get('nome')
        crmv = self.cleaned_data.get('crmv')
        uf = self.cleaned_data.get('uf')
        lista_de_erros = {}
        
        campo_nao_preechido(nome,'nome', lista_de_erros)
        campo_nao_preechido(crmv,'crmv', lista_de_erros)
        escolha_valida(uf,'uf', lista_de_erros)
        
        if lista_de_erros is not None:
            for erro in lista_de_erros:
                mensagem_erro = lista_de_erros[erro]
                self.add_error(erro, mensagem_erro) 
        return self.cleaned_data
    
class HistoricoForms (forms.Form, Buscador):
    paciente = forms.ChoiceField(label='', required=True, choices=([(0, 'ESCOLHA O PACIENTE')] + [(int(linha.id), str(linha.tutor).upper() +  ' - COD ' + str(linha.id) + ' - ' + str(linha.nome).upper()) 
                for linha in Buscador.busca_pacientes_all()]), widget=forms.Select(attrs={"class": "e1 !important", 'id': 'paciente_id'}))

