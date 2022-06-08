from django.db.models import Count, F, Value
from adm.models import Unidades_suvsu, Equipes, Aniversario
from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect
from pprint import pprint
from django.db.models.functions import Concat
from datetime import datetime
from adm.models import Equipes
import os
from django.contrib import messages
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
from bs4 import BeautifulSoup
import urllib.request as urllib_request
import pandas as pd

class Scraping:
    
    def __init__(self):
        self.headers = headers = {
                                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0',
                                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                                    'Accept-Language': 'fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3',
                                    'Upgrade-Insecure-Requests': '1',
                                    'Connection': 'keep-alive',
                                    'Pragma': 'no-cache',
                                    'Cache-Control': 'no-cache',
                                    'Cookie': 'ASPSESSIONIDQCTDTDCA=PGKADCNALLHDIEHFDEMCGMKB',
                                    'ASPSESSIONIDQCTDTDCA': 'PGKADCNALLHDIEHFDEMCGMKB'
                                }
        self.payload = payload={
                            'session-key' : 'corpcaixa\c105522',
                            'session-password' : 'Brasil19'
                        }
  
    def busca(self, url, headers):
        try:
            req = Request(url, headers=headers, data=self.payload)
            response = urlopen(req)
            html =  response.read().decode('utf-8')
            html = self.trata_html(html)
            soup = BeautifulSoup(html, 'html.parser')
            return soup
        except HTTPError as e:
            print (e.status, e.reason)

        except URLError as e:
           print(e.reason)

    def trata_html(self,html):
        return " ".join(html.split()).replace('> <', '><')

    def sifec(self, request):
        url='http://mpe.caixa/ferramentas/P_1039_pronampe/f151_reserva_sintetico.asp?id_unidade_sintetica_pronampe=5174'
        site = self.busca(url, self.headers)
        table = []
        try:
            dados = site.find('table').find_all('tr')
            print(dados)
        except:
            messages.error(request,'Dados não encontrados')
            return redirect('scraping')
        for linha in dados:
            dado = {}
            dado['th'] = linha.get_text()
            table.append(dado)
            dado['td'] = linha.get_text()
            table.append(dado)
           
            
        data_set = pd.DataFrame(table)
        return data_set
