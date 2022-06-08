from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter
@stringfilter
def upper(value):
    return value.upper()

@register.filter(needs_autoescape=True)
def real_br_money_mask(my_value, autoescape=True):
    if my_value == None:
        return ''
    a = '{:,.2f}'.format(float(my_value))
    b = a.replace(',','v')
    c = b.replace('.',',')
    return c.replace('v','.')

@register.filter(needs_autoescape=True)
def top(value, autoescape=True):
    if value == 1: 
        return mark_safe("<img class='icone_top' src='/static/img/icone_tops/top1.png'>")
    elif value == 2:
        return mark_safe("<img class='icone_top' src='/static/img/icone_tops/top2.png'>")
    elif value == 3:
        return mark_safe("<img class='icone_top' src='/static/img/icone_tops/top3.png'>")
    else:
        return mark_safe(str(value) + 'º')

@register.filter(needs_autoescape=True)
def icone_especie(value, autoescape=True):
    if value == 'CANINO': 
        return mark_safe("<img class='icone_top' src='/static/img/outros/canino.png'>")
    elif value == 'FELINO':
        return mark_safe("<img class='icone_top' src='/static/img/outros/felino.png'>")
    elif value == 'EXÓTICO':
        return mark_safe("<img class='icone_top' src='/static/img/outros/exotico.png'>")
    else:
        return mark_safe(value)


@register.filter(needs_autoescape=True)
def meses_do_ano(value, autoescape=True):
    switcher = {
        1: JANEIRO,
        2: FEVEREIRO,
        3: MARÇO,
        4: ABRIL,
        5: MARIO,
        6: JUNHO,
        7: JULHO,
        8: AGOSTO,
        9: SETEMBRO,
        10: OUTUBRO,
        11: NOVEMBRO,
        12: DEZEMBRO
    }
    mes = switcher.get(value, lambda: "Mês inválido")
    return mes


@register.filter(needs_autoescape=True)
def formata_tipo(value, autoescape=True):
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

@register.filter(needs_autoescape=True)
def recorrente(value, autoescape=True):
    if value == True:
        return 'SIM'
    else:
        return ''  

@register.filter(needs_autoescape=True)
def stringToData(value, autoescape=True):
    """ Transforma em formato de data"""
    year = value[0:4]
    month = value[5:7][:2]
    day = value[8:10][:2]
    data = "{}/{}/{}".format(day,month,year)
    return data