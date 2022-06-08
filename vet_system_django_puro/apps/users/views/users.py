import io
import re
from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect
from django.contrib import messages
from django.db.models import Q
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django_tables2 import RequestConfig
from django.template.response import TemplateResponse
from users.forms import CadastroUsersForms, LoginUsersForms
from django.contrib.auth.models import User
from django.contrib import auth, messages
from django.contrib.auth.hashers import *
from service.Buscador import *
from service.Formata import *


def cadastro(request):
    """ CARREGA A TABELA PRINCIPAL COM OS DADOS """

    if request.method == 'POST': 
        nome = request.POST['nome']
        sobrenome = request.POST['sobrenome']
        username = request.POST['username']
        email = request.POST['email']
        senha = request.POST['senha']
        
        form = CadastroUsersForms(request.POST)
        
        if form.is_valid():
           
            store = User.objects.create(
                first_name = nome,
                last_name = sobrenome,
                username = username,
                email = email,
                password = make_password(senha)
            )   
            store.save()
            
            user = auth.authenticate(request, username=username, password=senha)
            if user is not None:
                auth.login(request, user)
                return redirect('home')
        else:
            url = Buscador.busca_url_base('/cadastro')
            form = CadastroUsersForms(request.POST)
            dados = {
                'title': url.nome, 
                'cor': url.cor, 
                'titulo': url.nome,
                'form': form,
                'img': url.img,
                'url_base': 'login',
                'url_action': 'login.cadastro'
            }
            
            return render(request, 'users/cadastro.html',dados)

    form = CadastroUsersForms()
    url = Buscador.busca_url_base('/cadastro')
    dados = {
        'title': url.nome, 
        'cor': url.cor, 
        'titulo': url.nome,
        'form': form,
        'img': url.img,
        'url_base': 'login',
        'url_action': 'login.cadastro'
    }
    
    return render(request, 'users/cadastro.html',dados)

def login(request):
    """ PÁGINA DO ADICIONAR """

    if request.method == 'POST':
        username = request.POST['username']
        senha = request.POST['senha']

        form = LoginUsersForms(request.POST)

        if form.is_valid():  
            user = auth.authenticate(request, username=username, password=senha)
            if user is not None:
                auth.login(request, user)
                return redirect('home')
            else:
                messages.error(request,'Usuário não cadastrado!')
                return redirect('login')  
        else:
            form = LoginUsersForms(request.POST)
            url = Buscador.busca_url_base('/login')
            dados = {
                'title': url.nome, 
                'cor': url.cor, 
                'titulo': url.nome,
                'form': form,
                'img': url.img,
                'url_base': 'login',
                'url_action': 'login'
            }
            return render(request, 'users/login.html',dados)
            
    form = LoginUsersForms()
    url = Buscador.busca_url_base('/login')
    dados = {
        'title': url.nome, 
        'cor': url.cor, 
        'titulo': url.nome,
        'form': form,
        'img': url.img,
        'url_base': 'login',
        'url_action': 'login'
    }
    
    return render(request, 'users/login.html',dados)
    
def logout(request):
    """PARA FAZER O LOGOUT"""
    auth.logout(request)
    return redirect('login')
