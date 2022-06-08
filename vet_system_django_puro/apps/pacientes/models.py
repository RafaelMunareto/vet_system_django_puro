from django.db import models
from datetime import datetime
from clientes.models import Clientes
from administrativo.models import Produtos, Servicos
from django.contrib.auth.models import User
  
class Pacientes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tutor = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    raca = models.CharField(max_length=50)
    especie = models.CharField(max_length=50, blank=True)
    sexo = models.CharField(max_length=100)
    idade = models.CharField(max_length=50, blank=True)
    peso = models.CharField(max_length=50, blank=True)
    data_nascimento = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'Pacientes'
        verbose_name_plural = 'Pacientes'
        ordering = ['id']
        
class FaturaProduto(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    paciente = models.ForeignKey(Pacientes, on_delete=models.CASCADE)
    tutor = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    cod = models.IntegerField()
    produto = models.CharField(max_length=200, blank=True)
    faturado = models.IntegerField(default=0)
    key = models.IntegerField()
    qtd = models.FloatField(null=True, blank=True)
    valor = models.FloatField(null=True, blank=True)
    data_cadastro = models.DateField(default=datetime.today, blank=True)
    
    class Meta:
        verbose_name = 'Fatura Produto'
        verbose_name_plural = 'Fatura Produto'
        ordering = ['id']     

class HistoricoFatura(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    paciente = models.ForeignKey(Pacientes, on_delete=models.CASCADE)
    tutor = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    total = models.FloatField(null=True, blank=True)
    key = models.IntegerField()
    data_cadastro = models.DateField(default=datetime.today, blank=True)

    class Meta:
        verbose_name = 'Histórico Fatura'
        verbose_name_plural = 'Histórico Fatura'
        ordering = ['id']       

class AssinaturaVeterinario (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=200, blank=True)
    crmv = models.IntegerField()
    uf = models.CharField(max_length=2, blank=True)

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'Assinatura Veterinário'
        verbose_name_plural = 'Assinatura Veterinário'
        ordering = ['id']
         
class Prescricao (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    paciente = models.ForeignKey(Pacientes, on_delete=models.CASCADE)
    tutor = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    prescricao = models.TextField(max_length=1000, blank=True)
    vet = models.ForeignKey(AssinaturaVeterinario, on_delete=models.CASCADE)
    data_cadastro = models.DateTimeField(default=datetime.now, blank=True)

    class Meta:
        verbose_name = 'Prescricao'
        verbose_name_plural = 'Prescricao'
        ordering = ['id']
        