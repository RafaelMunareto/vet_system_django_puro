from django.db.models import Count, F, Value
from pprint import pprint
from django.db.models.functions import Concat
from datetime import datetime
from administrativo.models import CustosFixos

class Formata:
    
    def dia_extenso(dado):
        Semana = ('segunda feira','terceira feira','quarta feira','quinta feira','sexta feira','sabado','domingo')
        return str(Semana[dado]).capitalize()

    def mes_extenso(dado):
        Meses=('janeiro','fevereiro','mar','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro')
        return str(Meses[dado]).capitalize()

    def dia_mais_mes_extenso(dia, mes):
        dia_mes = str(dia) +  ' de ' + Formata.mes_extenso(dado=mes)
        return dia_mes

    def stringToFloat(dado):
        """ Transforma String em Float"""
        return float(dado.replace('.', '').replace(',', '.'))

    def moeda(dado):
        """ Transforma em formato de moeda"""
        a = '{:,.2f}'.format(float(dado))
        b = a.replace(',','v')
        c = b.replace('.',',')
        return c.replace('v','.')

    def stringToData(dado):
        """ Transforma em formato de data"""
        year = dado[0:4]
        month = dado[5:7][:2]
        day = dado[8:10][:2]
        data = "{}/{}/{}".format(day,month,year)
        if year == '9999':
            data =  day + ' de cada mês'
        return data
    
    def data_aniversario(dado):
        data = dado.replace('/','-')
        return data[0:5]
    
    def meses_do_ano(argument):
        switcher = {
            1: 'JANEIRO',
            2: 'FEVEREIRO',
            3: 'MARÇO',
            4: 'ABRIL',
            5: 'MARIO',
            6: 'JUNHO',
            7: 'JULHO',
            8: 'AGOSTO',
            9: 'SETEMBRO',
            10: 'OUTUBRO',
            11: 'NOVEMBRO',
            12: 'DEZEMBRO'
        }
        mes = switcher.get(argument, lambda: "Mês inválido")
        return mes
    
    def data_menos_hoje(d1):
        """Calcula a data de hoje menos a data Atual"""
        dia = int(d1[0:2])
        mes = int(d1[3:5][:2])
        ano = int(d1[6:10][:4])   
        print('dia:{} mes:{} ano:{}'.format(dia, mes,ano))
        d1 = datetime(ano,mes,dia)
        d2 = datetime.now()
        diff = d2 - d1
        days = diff.days
        years, days = days // 365, days % 365
        months, days = days // 30, days % 30
        if months > 0:
            if ano == 1:
               return "{} ano e {} meses".format(years, months)
            if mes == 1:
                return "{} anos e {} mês".format(years, months)
            else:
                return "{} anos e {} meses".format(years, months)
        else:
            if ano == 1:
                return "{} anos".format(years)
            else:
                return "{} ano".format(years)
            
    def formata_tipo(value):
        """ Formata tipo do agendamento"""
        switcher = {
            0: 'TODOS',
            1: 'CONSULTA',
            2: 'VACINA',
            3: 'RETORNO',
            4: 'BANHO E TOSA',
            5: 'CIRURGIA'
        }
        tipo = switcher.get(value, lambda: "tipo inválido")
        return tipo

    def formata_periodo(value):
        """Formata periodo do agendamento"""
        switcher = {
            0: 'TODOS',
            1: 'DIA',
            2: 'SEMANA',
            3: 'MÊS'
        }
        periodo = switcher.get(value, lambda: "periodo inválido")
        return periodo

    def dinheiro(my_value):
        if my_value == None:
            return ''
        a = '{:,.2f}'.format(float(my_value))
        b = a.replace(',','v')
        c = b.replace('.',',')
        return c.replace('v','.')
    
    def true_false(value):
        if value == True:
            return 'SIM'
        else:
            return ''
        
        