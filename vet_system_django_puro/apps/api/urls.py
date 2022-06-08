from django.urls import path, include
from django.contrib import admin 
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()

"""ADMINISTRATIVO"""
router.register('fornecedores', FornecedoresViewSet, basename='fornecedores')
router.register('produtos', ProdutosViewSet, basename='produtos')
router.register('estoque', EstoqueViewSet, basename='estoque')
router.register('parceiros', ParceirosViewSet, basename='parceiros')
router.register('servicos', ServicosViewSet, basename='servicos')
router.register('pagamentos', PagamentosViewSet, basename='pagamentos')
router.register('custos_fixos', CustosFixosViewSet, basename='custos_fixos')

"""AGENDAMENTOS"""
router.register('agendamentos', AgendamentosViewSet, basename='agendamentos')

"""CLIENTES"""
router.register('clientes', ClientesViewSet, basename='clientes')

"""HOME"""
router.register('urls', UrlsViewSet, basename='urls')

""" PACIENTES """
router.register('pacientes', PacientesViewSet, basename='pacientes')
router.register('fatura_produto', FaturaProdutoViewSet, basename='fatura_produto')
router.register('historico_fatura', HistoricoFaturaViewSet, basename='historico_fatura')
router.register('assinatura_veterinario', AssinaturaVeterinarioViewSet, basename='assinatura_veterinario')
router.register('prescricao', PrecricaoViewSet, basename='prescricao')


urlpatterns = [
    path('api/', include(router.urls)),
    path('api/fornecedores/<int:pk>/produtos/', ProdutosDoFornecedor.as_view()),
    path('api/clientes/<int:pk>/pacientes/', PacientesDosClientes.as_view()),
    path('api/pacientes/<int:pk>/faturas/', HistoricoFaturasDosPacientes.as_view()),
    path('api/pacientes/<int:pk>/prescricao/', PrescricaoDosPacientes.as_view()),
]
