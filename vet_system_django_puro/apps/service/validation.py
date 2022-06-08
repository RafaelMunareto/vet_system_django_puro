import datetime
import re

def datas_iguais(de, ate, lista_de_erros):
    """Verifica se as datas são iguais"""
    if de == ate:
        lista_de_erros['ate'] = 'As datas não podem ser iguais!'

def data_ate_maior(de, ate, lista_de_erros):
    """Verifica se data de ida é maior que data de volta"""
    if de > ate :
        lista_de_erros['ate'] = 'Data retorno menor que data de ida'
        
def campo_nao_preechido(valor_campo, nome_campo, lista_de_erros):
    """Verifica se possui algum digito numérico"""
    if valor_campo == '':
        lista_de_erros[nome_campo] = 'Campo deve ser preenchido'

def campo_nao_preenchido(valor_campo, nome_campo, lista_de_erros):
    """Verifica se possui algum digito numérico"""
    if valor_campo == '':
        lista_de_erros[nome_campo] = 'Campo deve ser preenchido'

def min_len_3(valor_campo, nome_campo, lista_de_erros):
    """Verifica se possui algum digito numérico"""
    if len(valor_campo) < 3:
        lista_de_erros[nome_campo] = 'Campo deve ter no minimo 3 caracteres'

def min_len_6(valor_campo, nome_campo, lista_de_erros):
    """Verifica se a senha possui pelo menos 6 digitos"""
    if len(valor_campo) < 6:
        lista_de_erros[nome_campo] = 'Campo deve ter no minimo 6 caracteres'

def escolha_valida(valor_campo, nome_campo, lista_de_erros):
    """Verifica se a escolha do select é válida """

    if valor_campo == '0' or valor_campo == 0:
        lista_de_erros[nome_campo] = 'Escolha uma opção válida!'

def valida_data(valor_campo, nome_campo, lista_de_erros):
    """Verifica se a data é dentro do ano"""
    if valor_campo:
        lista_de_erros[nome_campo] = 'Escolha uma data válida!'

def titu_event_iguais(mat_titu, mat_event, lista_de_erros):
    """Verifica se as datas são iguais"""
    if mat_titu == mat_event and mat_titu != '':
        lista_de_erros['mat_event'] = 'O titular e o eventual não podem ser iguais!'
        
def tamanho_data(valor_campo, nome_campo, lista_de_erros):
    """Verifica o tamanho minimo da data"""
    if len(valor_campo) < 10:
        lista_de_erros[nome_campo] = 'Data incorreta'

       
def tamanho_telefone(valor_campo, nome_campo, lista_de_erros):
    """Verifica o tamanho minimo do telefone"""
    if len(valor_campo) < 14:
        lista_de_erros[nome_campo] = 'Telefone incorreto'

       
def tamanho_celular(valor_campo, nome_campo, lista_de_erros):
    """Verifica o tamanho minimo da data"""
    if len(valor_campo) < 15:
        lista_de_erros[nome_campo] = 'Celular incorreto'
       
def tamanho_cep(valor_campo, nome_campo, lista_de_erros):
    """Verifica o tamanho minimo da data"""
    if len(valor_campo) < 9:
        lista_de_erros[nome_campo] = 'CEP incorreto'

    
def verifica_email(valor_campo, nome_campo, lista_de_erros):
    """Verifica email"""
    if "@" not in valor_campo:
        lista_de_erros[nome_campo] = 'email incorreto'


def tamanho_cpf(valor_campo, nome_campo, lista_de_erros):
    """Verifica email"""
    if len(valor_campo) < 14:
        lista_de_erros[nome_campo] = 'CPF incorreto'

def compara_senhas(valor_campo, valor_campo2, nome_campo, lista_de_erros):
    """comparanha senhas"""
    if valor_campo != valor_campo2:
          lista_de_erros[nome_campo] = 'As senhas não são iguais!'
