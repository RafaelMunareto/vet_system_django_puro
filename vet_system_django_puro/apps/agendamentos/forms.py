from django import forms
from .models import Agendamentos
from service.Buscador import *
from service.Formata import *
from service.validation import *

TIPO = [
    (0, 'TIPO'),
    (1, 'CONSULTA'),
    (2, 'VACINA'),
    (3, 'RETORNO'),
    (4, 'BANHO E TOSA'),
    (5, 'CIRURGIA')]

class AgendamentosForms (forms.ModelForm, Buscador, Formata):
    
    paciente_id = forms.ChoiceField(label='', required=False, choices=([(0, 'ESCOLHA O PACIENTE')] + [(linha['id'], str(linha['id']) + ' - ' + str(linha['nome'].upper())) 
                    for linha in Buscador.busca_pacientes()]), widget=forms.Select(attrs={"name": "pacientes","class": "e1 !important"}))
    data = forms.DateField(label='', required=True, widget=forms.DateInput(attrs={'class': 'datepicker', 'placeholder':'DATA'}))    
    time = forms.CharField(label='', required=True,widget=forms.TimeInput(attrs={'class': 'timepicker', 'placeholder':'HORÁRIO'}))                    
    tipo = forms.ChoiceField(label='', required=False, choices=TIPO , widget=forms.Select(attrs={'class': 'comite_select'}))   
    obs = forms.CharField(label='OBS', required=False)
    
    class Meta:
        model = Agendamentos
        fields = ['data', 'time', 'tipo','obs']
        widgets = {
           
            'obs': forms.Textarea(attrs={'cols': 80, 'rows': 20}),
        }

    
    def clean(self):
        cleaned_data = super(AgendamentosForms, self).clean()
       
        data = self.cleaned_data.get('data')
        time = self.cleaned_data.get('time')
        tipo = self.cleaned_data.get('tipo')
        paciente_id = self.cleaned_data.get('paciente_id')
        lista_de_erros = {}
        
        escolha_valida(paciente_id, 'paciente_id', lista_de_erros)
        escolha_valida(tipo,'tipo', lista_de_erros)
        campo_nao_preechido(data,'data', lista_de_erros)
        campo_nao_preechido(time,'time', lista_de_erros)
        
        if lista_de_erros is not None:
            for erro in lista_de_erros:
                mensagem_erro = lista_de_erros[erro]
                self.add_error(erro, mensagem_erro) 
        return self.cleaned_data
    
