from django.urls import path
from .views import *

urlpatterns = [
    
    path('pacientes', pacientes.listar, name='pacientes'),
    path('pacientes/detalhes/<int:id>', pacientes.detalhes, name='pacientes.detalhes'),
    path('pacientes/associados/<int:id>', pacientes.associados, name='pacientes.associados'),
    path('pacientes/adicionar_novo', pacientes.adicionar_novo, name='pacientes.adicionar_novo'),
    path('pacientes/adicionar/<int:id>', pacientes.adicionar, name='pacientes.adicionar'),
    path('pacientes/editar/<int:id>', pacientes.editar, name='pacientes.editar'),
    path('pacientes/delete/<int:id>', pacientes.delete, name='pacientes.delete'),
    path('pacientes/store', pacientes.store, name='pacientes.store'),
    path('pacientes/put/<int:id>', pacientes.put, name='pacientes.put'),
    path('pacientes_export', pacientes.export, name='pacientes.export'),

    path('fatura', fatura.listar, name='fatura'),    
    path('fatura/<int:id>', fatura.lista, name='fatura.detalhes'),    
    path('fatura/cliente_paciente/<int:id>', fatura.cliente_paciente, name='cliente_paciente'),    
    path('fatura/store', fatura.store, name='fatura.store'),    
    path('fatura/delete/<int:id>', fatura.delete, name='fatura.delete'),    

    path('historico_fatura/<int:id>', historico_fatura.listar, name='historico_fatura'),    
    path('historico_fatura/delete/<int:id>', historico_fatura.delete, name='historico_fatura.delete'),
    path('historico_fatura/store', historico_fatura.store, name='historico_fatura.store'),
    path('historico_faturas/export/<int:id>', historico_fatura.HelloPDFView.as_view(),  name='historico_fatura.export'),

    path('prescricao', prescricao.listar, name='prescricao'),
    path('prescricao/store', prescricao.store, name='prescricao.store'),    
    path('historico_prescricao/<int:id>', prescricao.historico_prescricao, name='prescricao.historico_prescricao'),    
    path('historico_prescricao/export/<int:id>', prescricao.HelloPDFView.as_view(),  name='historico_prescricao.export'),
    path('prescricao/delete/<int:id>', prescricao.delete, name='prescricao.delete'),    

    path('veterinario', veterinario.listar, name='veterinario'),
    path('veterinario/adicionar', veterinario.adicionar, name='veterinario.adicionar'),
    path('veterinario/editar/<int:id>', veterinario.editar, name='veterinario.editar'),
    path('veterinario/delete/<int:id>', veterinario.delete, name='veterinario.delete'),
    path('veterinario/store', veterinario.store, name='veterinario.store'),
    path('veterinario/put/<int:id>', veterinario.put, name='veterinario.put'),
    path('veterinario_export', veterinario.export, name='veterinario.export'),
    
]
