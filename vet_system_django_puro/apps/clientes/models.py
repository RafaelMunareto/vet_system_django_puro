from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class Clientes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=200)
    cpf = models.CharField(max_length=50)
    data_nascimento = models.CharField(max_length=200)
    telefone_residencial = models.CharField(max_length=200, blank=True)
    telefone_celular = models.CharField(max_length=100, blank=True)
    telefone_comercial = models.CharField(max_length=100, blank=True)
    email = models.CharField(max_length=100, blank=True)
    cep = models.CharField(max_length=100, blank=True)
    estado = models.CharField(max_length=3, blank=True)
    cidade = models.CharField(max_length=100, blank=True)
    bairro = models.CharField(max_length=100, blank=True)
    endereco = models.CharField(max_length=250, blank=True)
    numero = models.IntegerField(blank=True)
    complemento = models.CharField(max_length=200, blank=True)
    data_cadastro = models.DateTimeField(default=datetime.now, blank=True)
    
    def __str__(self):
        return self.nome
        
    class Meta:
        verbose_name = 'Clientes'
        verbose_name_plural = 'Clientes'
        ordering = ['id']      
  
    