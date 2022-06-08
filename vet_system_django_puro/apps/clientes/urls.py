from django.urls import path
from .views import *

urlpatterns = [
    
    path('clientes', clientes.listar, name='clientes'),
    path('clientes/<int:id>', clientes.detalhes, name='clientes.detalhes'),
    path('clientes/contatos/<int:id>', clientes.contatos, name='clientes.contatos'),
    path('clientes/endereco/<int:id>', clientes.endereco, name='clientes.endereco'),
    path('clientes/adicionar', clientes.adicionar, name='clientes.adicionar'),
    path('clientes/editar/<int:id>', clientes.editar, name='clientes.editar'),
    path('clientes/delete/<int:id>', clientes.delete, name='clientes.delete'),
    path('clientes/store', clientes.store, name='clientes.store'),
    path('clientes/put/<int:id>', clientes.put, name='clientes.put'),
    path('clientes_export', clientes.export, name='clientes.export'),

    path('aniversarios', aniversarios.listar, name='aniversarios.listar'),
    path('aniversarios_tutor/<slug:data>', aniversarios.aniversarios_tutor, name='aniversarios.tutor'),
    path('aniversarios_pet/<slug:data>', aniversarios.aniversarios_pet, name='aniversarios.pet'),

]
