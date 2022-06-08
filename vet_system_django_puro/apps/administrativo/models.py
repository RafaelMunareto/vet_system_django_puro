from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class Fornecedores(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=200)
    cnpj = models.CharField(max_length=50)
    ramo = models.CharField(max_length=200)
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
    obs = models.CharField(max_length=200, blank=True)
    banco = models.CharField(max_length=100, blank=True)
    agencia = models.CharField(max_length=100, blank=True)
    conta = models.CharField(max_length=100, blank=True)
    data_cadastro = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.nome
        
    class Meta:
        verbose_name = 'Fornecedores'
        verbose_name_plural = 'Fornecedores'
        ordering = ['id']      
    
class Produtos(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fornecedor = models.ForeignKey(Fornecedores, on_delete=models.CASCADE)
    produto = models.CharField(max_length=200)
    descricao = models.CharField(max_length=255, blank=True)
    un_medida = models.CharField(max_length=50)
    custo = models.CharField(max_length=100)
    venda = models.CharField(max_length=100, blank=True)
    data_cadastro = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.produto

    class Meta:
        verbose_name = 'Produtos'
        verbose_name_plural = 'Produtos'
        ordering = ['id']      

class Estoque(models.Model): 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produtos, on_delete=models.CASCADE)
    qtd_total = models.CharField(max_length=200)
    valor_total = models.FloatField()
    data_movimento = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.produto.produto
    
    class Meta:
        verbose_name = 'Estoque'
        verbose_name_plural = 'Estoque'
        ordering = ['id'] 
    
class Parceiros(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=200)
    cpf = models.CharField(max_length=50)
    especialidade = models.CharField(max_length=200)
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
        verbose_name = 'Parceiros'
        verbose_name_plural = 'Parceiros'
        ordering = ['id']      

class Servicos(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    servico = models.CharField(max_length=200)
    descricao = models.CharField(max_length=255, blank=True)
    venda = models.CharField(max_length=100, blank=True)
    data_cadastro = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.servico
        
    class Meta:
        verbose_name = 'Servicos'
        verbose_name_plural = 'Servicos'
        ordering = ['id']      

class Pagamentos(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produtos, on_delete=models.CASCADE)
    qtd_total = models.CharField(max_length=200)
    valor_total = models.FloatField()
    pagamento = models.CharField(max_length=200, blank=True)
    
    class Meta:
        verbose_name = 'Pagamentos'
        verbose_name_plural = 'Pagamentos'
        ordering = ['id'] 

class CustosFixos(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=200)
    descricao = models.CharField(max_length=255, blank=True)
    pagamento = models.CharField(max_length=200, blank=True)
    custo = models.FloatField()
    recorrente = models.BooleanField(default=False, blank=True)
    data_cadastro = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Custos Fixos'
        verbose_name_plural = 'Custos Fixos'
        ordering = ['id']      
