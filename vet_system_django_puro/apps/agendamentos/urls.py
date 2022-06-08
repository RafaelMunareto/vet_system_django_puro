from django.urls import path
from .views import *

urlpatterns = [
    
    path('agendamentos/<int:tipo>/<int:periodo>', agendamentos.listar, name='agendamentos'),
    path('agendamentos/adicionar', agendamentos.adicionar, name='agendamentos.adicionar'),
    path('agendamentos/adicionar_novo/<int:id>', agendamentos.adicionar_novo, name='agendamentos.adicionar_novo'),
    path('agendamentos/editar/<int:id>', agendamentos.editar, name='agendamentos.editar'),
    path('agendamentos/delete/<int:id>', agendamentos.delete, name='agendamentos.delete'),
    path('agendamentos/store', agendamentos.store, name='agendamentos.store'),
    path('agendamentos/put/<int:id>', agendamentos.put, name='agendamentos.put'),
    path('agendamentos_export', agendamentos.export, name='agendamentos.export'),
   
]
