from django.db import models
from datetime import datetime
from pacientes.models import Pacientes
from django.contrib.auth.models import User

class Agendamentos(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    paciente = models.ForeignKey(Pacientes, on_delete=models.CASCADE)
    data = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    tipo = models.IntegerField()
    obs = models.CharField(max_length=250, blank=True)
        
    class Meta:
        verbose_name = 'Agendamentos'
        verbose_name_plural = 'Agendamentos'
        ordering = ['id']      
  