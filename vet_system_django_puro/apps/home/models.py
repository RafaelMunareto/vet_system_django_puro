from django.db import models

class Urls(models.Model):
    urls = models.CharField(max_length=100, blank=True)
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=250, blank=True)
    img = models.CharField(max_length=100, blank=True)
    cor = models.CharField(max_length=100)
    icone = models.CharField(max_length=50)
    rota = models.CharField(max_length=50)
    grupo = models.CharField(max_length=50)
    
    class Meta:
        verbose_name = 'URL'
        verbose_name_plural = 'URLs'
        ordering = ['nome']